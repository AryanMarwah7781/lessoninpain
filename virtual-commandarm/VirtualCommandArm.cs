// Virtual CommandARM: stands in for the SBM box (the USB "Simulator Bridge Module") so the Apr 20
// Connections app can be driven without hardware.
//
// How the app finds us: if a process named "SBMEmulator" is running when "Connect to Simulator Bridge"
// is pressed, the app serves the named pipe \\.\pipe\ConnectionsAppToSBMEmulator instead of opening the
// USB COM port (SBMCommnHandler.cs:117, SBMNamedPipeInterface.cs). So this exe MUST be named SBMEmulator.exe.
//
// Wire format (decoded in re/apr20-connections/reports/01-app-controls.md section 2.2):
//   frames are COBS-encoded and end in 0x00; payload is MessagePack [msgId, {key: value}].
//   The app polls with [64,85] (data) and [59,0] (CAN rx) and reads ONE reply to each.
//   It pushes button-light messages (61 DCM, 63 SCM) and CAN tx (60) without expecting a reply.
//
// Every control, key and light comes from controls.json next to the exe.
//
// Scripted control: a text protocol on 127.0.0.1:47800 (one command per line, "help" lists them),
// used by the tests and later by the lesson panel's "show me".
//
// The pipe is opened overlapped, with a separate reader and writer, so a stalled write on either side
// can never stop us reading what the app sends (the app froze on Disconnect once with the v1 box).
//
// Build: build.cmd (C# 5 compiler that ships with Windows; no SDK needed).

using System;
using System.Collections.Concurrent;
using System.Collections.Generic;
using System.Drawing;
using System.IO;
using System.IO.Pipes;
using System.Linq;
using System.Net;
using System.Net.Sockets;
using System.Text;
using System.Threading;
using System.Web.Script.Serialization;
using System.Windows.Forms;
using System.Xml;

class Ctl
{
    public string Id, Label, Module, Key, Kind, Dest, Vio, Certainty, Note, Game;
    public int LedMsg, Min, Max, On = 1, Off;
    public string LedKey;
    public Control Widget;          // the button/checkbox that shows it
    public Color BaseColor = Color.WhiteSmoke;
}

class ModuleDef
{
    public string Id, Name;
    public int Msg, Pressed, Released;
    public string[] Keys = new string[0];
}

class VirtualCommandArm : Form
{
    const string PipeName = "ConnectionsAppToSBMEmulator";
    const int ScriptPort = 47800;
    const byte MSG_CAN_RX_REQ = 59, MSG_CAN_TX = 60, MSG_DCM_LED = 61, MSG_SCM_LED = 63, MSG_MODE_REQ = 64;
    const byte MSG_STEER = 119, MSG_PEDALS = 120;
    const int MIN_HOLD_MS = 250;

    // ---------- catalogue ----------
    readonly Dictionary<string, ModuleDef> _modules = new Dictionary<string, ModuleDef>();
    readonly List<Ctl> _controls = new List<Ctl>();
    readonly Dictionary<string, Ctl> _byId = new Dictionary<string, Ctl>();

    // ---------- live state (guarded by _lock) ----------
    readonly object _lock = new object();
    readonly Dictionary<string, Dictionary<string, int>> _keys = new Dictionary<string, Dictionary<string, int>>();
    bool _footSwitch, _parked = true;
    int _lever = 125, _dial;
    float _wheelTarget, _wheelSent;            // steering-wheel degrees, positive = left
    readonly HashSet<string> _dirty = new HashSet<string>();
    // Every lever / park-slot change is sent as its own frame, in order, so the app sees each position the
    // way a real handle reports it (e.g. "neutral" on the way into the park slot is never skipped).
    readonly Queue<byte[]> _hydroFrames = new Queue<byte[]>();
    readonly Dictionary<string, int> _leds = new Dictionary<string, int>();     // "63:1a" -> value
    readonly Dictionary<string, string> _game = new Dictionary<string, string>();
    int _rotation;
    static readonly string[] Rotation = { "pedals", "steer", "mhc", "scm", "dcm", "hydro" };

    volatile bool _closing, _connected;
    int _polls, _ledMsgs, _canMsgs, _pollsLastSecond;
    string _mode = "data";
    BlockingCollection<byte[]> _outbox;

    // ---------- script clients that asked to "watch" ----------
    readonly List<StreamWriter> _watchers = new List<StreamWriter>();

    readonly string _dir = AppDomain.CurrentDomain.BaseDirectory;
    readonly string _gameFile = Path.Combine(
        Environment.GetFolderPath(Environment.SpecialFolder.MyDocuments),
        @"My Games\FarmingSimulator2025\mods\DeereVehicleControl\src\VehicleInfo.xml");

    // ---------- UI ----------
    TextBox _log;
    Label _status, _gameLabel, _leverLabel, _wheelLabel, _dialLabel;
    TrackBar _leverBar, _wheelBar;
    CheckBox _parkBox, _footBox, _warnBox;

    [STAThread]
    static void Main()
    {
        Application.EnableVisualStyles();
        Application.Run(new VirtualCommandArm());
    }

