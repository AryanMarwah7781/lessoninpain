// THROWAWAY SPIKE: a fake CommandARM box ("SBM") for the Apr 20 Connections app.
//
// The app has a built-in hook for this. When a process called "SBMEmulator" is running
// and you press "Connect to Simulator Bridge", the app opens the named pipe
// \\.\pipe\ConnectionsAppToSBMEmulator instead of the USB COM port
// (SBMCommnHandler.cs:117, SBMNamedPipeInterface.cs).
// Frames are COBS-encoded and end in 0x00. The payload is MessagePack [msgId, {key: value}].
// The app polls with [64,85] (data) and [59,0] (CAN rx), and reads ONE reply to each.
// It also pushes LED messages (61 DCM, 63 SCM) and CAN tx (60) without expecting a reply.
//
// Messages we send (decoded in the earlier reports, apr20-connections/reports/01-app-controls.md):
//   120 Pedals {fs: bool}            foot switch, boom-fold modifier (never sent to the cloud)
//   124 MHC    25 int keys           multi-function handle buttons; pressed == 1; y0/y1 = speed dial
//   125 SCM    20 int keys           armrest keypad;  pressed == even && != 8, so released = 1
//   123 DCM    17 int keys           keys by the display; same pressed rule as SCM
//   126 Hydro  {v int 0-250, f,r,n,p bool}  multi-function lever; 125 = neutral; p = in park slot
//
// Build (C# 5, .NET Framework csc): see build.cmd. Exe name MUST stay SBMEmulator.exe.

using System;
using System.Collections.Generic;
using System.Drawing;
using System.IO;
using System.IO.Pipes;
using System.Text;
using System.Threading;
using System.Windows.Forms;
using System.Xml;

class SBMEmulator : Form
{
    const string PipeName = "ConnectionsAppToSBMEmulator";
    const byte MSG_CAN_RX_REQ = 59, MSG_CAN_TX = 60, MSG_DCM_LED = 61, MSG_SCM_LED = 63, MSG_MODE_REQ = 64;
    const byte MSG_PEDALS = 120, MSG_DCM = 123, MSG_MHC = 124, MSG_SCM = 125, MSG_HYDRO = 126;
    const int KEY_UP = 1, KEY_DOWN = 2;      // SCM/DCM: "pressed" means even and not 8
    const int MIN_HOLD_MS = 350;             // a press must survive at least one full reply cycle

    static readonly string[] MhcKeys = {
        "v1","b1","c1","d1","e1","f1","g1","h1","i1","j1","k1","l1","m1",
        "n1","o1","p1","q1","r1","s1","t1","u1","y0","y1","y2","z1" };
    static readonly string[] ScmKeys = {
        "1a","2a","3a","4a","5a","6a","7a","8a","9a","eb","ep",
        "1c","2c","3c","4c","5c","6c","7c","8c","9c" };
    static readonly string[] DcmKeys = {
        "b1","b2","b3","b4","b5","b6","b7","b8","b9","b10","b11","b12","b13","b14","e1","e2","lb" };

    readonly object _lock = new object();
    readonly Dictionary<string, int> _mhc = new Dictionary<string, int>();
    readonly Dictionary<string, int> _scm = new Dictionary<string, int>();
    readonly Dictionary<string, int> _dcm = new Dictionary<string, int>();
    volatile bool _footSwitch;
    volatile int _lever = 125;
    volatile bool _parked = true;
    volatile int _dial;                      // 0..48 -> PLT_MHC_Encoder 1000..25000
    volatile bool _closing;
    volatile bool _connected;
    int _replyIndex, _polls, _ledMsgs, _canMsgs;

    readonly string _gameFile = Path.Combine(
        Environment.GetFolderPath(Environment.SpecialFolder.MyDocuments),
        @"My Games\FarmingSimulator2025\mods\DeereVehicleControl\src\VehicleInfo.xml");

