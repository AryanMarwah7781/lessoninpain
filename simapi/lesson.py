"""Lesson engine: walks a lesson file step by step against the live Store.

It decides when the current step is done, which mistakes happened, and which hint is due.
It never touches the simulator itself; "show me" goes through the armrest client.
Format: lessons/FORMAT.md. Standard library only.
"""
import json
import time

TRUE, FALSE, UNKNOWN = "true", "false", "unknown"


def _num(v):
    try:
        return float(v)
    except (TypeError, ValueError):
        return None


def value_matches(leaf, value):
    if value is None:
        return False
    v = _num(value)
    if "eq" in leaf:
        want = leaf["eq"]
        if _num(want) is not None and v is not None:
            return abs(v - _num(want)) < 1e-6
        return str(value) == str(want)
    if v is None:
        return False
    if "gte" in leaf and not v >= leaf["gte"]: return False
    if "lte" in leaf and not v <= leaf["lte"]: return False
    if "gt" in leaf and not v > leaf["gt"]: return False
    if "lt" in leaf and not v < leaf["lt"]: return False
    if "between" in leaf and not (leaf["between"][0] <= v <= leaf["between"][1]): return False
    if "outside" in leaf and (leaf["outside"][0] <= v <= leaf["outside"][1]): return False
    return True


def describe(check):
    """Plain-language description of a check (for reports and the panel)."""
    if "all" in check: return " and ".join(describe(c) for c in check["all"])
    if "any" in check: return " or ".join(describe(c) for c in check["any"])
    if "then" in check: return ", then ".join(describe(c) for c in check["then"])
    if "before" in check: return f"{describe(check['before'][0])} before {describe(check['before'][1])}"
    if "not" in check: return f"not ({describe(check['not'])})"
    if "confirm" in check: return f"trainee confirms: {check['confirm']}"
    for src in ("sent", "cloud", "game", "control", "now_sent"):
        if src in check:
            tests = [f"{k} {check[k]}" for k in ("eq", "gte", "lte", "gt", "lt", "between", "outside") if k in check]
            where = {"sent": "app sends", "cloud": "cloud returns", "game": "game file", "control": "armrest",
                     "now_sent": "last value sent of"}[src]
            return f"{where} {check[src]} {' '.join(tests)}"
    return "?"


def _leaves(check):
    """All leaf checks of a check tree."""
    for k in ("all", "any", "then", "before"):
        if k in check:
            return [l for c in check[k] for l in _leaves(c)]
    if "not" in check:
        return _leaves(check["not"])
    return [check]


class Evaluator:
    def __init__(self, store, online=None, armrest=True):
        self.store = store
        self.online_override = online
        self.armrest = armrest

    def online(self):
        return self.online_override if self.online_override is not None else self.store.online()

    def eval(self, check, since):
        """-> (TRUE|FALSE|UNKNOWN, time it became true or None)"""
        if "all" in check:
            parts = [self.eval(c, since) for c in check["all"]]
            if any(p[0] == FALSE for p in parts): return FALSE, None
            if any(p[0] == UNKNOWN for p in parts): return UNKNOWN, None
            return TRUE, max(p[1] for p in parts)
        if "any" in check:
            parts = [self.eval(c, since) for c in check["any"]]
            hits = [p[1] for p in parts if p[0] == TRUE]
            if hits: return TRUE, min(hits)
            if all(p[0] == UNKNOWN for p in parts): return UNKNOWN, None
            return FALSE, None
        if "then" in check:
            cursor = since
            for c in check["then"]:
                status, t = self.eval(c, cursor)
                if status != TRUE:
                    return status, None
                cursor = t
            return TRUE, cursor
        if "before" in check:
            # [A, B]: A happened and B had not happened before it ("master on before the pump").
            a, b = check["before"]
            sa, ta = self.eval(a, since)
            if sa != TRUE:
                return sa, None
            sb, tb = self.eval(b, since)
            if sb == TRUE and tb <= ta:
                return FALSE, None
            return TRUE, ta
        if "not" in check:
            s, _ = self.eval(check["not"], since)
            if s == UNKNOWN:
                return UNKNOWN, None
            return (TRUE, since) if s == FALSE else (FALSE, None)
        return self._leaf(check, since)

    def _leaf(self, leaf, since):
        s = self.store
        if "confirm" in leaf:
            # things the simulator can't sense (a walk-around check, the fill station): the trainee presses Done
            for t, k, name, value in s.since(since, "confirm"):
                if name in (leaf["confirm"], "*"):
                    return TRUE, t
            return FALSE, None
        if "now_sent" in leaf:
            # the last value the app sent for this signal, whenever it was sent ("is the lever forward now?")
            cur = s.sent.get(leaf["now_sent"])
            if cur is None:
                return UNKNOWN, None
            return (TRUE, max(cur[1], since)) if value_matches(leaf, cur[0]) else (FALSE, None)
        if "sent" in leaf or "cloud" in leaf:
            kind = "sent" if "sent" in leaf else "cloud"
            if kind == "cloud" and not self.online():
                return UNKNOWN, None
            for t, k, name, value in s.since(since, kind, leaf[kind]):
                if value_matches(leaf, value):
                    return TRUE, t
            return FALSE, None
        if "game" in leaf or "control" in leaf:
            kind = "game" if "game" in leaf else "control"
            if kind == "game" and leaf.get("online") and not self.online():
                return UNKNOWN, None
            if kind == "control" and not self.armrest:
                return UNKNOWN, None
            # A state counts if it was reached at any point since `since` (so "camera 3, then 4, then 1"
            # works), or if it already held when `since` began.
            for t, k, name, value in s.since(since, kind, leaf[kind]):
                if value_matches(leaf, value):
                    return TRUE, t
            cur = (s.game if kind == "game" else s.controls).get(leaf[kind])
            if cur is None:
                return UNKNOWN, None
            if cur[1] <= since and value_matches(leaf, cur[0]):
                return TRUE, since
            return FALSE, None
        return UNKNOWN, None