    VirtualCommandArm()
    {
        LoadCatalogue(Path.Combine(_dir, "controls.json"));
        foreach (var m in _modules.Values)
        {
            var d = new Dictionary<string, int>();
            foreach (string k in m.Keys) d[k] = m.Released;
            _keys[m.Id] = d;
        }
        foreach (string r in Rotation) _dirty.Add(r);

        BuildUi();

        var t = new System.Windows.Forms.Timer { Interval = 300 };
        t.Tick += (s, e) => ReadGameFile();
        t.Start();
        var t2 = new System.Windows.Forms.Timer { Interval = 1000 };
        t2.Tick += (s, e) => { _pollsLastSecond = Interlocked.Exchange(ref _polls, 0); RefreshStatus(); };
        t2.Start();

        FormClosing += (s, e) => { _closing = true; };
        new Thread(PipeLoop) { IsBackground = true, Name = "pipe" }.Start();
        new Thread(ScriptServer) { IsBackground = true, Name = "script" }.Start();
        Log("Virtual CommandARM started (" + _controls.Count + " controls). Process name: " +
            System.Diagnostics.Process.GetCurrentProcess().ProcessName);
        Log("Scripted control on 127.0.0.1:" + ScriptPort + ". Now press 'Connect to Simulator Bridge' in the app.");
    }

    // =====================================================================================
    // Catalogue
    // =====================================================================================

    void LoadCatalogue(string path)
    {
        var js = new JavaScriptSerializer();
        var root = (Dictionary<string, object>)js.DeserializeObject(File.ReadAllText(path));
        foreach (Dictionary<string, object> m in (object[])root["modules"])
        {
            var md = new ModuleDef { Id = S(m, "id"), Name = S(m, "name"), Msg = I(m, "msg", 0),
                Pressed = I(m, "pressed", 1), Released = I(m, "released", 0) };
            if (m.ContainsKey("keys")) md.Keys = ((object[])m["keys"]).Select(o => (string)o).ToArray();
            _modules[md.Id] = md;
        }
        foreach (Dictionary<string, object> c in (object[])root["controls"])
        {
            var ctl = new Ctl { Id = S(c, "id"), Label = S(c, "label"), Module = S(c, "module"), Key = S(c, "key"),
                Kind = S(c, "kind"), Dest = S(c, "dest"), Vio = S(c, "vio"), Certainty = S(c, "certainty"),
                Note = S(c, "note"), Game = S(c, "game"), Min = I(c, "min", 0), Max = I(c, "max", 0),
                On = I(c, "on", 1), Off = I(c, "off", 0) };
            if (c.ContainsKey("led"))
            {
                var led = (Dictionary<string, object>)c["led"];
                ctl.LedMsg = I(led, "msg", 0); ctl.LedKey = S(led, "key");
            }
            _controls.Add(ctl);
            _byId[ctl.Id] = ctl;
        }
    }

    static string S(Dictionary<string, object> d, string k) { object v; return d.TryGetValue(k, out v) && v != null ? v.ToString() : null; }
    static int I(Dictionary<string, object> d, string k, int def) { object v; return d.TryGetValue(k, out v) && v != null ? Convert.ToInt32(v) : def; }

    // =====================================================================================
    // UI
    // =====================================================================================

    void BuildUi()
    {
        Text = "Virtual CommandARM (Apr 20 + Aug 26 builds) | SBMEmulator";
        Width = 1180; Height = 980;
        Font = new Font("Segoe UI", 9f);

        _status = new Label { Dock = DockStyle.Top, Height = 30, Padding = new Padding(10, 6, 10, 0),
            Font = new Font("Segoe UI", 10.5f, FontStyle.Bold), Text = "Starting..." };
        _gameLabel = new Label { Dock = DockStyle.Top, Height = 26, Padding = new Padding(10, 2, 10, 0),
            ForeColor = Color.DarkGreen, Text = "Game file: not read yet" };

        var body = new FlowLayoutPanel { Dock = DockStyle.Top, Height = 640, AutoScroll = true, Padding = new Padding(6),
            FlowDirection = FlowDirection.LeftToRight, WrapContents = true };

        // Physical groups, in the order an operator meets them.
        body.Controls.Add(BuildLeverGroup());
        body.Controls.Add(BuildButtonGroup("Multi-function handle (msg 124)", "mhc", 560, false));
        body.Controls.Add(BuildButtonGroup("Armrest keypad (msg 125)", "scm", 560, false));
        body.Controls.Add(BuildButtonGroup("Keys beside the display (msg 123)", "dcm", 560, false));
        body.Controls.Add(BuildWheelGroup());

        var legend = new Label { Dock = DockStyle.Top, Height = 34, Padding = new Padding(10, 2, 10, 0), ForeColor = Color.DimGray,
            Text = "Buttons act while the mouse is held (at least " + MIN_HOLD_MS + " ms). Tags: [game] only changes the game file | " +
                   "[not sent] the app reads it but sends nothing | ? name not confirmed. A lit button (amber) is a light the cloud switched on." };

        _log = new TextBox { Dock = DockStyle.Fill, Multiline = true, ReadOnly = true, ScrollBars = ScrollBars.Vertical,
            Font = new Font("Consolas", 9f), BackColor = Color.White };

        Controls.Add(_log);
        Controls.Add(legend);
        Controls.Add(body);
        Controls.Add(_gameLabel);
        Controls.Add(_status);
        RefreshStatus();
    }

    GroupBox NewGroup(string title, int w, int h, out FlowLayoutPanel flow)
    {
        var g = new GroupBox { Text = title, Width = w, Height = h, Padding = new Padding(6) };
        flow = new FlowLayoutPanel { Dock = DockStyle.Fill, AutoScroll = true };
        g.Controls.Add(flow);
        return g;
    }

