using System;
using System.Collections.Generic;
using System.Collections.ObjectModel;
using System.Linq;
using System.Threading;
using System.Threading.Tasks;
using System.Windows;
using System.Windows.Media.Imaging;
using System.Windows.Threading;
using LessonPanel.Controls;
using LessonPanel.Services;

namespace LessonPanel.ViewModels;

/// <summary>Everything the lesson monitor shows, kept current from the simulator API (poll + live stream).</summary>
public sealed class LessonViewModel : Observable, IDisposable
{
    static readonly HashSet<string> LiveControls = new() { "lever", "park_slot", "steering", "foot_switch", "speed_dial" };

    readonly SimApi _api;
    readonly Dispatcher _ui;
    readonly DispatcherTimer _poll = new() { Interval = TimeSpan.FromMilliseconds(500) };
    readonly DispatcherTimer _healthTimer = new() { Interval = TimeSpan.FromSeconds(3) };
    readonly CancellationTokenSource _cts = new();
    readonly Dictionary<string, BitmapImage?> _figures = new();
    readonly Dictionary<string, Task<BitmapImage?>> _loading = new();
    readonly HashSet<string> _pressedThisStep = new();
    readonly HashSet<string> _lit = new();
    readonly Dictionary<string, string> _liveValues = new();
    FigureMap? _map;
    string? _planLesson;
    string? _stepId;
    bool _hintAsked;
    bool _busy;
    bool _choosing;
    DateTime _lessonStarted = DateTime.Now;
    int _mistakeCount;
    readonly HashSet<string> _countedMistakes = new();

    public LessonViewModel(SimApi api, Dispatcher ui)
    {
        _api = api;
        _ui = ui;
        ShowMeCommand = new RelayCommand(async _ => await Act(() => _api.ShowMeAsync(), "Showing you on the armrest..."), _ => Mode == "running" && !_busy && !IsAssess);
        HintCommand = new RelayCommand(_ => { _hintAsked = true; UpdateHint(); }, _ => Mode == "running" && HintAvailable && !HintVisible && !IsAssess);
        ConfirmCommand = new RelayCommand(async p => await ConfirmAsync(p as ConfirmItem), p => p is ConfirmItem c && !c.Done && Mode == "running");
        SkipCommand = new RelayCommand(async _ => await Act(() => _api.SkipAsync(), "Skipped."), _ => Mode == "running" && !_busy);
        // a lesson needs the armrest talking to the Connections app; without it nothing can judge the steps
        StartCommand = new RelayCommand(async p => await StartLessonAsync(p as string), _ => !_busy && ArmrestLinked);
        ChooseCommand = new RelayCommand(_ => { _choosing = true; Mode = "choose"; _ = LoadLessonsAsync(); });
        _poll.Tick += async (_, _) => await PollAsync();
        _healthTimer.Tick += async (_, _) => await HealthAsync();
    }

    // ---- shell state
    string _mode = "connecting";
    public string Mode { get => _mode; set { if (Set(ref _mode, value)) CommandManagerInvalidate(); } }
    string _problem = "";
    public string Problem { get => _problem; set => Set(ref _problem, value); }
    string _toast = "";
    public string Toast { get => _toast; set => Set(ref _toast, value); }
    bool _armrestLinked, _online, _displayOpen, _apiUp;
    public bool ArmrestLinked { get => _armrestLinked; set { if (Set(ref _armrestLinked, value)) CommandManagerInvalidate(); } }
    public bool Online { get => _online; set => Set(ref _online, value); }
    public bool DisplayOpen { get => _displayOpen; set => Set(ref _displayOpen, value); }
    public bool ApiUp { get => _apiUp; set => Set(ref _apiUp, value); }

    // ---- lesson
    string _lessonTitle = "", _machine = "", _objective = "", _stepCounter = "", _stepTimer = "", _lessonTimer = "";
    public string LessonTitle { get => _lessonTitle; set => Set(ref _lessonTitle, value); }
    public string Machine { get => _machine; set => Set(ref _machine, value); }
    public string Objective { get => _objective; set => Set(ref _objective, value); }
    public string StepCounter { get => _stepCounter; set => Set(ref _stepCounter, value); }
    public string StepTimer { get => _stepTimer; set => Set(ref _stepTimer, value); }
    public string LessonTimer { get => _lessonTimer; set => Set(ref _lessonTimer, value); }
    public ObservableCollection<object> Rows { get; } = new();
    public ObservableCollection<LessonChoice> Lessons { get; } = new();

