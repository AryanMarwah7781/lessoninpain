using System.Collections.Generic;
using Newtonsoft.Json;
using Newtonsoft.Json.Linq;

namespace LessonPanel.Services;

// Shapes of the simulator API's JSON (simapi/server.py, simapi/lesson.py). Field names follow the API.

public sealed class LessonInfo
{
    [JsonProperty("id")] public string Id { get; set; } = "";
    [JsonProperty("title")] public string Title { get; set; } = "";
    [JsonProperty("machine")] public string Machine { get; set; } = "";
    [JsonProperty("steps")] public int Steps { get; set; }
    [JsonProperty("minutes")] public int? Minutes { get; set; }
}

public sealed class LessonResponse
{
    [JsonProperty("running")] public bool Running { get; set; }
    [JsonProperty("lesson")] public string? Lesson { get; set; }
    [JsonProperty("view")] public StepView? View { get; set; }
}

public sealed class StepView
{
    [JsonProperty("finished")] public bool Finished { get; set; }
    [JsonProperty("index")] public int Index { get; set; }
    [JsonProperty("of")] public int Of { get; set; }
    [JsonProperty("section")] public string Section { get; set; } = "";
    [JsonProperty("step")] public string Step { get; set; } = "";
    [JsonProperty("say")] public string Say { get; set; } = "";
    [JsonProperty("why")] public string Why { get; set; } = "";
    [JsonProperty("controls")] public List<string> Controls { get; set; } = new();
    [JsonProperty("seconds_on_step")] public double SecondsOnStep { get; set; }
    [JsonProperty("done_status")] public string DoneStatus { get; set; } = "";
    [JsonProperty("mistakes")] public List<string> Mistakes { get; set; } = new();
    [JsonProperty("hint")] public Hint? Hint { get; set; }
    /// <summary>All of the step's hints, due or not, so the trainee can ask for one early.</summary>
    [JsonProperty("hints")] public List<Hint> Hints { get; set; } = new();
    [JsonProperty("check")] public string Check { get; set; } = "";
    [JsonProperty("armrest")] public List<ArmrestTarget> Armrest { get; set; } = new();
    [JsonProperty("screen")] public ScreenTargets Screen { get; set; } = new();
    [JsonProperty("figures")] public List<ManualFigure> Figures { get; set; } = new();
    [JsonProperty("advanced")] public bool Advanced { get; set; }
    /// <summary>learn | practice | assess (assess: no hints, no Show me).</summary>
    [JsonProperty("mode")] public string Mode { get; set; } = "learn";
    /// <summary>Texts of the step's confirm checks: things the trainee marks Done.</summary>
    [JsonProperty("confirm")] public List<string> Confirm { get; set; } = new();
    [JsonProperty("source")] public StepSource? Source { get; set; }
    [JsonProperty("figure")] public string? Figure { get; set; }
}

public sealed class StepSource
{
    [JsonProperty("pages")] public List<string> Pages { get; set; } = new();
    [JsonProperty("topic")] public string? Topic { get; set; }
}

public sealed class Hint
{
    [JsonProperty("after_s")] public double AfterSeconds { get; set; }
    [JsonProperty("say")] public string Say { get; set; } = "";
    [JsonProperty("highlight")] public List<string> Highlight { get; set; } = new();
}

public sealed class ArmrestTarget
{
    [JsonProperty("id")] public string Id { get; set; } = "";
    [JsonProperty("label")] public string Label { get; set; } = "";
    [JsonProperty("module_id")] public string? ModuleId { get; set; }
    [JsonProperty("module")] public string Module { get; set; } = "";
    [JsonProperty("sends")] public string? Sends { get; set; }
    [JsonProperty("certainty")] public string? Certainty { get; set; }
    [JsonProperty("manual")] public ManualRef? Manual { get; set; }
}

public sealed class ManualRef
{
    [JsonProperty("handle")] public string? Handle { get; set; }
    [JsonProperty("figures")] public List<string> Figures { get; set; } = new();
    [JsonProperty("certainty")] public string Certainty { get; set; } = "";
    [JsonProperty("where")] public string Where { get; set; } = "";
}

public sealed class ScreenTargets
{
    [JsonProperty("press")] public List<ScreenTarget> Press { get; set; } = new();
    [JsonProperty("watch")] public List<ScreenTarget> Watch { get; set; } = new();
}