    GroupBox BuildButtonGroup(string title, string module, int width, bool unused)
    {
        var list = _controls.Where(c => c.Module == module && (c.Kind == "button" || c.Kind == "switch" || c.Kind == "dial")).ToList();
        int rows = (int)Math.Ceiling(list.Count / 4.0);
        FlowLayoutPanel flow;
        var g = NewGroup(title, width, Math.Min(330, 40 + rows * 46), out flow);
        foreach (var c in list)
        {
            if (c.Kind == "dial") { AddDial(flow, c); continue; }
            if (c.Kind == "switch") { AddSwitch(flow, c); continue; }
            AddHold(flow, c);
        }
        return g;
    }

    string Caption(Ctl c)
    {
        string tag = c.Dest == "game" ? " [game]" : c.Dest == "none" ? " [not sent]" : "";
        string q = c.Certainty == "named" ? "" : " ?";
        return c.Label + q + tag;
    }

    void AddHold(FlowLayoutPanel flow, Ctl c)
    {
        var b = new Button { Text = Caption(c), Width = 132, Height = 40, BackColor = c.BaseColor, Tag = c };
        if (c.Dest == "none") b.ForeColor = Color.Gray;
        if (c.Dest == "game") b.ForeColor = Color.SteelBlue;
        var tip = new ToolTip();
        tip.SetToolTip(b, c.Id + (c.Vio != null ? "  ->  " + c.Vio : "") + (c.Note != null ? "\n" + c.Note : ""));
        DateTime pressedAt = DateTime.MinValue;
        b.MouseDown += (s, e) => { pressedAt = DateTime.Now; SetButton(c, true, "mouse"); };
        b.MouseUp += (s, e) =>
        {
            int wait = MIN_HOLD_MS - (int)(DateTime.Now - pressedAt).TotalMilliseconds;
            if (wait <= 0) { SetButton(c, false, "mouse"); return; }
            var once = new System.Windows.Forms.Timer { Interval = wait };
            once.Tick += (s2, e2) => { once.Stop(); once.Dispose(); SetButton(c, false, "mouse"); };
            once.Start();
        };
        c.Widget = b;
        flow.Controls.Add(b);
    }

    void AddSwitch(FlowLayoutPanel flow, Ctl c)
    {
        var cb = new CheckBox { Appearance = Appearance.Button, Text = Caption(c) + ": off", Width = 160, Height = 40,
            TextAlign = ContentAlignment.MiddleCenter, BackColor = c.BaseColor, Tag = c };
        cb.CheckedChanged += (s, e) => SetSwitch(c, cb.Checked, "mouse");
        c.Widget = cb;
        if (c.Id == "warning_switch") _warnBox = cb;
        flow.Controls.Add(cb);
    }

    void AddDial(FlowLayoutPanel flow, Ctl c)
    {
        var minus = new Button { Text = "Dial -", Width = 64, Height = 40 };
        var plus = new Button { Text = "Dial +", Width = 64, Height = 40 };
        _dialLabel = new Label { Width = 150, Height = 40, TextAlign = ContentAlignment.MiddleLeft };
        minus.Click += (s, e) => SetValue(c, _dial - 1, "mouse");
        plus.Click += (s, e) => SetValue(c, _dial + 1, "mouse");
        c.Widget = _dialLabel;
        flow.Controls.Add(minus); flow.Controls.Add(plus); flow.Controls.Add(_dialLabel);
        UpdateDialLabel();
    }

    GroupBox BuildLeverGroup()
    {
        FlowLayoutPanel flow;
        var g = NewGroup("Multi-function lever / foot switch (msg 126, 120): the accelerator", 560, 150, out flow);
        _parkBox = new CheckBox { Appearance = Appearance.Button, Checked = true, Width = 160, Height = 40,
            TextAlign = ContentAlignment.MiddleCenter, Text = "Lever IN park slot", BackColor = Color.Gold };
        _parkBox.CheckedChanged += (s, e) => SetSwitch(_byId["park_slot"], _parkBox.Checked, "mouse");
        _byId["park_slot"].Widget = _parkBox;
        flow.Controls.Add(_parkBox);

        _footBox = new CheckBox { Appearance = Appearance.Button, Width = 160, Height = 40,
            TextAlign = ContentAlignment.MiddleCenter, Text = "Foot switch: released", BackColor = Color.WhiteSmoke };
        _footBox.CheckedChanged += (s, e) => SetSwitch(_byId["foot_switch"], _footBox.Checked, "mouse");
        _byId["foot_switch"].Widget = _footBox;
        flow.Controls.Add(_footBox);

        var lever = _byId["lever"];
        _leverBar = new TrackBar { Minimum = lever.Min, Maximum = lever.Max, Value = 125, TickFrequency = 25, Width = 250,
            SmallChange = 5, LargeChange = 25, Enabled = false };
        _leverBar.ValueChanged += (s, e) => { if (_leverBar.Value != _lever) SetValue(lever, _leverBar.Value, "mouse"); };
        flow.Controls.Add(_leverBar);
        foreach (var pair in new[] { new { t = "-25", d = -25 }, new { t = "Neutral", d = 0 }, new { t = "+25", d = 25 } })
        {
            int delta = pair.d; string text = pair.t;
            var b = new Button { Text = text, Width = 70, Height = 32 };
            b.Click += (s, e) => SetValue(lever, delta == 0 ? 125 : _lever + delta, "mouse");
            flow.Controls.Add(b);
        }
        _leverLabel = new Label { Width = 260, Height = 32, TextAlign = ContentAlignment.MiddleLeft };
        flow.Controls.Add(_leverLabel);
        UpdateLeverLabel();
        return g;
    }

