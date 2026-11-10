/* Operations panel: the app's two scenarios plus the 612R lessons (window.OPS_LESSONS from lessons.js).
   Opened from the app folder (file:) it lists the steps and keeps looking for Lesson Studio's simulator API;
   once the API answers it moves to the API's copy of this page, which follows the running lesson live. */
"use strict";

const API = "http://127.0.0.1:47900";
const LIVE = location.protocol === "http:";
const LESSONS = Array.isArray(window.OPS_LESSONS) ? window.OPS_LESSONS : [];

// The app's own scenarios, as its Operations page shows them (spelling fixed).
const GUIDES = [
    {
        id: "guide-begin-spraying", title: "Begin Spraying",
        steps: [["Turn ON Solution Pump 1", "solution_pump.png"],
                ["Turn ON Solution Pump 2 (See & Spray™ Ultimate only)", "sprayer_solution_pump1.png"],
                ["Set Engine Speed", "engine_speed_sprayer.png"],
                ["Disengage Park Brake", "park_brake.png"],
                ["Move Multi-Function Lever forward", "combine_foward.png"],
                ["Turn ON Master Switch", "master_switch_sprayer.png"]],
        tips: [["To increase target speed, turn the Speed Range Adjustment Dial on the Multi-Function Lever", "handle_adjustment_wheel.png"],
               ["Press the Adjustment Dial to toggle between Field 1 and Field 2 set speeds", "handle_adjustment_wheel.png"]],
    },
    {
        id: "guide-see-spray", title: "Enable See & Spray",
        steps: [["Go to Work Setup and set Crop Type to “No Crop” (See & Spray™ Select only)", "gen4_work_setup.png"],
                ["Go to Display Menu", "gen4_menu.png"],
                ["Select See & Spray", "sprayer_see_spray.png"],
                ["Select Nozzle Turret Setup", "sprayer_turret_setup.png"],
                ["Set Spray Method for Nozzle B to See & Spray", "sprayer_spray_method.png"],
                ["Go to CommandARM and turn on Nozzle B", "sprayer_nozzleB.png"]],
        tips: [],
    },
];

const $ = id => document.getElementById(id);
const sheet = $("sheet");
const picker = $("scenario");

/** Small DOM builder: h("p", {class: "x"}, "text", child). Text always goes in as text, never as HTML. */
function h(tag, attrs, ...kids) {
    const el = document.createElement(tag);
    for (const [k, v] of Object.entries(attrs || {})) {
        if (v === null || v === undefined || v === false) continue;
        if (k.startsWith("on")) el.addEventListener(k.slice(2), v);
        else el.setAttribute(k, v === true ? "" : v);
    }
    for (const kid of kids.flat(Infinity)) {
        if (kid === null || kid === undefined || kid === false) continue;
        el.append(kid instanceof Node ? kid : document.createTextNode(String(kid)));
    }
    return el;
}

/** replaceChildren that skips null/false and flattens lists (replaceChildren itself would print "null"). */
function put(el, ...kids) {
    el.replaceChildren(...kids.flat(Infinity).filter(k => k !== null && k !== undefined && k !== false));
}

const SVG_NS = "http://www.w3.org/2000/svg";
function icon(kind) {
    const svg = document.createElementNS(SVG_NS, "svg");
    svg.setAttribute("viewBox", "0 0 16 16");
    svg.setAttribute("aria-hidden", "true");
    const p = document.createElementNS(SVG_NS, "path");
    p.setAttribute("fill", "none");
    p.setAttribute("stroke", "currentColor");
    p.setAttribute("stroke-width", "2");
    p.setAttribute("stroke-linecap", "round");
    p.setAttribute("stroke-linejoin", "round");
    p.setAttribute("d", { check: "M3 8.5l3.2 3L13 4.5", skip: "M4 8h8", tip: "M8 4.5v4M8 11.5v.01" }[kind]);
    svg.append(p);
    return svg;
}