    // ---- lesson chooser: which machine's lessons to list. 612R = Sprayer Operator Experience on the Aug 26 build;
    // R4045 = Sprayer 2019 Operator Experience (Aug 26) or the Apr 20 app. Remembered between runs.
    static readonly string PrefsFile = System.IO.Path.Combine(
        Environment.GetFolderPath(Environment.SpecialFolder.LocalApplicationData), "LessonStudio", "prefs.json");
    readonly List<LessonChoice> _allLessons = new();
    static readonly string[] CourseOrder =
    {
        "612r-controls-tour", "612r-drive-transport", "612r-fill-load", "612r-boom-handling", "612r-field-spraying",
        "612r-no-spray-fault", "612r-full-shift",
        "field-ready-r4045", "headland-hms", "zones-rates", "fold-recovery", "obstacle-right", "no-spray-fault",
    };
    string _chosenMachine = LoadMachinePref();
    string _summary612R = "", _summaryR4045 = "";
    public bool Is612R { get => _chosenMachine == "612R"; set { if (value) ChooseMachine("612R"); } }
    public bool IsR4045 { get => _chosenMachine == "R4045"; set { if (value) ChooseMachine("R4045"); } }
    public string Summary612R { get => _summary612R; set => Set(ref _summary612R, value); }
    public string SummaryR4045 { get => _summaryR4045; set => Set(ref _summaryR4045, value); }
    public string LinkHelp => _chosenMachine == "R4045"
        ? "Lessons are judged from what the app reports, so they can't start yet. In the Connections app, open Sprayer 2019 Operator Experience and press Connect Simulator Bridge; the lessons unlock as soon as it links."
        : "Lessons are judged from what the app reports, so they can't start yet. In the Connections app, open Sprayer Operator Experience (the 612R) and press Connect Simulator Bridge; the lessons unlock as soon as it links. On a real armrest, tick Message Replay Logger first.";

    void ChooseMachine(string key)
    {
        if (_chosenMachine == key) return;
        _chosenMachine = key;
        Raise(nameof(Is612R)); Raise(nameof(IsR4045)); Raise(nameof(LinkHelp));
        ApplyMachineFilter();
        try
        {
            System.IO.Directory.CreateDirectory(System.IO.Path.GetDirectoryName(PrefsFile)!);
            System.IO.File.WriteAllText(PrefsFile, Newtonsoft.Json.JsonConvert.SerializeObject(new { machine = key }));
        }
        catch (Exception) { /* a preference, not worth failing over */ }
    }

    static string LoadMachinePref()
    {
        try
        {
            var o = Newtonsoft.Json.Linq.JObject.Parse(System.IO.File.ReadAllText(PrefsFile));
            var m = (string?)o["machine"];
            if (m == "612R" || m == "R4045") return m;
        }
        catch (Exception) { }
        return "612R";
    }

    void ApplyMachineFilter()
    {
        Lessons.Clear();
        foreach (var l in _allLessons.Where(l => l.MachineKey == _chosenMachine)) Lessons.Add(l);
    }

    static string Summarise(IEnumerable<LessonChoice> lessons)
    {
        var list = lessons.ToList();
        int min = list.Sum(l => l.Minutes);
        string time = min >= 60 ? $"about {min / 60} h {min % 60:00} min" : $"about {min} min";
        return list.Count == 0 ? "No lessons yet" : $"{list.Count} lesson{(list.Count == 1 ? "" : "s")} · {time}";
    }

    // ---- current step
    string _action = "", _why = "", _mistake = "", _hintText = "", _watchingFor = "", _section = "";
    bool _hintVisible, _hintAvailable;
    public string Section { get => _section; set => Set(ref _section, value); }
    public string Action { get => _action; set => Set(ref _action, value); }
    public string Why { get => _why; set => Set(ref _why, value); }
    public string Mistake { get => _mistake; set => Set(ref _mistake, value); }
    public string HintText { get => _hintText; set => Set(ref _hintText, value); }
    public bool HintVisible { get => _hintVisible; set { if (Set(ref _hintVisible, value)) CommandManagerInvalidate(); } }
    public bool HintAvailable { get => _hintAvailable; set { if (Set(ref _hintAvailable, value)) CommandManagerInvalidate(); } }
    public string WatchingFor { get => _watchingFor; set => Set(ref _watchingFor, value); }
    public ObservableCollection<TargetCard> Targets { get; } = new();
    public ObservableCollection<ScreenNote> ScreenNotes { get; } = new();
    public ScreenTargets ScreenTargets { get; private set; } = new();