    GroupBox BuildWheelGroup()
    {
        FlowLayoutPanel flow;
        var g = NewGroup("Steering wheel (msg 119)", 560, 110, out flow);
        var wheel = _byId["steering"];
        _wheelBar = new TrackBar { Minimum = wheel.Min, Maximum = wheel.Max, Value = 0, TickFrequency = 180, Width = 330,
            SmallChange = 45, LargeChange = 180 };
        _wheelBar.ValueChanged += (s, e) => { if (_wheelBar.Value != (int)_wheelTarget) SetValue(wheel, _wheelBar.Value, "mouse"); };
        // The slider runs right-to-left so dragging left steers left.
        _wheelBar.RightToLeft = RightToLeft.Yes; _wheelBar.RightToLeftLayout = true;
        flow.Controls.Add(_wheelBar);
        var centre = new Button { Text = "Centre", Width = 70, Height = 32 };
        centre.Click += (s, e) => SetValue(wheel, 0, "mouse");
        flow.Controls.Add(centre);
        _wheelLabel = new Label { Width = 500, Height = 28, TextAlign = ContentAlignment.MiddleLeft };
        flow.Controls.Add(_wheelLabel);
        UpdateWheelLabel();
        return g;
    }

    void UI(Action a)
    {
        if (IsDisposed) return;
        if (InvokeRequired) { try { BeginInvoke(a); } catch { } }
        else a();
    }

    void UpdateLeverLabel()
    {
        UI(() => _leverLabel.Text = "Lever " + _lever + " (125 neutral)" + (_parked ? " | in park slot" : ""));
    }
    void UpdateDialLabel()
    {
        UI(() => { if (_dialLabel != null) _dialLabel.Text = "Dial step " + _dial + " -> " + (_dial * 500 + 1000); });
    }
    void UpdateWheelLabel()
    {
        UI(() => _wheelLabel.Text = string.Format("Wheel {0:+0;-0;0} deg (sent {1:+0;-0;0} deg) -> road wheels {2:+0.0;-0.0;0.0} deg | positive = left",
            _wheelTarget, _wheelSent, _wheelSent * 35f / 900f));
    }

    // =====================================================================================
    // State changes (from the mouse or from scripts)
    // =====================================================================================

    void SetButton(Ctl c, bool down, string who)
    {
        var m = _modules[c.Module];
        lock (_lock) { _keys[c.Module][c.Key] = down ? m.Pressed : m.Released; _dirty.Add(c.Module); }
        PaintButton(c, down);
        Log((down ? "press   " : "release ") + c.Id + "  (" + c.Module + "." + c.Key + "=" + (down ? m.Pressed : m.Released) + ")" + (who == "mouse" ? "" : "  [" + who + "]"));
        Emit((down ? "press " : "release ") + c.Id);
    }

    void SetSwitch(Ctl c, bool on, string who)
    {
        bool changed;
        lock (_lock)
        {
            if (c.Id == "foot_switch") { changed = _footSwitch != on; _footSwitch = on; _dirty.Add("pedals"); }
            else if (c.Id == "park_slot")
            {
                changed = _parked != on;
                if (changed && on) { _lever = 125; _hydroFrames.Enqueue(BuildHydro()); }  // passes neutral, still unparked
                _parked = on;
                if (on) _lever = 125;
                if (changed) _hydroFrames.Enqueue(BuildHydro());
                _dirty.Add("hydro");
            }
            else
            {
                var m = _modules[c.Module];
                int v = on ? c.On : c.Off;
                changed = _keys[c.Module][c.Key] != v;
                _keys[c.Module][c.Key] = v; _dirty.Add(c.Module);
            }
        }
        UI(() =>
        {
            var cb = c.Widget as CheckBox;
            if (cb != null && cb.Checked != on) cb.Checked = on;
            if (c.Id == "foot_switch") { _footBox.Text = on ? "Foot switch: HELD" : "Foot switch: released"; _footBox.BackColor = on ? Color.Gold : Color.WhiteSmoke; }
            else if (c.Id == "park_slot")
            {
                _parkBox.Text = on ? "Lever IN park slot" : "Lever OUT of park slot"; _parkBox.BackColor = on ? Color.Gold : Color.WhiteSmoke;
                _leverBar.Enabled = !on; if (on) _leverBar.Value = 125;
            }
            else if (cb != null) { cb.Text = Caption(c) + (on ? ": ON" : ": off"); cb.BackColor = on ? Color.Gold : c.BaseColor; }
        });
        if (c.Id == "park_slot") UpdateLeverLabel();
        if (!changed) return;
        Log("switch  " + c.Id + " " + (on ? "on" : "off") + (who == "mouse" ? "" : "  [" + who + "]"));
        Emit("switch " + c.Id + " " + (on ? "1" : "0"));
    }

    // Returns null on success or an error message.
    string SetValue(Ctl c, int value, string who)
    {
        if (c.Id == "lever")
        {
            lock (_lock)
            {
                if (_parked) return "lever is in the park slot; set park_slot 0 first";
                value = Math.Max(c.Min, Math.Min(c.Max, value));
                if (value == _lever) return null;
                _lever = value; _hydroFrames.Enqueue(BuildHydro()); _dirty.Add("hydro");
            }
            UI(() => { if (_leverBar.Value != value) _leverBar.Value = value; });
            UpdateLeverLabel();
        }
        else if (c.Id == "steering")
        {
            lock (_lock)
            {
                value = Math.Max(c.Min, Math.Min(c.Max, value));
                if (value == (int)_wheelTarget) return null;
                _wheelTarget = value; _dirty.Add("steer");
            }
            UI(() => { if (_wheelBar.Value != value) _wheelBar.Value = value; });
            UpdateWheelLabel();
        }
        else if (c.Id == "speed_dial")
        {
            lock (_lock)
            {
                value = Math.Max(c.Min, Math.Min(c.Max, value));
                if (value == _dial) return null;
                _dial = value; _dirty.Add("mhc");
            }
            UpdateDialLabel();
        }
        else return c.Id + " has no value to set (it is a " + c.Kind + ")";
        Log("set     " + c.Id + " " + value + (who == "mouse" ? "" : "  [" + who + "]"));
        Emit("set " + c.Id + " " + value);
        return null;
    }