const figureUrl = key => LIVE ? `/api/manual/${key}.png` : `images/manual/${key}.png`;
const lessonById = id => LESSONS.find(l => l.id === id);
const stepsOf = lesson => lesson.sections.flatMap(s => s.steps);
const modeName = { practice: "Practice", assess: "Assessment: no hints" };

// ---------------------------------------------------------------- state
let selected = null;          // scenario id in the dropdown
let apiUp = LIVE ? null : false;
let health = null;
let run = null;               // {lesson, view} while the API runs a lesson
let plan = null;              // /api/lesson/plan: step statuses for the running lesson
let planKey = "";
let busy = false;
let liveKey = "";             // what the current step's live part shows, so polls only redraw on change
let confirmed = new Set();    // Done items pressed on the current step
let hintsAsked = 0;           // hints the trainee asked for early on the current step
let lastStep = null;

function remember(id) { try { localStorage.setItem("ops.scenario", id); } catch (e) { /* storage off */ } }
function recalled() { try { return localStorage.getItem("ops.scenario"); } catch (e) { return null; } }

// ---------------------------------------------------------------- dropdown
function fillPicker() {
    put(picker);
    if (LESSONS.length) {
        picker.append(h("optgroup", { label: "612R lessons" },
            LESSONS.map(l => h("option", { value: l.id }, l.minutes ? `${l.title} (${l.minutes} min)` : l.title))));
    }
    picker.append(h("optgroup", { label: "Quick guides" }, GUIDES.map(g => h("option", { value: g.id }, g.title))));
    const wanted = new URLSearchParams(location.search).get("s") || recalled();
    const known = id => id && (lessonById(id) || GUIDES.some(g => g.id === id));
    selected = known(wanted) ? wanted : (LESSONS[0] || GUIDES[0]).id;
    picker.value = selected;
}

picker.addEventListener("change", () => {
    selected = picker.value;
    remember(selected);
    render();
    sheet.scrollTop = 0;
});

// ---------------------------------------------------------------- status line
function setStatus(text, tone) {
    const el = $("status");
    el.hidden = !text;
    el.textContent = text || "";
    el.className = "status" + (tone ? " is-" + tone : "");
}

function showStatus() {
    if (!LIVE) {
        return setStatus(LESSONS.length
            ? "Lesson Studio isn't running on this PC, so the steps won't tick off. Start Lesson Studio to follow a lesson live."
            : "", null);
    }
    if (apiUp === false) {
        return setStatus("Lost Lesson Studio on this PC. Start it again with Start Lesson Studio; the lesson carries on from where the simulator is.", "warn");
    }
    if (!health) return setStatus("Connecting to Lesson Studio…", null);
    const src = health.armrest_source;
    if (src === "virtual") return setStatus("Live · virtual armrest linked", "live");
    if (src) return setStatus("Live · real armrest: a press can take up to 2 s to tick off", "live");
    setStatus("Live · armrest not linked. With the real box, tick Message Replay Logger, then Disconnect and Connect.", "warn");
}

// ---------------------------------------------------------------- rendering
function render() {
    liveKey = "";
    const guide = GUIDES.find(g => g.id === selected);
    if (guide) return renderGuide(guide);
    const lesson = lessonById(selected);
    if (!lesson) return put(sheet, h("p", { class: "empty" }, "This lesson isn't on this PC."));
    if (run && run.lesson === lesson.id) return renderRun(lesson);
    renderIntro(lesson);
}

function guideRow(n, text, img, isTip) {
    return h("li", { class: "row" },
        h("span", { class: "mark" }, isTip ? icon("tip") : `${n}.`),
        h("p", { class: "say" }, text),
        h("img", { class: "thumb", src: `images/${img}`, alt: "" }));
}