    // ---- armrest card
    string _stageMode = "handle", _stageCaption = "", _liveState = "", _machineNote = "";
    BitmapImage? _stagePhoto, _handleFigure;
    public string StageMode { get => _stageMode; set => Set(ref _stageMode, value); }
    public BitmapImage? StagePhoto { get => _stagePhoto; set => Set(ref _stagePhoto, value); }
    public string StageCaption { get => _stageCaption; set => Set(ref _stageCaption, value); }
    public string LiveState { get => _liveState; set => Set(ref _liveState, value); }
    public string MachineNote { get => _machineNote; set => Set(ref _machineNote, value); }
    public BitmapImage? HandleFigure { get => _handleFigure; set => Set(ref _handleFigure, value); }
    public HandleMap? HandleMap => _map?.Handle;

    // ---- finished
    string _summary = "";
    public string Summary { get => _summary; set => Set(ref _summary, value); }

    public RelayCommand ConfirmCommand { get; }
    public ObservableCollection<ConfirmItem> ConfirmItems { get; } = new();
    bool _isAssess;
    string _sourceText = "";
    public bool IsAssess { get => _isAssess; set { if (Set(ref _isAssess, value)) CommandManagerInvalidate(); } }
    /// <summary>"Manual page 30-19": where the step comes from.</summary>
    public string SourceText { get => _sourceText; set => Set(ref _sourceText, value); }

    public RelayCommand ShowMeCommand { get; }
    public RelayCommand HintCommand { get; }
    public RelayCommand SkipCommand { get; }
    public RelayCommand StartCommand { get; }
    public RelayCommand ChooseCommand { get; }

    /// <summary>Raised when the handle rings must be redrawn.</summary>
    public event Action<IReadOnlyList<HandleTarget>>? HandleTargetsChanged;
    /// <summary>Raised when the trainee presses a button that has a place on the handle drawing.</summary>
    public event Action<string>? HandlePressed;
    /// <summary>Raised when the display or corner-post targets change (for the ring overlay).</summary>
    public event Action<ScreenTargets>? ScreenTargetsChanged;

    public async Task StartAsync()
    {
        _poll.Start();
        _healthTimer.Start();
        _ = _api.StreamAsync(ev => _ui.BeginInvoke(() => OnEvent(ev)), up => _ui.BeginInvoke(() => ApiUp = up), _cts.Token);
        await HealthAsync();
        await PollAsync();
    }

    /// <summary>Loads the manual figure map and the handle drawing; retried from the health timer until it works,
    /// so the panel recovers when it was started before the API.</summary>
    async Task LoadMapAsync()
    {
        try
        {
            var map = await _api.FigureMapAsync();
            if (map?.Handle == null) return;
            var fig = await Figure(map.Handle.Figure);
            if (fig == null) return;
            _map = map;
            MachineNote = map.MachineNote;
            HandleFigure = fig;
            Raise(nameof(HandleMap));
            PushHandleTargets();
        }
        catch (Exception) { }
    }

    async Task HealthAsync()
    {
        try
        {
            var h = await _api.HealthAsync();
            ApiUp = h?.Ok == true;
            // linked = the armrest is talking to the Connections app, not merely reachable by the API
            ArmrestLinked = h?.Armrest == true && h.ArmrestLink == "connected";
            var appClosed = h?.App != null && h.App.TryGetValue("app", out var a) && a == "exited";
            Online = h?.Online == true && !appClosed;
            DisplayOpen = !appClosed && h?.App != null && h.App.TryGetValue("display", out var d) && !string.IsNullOrEmpty(d);
            if (Mode == "offline") Mode = "connecting";
            if (_map == null) await LoadMapAsync();
        }
        catch (Exception)
        {
            ApiUp = false;
            Mode = "offline";
            Problem = "The lesson panel can't reach the simulator API on this PC (127.0.0.1:47900). Start it from the lesson-studio folder with: python -I run_simapi.py";
        }
    }

    async Task PollAsync()
    {
        if (Mode == "offline") return;
        if (_choosing) { if (Mode != "choose") Mode = "choose"; return; }   // the trainee asked for the chooser
        LessonResponse? r;
        try { r = await _api.LessonAsync(); }
        catch (Exception) { return; }
        if (r == null) return;
        if (!r.Running)
        {
            if (Mode != "choose") { Mode = "choose"; await LoadLessonsAsync(); }
            return;
        }
        var v = r.View;
        if (v == null) return;
        if (v.Finished)
        {
            if (Mode != "finished") await ShowFinishedAsync();
            return;
        }
        if (_planLesson != r.Lesson) await LoadPlanAsync(r.Lesson!);
        Mode = "running";
        ApplyStep(v);
    }

