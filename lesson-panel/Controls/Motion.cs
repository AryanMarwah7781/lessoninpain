using System.Windows;

namespace LessonPanel.Controls;

/// <summary>Whether to animate: follows Windows' "Show animations" setting (Settings, Accessibility, Visual effects).</summary>
public static class Motion
{
    public static bool Enabled => SystemParameters.ClientAreaAnimation;
}
