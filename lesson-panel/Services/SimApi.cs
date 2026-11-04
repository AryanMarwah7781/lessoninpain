using System;
using System.IO;
using System.Net.Http;
using System.Text;
using System.Threading;
using System.Threading.Tasks;
using System.Windows.Media.Imaging;
using Newtonsoft.Json;

namespace LessonPanel.Services;

/// <summary>Client for the local simulator API (simapi, 127.0.0.1:47900). POSTs are JSON, as the API requires.</summary>
public sealed class SimApi : IDisposable
{
    readonly HttpClient _http;
    readonly HttpClient _stream;

    public SimApi(string baseUrl = "http://127.0.0.1:47900")
    {
        BaseUrl = baseUrl.TrimEnd('/');
        _http = new HttpClient { BaseAddress = new Uri(BaseUrl), Timeout = TimeSpan.FromSeconds(15) };
        _stream = new HttpClient { BaseAddress = new Uri(BaseUrl), Timeout = Timeout.InfiniteTimeSpan };
    }

    public string BaseUrl { get; }

    public async Task<T?> GetAsync<T>(string path, CancellationToken ct = default)
    {
        using var r = await _http.GetAsync(path, ct).ConfigureAwait(false);
        r.EnsureSuccessStatusCode();
        var s = await r.Content.ReadAsStringAsync(ct).ConfigureAwait(false);
        return JsonConvert.DeserializeObject<T>(s);
    }

    public async Task<string> PostAsync(string path, object? body = null, CancellationToken ct = default)
    {
        var json = JsonConvert.SerializeObject(body ?? new { });
        using var content = new StringContent(json, Encoding.UTF8, "application/json");
        using var r = await _http.PostAsync(path, content, ct).ConfigureAwait(false);
        var s = await r.Content.ReadAsStringAsync(ct).ConfigureAwait(false);
        if (!r.IsSuccessStatusCode) throw new HttpRequestException($"{(int)r.StatusCode}: {s}");
        return s;
    }

    public Task<Health?> HealthAsync(CancellationToken ct = default) => GetAsync<Health>("/api/health", ct);
    public Task<LessonResponse?> LessonAsync(CancellationToken ct = default) => GetAsync<LessonResponse>("/api/lesson", ct);
    public Task<FigureMap?> FigureMapAsync(CancellationToken ct = default) => GetAsync<FigureMap>("/api/manual/figure-map", ct);
    public Task<LessonInfo[]?> LessonsAsync(CancellationToken ct = default) => GetAsync<LessonInfo[]>("/api/lessons", ct);
    public Task<LessonPlan?> PlanAsync(CancellationToken ct = default) => GetAsync<LessonPlan>("/api/lesson/plan", ct);
    /// <summary>The app's windows by kind ("display", "pdu", "main"); the display carries its picture box.</summary>
    public Task<System.Collections.Generic.Dictionary<string, Newtonsoft.Json.Linq.JToken>?> ScreensAsync(CancellationToken ct = default)
        => GetAsync<System.Collections.Generic.Dictionary<string, Newtonsoft.Json.Linq.JToken>>("/api/screens", ct);

    public Task StartLessonAsync(string id) => PostAsync("/api/lesson/start", new { id });
    /// <summary>Setup holds buttons down (folding the boom takes a while), so it gets its own long timeout.</summary>
    public async Task SetupLessonAsync(string id)
    {
        using var cts = new CancellationTokenSource(TimeSpan.FromSeconds(90));
        using var content = new StringContent(JsonConvert.SerializeObject(new { id }), Encoding.UTF8, "application/json");
        using var r = await _stream.PostAsync("/api/lesson/setup", content, cts.Token).ConfigureAwait(false);
        if (!r.IsSuccessStatusCode) throw new HttpRequestException($"{(int)r.StatusCode}: {await r.Content.ReadAsStringAsync().ConfigureAwait(false)}");
    }
    public Task ShowMeAsync() => PostAsync("/api/lesson/showme");
    public Task SkipAsync() => PostAsync("/api/lesson/skip");
    public Task ConfirmAsync(string item) => PostAsync("/api/lesson/confirm", new { item });

    /// <summary>Downloads a PNG (a manual figure or a live capture) as a frozen bitmap usable from any thread.</summary>
    public async Task<BitmapImage?> ImageAsync(string path, CancellationToken ct = default)
    {
        using var r = await _http.GetAsync(path, ct).ConfigureAwait(false);
        if (!r.IsSuccessStatusCode) return null;
        var bytes = await r.Content.ReadAsByteArrayAsync(ct).ConfigureAwait(false);
        var bmp = new BitmapImage();
        using (var ms = new MemoryStream(bytes))
        {
            bmp.BeginInit();
            bmp.CacheOption = BitmapCacheOption.OnLoad;
            bmp.StreamSource = ms;
            bmp.EndInit();
        }
        bmp.Freeze();
        return bmp;
    }

    /// <summary>Reads /api/stream (Server-Sent Events) until cancelled, reconnecting after a drop.</summary>
    public async Task StreamAsync(Action<SimEvent> onEvent, Action<bool> onLink, CancellationToken ct)
    {
        while (!ct.IsCancellationRequested)
        {
            try
            {
                using var r = await _stream.GetAsync("/api/stream", HttpCompletionOption.ResponseHeadersRead, ct).ConfigureAwait(false);
                r.EnsureSuccessStatusCode();
                onLink(true);
                using var s = await r.Content.ReadAsStreamAsync(ct).ConfigureAwait(false);
                using var reader = new StreamReader(s, Encoding.UTF8);
                while (!ct.IsCancellationRequested)
                {
                    var line = await reader.ReadLineAsync(ct).ConfigureAwait(false);
                    if (line == null) break;
                    if (!line.StartsWith("data: ", StringComparison.Ordinal)) continue;
                    var ev = SimEvent.FromJson(line.Substring(6));
                    if (ev != null) onEvent(ev);
                }
            }
            catch (OperationCanceledException) { return; }
            catch (Exception) { }
            onLink(false);
            try { await Task.Delay(2000, ct).ConfigureAwait(false); } catch (OperationCanceledException) { return; }
        }
    }

    public void Dispose()
    {
        _http.Dispose();
        _stream.Dispose();
    }
}
