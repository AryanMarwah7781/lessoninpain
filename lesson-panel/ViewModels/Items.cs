using System.Windows.Media.Imaging;

namespace LessonPanel.ViewModels;

/// <summary>A section title in the procedure list.</summary>
public sealed class SectionRow
{
    public SectionRow(string title) => Title = title;
    public string Title { get; }
}

/// <summary>One numbered step in the procedure list. The current step is expanded by the view.</summary>
public sealed class StepRow : Observable
{
    BitmapImage? _thumb;
    string _state = "upcoming";

    public StepRow(int number, string id, string say)
    {
        Number = number;
        Id = id;
        Say = say;
    }

    public int Number { get; }
    public string Id { get; }
    public string Say { get; }
    public string? FigureKey { get; set; }

    /// <summary>"done", "skipped", "current" or "upcoming".</summary>
    public string State { get => _state; set { if (Set(ref _state, value)) { Raise(nameof(IsCurrent)); Raise(nameof(IsDone)); Raise(nameof(IsSkipped)); } } }
    public bool IsCurrent => _state == "current";
    public bool IsDone => _state == "done";
    public bool IsSkipped => _state == "skipped";
    public BitmapImage? Thumb { get => _thumb; set => Set(ref _thumb, value); }
}

/// <summary>A control the current step needs, shown as a numbered card with the manual's photo.</summary>
public sealed class TargetCard : Observable
{
    BitmapImage? _photo;
    bool _done;
    bool _lit;

    public int Order { get; init; }
    public string ControlId { get; init; } = "";
    public string Label { get; init; } = "";
    public string Where { get; init; } = "";
    public string? Note { get; init; }
    public string? FigureKey { get; init; }
    public string? PageText { get; init; }
    public string? HandleLetter { get; init; }
    public BitmapImage? Photo { get => _photo; set => Set(ref _photo, value); }
    public bool Done { get => _done; set => Set(ref _done, value); }
    public bool Lit { get => _lit; set => Set(ref _lit, value); }
}

/// <summary>Something the simulator can't sense: the trainee marks it Done.</summary>
public sealed class ConfirmItem : Observable
{
    bool _done;
    public ConfirmItem(string text) => Text = text;
    public string Text { get; }
    public bool Done { get => _done; set => Set(ref _done, value); }
}

/// <summary>Something to touch or watch on the display monitor.</summary>
public sealed class ScreenNote
{
    public ScreenNote(string verb, string label, string where)
    {
        Verb = verb;
        Label = label;
        Where = where;
    }

    public string Verb { get; }
    public string Label { get; }
    public string Where { get; }
}

/// <summary>A lesson in the chooser.</summary>
public sealed class LessonChoice
{
    public string Id { get; init; } = "";
    public string Title { get; init; } = "";
    public string Machine { get; init; } = "";
    public string Length { get; init; } = "";
    /// <summary>"612R" or "R4045", read from the lesson's machine line; picks which machine tile lists it.</summary>
    public string MachineKey { get; init; } = "";
    public int Minutes { get; init; }

    public static string KeyFor(string machine) =>
        machine.Contains("612R", StringComparison.OrdinalIgnoreCase) ? "612R"
        : machine.Contains("R4045", StringComparison.OrdinalIgnoreCase) || machine.Contains("4045") ? "R4045" : "";
}