    TextBox _log;
    Label _status, _game, _leverLabel, _dialLabel;
    TrackBar _leverBar;
    CheckBox _parkBox;

    [STAThread]
    static void Main()
    {
        Application.EnableVisualStyles();
        Application.Run(new SBMEmulator());
    }

    SBMEmulator()
    {
        foreach (string k in MhcKeys) _mhc[k] = 0;
        foreach (string k in ScmKeys) _scm[k] = KEY_UP;
        foreach (string k in DcmKeys) _dcm[k] = KEY_UP;

        Text = "SBM Emulator (test only)";
        Width = 900; Height = 860;
        Font = new Font("Segoe UI", 9.5f);

        _status = new Label { Dock = DockStyle.Top, Height = 40, Padding = new Padding(10, 6, 10, 0),
            Text = "Starting...", Font = new Font("Segoe UI", 10.5f, FontStyle.Bold) };
        _game = new Label { Dock = DockStyle.Top, Height = 40, Padding = new Padding(10, 2, 10, 0),
            Text = "Game file: not read yet", ForeColor = Color.DarkGreen };

        // --- multi-function handle ---
        var handle = NewGroup("Multi-function handle (msg 124)  ·  foot switch (msg 120)", 130);
        var foot = new CheckBox { Appearance = Appearance.Button, Width = 190, Height = 44,
            Text = "Foot switch: released", TextAlign = ContentAlignment.MiddleCenter, BackColor = Color.WhiteSmoke };
        foot.CheckedChanged += (s, e) =>
        {
            _footSwitch = foot.Checked;
            foot.Text = foot.Checked ? "Foot switch: HELD" : "Foot switch: released";
            foot.BackColor = foot.Checked ? Color.Gold : Color.WhiteSmoke;
            Log("Foot switch " + (foot.Checked ? "held" : "released"));
        };
        handle.Controls.Add(foot);
        AddHold(handle, "Centre boom RAISE", _mhc, "j1", 1, 0);
        AddHold(handle, "Centre boom LOWER", _mhc, "l1", 1, 0);
        AddHold(handle, "Master spray", _mhc, "b1", 1, 0);
        AddHold(handle, "Left boom raise", _mhc, "c1", 1, 0);
        AddHold(handle, "Left boom lower", _mhc, "f1", 1, 0);
        AddHold(handle, "Right boom raise", _mhc, "d1", 1, 0);
        AddHold(handle, "Right boom lower", _mhc, "e1", 1, 0);

        // --- keypad and display keys ---
        var keys = NewGroup("Armrest keypad (msg 125)  ·  keys beside the display (msg 123)", 80);
        AddHold(keys, "Solution pump", _scm, "1a", KEY_DOWN, KEY_UP);
        AddHold(keys, "Rate 1", _scm, "2c", KEY_DOWN, KEY_UP);
        AddHold(keys, "Rate 2", _scm, "3a", KEY_DOWN, KEY_UP);
        AddHold(keys, "Rate 3", _scm, "3c", KEY_DOWN, KEY_UP);
        AddHold(keys, "Engine low idle", _dcm, "b1", KEY_DOWN, KEY_UP);
        AddHold(keys, "Engine high idle", _dcm, "b3", KEY_DOWN, KEY_UP);
        AddHold(keys, "Park brake", _dcm, "b8", KEY_DOWN, KEY_UP);

        // --- lever ---
        var lever = NewGroup("Multi-function lever / hydro handle (msg 126)  ·  this is the accelerator", 110);
        _parkBox = new CheckBox { Appearance = Appearance.Button, Width = 190, Height = 44, Checked = true,
            Text = "Lever IN park slot", TextAlign = ContentAlignment.MiddleCenter, BackColor = Color.Gold };
        _parkBox.CheckedChanged += (s, e) =>
        {
            _parked = _parkBox.Checked;
            if (_parked) { _leverBar.Value = 125; _lever = 125; }
            _leverBar.Enabled = !_parked;
            _parkBox.Text = _parked ? "Lever IN park slot" : "Lever OUT of park slot";
            _parkBox.BackColor = _parked ? Color.Gold : Color.WhiteSmoke;
            UpdateLeverLabel();
            Log(_parked ? "Lever put in the park slot" : "Lever taken out of the park slot");
        };
        lever.Controls.Add(_parkBox);
        _leverBar = new TrackBar { Minimum = 0, Maximum = 250, Value = 125, TickFrequency = 25, Width = 300, Enabled = false,
            SmallChange = 5, LargeChange = 25 };
        _leverBar.ValueChanged += (s, e) => { _lever = _leverBar.Value; UpdateLeverLabel(); };
        lever.Controls.Add(_leverBar);
        AddClick(lever, "Lever -10", () => NudgeLever(-10));
        AddClick(lever, "Neutral", () => NudgeLever(125 - _lever));
        AddClick(lever, "Lever +10", () => NudgeLever(10));
        _leverLabel = new Label { Width = 300, Height = 30, TextAlign = ContentAlignment.MiddleLeft };
        lever.Controls.Add(_leverLabel);
        UpdateLeverLabel();

        // --- speed dial ---
        var dial = NewGroup("Speed Range Adjustment Dial (msg 124 y0/y1/y2)", 80);
        AddClick(dial, "Dial -", () => { if (_dial > 0) _dial--; UpdateDialLabel(); Log("Dial turned down"); });
        AddClick(dial, "Dial +", () => { if (_dial < 48) _dial++; UpdateDialLabel(); Log("Dial turned up"); });
        AddHold(dial, "Dial push", _mhc, "y2", 1, 0);
        _dialLabel = new Label { Width = 360, Height = 30, TextAlign = ContentAlignment.MiddleLeft };
        dial.Controls.Add(_dialLabel);
        UpdateDialLabel();

        var hint = new Label { Dock = DockStyle.Top, Height = 38, Padding = new Padding(10, 2, 10, 0), ForeColor = Color.DimGray,
            Text = "Hold buttons act while the mouse is down (min " + MIN_HOLD_MS + " ms). Fold = foot switch + Centre RAISE; " +
                   "unfold = foot switch + Centre LOWER. Which lever direction is forward is not known yet." };

        _log = new TextBox { Dock = DockStyle.Fill, Multiline = true, ReadOnly = true, ScrollBars = ScrollBars.Vertical,
            Font = new Font("Consolas", 9f), BackColor = Color.White };

        Controls.Add(_log);
        Controls.Add(hint);
        Controls.Add(dial.Parent);
        Controls.Add(lever.Parent);
        Controls.Add(keys.Parent);
        Controls.Add(handle.Parent);
        Controls.Add(_game);
        Controls.Add(_status);

        var t = new System.Windows.Forms.Timer { Interval = 1000 };
        t.Tick += (s, e) => { RefreshStatus(); ReadGameFile(); };
        t.Start();

        FormClosing += (s, e) => { _closing = true; };
        new Thread(PipeLoop) { IsBackground = true }.Start();
        Log("Emulator v2 started. Process name: " + System.Diagnostics.Process.GetCurrentProcess().ProcessName);
        Log("Now press 'Connect to Simulator Bridge' in the Connections app.");
    }