    async Task LoadLessonsAsync()
    {
        try
        {
            var list = await _api.LessonsAsync() ?? Array.Empty<LessonInfo>();
            _allLessons.Clear();
            foreach (var l in list)
                _allLessons.Add(new LessonChoice
                {
                    Id = l.Id, Title = l.Title, Machine = l.Machine, MachineKey = LessonChoice.KeyFor(l.Machine),
                    Minutes = l.Minutes ?? 0,
                    Length = l.Minutes is int m ? $"{l.Steps} steps · about {m} min" : $"{l.Steps} steps",
                });
            // the order a trainee takes them in (cab first, full day last); unknown lessons after, by length
            int Rank(LessonChoice l) { int i = Array.IndexOf(CourseOrder, l.Id); return i < 0 ? 100 + l.Minutes : i; }
            _allLessons.Sort((a, b) => Rank(a).CompareTo(Rank(b)));
            Summary612R = Summarise(_allLessons.Where(l => l.MachineKey == "612R"));
            SummaryR4045 = Summarise(_allLessons.Where(l => l.MachineKey == "R4045"));
            ApplyMachineFilter();
        }
        catch (Exception) { }
    }

    async Task LoadPlanAsync(string lessonId)
    {
        var plan = await _api.PlanAsync();
        if (plan == null || !plan.Running) return;
        _planLesson = lessonId;
        _lessonStarted = DateTime.Now;
        _mistakeCount = 0;
        _countedMistakes.Clear();
        LessonTitle = plan.Title;
        Machine = plan.Machine;
        Objective = plan.Objective;
        Rows.Clear();
        var n = 0;
        foreach (var s in plan.Sections)
        {
            Rows.Add(new SectionRow(s.Title));
            foreach (var st in s.Steps)
            {
                var row = new StepRow(++n, st.Id, st.Say) { FigureKey = st.Figure, State = st.Status ?? "upcoming" };
                Rows.Add(row);
                if (st.Figure != null) _ = LoadThumbAsync(row, st.Figure);
            }
        }
    }

    async Task LoadThumbAsync(StepRow row, string key) => row.Thumb = await Figure(key);

    void ApplyStep(StepView v)
    {
        var changed = v.Step != _stepId;
        if (changed)
        {
            _stepId = v.Step;
            _pressedThisStep.Clear();
            _hintAsked = false;
            Section = v.Section;
            Action = v.Say;
            Why = v.Why;
            WatchingFor = string.IsNullOrEmpty(v.Check) ? "" : "Watching for: " + PlainCheck(v.Check);
            StepCounter = $"Step {v.Index + 1} of {v.Of}";
            var done = true;
            foreach (var row in Rows.OfType<StepRow>())
            {
                if (row.Id == v.Step) { row.State = "current"; done = false; }
                else if (done) { if (row.State != "skipped") row.State = "done"; }
                else if (row.State == "current") row.State = "upcoming";
            }
            IsAssess = v.Mode == "assess";
            SourceText = v.Source?.Pages.Count > 0
                ? (v.Source.Pages.Count == 1 ? "Manual page " : "Manual pages ") + string.Join(", ", v.Source.Pages) : "";
            ConfirmItems.Clear();
            foreach (var c in v.Confirm) ConfirmItems.Add(new ConfirmItem(c));
            BuildTargets(v);
            ScreenTargets = v.Screen;
            ScreenNotes.Clear();
            foreach (var t in v.Screen.Press) ScreenNotes.Add(new ScreenNote("Touch", t.Label, WindowName(t.Window)));
            foreach (var t in v.Screen.Watch) ScreenNotes.Add(new ScreenNote("Watch", t.Label, WindowName(t.Window)));
            ScreenTargetsChanged?.Invoke(v.Screen);
        }
        Mistake = v.Mistakes.Count > 0 ? v.Mistakes[^1] : "";
        foreach (var m in v.Mistakes)
            if (_countedMistakes.Add(v.Step + "|" + m)) _mistakeCount++;
        StepTimer = Clock(v.SecondsOnStep);
        LessonTimer = Clock((DateTime.Now - _lessonStarted).TotalSeconds);
        var first = v.Hints.FirstOrDefault();
        HintAvailable = first != null && !string.IsNullOrEmpty(first.Say);
        HintText = v.Hint?.Say ?? first?.Say ?? "";
        UpdateHint(v);
        UpdateLiveState();
    }

