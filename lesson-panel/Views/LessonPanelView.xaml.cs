using System;
using System.ComponentModel;
using System.Linq;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Media;
using System.Windows.Media.Animation;
using LessonPanel.Controls;
using LessonPanel.Services;
using LessonPanel.ViewModels;

namespace LessonPanel.Views;

/// <summary>The lesson monitor: the lesson as the manual's numbered procedure, beside the armrest.
/// Built as a UserControl so the Connections app can host it later.</summary>
public partial class LessonPanelView : UserControl
{
    public LessonPanelView()
    {
        InitializeComponent();
        DataContextChanged += (_, e) =>
        {
            if (e.OldValue is LessonViewModel old) Unhook(old);
            if (e.NewValue is LessonViewModel vm) Hook(vm);
        };
    }

    void Hook(LessonViewModel vm)
    {
        vm.HandleTargetsChanged += OnHandleTargets;
        vm.HandlePressed += Handle.Flash;
        vm.PropertyChanged += OnVmChanged;
        UpdateChips(vm);
        if (vm.HandleMap != null) Handle.SetFigure(vm.HandleFigure, vm.HandleMap);
    }

    void Unhook(LessonViewModel vm)
    {
        vm.HandleTargetsChanged -= OnHandleTargets;
        vm.HandlePressed -= Handle.Flash;
        vm.PropertyChanged -= OnVmChanged;
    }

    void OnHandleTargets(System.Collections.Generic.IReadOnlyList<HandleTarget> targets)
    {
        Handle.SetTargets(targets);
        Dispatcher.BeginInvoke(ScrollToCurrent, System.Windows.Threading.DispatcherPriority.Loaded);
    }

    void OnVmChanged(object? sender, PropertyChangedEventArgs e)
    {
        if (sender is not LessonViewModel vm) return;
        switch (e.PropertyName)
        {
            case nameof(LessonViewModel.ArmrestLinked):
            case nameof(LessonViewModel.Online):
            case nameof(LessonViewModel.DisplayOpen):
            case nameof(LessonViewModel.ApiUp):
                UpdateChips(vm);
                break;
            case nameof(LessonViewModel.HandleFigure):
            case nameof(LessonViewModel.HandleMap):
                if (vm.HandleMap != null) Handle.SetFigure(vm.HandleFigure, vm.HandleMap);
                break;
        }
    }

    // Chips say their state in words; the dot only repeats it.
    void UpdateChips(LessonViewModel vm)
    {
        Chip(chipArm, dotArm, txtArm, vm.ArmrestLinked, "Armrest linked", "Armrest not linked");
        Chip(chipOnline, dotOnline, txtOnline, vm.Online, "Signed in, online", "Offline");
        Chip(chipDisplay, dotDisplay, txtDisplay, vm.DisplayOpen, "Gen 4 display open", "Display not open");
    }

    void Chip(Border chip, System.Windows.Shapes.Ellipse dot, TextBlock text, bool ok, string yes, string no)
    {
        text.Text = ok ? yes : no;
        chip.Background = (Brush)FindResource(ok ? "GreenSoft" : "Soft");
        chip.BorderBrush = ok ? new SolidColorBrush(Color.FromRgb(0xCF, 0xE3, 0xCA)) : (Brush)FindResource("Line");
        text.Foreground = (Brush)FindResource(ok ? "Green" : "Muted");
        dot.Fill = ok ? (Brush)FindResource("GreenBright") : Brushes.Transparent;
        dot.Stroke = ok ? null : (Brush)FindResource("Faint");
        dot.StrokeThickness = ok ? 0 : 1.5;
    }

    /// <summary>Keeps the opened-up step in view, a little below the top, so finished steps stay visible above it.</summary>
    void ScrollToCurrent()
    {
        var current = FindCurrent(ProcedureScroll);
        if (current == null) return;
        var pos = current.TransformToAncestor(ProcedureScroll).Transform(new Point(0, 0)).Y + ProcedureScroll.VerticalOffset;
        var target = Math.Max(0, pos - 180);
        if (!Motion.Enabled || Math.Abs(target - ProcedureScroll.VerticalOffset) < 2)
        {
            ProcedureScroll.ScrollToVerticalOffset(target);
            return;
        }
        var from = ProcedureScroll.VerticalOffset;
        var start = DateTime.Now;
        void Step(object? s, EventArgs e)
        {
            var t = Math.Min(1, (DateTime.Now - start).TotalMilliseconds / 320);
            var eased = 1 - Math.Pow(1 - t, 3);
            ProcedureScroll.ScrollToVerticalOffset(from + (target - from) * eased);
            if (t >= 1) CompositionTarget.Rendering -= Step;
        }
        CompositionTarget.Rendering += Step;
    }

    static FrameworkElement? FindCurrent(DependencyObject root)
    {
        for (var i = 0; i < VisualTreeHelper.GetChildrenCount(root); i++)
        {
            var child = VisualTreeHelper.GetChild(root, i);
            if (child is FrameworkElement fe && Equals(fe.Tag, "current-step") && fe.IsVisible) return fe;
            var found = FindCurrent(child);
            if (found != null) return found;
        }
        return null;
    }
}