class LessonRun:
    """One trainee's run through one lesson."""

    def __init__(self, lesson, store, online=None, armrest=True, clock=time.time):
        self.lesson = lesson
        self.steps = [(si, sec["title"], st) for si, sec in enumerate(lesson["sections"]) for st in sec["steps"]]
        self.ev = Evaluator(store, online, armrest)
        self.clock = clock
        self.index = 0
        self.step_started = clock()
        self.log = []                  # (t, kind, step id, text)
        self.mistakes_seen = set()

    @staticmethod
    def load(path):
        with open(path, encoding="utf-8") as fh:
            return json.load(fh)

    @property
    def finished(self):
        return self.index >= len(self.steps)

    def current(self):
        return None if self.finished else self.steps[self.index][2]

    def restart_step(self):
        self.step_started = self.clock()
        self.mistakes_seen = set()

    def poll(self):
        """Check the current step. Returns a dict describing what the panel should show now."""
        if self.finished:
            return {"finished": True}
        si, section, step = self.steps[self.index]
        now = self.clock()
        on_step = now - self.step_started
        mistakes = []
        for i, w in enumerate(step.get("wrong", [])):
            status, _ = self.ev.eval(w["if"], self.step_started)
            if status == TRUE:
                mistakes.append(w["say"])
                if i not in self.mistakes_seen:
                    self.mistakes_seen.add(i)
                    self.log.append((now, "mistake", step["id"], w["say"]))
        status, t_done = self.ev.eval(step["done"], self.step_started)
        hint = None
        for h in step.get("hints", []):
            if on_step >= h["after_s"]:
                hint = h
        view = {"finished": False, "index": self.index, "of": len(self.steps), "section": section,
                "step": step["id"], "say": step["say"], "why": step.get("why"), "controls": step.get("controls", []),
                "seconds_on_step": round(on_step, 1), "done_status": status, "mistakes": mistakes,
                "hint": hint, "hints": [{"after_s": h["after_s"], "say": h["say"]} for h in step.get("hints", [])],
                "check": describe(step["done"]),
                # learn | practice | assess: assess sections run without hints or Show me
                "mode": self.lesson["sections"][si].get("mode", "learn"),
                "confirm": [l["confirm"] for l in _leaves(step["done"]) if "confirm" in l],
                "source": step.get("source"), "figure": step.get("figure")}
        if view["mode"] == "assess":
            view["hint"], view["hints"] = None, []
        if status == TRUE:
            self.log.append((now, "done", step["id"], f"{round(on_step, 1)} s"))
            self.index += 1
            self.restart_step()
            view["advanced"] = True
        return view

    def skip(self, reason):
        if self.finished:
            return
        step = self.steps[self.index][2]
        self.log.append((self.clock(), "skipped", step["id"], reason))
        self.index += 1
        self.restart_step()

    def chatbot_context(self, store_snapshot):
        """What to hand the RAG chatbot when the trainee opens it on the current step."""
        if self.finished:
            return {"lesson": self.lesson["title"], "status": "finished"}
        si, section, step = self.steps[self.index]
        return {
            "about": self.lesson.get("chatbot", {}).get("about"),
            "lesson": self.lesson["title"], "section": section, "step": step["say"],
            "question_hint": step.get("ask"), "seconds_on_step": round(self.clock() - self.step_started),
            "last_controls": store_snapshot.get("last_controls", []),
            "game": store_snapshot.get("game", {}), "lights_on": store_snapshot.get("lights", []),
        }