    void PaintButton(Ctl c, bool down)
    {
        UI(() =>
        {
            var b = c.Widget as Button;
            if (b == null) return;
            b.BackColor = down ? Color.LightGreen : (LedOn(c) ? Color.Orange : c.BaseColor);
        });
    }

    bool LedOn(Ctl c)
    {
        if (c.LedKey == null) return false;
        int v; lock (_lock) { _leds.TryGetValue(c.LedMsg + ":" + c.LedKey, out v); }
        return v == 1;
    }

    // =====================================================================================
    // Pipe
    // =====================================================================================

    void PipeLoop()
    {
        while (!_closing)
        {
            PipeStream pipe = null;
            Thread writer = null;
            try
            {
                pipe = OpenPipe();
                if (_closing) return;
                if (pipe == null) continue;      // the running app changed: open the pipe the other way round

                _outbox = new BlockingCollection<byte[]>();
                var box = _outbox; var p = pipe;
                writer = new Thread(() => WriterLoop(p, box)) { IsBackground = true, Name = "pipe-writer" };
                writer.Start();
                lock (_lock) { foreach (string r in Rotation) _dirty.Add(r); }
                _connected = true; _mode = "data";
                Log("CONNECTED to the Connections app (" + _role + ").");
                Emit("link connected");
                _framesLogged = 0;

                var frame = new List<byte>(256);
                var buf = new byte[512];
                while (!_closing && pipe.IsConnected)
                {
                    int n = pipe.Read(buf, 0, buf.Length);
                    if (n <= 0) break;
                    for (int i = 0; i < n; i++)
                    {
                        if (buf[i] != 0) { frame.Add(buf[i]); continue; }
                        if (frame.Count == 0) continue;
                        byte[] msg = CobsDecode(frame.ToArray());
                        frame.Clear();
                        HandleFrame(msg);
                    }
                }
                Log("The app closed the link (Disconnect, or the app closed).");
            }
            catch (Exception ex) { Log("Link error: " + ex.Message); }
            finally
            {
                _connected = false;
                if (_outbox != null) _outbox.CompleteAdding();
                if (pipe != null) { try { pipe.Dispose(); } catch { } }
                Emit("link disconnected");
            }
            Thread.Sleep(500);
        }
    }

    // The two app builds open the pipe in opposite directions:
    //   Apr 20 ("Online - Display and CommandARM Simulator") serves \\.\pipe\ConnectionsAppToSBMEmulator; we connect.
    //   Aug 26 ("SimulatorConnections", UseSBMEmulator=true) connects as a client
    //   (SBMDirectTransportNamedPipe.GetCOMPortNameOrWait, NamedPipeClientStream.Connect() with no timeout); we serve.
    // Same COBS + MessagePack frames either way.
    string _role = "client";
    readonly object _logFileLock = new object();
    int _framesLogged;

    static bool AppConnectsAsClient()
    {
        try { return System.Diagnostics.Process.GetProcessesByName("SimulatorConnections").Length > 0; }
        catch { return false; }
    }

    // Returns a connected pipe, or null when the running app changed while waiting (or we are closing).
    PipeStream OpenPipe()
    {
        if (AppConnectsAsClient())
        {
            _role = "server";
            var server = new NamedPipeServerStream(PipeName, PipeDirection.InOut, 1, PipeTransmissionMode.Byte, PipeOptions.Asynchronous);
            Log("Waiting for the Aug 26 app to connect (serving the pipe).");
            IAsyncResult wait = server.BeginWaitForConnection(null, null);
            while (!_closing)
            {
                if (wait.AsyncWaitHandle.WaitOne(500))
                {
                    try { server.EndWaitForConnection(wait); return server; }
                    catch (IOException) { break; }
                }
                if (!AppConnectsAsClient()) break;
            }
            try { server.Dispose(); } catch { }
            return null;
        }
        _role = "client";
        var client = new NamedPipeClientStream(".", PipeName, PipeDirection.InOut, PipeOptions.Asynchronous);
        while (!_closing)
        {
            try { client.Connect(500); return client; }
            catch (TimeoutException) { }
            catch (IOException) { Thread.Sleep(300); }
            if (AppConnectsAsClient()) break;
        }
        try { client.Dispose(); } catch { }
        return null;
    }

    void WriterLoop(PipeStream pipe, BlockingCollection<byte[]> box)
    {
        try
        {
            foreach (var data in box.GetConsumingEnumerable())
            {
                pipe.Write(data, 0, data.Length);
                pipe.Flush();
            }
        }
        catch (Exception ex) { if (!_closing) Log("Write stopped: " + ex.Message); }
    }