    FlowLayoutPanel NewGroup(string title, int height)
    {
        var box = new GroupBox { Text = title, Dock = DockStyle.Top, Height = height, Padding = new Padding(6) };
        var flow = new FlowLayoutPanel { Dock = DockStyle.Fill, AutoScroll = true };
        box.Controls.Add(flow);
        return flow;
    }

    void AddHold(FlowLayoutPanel panel, string label, Dictionary<string, int> map, string key, int down, int up)
    {
        var b = new Button { Text = label, Width = 140, Height = 44, BackColor = Color.WhiteSmoke };
        DateTime pressedAt = DateTime.MinValue;
        b.MouseDown += (s, e) =>
        {
            lock (_lock) map[key] = down;
            pressedAt = DateTime.Now;
            b.BackColor = Color.LightGreen;
            Log(label + " pressed (" + key + "=" + down + ")");
        };
        b.MouseUp += (s, e) =>
        {
            int wait = MIN_HOLD_MS - (int)(DateTime.Now - pressedAt).TotalMilliseconds;
            Action release = () =>
            {
                lock (_lock) map[key] = up;
                b.BackColor = Color.WhiteSmoke;
                Log(label + " released (" + key + "=" + up + ")");
            };
            if (wait <= 0) release();
            else
            {
                var once = new System.Windows.Forms.Timer { Interval = wait };
                once.Tick += (s2, e2) => { once.Stop(); once.Dispose(); release(); };
                once.Start();
            }
        };
        panel.Controls.Add(b);
    }

