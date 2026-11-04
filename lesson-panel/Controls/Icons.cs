using System.Windows.Media;

namespace LessonPanel.Controls;

/// <summary>Drawn icons, one stroke family (round caps, 2px at 24px), so no glyph stands in for an icon.</summary>
public static class Icons
{
    static Geometry G(string d)
    {
        var g = Geometry.Parse(d);
        g.Freeze();
        return g;
    }

    public static readonly Geometry Check = G("M2,8 L7,13 L18,2");
    public static readonly Geometry Cross = G("M3,3 L15,15 M15,3 L3,15");
    public static readonly Geometry Play = G("M5,3 L17,10 L5,17 Z");
    public static readonly Geometry Bulb = G("M10,2 C6,2 4,5 4,8 C4,11 6,12 7,14 L13,14 C14,12 16,11 16,8 C16,5 14,2 10,2 Z M7.5,17 L12.5,17");
    public static readonly Geometry Chat = G("M3,4 L17,4 L17,13 L9,13 L5,17 L5,13 L3,13 Z");
    public static readonly Geometry Skip = G("M4,4 L12,10 L4,16 Z M15,4 L15,16");
    public static readonly Geometry Dot = G("M6,0 A6,6 0 1 1 5.99,0 Z");
}