    void BuildTargets(StepView v)
    {
        Targets.Clear();
        var order = 0;
        foreach (var a in v.Armrest)
        {
            var m = a.Manual;
            var key = m?.Figures.FirstOrDefault();
            var fig = key == null ? null : v.Figures.FirstOrDefault(f => f.Key == key);
            var card = new TargetCard
            {
                Order = ++order,
                ControlId = a.Id,
                Label = a.Label,
                Where = m?.Where ?? a.Module,
                HandleLetter = m?.Handle,
                FigureKey = key,
                PageText = fig?.Page is int p ? $"Manual page {p}" : null,
                Note = m?.Certainty switch
                {
                    "inferred" => "Position inferred: the manual's handle has no such button.",
                    "likely" => "Position read from the manual's drawing; check it on the machine.",
                    _ => null
                },
                Lit = _lit.Contains(a.Id)
            };
            Targets.Add(card);
            if (key != null) _ = LoadCardPhotoAsync(card, key);
        }
        // armrest card: the handle drawing when a target sits on the handle, else the first target's photo,
        // else the step's own manual figure (walk-around and fill-station steps)
        var onHandle = Targets.Any(t => !string.IsNullOrEmpty(t.HandleLetter));
        var first = Targets.FirstOrDefault(t => t.FigureKey != null) ?? Targets.FirstOrDefault();
        var stepFigure = v.Figure;
        StageMode = onHandle ? "handle" : (first?.FigureKey != null || stepFigure != null ? "photo" : "none");
        if (!onHandle)
        {
            StagePhoto = null;
            if (first?.FigureKey != null)
            {
                StageCaption = $"{first.Label}: {first.Where}";
                _ = LoadStagePhotoAsync(first.FigureKey);
            }
            else if (stepFigure != null)
            {
                var f = v.Figures.FirstOrDefault(x => x.Key == stepFigure);
                StageCaption = f?.Page is int p ? $"From the manual, page {p}" : "From the manual";
                _ = LoadStagePhotoAsync(stepFigure);
            }
        }
        PushHandleTargets();
    }

    async Task LoadCardPhotoAsync(TargetCard c, string key) => c.Photo = await Figure(key);
    async Task LoadStagePhotoAsync(string key) => StagePhoto = await Figure(key);

    void PushHandleTargets()
    {
        var list = Targets.Where(t => !string.IsNullOrEmpty(t.HandleLetter))
                          .Select(t => new HandleTarget(t.HandleLetter!, t.Order, t.Done)).ToList();
        HandleTargetsChanged?.Invoke(list);
    }

    void UpdateHint(StepView? v = null)
    {
        var due = v != null && v.Hint != null;      // the API sends "hint" only once one is due
        HintVisible = HintAvailable && (_hintAsked || due || HintVisible && v == null);
    }

    void OnEvent(SimEvent ev)
    {
        switch (ev.Kind)
        {
            case "control":
                if (LiveControls.Contains(ev.Name)) { _liveValues[ev.Name] = ev.Value; UpdateLiveState(); }
                if (ev.Value == "0") break;
                var card = Targets.FirstOrDefault(t => t.ControlId == ev.Name);
                if (card != null)
                {
                    if (!LiveControls.Contains(ev.Name) || ev.Name == "foot_switch") card.Done = true;
                    if (!string.IsNullOrEmpty(card.HandleLetter)) { HandlePressed?.Invoke(card.HandleLetter!); PushHandleTargets(); }
                }
                break;
            case "led":
                if (ev.Value == "1") _lit.Add(ev.Name); else _lit.Remove(ev.Name);
                foreach (var t in Targets.Where(t => t.ControlId == ev.Name)) t.Lit = ev.Value == "1";
                break;
            case "lesson":
                _ = PollAsync();
                break;
            case "link":
                ArmrestLinked = ev.Name == "connected";
                break;
        }
    }

    void UpdateLiveState()
    {
        var parts = new List<string>();
        foreach (var t in Targets)
        {
            if (!_liveValues.TryGetValue(t.ControlId, out var v)) continue;
            parts.Add(t.ControlId switch
            {
                "lever" => int.TryParse(v, out var lv) ? $"Lever at {lv} ({(lv > 130 ? "forward" : lv < 120 ? "back" : "neutral")})" : $"Lever {v}",
                "park_slot" => v == "1" ? "Lever in park" : "Lever out of park",
                "steering" => $"Wheel turned {v} degrees",
                "foot_switch" => v == "1" ? "Foot switch held" : "Foot switch released",
                "speed_dial" => $"Speed dial at step {v}",
                _ => ""
            });
        }
        LiveState = string.Join(" · ", parts.Where(p => p.Length > 0));
    }