    void AddClick(FlowLayoutPanel panel, string label, Action onClick)
    {
        var b = new Button { Text = label, Width = 90, Height = 44, BackColor = Color.WhiteSmoke };
        b.Click += (s, e) => onClick();
        panel.Controls.Add(b);
    }

    void NudgeLever(int delta)
    {
        if (_parked) { Log("Lever is in the park slot: take it out first"); return; }
        int v = Math.Max(0, Math.Min(250, _lever + delta));
        _leverBar.Value = v;
        Log("Lever moved to " + v);
    }

    void UpdateLeverLabel()
    {
        _leverLabel.Text = "Lever position: " + _lever + "  (125 = neutral)" + (_parked ? "  · parked" : "");
    }

    void UpdateDialLabel()
    {
        _dialLabel.Text = "Dial step " + _dial + " → PLT_MHC_Encoder = " + (_dial * 500 + 1000);
    }

    // ---------- pipe ----------

    void PipeLoop()
    {
        while (!_closing)
        {
            NamedPipeClientStream pipe = null;
            try
            {
                pipe = new NamedPipeClientStream(".", PipeName, PipeDirection.InOut);
                while (!_closing)
                {
                    try { pipe.Connect(500); break; }
                    catch (TimeoutException) { }
                    catch (IOException) { Thread.Sleep(300); }
                }
                if (_closing) return;

                _connected = true;
                Log("CONNECTED to the Connections app over the pipe.");
                var frame = new List<byte>();
                while (!_closing && pipe.IsConnected)
                {
                    int b = pipe.ReadByte();
                    if (b < 0) break;
                    if (b != 0) { frame.Add((byte)b); continue; }
                    if (frame.Count == 0) continue;
                    byte[] msg = CobsDecode(frame.ToArray());
                    frame.Clear();
                    HandleFrame(pipe, msg);
                }
                Log("The app closed the pipe (Disconnect, or app closed).");
            }
            catch (Exception ex) { Log("Pipe error: " + ex.Message); }
            finally
            {
                _connected = false;
                if (pipe != null) pipe.Dispose();
            }
            Thread.Sleep(500);
        }
    }

