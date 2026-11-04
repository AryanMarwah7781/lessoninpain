using System;
using System.IO;
using System.Windows;
using LessonPanel.Overlay;
using LessonPanel.Services;
using LessonPanel.ViewModels;
using Newtonsoft.Json;

namespace LessonPanel;

/// <summary>Standalone host for the lesson monitor. The Connections app can host LessonPanelView directly later.</summary>
public partial class MainWindow : Window
{
    static readonly string PlacementFile = Path.Combine(Environment.GetFolderPath(Environment.SpecialFolder.LocalApplicationData), "LessonStudio", "window.json");
    readonly SimApi _api;
    readonly LessonViewModel _vm;
    readonly ScreenOverlay _displayRing, _cornerRing;

    public MainWindow()
    {
        InitializeComponent();
        _api = new SimApi(Environment.GetEnvironmentVariable("LESSON_STUDIO_API") ?? "http://127.0.0.1:47900");
        _vm = new LessonViewModel(_api, Dispatcher);
        Panel.DataContext = _vm;
        _displayRing = new ScreenOverlay("display", _api);
        _cornerRing = new ScreenOverlay("pdu", _api);
        _vm.ScreenTargetsChanged += t => { _displayRing.SetTargets(t); _cornerRing.SetTargets(t); };
        RestorePlacement();
        Loaded += async (_, _) =>
        {
            _displayRing.Start();
            _cornerRing.Start();
            await _vm.StartAsync();
        };
        Closing += (_, _) => SavePlacement();
        Closed += (_, _) =>
        {
            _displayRing.Close();
            _cornerRing.Close();
            _vm.Dispose();
            _api.Dispose();
        };
    }

    sealed record Placement(double Left, double Top, double Width, double Height, bool Maximized);

    // Opens where it was last (normally the trainee's second monitor), maximized.
    void RestorePlacement()
    {
        try
        {
            var p = JsonConvert.DeserializeObject<Placement>(File.ReadAllText(PlacementFile));
            if (p != null && p.Width > 200 && IsOnScreen(p))
            {
                Left = p.Left; Top = p.Top; Width = p.Width; Height = p.Height;
                if (p.Maximized) WindowState = WindowState.Maximized;
                return;
            }
        }
        catch (Exception) { }
        Left = SystemParameters.WorkArea.Left;
        Top = SystemParameters.WorkArea.Top;
        WindowState = WindowState.Maximized;
    }

    static bool IsOnScreen(Placement p) =>
        p.Left + 100 > SystemParameters.VirtualScreenLeft && p.Top + 50 > SystemParameters.VirtualScreenTop &&
        p.Left < SystemParameters.VirtualScreenLeft + SystemParameters.VirtualScreenWidth - 100 &&
        p.Top < SystemParameters.VirtualScreenTop + SystemParameters.VirtualScreenHeight - 50;

    void SavePlacement()
    {
        try
        {
            var r = RestoreBounds;
            Directory.CreateDirectory(Path.GetDirectoryName(PlacementFile)!);
            File.WriteAllText(PlacementFile, JsonConvert.SerializeObject(new Placement(r.Left, r.Top, r.Width, r.Height, WindowState == WindowState.Maximized)));
        }
        catch (Exception) { }
    }
}
