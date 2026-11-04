using System;
using System.Collections.Generic;
using System.Linq;
using System.Runtime.InteropServices;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Interop;
using System.Windows.Media;
using System.Windows.Media.Animation;
using System.Windows.Shapes;
using System.Windows.Threading;
using LessonPanel.Controls;
using LessonPanel.Services;
using Newtonsoft.Json.Linq;

namespace LessonPanel.Overlay;

/// <summary>A click-through, always-on-top window laid exactly over one of the Connections app's windows
/// ("display" = Gen 4, "pdu" = corner post), drawing yellow rings on what to touch or watch.
/// Works in that window's own pixels, so it lines up on any monitor and scaling.</summary>
public sealed class ScreenOverlay : Window
{
    readonly string _kind;
    readonly SimApi _api;
    readonly Canvas _canvas = new();
    readonly DispatcherTimer _follow = new() { Interval = TimeSpan.FromMilliseconds(250) };
    readonly DispatcherTimer _lookup = new() { Interval = TimeSpan.FromSeconds(4) };
    IntPtr _self, _target;
    int[]? _picture;
    int _w, _h;
    List<ScreenTarget> _press = new(), _watch = new();

    public ScreenOverlay(string kind, SimApi api)
    {
        _kind = kind;
        _api = api;
        Title = "Lesson Studio ring overlay (" + kind + ")";
        WindowStyle = WindowStyle.None;
        AllowsTransparency = true;
        Background = Brushes.Transparent;
        Topmost = true;
        ShowInTaskbar = false;
        ShowActivated = false;
        ResizeMode = ResizeMode.NoResize;
        Content = new Viewbox { Stretch = Stretch.Fill, Child = _canvas };
        _follow.Tick += (_, _) => Follow();
        _lookup.Tick += async (_, _) => await LookupAsync();
        SourceInitialized += (_, _) =>
        {
            _self = new WindowInteropHelper(this).Handle;
            var ex = GetWindowLong(_self, GWL_EXSTYLE);
            SetWindowLong(_self, GWL_EXSTYLE, ex | WS_EX_TRANSPARENT | WS_EX_LAYERED | WS_EX_TOOLWINDOW | WS_EX_NOACTIVATE);
        };
    }

    public void Start()
    {
        Width = 1; Height = 1; Left = -10; Top = -10;
        Show();
        Hide();
        _follow.Start();
        _lookup.Start();
        _ = LookupAsync();
    }

    public void SetTargets(ScreenTargets targets)
    {
        _press = targets.Press.Where(t => t.Window == _kind).ToList();
        _watch = targets.Watch.Where(t => t.Window == _kind).ToList();
        Draw();
        Follow();
    }

    async System.Threading.Tasks.Task LookupAsync()
    {
        try
        {
            var screens = await _api.ScreensAsync();
            if (screens == null || !screens.TryGetValue(_kind, out var w) || w is not JObject o)
            {
                _target = IntPtr.Zero;
                return;
            }
            var win = o.ToObject<ScreenWindow>()!;
            _target = new IntPtr(win.Hwnd);
            var changed = _picture == null != (win.Picture == null) || (_picture != null && win.Picture != null && !_picture.SequenceEqual(win.Picture));
            _picture = win.Picture;
            if (changed) Draw();
        }
        catch (Exception) { }
    }

    void Follow()
    {
        if (_target == IntPtr.Zero || (_press.Count == 0 && _watch.Count == 0) || !IsWindow(_target) || IsIconic(_target) || !IsWindowVisible(_target))
        {
            if (IsVisible) Hide();
            return;
        }
        if (!GetWindowRect(_target, out var r)) return;
        int w = r.Right - r.Left, h = r.Bottom - r.Top;
        if (w != _w || h != _h)
        {
            _w = w; _h = h;
            Draw();
            _ = LookupAsync();       // the picture box moves when the window is resized
        }
        // hide when something else covers the first target, so rings never float over other windows
        var first = _press.Concat(_watch).First();
        var c = ToWindow(first);
        var pt = new POINT { X = r.Left + (int)((c.Left + c.Right) / 2), Y = r.Top + (int)((c.Top + c.Bottom) / 2) };
        var hit = WindowFromPoint(pt);
        var covered = hit != IntPtr.Zero && GetAncestor(hit, GA_ROOT) != _target;
        if (covered) { if (IsVisible) Hide(); return; }
        if (!IsVisible) Show();
        SetWindowPos(_self, HWND_TOPMOST, r.Left, r.Top, w, h, SWP_NOACTIVATE | SWP_SHOWWINDOW);
    }