    async Task ShowFinishedAsync()
    {
        Mode = "finished";
        var skipped = Rows.OfType<StepRow>().Count(r => r.IsSkipped);
        foreach (var row in Rows.OfType<StepRow>()) if (row.State == "current" || row.State == "upcoming") row.State = "done";
        Summary = $"{Rows.OfType<StepRow>().Count()} steps in {Clock((DateTime.Now - _lessonStarted).TotalSeconds)}"
                  + (_mistakeCount > 0 ? $" · {_mistakeCount} mistake{(_mistakeCount == 1 ? "" : "s")} explained" : " · no mistakes")
                  + (skipped > 0 ? $" · {skipped} skipped" : "");
        Targets.Clear();
        ScreenNotes.Clear();
        ScreenTargetsChanged?.Invoke(new ScreenTargets());
        HandleTargetsChanged?.Invoke(Array.Empty<HandleTarget>());
        await Task.CompletedTask;
    }

    async Task StartLessonAsync(string? id)
    {
        if (string.IsNullOrEmpty(id)) return;
        _busy = true;
        Toast = "Setting up the simulator for this lesson...";
        try
        {
            try { await _api.SetupLessonAsync(id); } catch (Exception) { /* real rigs: the trainer sets it up */ }
            await _api.StartLessonAsync(id);
            _choosing = false;
            _planLesson = null;
            _stepId = null;
            Toast = "";
            await PollAsync();
        }
        catch (Exception ex) { Toast = "Couldn't start the lesson: " + ex.Message; }
        finally { _busy = false; CommandManagerInvalidate(); }
    }

    /// <summary>The trainee marks something Done that the simulator can't sense.</summary>
    async Task ConfirmAsync(ConfirmItem? item)
    {
        if (item == null) return;
        try
        {
            await _api.ConfirmAsync(item.Text);
            item.Done = true;
            CommandManagerInvalidate();
            await PollAsync();
        }
        catch (Exception ex) { Toast = "Couldn't record that: " + ex.Message; }
    }

    async Task Act(Func<Task> call, string toast)
    {
        _busy = true;
        Toast = toast;
        try { await call(); await PollAsync(); }
        catch (Exception ex) { Toast = "That didn't work: " + ex.Message; }
        finally
        {
            _busy = false;
            CommandManagerInvalidate();
            _ = ClearToastAsync(toast);
        }
    }

    async Task ClearToastAsync(string toast)
    {
        await Task.Delay(2500);
        if (Toast == toast) Toast = "";
    }

    /// <summary>One download per figure, shared by everyone asking at once; a failure is not remembered,
    /// so the next request tries again.</summary>
    Task<BitmapImage?> Figure(string key)
    {
        if (_figures.TryGetValue(key, out var done) && done != null) return Task.FromResult<BitmapImage?>(done);
        if (_loading.TryGetValue(key, out var pending)) return pending;
        var t = LoadFigureAsync(key);
        _loading[key] = t;
        return t;
    }

    async Task<BitmapImage?> LoadFigureAsync(string key)
    {
        BitmapImage? img = null;
        for (var attempt = 0; attempt < 3 && img == null; attempt++)
        {
            try { img = await _api.ImageAsync($"/api/manual/{key}.png"); }
            catch (Exception) { await Task.Delay(300); }
        }
        _loading.Remove(key);
        if (img != null) _figures[key] = img;
        return img;
    }

    static string WindowName(string w) => w == "pdu" ? "corner post" : w == "display" ? "Gen 4 display" : w;
    static string Clock(double s) => TimeSpan.FromSeconds(Math.Max(0, s)).ToString(s >= 3600 ? @"h\:mm\:ss" : @"m\:ss");

    /// <summary>"app sends PLT_MHC_HMS eq 1" reads better as "the app to send PLT_MHC_HMS = 1".</summary>
    static string PlainCheck(string check) => check.Replace(" eq ", " = ").Replace(" ne ", " is not ").Replace(" gt ", " above ").Replace(" lt ", " below ");

    static void CommandManagerInvalidate() => System.Windows.Input.CommandManager.InvalidateRequerySuggested();

    public void Dispose()
    {
        _cts.Cancel();
        _poll.Stop();
        _healthTimer.Stop();
    }
}