    void HandleFrame(byte[] msg)
    {
        if (_framesLogged < 6) { _framesLogged++; Log("Frame from app: " + Hex(msg)); }
        if (msg.Length < 2 || msg[0] != 0x92) { Log("Unrecognised frame from app: " + Hex(msg)); return; }
        byte id = msg[1];
        if (id == MSG_MODE_REQ || id == MSG_CAN_RX_REQ)
        {
            Interlocked.Increment(ref _polls);
            if (id == MSG_MODE_REQ && msg.Length >= 3)
            {
                string mode = msg[2] == 85 ? "data" : msg[2] == 84 ? "calibration" : msg[2] == 83 ? "log" : msg[2].ToString();
                if (mode != _mode) { _mode = mode; Log("App switched the box to " + mode + " mode"); Emit("mode " + mode); }
            }
            Thread.Sleep(4);          // a real serial link is slow; keeps the app from spinning
            byte[] reply = NextStateMessage();
            var box = _outbox;
            if (box != null && !box.IsAddingCompleted) { try { box.Add(CobsEncode(reply)); } catch (InvalidOperationException) { } }
        }
        else if (id == MSG_DCM_LED || id == MSG_SCM_LED)
        {
            Interlocked.Increment(ref _ledMsgs);
            ApplyLeds(id, msg);
        }
        else if (id == MSG_CAN_TX) Interlocked.Increment(ref _canMsgs);
        else Log("Message " + id + " from app: " + Hex(msg));
    }

    // Send what changed first; otherwise rotate through every message so the app always has fresh state.
    byte[] NextStateMessage()
    {
        string which = null;
        lock (_lock)
        {
            if (_hydroFrames.Count > 0) { _dirty.Remove("hydro"); return _hydroFrames.Dequeue(); }
            foreach (string r in Rotation) if (_dirty.Contains(r)) { which = r; break; }
            if (which == null) which = Rotation[_rotation++ % Rotation.Length];
            _dirty.Remove(which);
            if (which == "steer" && Math.Abs(_wheelTarget - _wheelSent) > 0.01f) _dirty.Add("steer");  // still turning
            switch (which)
            {
                case "pedals": return new byte[] { 0x92, MSG_PEDALS, 0x81, 0xA2, (byte)'f', (byte)'s', (byte)(_footSwitch ? 0xC3 : 0xC2) };
                case "steer": return BuildSteer();
                case "hydro": return BuildHydro();
                default: return BuildKeys(_modules[which]);
            }
        }
    }

    byte[] BuildKeys(ModuleDef m)
    {
        var o = new List<byte> { 0x92, (byte)m.Msg };
        MapHeader(o, m.Keys.Length);
        var d = _keys[m.Id];
        foreach (string k in m.Keys)
        {
            Str(o, k);
            int v = d[k];
            if (m.Id == "mhc" && k == "y0") v = _dial;      // speed dial: (y0 - y1) % 49 * 500 + 1000
            if (m.Id == "mhc" && k == "y1") v = 0;
            Int(o, v);
        }
        return o.ToArray();
    }

    byte[] BuildHydro()
    {
        int v = _parked ? 125 : _lever;
        bool p = _parked, f = !p && v > 130, r = !p && v < 120, n = !p && !f && !r;
        var o = new List<byte> { 0x92, 126, 0x85 };
        Str(o, "v"); Int(o, v);
        Str(o, "f"); o.Add((byte)(f ? 0xC3 : 0xC2));
        Str(o, "r"); o.Add((byte)(r ? 0xC3 : 0xC2));
        Str(o, "n"); o.Add((byte)(n ? 0xC3 : 0xC2));
        Str(o, "p"); o.Add((byte)(p ? 0xC3 : 0xC2));
        return o.ToArray();
    }

    // The app accumulates the shortest step between successive absolute readings (0-359), and a
    // rising reading turns the wheel right. So report an = (-wheel) mod 360 and never move more
    // than 90 degrees between two messages.
    byte[] BuildSteer()
    {
        float diff = _wheelTarget - _wheelSent;
        if (Math.Abs(diff) > 90f) diff = Math.Sign(diff) * 90f;
        _wheelSent += diff;
        int an = (int)Math.Round(-_wheelSent) % 360; if (an < 0) an += 360;
        var o = new List<byte> { 0x92, MSG_STEER, 0x82 };
        Str(o, "an"); Int(o, an);
        Str(o, "st"); Int(o, 0);
        UpdateWheelLabel();
        return o.ToArray();
    }

    void ApplyLeds(byte msgId, byte[] msg)
    {
        var map = ReadMap(msg, 2);
        if (map == null) { Log("Unreadable light message: " + Hex(msg)); return; }
        var changed = new List<string>();
        lock (_lock)
        {
            foreach (var kv in map)
            {
                string k = msgId + ":" + kv.Key; int old;
                if (!_leds.TryGetValue(k, out old) || old != kv.Value) { _leds[k] = kv.Value; changed.Add(kv.Key); }
            }
        }
        foreach (var c in _controls.Where(c => c.LedMsg == msgId && c.LedKey != null && changed.Contains(c.LedKey)))
        {
            bool on = LedOn(c);
            PaintButton(c, false);
            Log("light   " + c.Id + " " + (on ? "ON" : "off"));
            Emit("led " + c.Id + " " + (on ? "1" : "0"));
        }
    }

    // ---------- MessagePack helpers ----------

    static void MapHeader(List<byte> o, int n) { if (n <= 15) o.Add((byte)(0x80 | n)); else { o.Add(0xDE); o.Add((byte)(n >> 8)); o.Add((byte)n); } }
    static void Str(List<byte> o, string s) { o.Add((byte)(0xA0 | s.Length)); foreach (char ch in s) o.Add((byte)ch); }
    static void Int(List<byte> o, int v)
    {
        if (v >= 0 && v <= 0x7F) o.Add((byte)v);
        else if (v >= 0 && v <= 0xFF) { o.Add(0xCC); o.Add((byte)v); }
        else if (v >= 0 && v <= 0xFFFF) { o.Add(0xCD); o.Add((byte)(v >> 8)); o.Add((byte)v); }
        else if (v < 0 && v >= -32) o.Add((byte)(sbyte)v);
        else { o.Add(0xD2); o.Add((byte)(v >> 24)); o.Add((byte)(v >> 16)); o.Add((byte)(v >> 8)); o.Add((byte)v); }
    }

