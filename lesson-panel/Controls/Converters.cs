using System;
using System.Globalization;
using System.Windows;
using System.Windows.Data;

namespace LessonPanel.Controls;

/// <summary>Visible when the bound string has text (or any non-null object).</summary>
public sealed class NotEmptyToVisibility : IValueConverter
{
    public object Convert(object? value, Type t, object? p, CultureInfo c) =>
        value switch { null => Visibility.Collapsed, string s => s.Length > 0 ? Visibility.Visible : Visibility.Collapsed, _ => Visibility.Visible };
    public object ConvertBack(object? value, Type t, object? p, CultureInfo c) => throw new NotSupportedException();
}

/// <summary>Visible when the bound value's text equals the parameter (one of several "|"-separated values).</summary>
public sealed class EqualsToVisibility : IValueConverter
{
    public object Convert(object? value, Type t, object? p, CultureInfo c)
    {
        var v = value?.ToString() ?? "";
        foreach (var option in (p?.ToString() ?? "").Split('|'))
            if (option == v) return Visibility.Visible;
        return Visibility.Collapsed;
    }
    public object ConvertBack(object? value, Type t, object? p, CultureInfo c) => throw new NotSupportedException();
}

/// <summary>bool to Visibility; parameter "invert" flips it.</summary>
public sealed class BoolToVisibility : IValueConverter
{
    public object Convert(object? value, Type t, object? p, CultureInfo c)
    {
        var b = value is bool x && x;
        if (p?.ToString() == "invert") b = !b;
        return b ? Visibility.Visible : Visibility.Collapsed;
    }
    public object ConvertBack(object? value, Type t, object? p, CultureInfo c) => throw new NotSupportedException();
}