    Rect ToWindow(ScreenTarget t)
    {
        double x0, y0, pw, ph;
        if (_kind == "display" && _picture != null && _picture.Length == 4)
        {
            x0 = _picture[0]; y0 = _picture[1]; pw = _picture[2] - _picture[0]; ph = _picture[3] - _picture[1];
        }
        else { x0 = 0; y0 = 0; pw = _w; ph = _h; }
        return new Rect(x0 + t.Rect[0] * pw, y0 + t.Rect[1] * ph, (t.Rect[2] - t.Rect[0]) * pw, (t.Rect[3] - t.Rect[1]) * ph);
    }

    void Draw()
    {
        _canvas.Children.Clear();
        if (_w <= 0 || _h <= 0) return;
        _canvas.Width = _w;
        _canvas.Height = _h;
        foreach (var t in _watch) Ring(t, false);
        foreach (var t in _press) Ring(t, true);
    }

    void Ring(ScreenTarget t, bool touch)
    {
        var r = ToWindow(t);
        r.Inflate(8, 8);
        var yellow = (Brush)FindResource("Yellow");
        var ink = (Brush)FindResource("Ink");
        Add(new Rectangle { Width = r.Width, Height = r.Height, RadiusX = 10, RadiusY = 10, Stroke = ink, StrokeThickness = 9, Opacity = 0.75 }, r.X, r.Y);
        var ring = new Rectangle { Width = r.Width, Height = r.Height, RadiusX = 10, RadiusY = 10, Stroke = yellow, StrokeThickness = touch ? 6 : 4 };
        if (!touch) ring.StrokeDashArray = new DoubleCollection { 3, 2 };
        Add(ring, r.X, r.Y);
        if (touch && Motion.Enabled)
        {
            var halo = new Rectangle { Width = r.Width + 24, Height = r.Height + 24, RadiusX = 16, RadiusY = 16, Stroke = yellow, StrokeThickness = 4 };
            Add(halo, r.X - 12, r.Y - 12);
            halo.BeginAnimation(OpacityProperty, new DoubleAnimation(0.9, 0, TimeSpan.FromMilliseconds(1200))
                { RepeatBehavior = RepeatBehavior.Forever, EasingFunction = new QuadraticEase { EasingMode = EasingMode.EaseOut } });
        }
        var label = new Border
        {
            Background = yellow, BorderBrush = ink, BorderThickness = new Thickness(2), CornerRadius = new CornerRadius(5), Padding = new Thickness(12, 4, 12, 5),
            Child = new TextBlock { Text = (touch ? "Touch: " : "Watch: ") + t.Label, FontFamily = (FontFamily)FindResource("Face"), FontSize = 24, FontWeight = FontWeights.Bold, Foreground = ink }
        };
        label.Measure(new Size(double.PositiveInfinity, double.PositiveInfinity));
        var ly = r.Y - label.DesiredSize.Height - 8;
        if (ly < 0) ly = r.Bottom + 8;
        var lx = Math.Max(6, Math.Min(r.X, _w - label.DesiredSize.Width - 6));
        Add(label, lx, ly);
    }

    void Add(UIElement e, double x, double y)
    {
        Canvas.SetLeft(e, x);
        Canvas.SetTop(e, y);
        _canvas.Children.Add(e);
    }

    protected override void OnClosed(EventArgs e)
    {
        _follow.Stop();
        _lookup.Stop();
        base.OnClosed(e);
    }

    // ---- Win32
    const int GWL_EXSTYLE = -20, WS_EX_TRANSPARENT = 0x20, WS_EX_LAYERED = 0x80000, WS_EX_TOOLWINDOW = 0x80, WS_EX_NOACTIVATE = 0x8000000;
    const uint SWP_NOACTIVATE = 0x10, SWP_SHOWWINDOW = 0x40, GA_ROOT = 2;
    static readonly IntPtr HWND_TOPMOST = new(-1);
    [StructLayout(LayoutKind.Sequential)] struct RECT { public int Left, Top, Right, Bottom; }
    [StructLayout(LayoutKind.Sequential)] struct POINT { public int X, Y; }
    [DllImport("user32.dll")] static extern int GetWindowLong(IntPtr h, int i);
    [DllImport("user32.dll")] static extern int SetWindowLong(IntPtr h, int i, int v);
    [DllImport("user32.dll")] static extern bool GetWindowRect(IntPtr h, out RECT r);
    [DllImport("user32.dll")] static extern bool SetWindowPos(IntPtr h, IntPtr after, int x, int y, int cx, int cy, uint flags);
    [DllImport("user32.dll")] static extern bool IsWindow(IntPtr h);
    [DllImport("user32.dll")] static extern bool IsIconic(IntPtr h);
    [DllImport("user32.dll")] static extern bool IsWindowVisible(IntPtr h);
    [DllImport("user32.dll")] static extern IntPtr WindowFromPoint(POINT p);
    [DllImport("user32.dll")] static extern IntPtr GetAncestor(IntPtr h, uint flags);
}