public sealed class ScreenTarget
{
    [JsonProperty("id")] public string Id { get; set; } = "";
    [JsonProperty("window")] public string Window { get; set; } = "";
    [JsonProperty("label")] public string Label { get; set; } = "";
    [JsonProperty("kind")] public string Kind { get; set; } = "";
    [JsonProperty("rect")] public double[] Rect { get; set; } = new double[4];
    [JsonProperty("figure")] public string? Figure { get; set; }
}

public sealed class ManualFigure
{
    [JsonProperty("key")] public string Key { get; set; } = "";
    [JsonProperty("page")] public int? Page { get; set; }
    [JsonProperty("caption")] public string Caption { get; set; } = "";
    [JsonProperty("callouts")] public Dictionary<string, string> Callouts { get; set; } = new();
}

public sealed class LessonPlan
{
    [JsonProperty("running")] public bool Running { get; set; }
    [JsonProperty("id")] public string Id { get; set; } = "";
    [JsonProperty("title")] public string Title { get; set; } = "";
    [JsonProperty("machine")] public string Machine { get; set; } = "";
    [JsonProperty("objective")] public string Objective { get; set; } = "";
    [JsonProperty("index")] public int Index { get; set; }
    [JsonProperty("sections")] public List<PlanSection> Sections { get; set; } = new();
}

public sealed class PlanSection
{
    [JsonProperty("title")] public string Title { get; set; } = "";
    [JsonProperty("steps")] public List<PlanStep> Steps { get; set; } = new();
}

public sealed class PlanStep
{
    [JsonProperty("id")] public string Id { get; set; } = "";
    [JsonProperty("say")] public string Say { get; set; } = "";
    [JsonProperty("status")] public string? Status { get; set; }
    [JsonProperty("confidence")] public string? Confidence { get; set; }
    [JsonProperty("controls")] public List<string> Controls { get; set; } = new();
    [JsonProperty("figure")] public string? Figure { get; set; }
}

public sealed class ScreenWindow
{
    [JsonProperty("hwnd")] public long Hwnd { get; set; }
    [JsonProperty("size")] public int[] Size { get; set; } = new int[2];
    [JsonProperty("hung")] public bool Hung { get; set; }
    [JsonProperty("picture")] public int[]? Picture { get; set; }
}

public sealed class Health
{
    [JsonProperty("ok")] public bool Ok { get; set; }
    [JsonProperty("online")] public bool Online { get; set; }
    [JsonProperty("armrest")] public bool Armrest { get; set; }
    /// <summary>"connected" when the virtual armrest is linked to the Connections app.</summary>
    [JsonProperty("armrest_link")] public string? ArmrestLink { get; set; }
    [JsonProperty("app")] public Dictionary<string, string> App { get; set; } = new();
}

public sealed class HandleMap
{
    [JsonProperty("figure")] public string Figure { get; set; } = "";
    [JsonProperty("size")] public int[] Size { get; set; } = new int[2];
    [JsonProperty("buttons")] public Dictionary<string, HandleButton> Buttons { get; set; } = new();
    /// <summary>Areas of the drawing ("front", "side") as [x0, y0, x1, y1] pixels, for zooming in.</summary>
    [JsonProperty("views")] public Dictionary<string, double[]> Views { get; set; } = new();
}

public sealed class HandleButton
{
    [JsonProperty("box")] public double[] Box { get; set; } = new double[4];
    [JsonProperty("function")] public string Function { get; set; } = "";
}

public sealed class FigureMap
{
    [JsonProperty("handle")] public HandleMap? Handle { get; set; }
    [JsonProperty("controls")] public Dictionary<string, ManualRef> Controls { get; set; } = new();
    [JsonProperty("machine_note")] public string MachineNote { get; set; } = "";
}

/// <summary>One event from /api/stream: [time, kind, name, value].</summary>
public sealed record SimEvent(double Time, string Kind, string Name, string Value)
{
    public static SimEvent? FromJson(string json)
    {
        var a = JArray.Parse(json);
        if (a.Count < 4) return null;
        return new SimEvent(a[0].Value<double>(), a[1].ToString(), a[2].ToString(), a[3].ToString());
    }
}