function renderGuide(g) {
    put(sheet, 
        h("ol", { class: "steps" }, g.steps.map(([t, img], i) => guideRow(i + 1, t, img))),
        g.tips.length ? h("ul", { class: "tips", "aria-label": "Tips" }, g.tips.map(([t, img]) => guideRow(0, t, img, true))) : null);
}

function stepRow(step, n, state) {
    return h("li", { class: "row" + (state ? " is-" + state : ""), id: "step-" + step.id, "data-step": step.id },
        h("span", { class: "mark" }, state === "done" ? icon("check") : state === "skipped" ? icon("skip") : `${n}.`),
        h("div", { class: "body" },
            h("p", { class: "say" }, step.say,
                step.draft ? h("span", { class: "draft", title: "The button for this step is not yet confirmed on the 612R simulator" }, "draft") : null)),
        step.figure ? h("img", { class: "thumb", src: figureUrl(step.figure), alt: "", loading: "lazy" }) : h("span", { class: "thumb" }));
}

function stepList(lesson, stateOf) {
    let n = 0;
    return lesson.sections.map(sec => [
        h("h3", { class: "section-title" }, sec.title, modeName[sec.mode] ? h("span", { class: "mode" }, modeName[sec.mode]) : null),
        h("ol", { class: "steps" }, sec.steps.map(st => stepRow(st, ++n, stateOf(st)))),
    ]);
}

function lessonMeta(lesson) {
    const n = stepsOf(lesson).length;
    return `${n} steps` + (lesson.minutes ? ` · about ${lesson.minutes} min` : "");
}

function renderIntro(lesson) {
    const checkpoints = lesson.sections.map((s, i) => ({ s, i })).filter(x => x.i > 0 && x.s.checkpoint);
    const other = run && !run.view?.finished ? lessonById(run.lesson) : null;
    const realRig = !LIVE || !health || health.armrest_source !== "virtual";
    const from = checkpoints.length
        ? h("label", {}, "Start at", h("select", { id: "from" },
            h("option", { value: "0" }, lesson.sections[0].title),
            checkpoints.map(x => h("option", { value: String(x.i) }, x.s.title))))
        : null;
    const start = LIVE ? h("div", { class: "start-row" },
        h("button", { class: "primary", id: "start", onclick: () => startLesson(lesson.id), disabled: apiUp === false || busy },
            busy ? "Setting up the simulator…" : other ? "Start this lesson" : "Start lesson"),
        from) : null;
    put(sheet, 
        h("section", { class: "intro" },
            h("h2", {}, lesson.title),
            h("p", { class: "meta" }, lessonMeta(lesson)),
            lesson.objective ? h("p", {}, lesson.objective) : null,
            start,
            other ? h("p", { class: "note" }, `Starting it stops “${other.title}”, which is running now.`) : null,
            lesson.trainer ? h("details", { open: realRig },
                h("summary", {}, "Before you start"),
                h("p", {}, lesson.trainer)) : null),
        stepList(lesson, () => null));
}