    static Dictionary<string, int> ReadMap(byte[] d, int p)
    {
        try
        {
            int n;
            if ((d[p] & 0xF0) == 0x80) { n = d[p] & 0x0F; p += 1; }
            else if (d[p] == 0xDE) { n = (d[p + 1] << 8) | d[p + 2]; p += 3; }
            else return null;
            var r = new Dictionary<string, int>();
            for (int i = 0; i < n; i++)
            {
                byte t = d[p++];
                if ((t & 0xE0) != 0xA0) return null;
                int len = t & 0x1F; string key = Encoding.ASCII.GetString(d, p, len); p += len;
                t = d[p++]; int v;
                if (t <= 0x7F) v = t;
                else if (t == 0xCC) v = d[p++];
                else if (t == 0xCD) { v = (d[p] << 8) | d[p + 1]; p += 2; }
                else if (t == 0xC2) v = 0; else if (t == 0xC3) v = 1;
                else if (t >= 0xE0) v = (sbyte)t;
                else return null;
                r[key] = v;
            }
            return r;
        }
        catch { return null; }
    }

    // ---------- COBS ----------

    static byte[] CobsEncode(byte[] data)
    {
        var o = new List<byte>(data.Length + 2);
        int codeIdx = 0; byte code = 1; o.Add(0);
        foreach (byte b in data)
        {
            if (b == 0) { o[codeIdx] = code; codeIdx = o.Count; o.Add(0); code = 1; }
            else { o.Add(b); code++; if (code == 0xFF) { o[codeIdx] = code; codeIdx = o.Count; o.Add(0); code = 1; } }
        }
        o[codeIdx] = code;
        o.Add(0);
        return o.ToArray();
    }

    static byte[] CobsDecode(byte[] enc)
    {
        var o = new List<byte>(enc.Length);
        int i = 0;
        while (i < enc.Length)
        {
            int code = enc[i++];
            if (code == 0) break;
            for (int k = 1; k < code && i < enc.Length; k++) o.Add(enc[i++]);
            if (code != 0xFF && i < enc.Length) o.Add(0);
        }
        return o.ToArray();
    }

    // =====================================================================================
    // Game file
    // =====================================================================================

    void ReadGameFile()
    {
        try
        {
            if (!File.Exists(_gameFile)) { _gameLabel.Text = "Game file not created yet (the app makes it when the box connects)"; return; }
            string xml;
            using (var fs = new FileStream(_gameFile, FileMode.Open, FileAccess.Read, FileShare.ReadWrite | FileShare.Delete))
            using (var sr = new StreamReader(fs)) xml = sr.ReadToEnd();
            if (xml.Trim().Length == 0) { _gameLabel.Text = "Game file is empty: the app isn't writing it (restart the app once if it just created it)"; return; }
            var doc = new XmlDocument();
            doc.LoadXml(xml);
            var sb = new StringBuilder("Game file @ " + DateTime.Now.ToString("HH:mm:ss") + ":  ");
            foreach (XmlNode n in doc.DocumentElement.ChildNodes)
            {
                if (n.NodeType != XmlNodeType.Element) continue;
                string k = n.Name, v = n.InnerText.Trim();
                sb.Append(k).Append('=').Append(v).Append("   ");
                string old;
                bool changed;
                lock (_lock) { changed = !_game.TryGetValue(k, out old) || old != v; _game[k] = v; }
                if (changed) Emit("game " + k + " " + v);
            }
            _gameLabel.Text = sb.ToString();
        }
        catch (IOException) { _gameLabel.Text = "Game file is locked by another program right now"; }
        catch { /* the app rewrites the file every 80 ms without an atomic replace: a torn read is normal */ }
    }

    // =====================================================================================
    // Scripted control: 127.0.0.1:47800, one command per line
    // =====================================================================================

    void ScriptServer()
    {
        TcpListener listener;
        try { listener = new TcpListener(IPAddress.Loopback, ScriptPort); listener.Start(); }
        catch (Exception ex) { Log("Scripted control unavailable: " + ex.Message); return; }
        while (!_closing)
        {
            try
            {
                var client = listener.AcceptTcpClient();
                new Thread(() => ServeClient(client)) { IsBackground = true, Name = "script-client" }.Start();
            }
            catch { }
        }
    }

    void ServeClient(TcpClient client)
    {
        StreamWriter w = null;
        try
        {
            var stream = client.GetStream();
            var r = new StreamReader(stream, new UTF8Encoding(false));
            w = new StreamWriter(stream, new UTF8Encoding(false)) { AutoFlush = true, NewLine = "\n" };
            string line;
            while ((line = r.ReadLine()) != null)
            {
                line = line.Trim();
                if (line.Length == 0) continue;
                string reply;
                try { reply = Command(line, w); }
                catch (Exception ex) { reply = "err " + ex.Message; }
                lock (w) w.WriteLine(reply);
            }
        }
        catch { }
        finally
        {
            if (w != null) lock (_watchers) _watchers.Remove(w);
            try { client.Close(); } catch { }
        }
    }