    void HandleFrame(Stream pipe, byte[] msg)
    {
        if (msg.Length < 2 || msg[0] != 0x92) { Log("Unrecognised frame from app: " + Hex(msg)); return; }
        byte id = msg[1];

        if (id == MSG_MODE_REQ || id == MSG_CAN_RX_REQ)
        {
            Interlocked.Increment(ref _polls);
            if (id == MSG_MODE_REQ && msg.Length >= 3 && msg[2] != 85) Log("Mode request " + msg[2] + " (84 = calibration)");
            Thread.Sleep(5); // a real serial link is slow; don't let the app spin at 100% CPU
            // Answer every poll with the next state message in rotation. The app processes any valid
            // reply by its message ID, and skips a reply identical to the last one with the same map header.
            byte[] reply;
            switch (_replyIndex++ % 5)
            {
                case 0: reply = BuildPedals(); break;
                case 1: reply = BuildMap(MSG_MHC, MhcKeys, _mhc, true); break;
                case 2: reply = BuildMap(MSG_SCM, ScmKeys, _scm, false); break;
                case 3: reply = BuildMap(MSG_DCM, DcmKeys, _dcm, false); break;
                default: reply = BuildHydro(); break;
            }
            byte[] enc = CobsEncode(reply);
            pipe.Write(enc, 0, enc.Length);
            pipe.Flush();
        }
        else if (id == MSG_DCM_LED || id == MSG_SCM_LED)
        {
            Interlocked.Increment(ref _ledMsgs);
            Log("Button lights from app (" + (id == MSG_DCM_LED ? "DCM keys" : "SCM keypad") + "): " + DescribeMap(msg, 2));
        }
        else if (id == MSG_CAN_TX)
        {
            Interlocked.Increment(ref _canMsgs);
        }
        else
        {
            Log("Message " + id + " from app: " + Hex(msg));
        }
    }

    byte[] BuildPedals()
    {
        return new byte[] { 0x92, MSG_PEDALS, 0x81, 0xA2, (byte)'f', (byte)'s', (byte)(_footSwitch ? 0xC3 : 0xC2) };
    }

    byte[] BuildMap(byte id, string[] keys, Dictionary<string, int> map, bool withDial)
    {
        var m = new List<byte> { 0x92, id };
        AddMapHeader(m, keys.Length);
        lock (_lock)
        {
            foreach (string k in keys)
            {
                AddStr(m, k);
                int v = map[k];
                if (withDial && k == "y0") v = _dial;   // (y0 - y1) % 49 * 500 + 1000
                if (withDial && k == "y1") v = 0;
                m.Add((byte)v);                         // all values 0..48: positive fixint
            }
        }
        return m.ToArray();
    }

    byte[] BuildHydro()
    {
        int v = _parked ? 125 : _lever;
        bool p = _parked, f = !p && v > 130, r = !p && v < 120, n = !p && !f && !r;
        var m = new List<byte> { 0x92, MSG_HYDRO, 0x85 };
        AddStr(m, "v");
        if (v <= 0x7F) m.Add((byte)v); else { m.Add(0xCC); m.Add((byte)v); }   // uint8 above 127
        AddStr(m, "f"); m.Add((byte)(f ? 0xC3 : 0xC2));
        AddStr(m, "r"); m.Add((byte)(r ? 0xC3 : 0xC2));
        AddStr(m, "n"); m.Add((byte)(n ? 0xC3 : 0xC2));
        AddStr(m, "p"); m.Add((byte)(p ? 0xC3 : 0xC2));
        return m.ToArray();
    }

    static void AddMapHeader(List<byte> m, int n)
    {
        if (n <= 15) m.Add((byte)(0x80 | n));
        else { m.Add(0xDE); m.Add((byte)(n >> 8)); m.Add((byte)n); }
    }

    static void AddStr(List<byte> m, string s)
    {
        m.Add((byte)(0xA0 | s.Length));
        foreach (char c in s) m.Add((byte)c);
    }

    // ---------- COBS ----------