function renderRun(lesson) {
    const view = run.view || {};
    const steps = stepsOf(lesson);
    const status = {};
    for (const sec of plan?.sections || []) for (const st of sec.steps) if (st.status) status[st.id] = st.status;
    const current = view.finished ? null : view.step;
    const stateOf = st => st.id === current ? "current" : status[st.id] || null;
    const done = steps.filter(st => status[st.id] === "done").length;
    const skipped = steps.filter(st => status[st.id] === "skipped").length;

    const head = view.finished
        ? h("section", { class: "complete" },
            h("h2", {}, "Lesson complete"),
            h("p", {}, `${done} of ${steps.length} steps done` + (skipped ? ` · ${skipped} skipped` : "")),
            h("div", { class: "actions" }, nextLessonButton(lesson),
                h("button", { class: "quiet", onclick: () => stopLesson() }, "Close lesson")))
        : h("div", { class: "progress" },
            h("div", { class: "progress-line" },
                h("p", { class: "progress-text" },
                    h("strong", {}, `Step ${view.index + 1} of ${view.of}`), " ", h("span", {}, view.section || "")),
                h("button", { class: "quiet", onclick: () => stopLesson() }, "Stop lesson")),
            h("div", { class: "bar", role: "progressbar", "aria-valuemin": "0", "aria-valuemax": String(view.of),
                "aria-valuenow": String(view.index), "aria-label": "Lesson progress" },
                h("i", { style: `width:${Math.round(100 * view.index / Math.max(1, view.of))}%` })));
    put(sheet, head, stepList(lesson, stateOf));

    if (current) {
        const row = document.getElementById("step-" + current);
        const step = steps.find(st => st.id === current);
        if (row && step) fillCurrent(row, step, view);
        if (row && current !== lastStep) {
            // put the step just under the progress strip (the sheet is the rows' offset parent)
            const smooth = lastStep && !matchMedia("(prefers-reduced-motion: reduce)").matches;
            const strip = sheet.querySelector(".progress");
            sheet.scrollTo({ top: row.offsetTop - (strip ? strip.offsetHeight : 0), behavior: smooth ? "smooth" : "auto" });
        }
    }
    lastStep = current;
}

function nextLessonButton(lesson) {
    const i = LESSONS.findIndex(l => l.id === lesson.id);
    const next = LESSONS[i + 1];
    return next ? h("button", { class: "primary", onclick: () => { stopLesson(next.id); } }, `Next: ${next.title}`) : null;
}

/** The current step's own block: why, the manual figure, then the live part (hint, mistakes, buttons). */
function fillCurrent(row, step, view) {
    const body = row.querySelector(".body");
    if (step.why) body.append(h("p", { class: "why" }, step.why));
    if (step.figure) {
        body.append(h("figure", { class: "figure" },
            h("img", { src: figureUrl(step.figure), alt: `Operator's manual figure ${step.figure}` }),
            h("figcaption", {}, `Operator's manual, figure ${step.figure}`)));
    }
    body.append(h("div", { class: "live", id: "live" }));
    updateLive(step, view);
}

function updateLive(step, view) {
    const box = $("live");
    if (!box) return;
    const assess = view.mode === "assess";
    const hints = assess ? [] : (view.hints || []);
    const due = hints.filter(x => (view.seconds_on_step || 0) >= x.after_s).length;
    const shown = Math.min(hints.length, Math.max(due, hintsAsked));
    const virtual = health && health.armrest_source === "virtual";
    const key = JSON.stringify([shown, view.mistakes, view.confirm, [...confirmed], virtual, assess, busy, apiUp]);
    if (key === liveKey) return;
    liveKey = key;

    const items = (view.confirm && view.confirm.length ? view.confirm : step.confirm) || [];
    put(box, 
        shown ? h("p", { class: "callout hint" }, h("b", {}, "Hint"), hints[shown - 1].say) : null,
        (view.mistakes || []).map(m => h("p", { class: "callout wrong", role: "alert" }, h("b", {}, "Not quite."), m)),
        h("div", { class: "actions" },
            items.map(item => {
                const isDone = confirmed.has(item);
                return h("button", { class: "confirm" + (isDone ? " is-done" : ""), disabled: isDone || busy || apiUp === false,
                    onclick: () => confirmItem(item) }, icon("check"), isDone ? `${item}: done` : item);
            }),
            !assess && virtual ? h("button", { class: "quiet", disabled: busy || apiUp === false, onclick: showMe }, "Show me") : null,
            !assess && shown < hints.length ? h("button", { class: "quiet", onclick: () => { hintsAsked = shown + 1; updateLive(step, run.view); } },
                shown ? "Another hint" : "Hint") : null,
            h("button", { class: "quiet", disabled: busy || apiUp === false, onclick: skipStep }, "Skip step")));
}