    string Command(string line, StreamWriter w)
    {
        string[] a = line.Split(new[] { ' ' }, StringSplitOptions.RemoveEmptyEntries);
        string cmd = a[0].ToLowerInvariant();
        Ctl c = a.Length > 1 && _byId.ContainsKey(a[1]) ? _byId[a[1]] : null;
        switch (cmd)
        {
            case "help":
                return "ok commands: list | state | press <id> [ms] | down <id> | up <id> | set <id> <value> | " +
                       "switch <id> 0|1 | watch | ping";
            case "ping": return "ok pong";
            case "list":
                return "ok " + new JavaScriptSerializer().Serialize(_controls.Select(x => new Dictionary<string, object> {
                    { "id", x.Id }, { "label", x.Label }, { "kind", x.Kind }, { "dest", x.Dest }, { "vio", x.Vio }, { "certainty", x.Certainty } }).ToList());
            case "state": return "ok " + StateJson();
            case "watch":
                lock (_watchers) _watchers.Add(w);
                return "ok watching (events follow, one per line)";
            case "press":
            {
                if (c == null || c.Kind != "button") return "err unknown button: " + (a.Length > 1 ? a[1] : "");
                int ms = a.Length > 2 ? int.Parse(a[2]) : 300;
                SetButton(c, true, "script");
                Thread.Sleep(Math.Max(MIN_HOLD_MS, ms));
                SetButton(c, false, "script");
                return "ok pressed " + c.Id + " " + Math.Max(MIN_HOLD_MS, ms) + "ms";
            }
            case "down":
            case "up":
                if (c == null || c.Kind != "button") return "err unknown button: " + (a.Length > 1 ? a[1] : "");
                SetButton(c, cmd == "down", "script");
                return "ok " + cmd + " " + c.Id;
            case "switch":
                if (c == null || c.Kind != "switch" || a.Length < 3) return "err usage: switch <id> 0|1";
                SetSwitch(c, a[2] == "1" || a[2].ToLowerInvariant() == "on", "script");
                return "ok switch " + c.Id + " " + a[2];
            case "set":
            {
                if (c == null || a.Length < 3) return "err usage: set <id> <value>";
                if (c.Kind == "switch") { SetSwitch(c, a[2] == "1" || a[2].ToLowerInvariant() == "on", "script"); return "ok switch " + c.Id + " " + a[2]; }
                string err = SetValue(c, int.Parse(a[2]), "script");
                return err == null ? "ok set " + c.Id + " " + a[2] : "err " + err;
            }
            default: return "err unknown command (try help)";
        }
    }

    string StateJson()
    {
        var s = new Dictionary<string, object>();
        lock (_lock)
        {
            s["connected"] = _connected;
            s["mode"] = _mode;
            s["pollsPerSecond"] = _pollsLastSecond;
            s["footSwitch"] = _footSwitch;
            s["parked"] = _parked;
            s["lever"] = _lever;
            s["wheelTarget"] = _wheelTarget;
            s["wheelSent"] = _wheelSent;
            s["speedDial"] = _dial;
            var pressed = new List<string>();
            foreach (var c in _controls.Where(x => x.Kind == "button" || (x.Kind == "switch" && _modules.ContainsKey(x.Module) && _keys.ContainsKey(x.Module))))
            {
                if (c.Key == null || !_keys.ContainsKey(c.Module) || !_keys[c.Module].ContainsKey(c.Key)) continue;
                int v = _keys[c.Module][c.Key];
                bool on = c.Kind == "switch" ? v == c.On : v == _modules[c.Module].Pressed;
                if (on) pressed.Add(c.Id);
            }
            s["pressed"] = pressed;
            var lit = new List<string>();
            foreach (var c in _controls.Where(x => x.LedKey != null))
            {
                int v; if (_leds.TryGetValue(c.LedMsg + ":" + c.LedKey, out v) && v == 1) lit.Add(c.Id);
            }
            s["lit"] = lit;
            s["game"] = new Dictionary<string, string>(_game);
        }
        return new JavaScriptSerializer().Serialize(s);
    }

    void Emit(string evt)
    {
        string line = "evt " + DateTime.Now.ToString("HH:mm:ss.fff") + " " + evt;
        List<StreamWriter> dead = null;
        lock (_watchers)
        {
            foreach (var w in _watchers)
            {
                try { lock (w) w.WriteLine(line); }
                catch { if (dead == null) dead = new List<StreamWriter>(); dead.Add(w); }
            }
            if (dead != null) foreach (var w in dead) _watchers.Remove(w);
        }
    }

    // =====================================================================================
    // Status and log
    // =====================================================================================

    void RefreshStatus()
    {
        UI(() =>
        {
            _status.Text = _connected
                ? "CONNECTED to the app | " + _mode + " mode | polls " + _pollsLastSecond + "/s | light messages " + _ledMsgs + " | CAN messages " + _canMsgs
                : "Waiting for the app: press 'Connect to Simulator Bridge' in the Connections app";
            _status.ForeColor = _connected ? Color.DarkGreen : Color.DarkOrange;
        });
    }

    void Log(string line)
    {
        string s = DateTime.Now.ToString("HH:mm:ss.fff") + "  " + line + "\r\n";
        UI(() => { if (_log != null) { if (_log.TextLength > 200000) _log.Clear(); _log.AppendText(s); } });
        // also to SBMEmulator.log next to the exe, so the link can be diagnosed without looking at the window
        try { lock (_logFileLock) File.AppendAllText(Path.Combine(AppDomain.CurrentDomain.BaseDirectory, "SBMEmulator.log"), s); } catch { }
    }

    static string Hex(byte[] d) { return BitConverter.ToString(d).Replace("-", " "); }
}