    static byte[] CobsEncode(byte[] data)
    {
        var o = new List<byte>(data.Length + 2);
        int codeIdx = 0; byte code = 1; o.Add(0);
        foreach (byte b in data)
        {
            if (b == 0) { o[codeIdx] = code; codeIdx = o.Count; o.Add(0); code = 1; }
            else
            {
                o.Add(b); code++;
                if (code == 0xFF) { o[codeIdx] = code; codeIdx = o.Count; o.Add(0); code = 1; }
            }
        }
        o[codeIdx] = code;
        o.Add(0); // frame delimiter
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

    // ---------- small MessagePack reader, only for showing LED messages ----------

    static string DescribeMap(byte[] d, int p)
    {
        try
        {
            int n;
            if ((d[p] & 0xF0) == 0x80) { n = d[p] & 0x0F; p += 1; }
            else if (d[p] == 0xDE) { n = (d[p + 1] << 8) | d[p + 2]; p += 3; }
            else return Hex(d);
            var sb = new StringBuilder();
            for (int i = 0; i < n; i++)
            {
                string key = ReadScalar(d, ref p);
                string val = ReadScalar(d, ref p);
                if (sb.Length > 0) sb.Append(", ");
                sb.Append(key).Append('=').Append(val);
            }
            return sb.ToString();
        }
        catch { return Hex(d); }
    }

    static string ReadScalar(byte[] d, ref int p)
    {
        byte t = d[p++];
        if (t <= 0x7F) return t.ToString();
        if ((t & 0xE0) == 0xA0) { int len = t & 0x1F; string s = Encoding.ASCII.GetString(d, p, len); p += len; return s; }
        if (t == 0xC0) return "nil";
        if (t == 0xC2) return "false";
        if (t == 0xC3) return "true";
        if (t == 0xCC) return d[p++].ToString();
        if (t == 0xCD) { int v = (d[p] << 8) | d[p + 1]; p += 2; return v.ToString(); }
        if (t >= 0xE0) return ((sbyte)t).ToString();
        throw new Exception("unsupported type");
    }

    // ---------- status, game file, log ----------

    void RefreshStatus()
    {
        int polls = Interlocked.Exchange(ref _polls, 0);
        _status.Text = _connected
            ? "CONNECTED to the app · it polls " + polls + "/s · light messages: " + _ledMsgs + " · CAN messages: " + _canMsgs
            : "Waiting for the app. In the Connections app, press 'Connect to Simulator Bridge'.";
        _status.ForeColor = _connected ? Color.DarkGreen : Color.DarkOrange;
    }

    void ReadGameFile()
    {
        try
        {
            if (!File.Exists(_gameFile)) { _game.Text = "Game file not there yet (the app creates it once the box connects):\n" + _gameFile; return; }
            string xml;
            using (var fs = new FileStream(_gameFile, FileMode.Open, FileAccess.Read, FileShare.ReadWrite | FileShare.Delete))
            using (var sr = new StreamReader(fs)) xml = sr.ReadToEnd();
            if (xml.Trim().Length == 0) { _game.Text = "Game file is empty (the app hasn't managed to write it)"; return; }
            var doc = new XmlDocument();
            doc.LoadXml(xml);
            _game.Text = "Game file (VehicleInfo.xml) @ " + DateTime.Now.ToString("HH:mm:ss") + ":  boomUnfolded=" + Val(doc, "boomUnfolded") +
                "   boomHeight=" + Val(doc, "boomHeight") + "   nozzleOnOffStatus=" + Val(doc, "nozzleOnOffStatus") +
                "   hydroHandlePosition=" + Val(doc, "hydroHandlePosition") + "   wheelSpeed=" + Val(doc, "wheelSpeed");
        }
        catch (IOException) { _game.Text = "Game file is locked by another program (can't read it right now)"; }
        catch { /* the app rewrites the file every 80 ms; a half-written read is expected now and then */ }
    }

    static string Val(XmlDocument doc, string name)
    {
        XmlNode n = doc.SelectSingleNode("//" + name);
        return n == null ? "?" : n.InnerText;
    }

    void Log(string line)
    {
        string s = DateTime.Now.ToString("HH:mm:ss.fff") + "  " + line + "\r\n";
        if (_log == null) return;
        if (_log.InvokeRequired) { try { _log.BeginInvoke((Action)(() => _log.AppendText(s))); } catch { } }
        else _log.AppendText(s);
    }

    static string Hex(byte[] d) { return BitConverter.ToString(d).Replace("-", " "); }
}