// ---------------------------------------------------------------- API (live page only: same origin as the API)
async function getJSON(path) {
    const r = await fetch(path, { cache: "no-store" });
    if (!r.ok) throw new Error(`${path}: ${r.status}`);
    return r.json();
}

async function post(path, body) {
    const r = await fetch(path, { method: "POST", headers: { "Content-Type": "application/json" }, body: JSON.stringify(body || {}) });
    const j = await r.json().catch(() => ({}));
    if (!r.ok) throw new Error(j.error || `${path}: ${r.status}`);
    return j;
}

function setApi(up) {
    if (apiUp === up) return;
    apiUp = up;
    showStatus();
    render();
}

async function act(fn) {
    if (busy) return;
    busy = true;
    liveKey = "";
    render();
    try { await fn(); } catch (e) { setStatus("That didn't work: " + e.message, "warn"); }
    busy = false;
    await pollLesson(true);
}

function startLesson(id) {
    const from = $("from");
    const section = from ? Number(from.value) : 0;
    act(async () => {
        try { await post("/api/lesson/setup", { id }); } catch (e) { /* a real rig: the trainer sets it up */ }
        await post("/api/lesson/start", section ? { id, section } : { id });
        planKey = "";
        lastStep = null;
    });
}

function stopLesson(thenSelect) {
    act(async () => {
        await post("/api/lesson/stop");
        run = null;
        plan = null;
        planKey = "";
        if (thenSelect) { selected = thenSelect; picker.value = thenSelect; remember(thenSelect); sheet.scrollTop = 0; }
    });
}

const skipStep = () => act(() => post("/api/lesson/skip"));
const showMe = () => act(() => post("/api/lesson/showme"));
function confirmItem(item) {
    act(async () => { await post("/api/lesson/confirm", { item }); confirmed.add(item); });
}

async function pollLesson(force) {
    let r;
    try {
        r = await getJSON("/api/lesson");
        setApi(true);
    } catch (e) {
        setApi(false);
        return;
    }
    if (!r.running) {
        if (run || force) { run = null; plan = null; planKey = ""; render(); }
        return;
    }
    const view = r.view || {};
    const fresh = !run || run.lesson !== r.lesson;
    const key = r.lesson + ":" + (view.finished ? "end" : view.index);
    run = { lesson: r.lesson, view };
    if (fresh && lessonById(r.lesson) && selected !== r.lesson) {
        selected = r.lesson;            // a lesson started here or in Lesson Studio: follow it
        picker.value = selected;
        remember(selected);
    }
    if (key !== planKey || force) {
        try { plan = await getJSON("/api/lesson/plan"); } catch (e) { return; }
        planKey = key;
        if (view.step !== lastStep) { confirmed = new Set(); hintsAsked = 0; }
        if (selected === r.lesson) render();
        return;
    }
    if (selected === r.lesson && !view.finished) {
        const lesson = lessonById(r.lesson);
        const step = lesson && stepsOf(lesson).find(st => st.id === view.step);
        if (step) updateLive(step, view);
    }
}

async function pollHealth() {
    try {
        const was = health && health.armrest_source;
        health = await getJSON("/api/health");
        setApi(true);
        showStatus();
        if (was !== health.armrest_source) { liveKey = ""; render(); }
    } catch (e) {
        setApi(false);
    }
}

// ---------------------------------------------------------------- from the app folder: look for the API
function lookForApi() {
    const probe = new Image();
    probe.onload = () => location.replace(`${API}/operations/OperatingProcedure.html?s=${encodeURIComponent(selected)}`);
    probe.onerror = () => setTimeout(lookForApi, 4000);
    probe.src = `${API}/operations/images/park_brake.png?t=${Date.now()}`;
}

// ---------------------------------------------------------------- start
fillPicker();
showStatus();
render();
if (LIVE) {
    pollHealth();
    pollLesson();
    setInterval(pollLesson, 500);
    setInterval(pollHealth, 3000);
} else {
    lookForApi();
}
