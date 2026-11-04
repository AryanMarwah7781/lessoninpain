"""Machine state and event history, fed by the sources. Thread-safe. Standard library only."""
import threading
import time
from collections import deque


class Store:
    def __init__(self, history=5000):
        self._lock = threading.RLock()
        self.events = deque(maxlen=history)          # (t, kind, name, value)
        self.sent, self.cloud, self.game, self.controls, self.leds = {}, {}, {}, {}, {}
        self.app = {}                                 # milestone -> (detail, t)
        self.armrest_link = None
        self._subs = []
        self.started = time.time()

    # ---- writing
    def add(self, ev):
        t, kind, name, value = ev
        with self._lock:
            self.events.append(ev)
            if kind == "sent": self.sent[name] = (value, t)
            elif kind == "cloud": self.cloud[name] = (value, t)
            elif kind == "game": self.game[name] = (value, t)
            elif kind == "control": self.controls[name] = (value, t)
            elif kind == "led": self.leds[name] = (value, t)
            elif kind == "app":
                if name == "app" and value in ("started", "exited"):   # app restarted or closed: its cloud state is gone
                    self.app.clear()
                    self.cloud.clear()
                self.app[name] = (value, t)
            elif kind == "link": self.armrest_link = (name, t)
            subs = list(self._subs)
        for fn in subs:
            try:
                fn(ev)
            except Exception:
                pass

    def subscribe(self, fn):
        with self._lock:
            self._subs.append(fn)
        return lambda: self._subs.remove(fn)

    # ---- reading
    def since(self, t0, kind=None, name=None):
        with self._lock:
            return [e for e in self.events if e[0] >= t0 and (kind is None or e[1] == kind) and (name is None or e[2] == name)]

    def online(self):
        """True once the cloud has talked to the app since this store started (sign-in + machine sim)."""
        with self._lock:
            link = self.app.get("cloud_link")
            if link and link[0] == "down":
                return False
            return bool(self.cloud) or bool(link and link[0] == "up")

    def snapshot(self):
        with self._lock:
            def flat(d):
                return {k: v[0] for k, v in d.items()}
            return {
                "online": self.online(),
                "armrest": self.armrest_link[0] if self.armrest_link else None,
                "game": flat(self.game),
                "sent": flat(self.sent),
                "cloud": flat(self.cloud),
                "controls": flat(self.controls),
                "lights": sorted(k for k, v in self.leds.items() if v[0] == "1"),
                "app": {k: v[0] for k, v in self.app.items()},
                "last_controls": [e[2] for e in list(self.events)[::-1] if e[1] == "control" and e[3] == "1"][:10],
            }
