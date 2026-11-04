using System;
using System.Collections.Generic;
using System.Linq;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Media;
using System.Windows.Media.Animation;
using System.Windows.Media.Imaging;
using System.Windows.Shapes;
using LessonPanel.Services;

namespace LessonPanel.Controls;

/// <summary>One button to point at on the handle: its letter in the manual drawing, its order in the step, and
/// whether the trainee has already pressed it in this step.</summary>
public sealed record HandleTarget(string Letter, int Order, bool Done);

public partial class HandleView : UserControl
{
    HandleMap? _map;
    readonly Dictionary<string, FrameworkElement> _rings = new();

    public HandleView() => InitializeComponent();

    public void SetFigure(BitmapImage? image, HandleMap map)
    {
        _map = map;
        Figure.Source = image;
        Stage.Width = map.Size[0];
        Stage.Height = map.Size[1];
        ShowArea(0, 0, map.Size[0], map.Size[1]);
    }

    /// <summary>Zooms to the view (front or side) that holds every target; the whole drawing otherwise.</summary>
    void Zoom(IReadOnlyList<HandleTarget> targets)
    {
        if (_map == null) return;
        foreach (var v in _map.Views.Values)
        {
            var inside = targets.Count > 0 && targets.All(t => _map.Buttons.TryGetValue(t.Letter, out var b)
                         && b.Box[0] >= v[0] && b.Box[2] <= v[2] && b.Box[1] >= v[1] && b.Box[3] <= v[3]);
            if (inside) { ShowArea(v[0], v[1], v[2], v[3]); return; }
        }
        ShowArea(0, 0, _map.Size[0], _map.Size[1]);
    }

    void ShowArea(double x0, double y0, double x1, double y1)
    {
        Crop.Width = x1 - x0;
        Crop.Height = y1 - y0;
        Pan.X = -x0;
        Pan.Y = -y0;
    }

    /// <summary>Draws a ring and an order number on each target. The first target not yet done pulses.</summary>
    public void SetTargets(IReadOnlyList<HandleTarget> targets)
    {
        Overlay.Children.Clear();
        _rings.Clear();
        if (_map == null) return;
        Zoom(targets);
        var pulseDone = false;
        foreach (var t in targets)
        {
            if (!_map.Buttons.TryGetValue(t.Letter, out var b)) continue;
            var current = !t.Done && !pulseDone;
            if (current) pulseDone = true;
            var ring = BuildRing(b.Box, t, current);
            Overlay.Children.Add(ring);
            _rings[t.Letter] = ring;
        }
    }

    /// <summary>Brief green fill on a button the trainee just pressed (from the live event stream).</summary>
    public void Flash(string letter)
    {
        if (_map == null || !_map.Buttons.TryGetValue(letter, out var b)) return;
        var r = Inflate(b.Box, 6);
        var fill = new Rectangle { Width = r.Width, Height = r.Height, RadiusX = 8, RadiusY = 8, Fill = new SolidColorBrush(Color.FromArgb(150, 0x32, 0x93, 0x3A)) };
        Canvas.SetLeft(fill, r.X);
        Canvas.SetTop(fill, r.Y);
        Overlay.Children.Add(fill);
        var fade = new DoubleAnimation(1, 0, TimeSpan.FromMilliseconds(Motion.Enabled ? 700 : 1)) { BeginTime = TimeSpan.FromMilliseconds(Motion.Enabled ? 250 : 400) };
        fade.Completed += (_, _) => Overlay.Children.Remove(fill);
        fill.BeginAnimation(OpacityProperty, fade);
    }

    FrameworkElement BuildRing(double[] box, HandleTarget t, bool current)
    {
        var r = Inflate(box, 9);
        var accent = t.Done ? (Brush)FindResource("GreenBright") : (Brush)FindResource("Yellow");
        var ink = (Brush)FindResource("Ink");
        var g = new Canvas { Width = r.Width, Height = r.Height };
        // dark outline under the coloured ring keeps it visible on the light drawing and on the dark handle
        g.Children.Add(Shape(new Rectangle { RadiusX = 10, RadiusY = 10, Stroke = ink, StrokeThickness = 9 }, r.Width, r.Height, 0, 0));
        g.Children.Add(Shape(new Rectangle { RadiusX = 10, RadiusY = 10, Stroke = accent, StrokeThickness = 5 }, r.Width, r.Height, 0, 0));
        if (current)
        {
            var halo = Shape(new Rectangle { RadiusX = 16, RadiusY = 16, Stroke = accent, StrokeThickness = 4 }, r.Width + 20, r.Height + 20, -10, -10);
            g.Children.Add(halo);
            if (Motion.Enabled)
            {
                var a = new DoubleAnimation(0.9, 0.0, TimeSpan.FromMilliseconds(1200)) { RepeatBehavior = RepeatBehavior.Forever, EasingFunction = new QuadraticEase { EasingMode = EasingMode.EaseOut } };
                halo.BeginAnimation(OpacityProperty, a);
            }
        }
        // order badge (or a check once done), top-right corner
        var badge = new Grid { Width = 40, Height = 40 };
        badge.Children.Add(new Ellipse { Fill = accent, Stroke = ink, StrokeThickness = 3 });
        if (t.Done)
            badge.Children.Add(new Path { Data = Icons.Check, Stroke = Brushes.White, StrokeThickness = 4, StrokeStartLineCap = PenLineCap.Round, StrokeEndLineCap = PenLineCap.Round, StrokeLineJoin = PenLineJoin.Round, Width = 18, Height = 14, Stretch = Stretch.Uniform });
        else
            badge.Children.Add(new TextBlock
            {
                Text = t.Order.ToString(), FontFamily = (FontFamily)FindResource("Face"), FontSize = 24, FontWeight = FontWeights.Bold,
                Foreground = ink, HorizontalAlignment = HorizontalAlignment.Center, VerticalAlignment = VerticalAlignment.Center, Margin = new Thickness(0, -2, 0, 0)
            });
        Canvas.SetLeft(badge, r.Width - 22);
        Canvas.SetTop(badge, -22);
        g.Children.Add(badge);
        Canvas.SetLeft(g, r.X);
        Canvas.SetTop(g, r.Y);
        return g;
    }

    static FrameworkElement Shape(Shape s, double w, double h, double x, double y)
    {
        s.Width = w;
        s.Height = h;
        Canvas.SetLeft(s, x);
        Canvas.SetTop(s, y);
        return s;
    }

    static Rect Inflate(double[] box, double by) => new(box[0] - by, box[1] - by, box[2] - box[0] + 2 * by, box[3] - box[1] + 2 * by);
}
