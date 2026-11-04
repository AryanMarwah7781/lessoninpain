"""Live captures of the Connections app's windows (Windows only, standard library + ctypes).

Finds the app's visible top-level windows, tells them apart by what's on them (the display's dark backdrop
around its 4:3 picture, the corner post window's white edges and green Operations header), and captures one
as PNG with PrintWindow(PW_RENDERFULLCONTENT), which works
for the WebView2 content even when other windows cover it. A frozen window is never captured: PrintWindow
on a hung window blocks forever.
"""
import ctypes
import ctypes.wintypes as wt
import struct
import zlib

user32 = ctypes.WinDLL("user32", use_last_error=True)
gdi32 = ctypes.WinDLL("gdi32", use_last_error=True)
TITLE = "Display and CommandARM"
PW_RENDERFULLCONTENT = 2

EnumWindowsProc = ctypes.WINFUNCTYPE(wt.BOOL, wt.HWND, wt.LPARAM)
user32.EnumWindows.argtypes = [EnumWindowsProc, wt.LPARAM]
user32.GetWindowTextW.argtypes = [wt.HWND, wt.LPWSTR, ctypes.c_int]
user32.GetWindowRect.argtypes = [wt.HWND, ctypes.POINTER(wt.RECT)]
user32.IsWindowVisible.argtypes = [wt.HWND]
user32.IsIconic.argtypes = [wt.HWND]
user32.IsHungAppWindow.argtypes = [wt.HWND]
user32.GetDC.argtypes = [wt.HWND]
user32.GetDC.restype = wt.HDC
user32.ReleaseDC.argtypes = [wt.HWND, wt.HDC]
user32.PrintWindow.argtypes = [wt.HWND, wt.HDC, wt.UINT]
gdi32.CreateCompatibleDC.argtypes = [wt.HDC]
gdi32.CreateCompatibleDC.restype = wt.HDC
gdi32.CreateDIBSection.restype = wt.HBITMAP
gdi32.CreateDIBSection.argtypes = [wt.HDC, ctypes.c_void_p, wt.UINT, ctypes.POINTER(ctypes.c_void_p), wt.HANDLE, wt.DWORD]
gdi32.SelectObject.argtypes = [wt.HDC, wt.HGDIOBJ]
gdi32.SelectObject.restype = wt.HGDIOBJ
gdi32.DeleteObject.argtypes = [wt.HGDIOBJ]
gdi32.DeleteDC.argtypes = [wt.HDC]


class BITMAPINFOHEADER(ctypes.Structure):
    _fields_ = [("biSize", wt.DWORD), ("biWidth", wt.LONG), ("biHeight", wt.LONG), ("biPlanes", wt.WORD),
                ("biBitCount", wt.WORD), ("biCompression", wt.DWORD), ("biSizeImage", wt.DWORD),
                ("biXPelsPerMeter", wt.LONG), ("biYPelsPerMeter", wt.LONG), ("biClrUsed", wt.DWORD),
                ("biClrImportant", wt.DWORD)]


def app_windows():
    """Visible, non-minimised top-level windows of the Connections app: [(hwnd, title, (w, h), hung)]."""
    found = []

    def cb(hwnd, _):
        if not user32.IsWindowVisible(hwnd) or user32.IsIconic(hwnd):
            return True
        buf = ctypes.create_unicode_buffer(256)
        user32.GetWindowTextW(hwnd, buf, 256)
        if TITLE in buf.value:
            r = wt.RECT()
            user32.GetWindowRect(hwnd, ctypes.byref(r))
            found.append((hwnd, buf.value, (r.right - r.left, r.bottom - r.top), bool(user32.IsHungAppWindow(hwnd))))
        return True

    user32.EnumWindows(EnumWindowsProc(cb), 0)
    return found


def capture(hwnd, size):
    """-> (width, height, bytes of BGRA rows top-down)"""
    w, h = size
    hdc_screen = user32.GetDC(None)
    hdc = gdi32.CreateCompatibleDC(hdc_screen)
    bmi = BITMAPINFOHEADER(ctypes.sizeof(BITMAPINFOHEADER), w, -h, 1, 32, 0, 0, 0, 0, 0, 0)
    bits = ctypes.c_void_p()
    hbmp = gdi32.CreateDIBSection(hdc, ctypes.byref(bmi), 0, ctypes.byref(bits), None, 0)
    old = gdi32.SelectObject(hdc, hbmp)
    try:
        user32.PrintWindow(hwnd, hdc, PW_RENDERFULLCONTENT)
        data = ctypes.string_at(bits, w * h * 4)
    finally:
        gdi32.SelectObject(hdc, old)
        gdi32.DeleteObject(hbmp)
        gdi32.DeleteDC(hdc)
        user32.ReleaseDC(None, hdc_screen)
    return w, h, data


def px(img, x, y):
    w, h, data = img
    x, y = max(0, min(w - 1, int(x))), max(0, min(h - 1, int(y)))
    b, g, r, _ = data[(y * w + x) * 4:(y * w + x) * 4 + 4]
    return r, g, b


def pixel(img, fx, fy):
    return px(img, fx * img[0], fy * img[1])


def _light(p): return min(p) > 200
def _bezel(p): return all(abs(c - 40) < 8 for c in p)   # the display window's backdrop around the Gen 4 picture


def title_height(img):
    """Height of the app's light title bar (50 px at 100 % scaling)."""
    w, h, _ = img
    y = 0
    while y < min(h - 1, 160) and _light(px(img, w * 0.6, y)):
        y += 1
    return y


def picture_box(img):
    """(x0, y0, x1, y1) in pixels of the Gen 4 picture inside the display window. The display keeps its 4:3
    picture and fills the rest with the backdrop: bands left/right on a wide window, top/bottom on a tall one."""
    w, h, _ = img
    t = title_height(img)
    cx = w // 2
    y0 = t
    while y0 < h - 1 and _bezel(px(img, cx, y0)):
        y0 += 1
    y1 = h - 1
    while y1 > y0 and _bezel(px(img, cx, y1)):
        y1 -= 1
    row = min(y1, y0 + 4)                    # the top bar of every Gen 4 page spans the full width
    x0 = 0
    while x0 < w - 1 and _bezel(px(img, x0, row)):
        x0 += 1
    x1 = w - 1
    while x1 > x0 and _bezel(px(img, x1, row)):
        x1 -= 1
    pw, ph = x1 - x0 + 1, y1 - y0 + 1
    if ph > 0 and 1.28 < pw / ph < 1.39:
        return x0, y0, x1 + 1, y1 + 1
    cw, ch = w, h - t                         # fallback: a centred 4:3 box under the title bar
    pw, ph = (ch * 4 / 3, ch) if cw / ch > 4 / 3 else (cw, cw * 3 / 4)
    x0, y0 = (cw - pw) / 2, t + (ch - ph) / 2
    return int(x0), int(y0), int(x0 + pw), int(y0 + ph)


def classify(img):
    """'display' (Gen 4 display), 'pdu' (corner post + Operations + Navigation) or 'main'.

    Uses features that stay put on every page and window size: the Gen 4 display window shows its dark
    backdrop either at both sides (wide window) or above and below the picture (tall window), also under
    warnings and menus; the corner-post window is white at both edges with a green Operations header
    (sampled left of its title text). Checked on captures from 2 and 3 Nov."""
    def green(p): return p[1] > 100 and p[1] > p[0] + 40 and p[1] > p[2] + 40
    w, h, _ = img
    t = title_height(img)
    mid = (t + h) / 2
    sides = _bezel(px(img, w * 0.015, mid)) and _bezel(px(img, w * 0.985, mid))
    bands = all(_bezel(px(img, w * fx, y)) for fx in (0.25, 0.75) for y in (t + 3, h - 4))
    if sides or bands:
        return "display"
    left, right = pixel(img, 0.015, 0.50), pixel(img, 0.985, 0.50)
    if _light(left) and _light(right) and (green(pixel(img, 0.33, 0.077)) or green(pixel(img, 0.36, 0.077))):
        return "pdu"
    return "main"


def crop(img, box):
    w, h, data = img
    x0, y0, x1, y1 = box
    rows = [data[(y * w + x0) * 4:(y * w + x1) * 4] for y in range(y0, y1)]
    return x1 - x0, y1 - y0, b"".join(rows)


def to_png(img):
    w, h, data = img
    raw = bytearray()
    stride = w * 4
    for y in range(h):
        row = data[y * stride:(y + 1) * stride]
        raw.append(0)
        rgb = bytearray(w * 3)
        rgb[0::3] = row[2::4]
        rgb[1::3] = row[1::4]
        rgb[2::3] = row[0::4]
        raw += rgb

    def chunk(kind, body):
        c = struct.pack(">I", len(body)) + kind + body
        return c + struct.pack(">I", zlib.crc32(kind + body) & 0xFFFFFFFF)

    return (b"\x89PNG\r\n\x1a\n" + chunk(b"IHDR", struct.pack(">IIBBBBB", w, h, 8, 2, 0, 0, 0))
            + chunk(b"IDAT", zlib.compress(bytes(raw), 6)) + chunk(b"IEND", b""))


def screens():
    """-> {kind: {"hwnd", "size", "hung"[, "picture"]}} for each app window we can tell apart.
    For the display, "picture" is the Gen 4 picture's box in window pixels (what display.png contains)."""
    out = {}
    for hwnd, title, size, hung in app_windows():
        if hung:
            out.setdefault("frozen", []).append({"hwnd": hwnd, "size": size})
            continue
        img = capture(hwnd, size)
        kind = classify(img)
        if kind in out:
            continue
        out[kind] = {"hwnd": hwnd, "size": list(size), "hung": False}
        if kind == "display":
            out[kind]["picture"] = list(picture_box(img))
    return out


user32.EnumChildWindows.argtypes = [wt.HWND, EnumWindowsProc, wt.LPARAM]
user32.GetClassNameW.argtypes = [wt.HWND, wt.LPWSTR, ctypes.c_int]
user32.PostMessageW.argtypes = [wt.HWND, wt.UINT, wt.WPARAM, wt.LPARAM]
user32.ScreenToClient.argtypes = [wt.HWND, ctypes.POINTER(wt.POINT)]
WM_MOUSEMOVE, WM_LBUTTONDOWN, WM_LBUTTONUP, MK_LBUTTON = 0x0200, 0x0201, 0x0202, 0x0001


def find_window(kind):
    """-> (hwnd, size, img) of the app window of that kind, or None."""
    for hwnd, title, size, hung in app_windows():
        if hung:
            continue
        img = capture(hwnd, size)
        if classify(img) == kind:
            return hwnd, size, img
    return None


def _render_widget(hwnd):
    """The Chromium child window that draws the window's web content (the display's noVNC canvas)."""
    best = [None, 0]

    def cb(child, _):
        buf = ctypes.create_unicode_buffer(128)
        user32.GetClassNameW(child, buf, 128)
        if buf.value == "Chrome_RenderWidgetHostHWND" and user32.IsWindowVisible(child):
            r = wt.RECT()
            user32.GetWindowRect(child, ctypes.byref(r))
            area = (r.right - r.left) * (r.bottom - r.top)
            if area > best[1]:
                best[0], best[1] = child, area
        return True

    user32.EnumChildWindows(hwnd, EnumWindowsProc(cb), 0)
    return best[0]


def tap(kind, fx, fy, hold_ms=90):
    """Tap the app's display (or corner post) at (fx, fy): fractions of the Gen 4 picture for "display", of the
    window for "pdu" -- the same frame as the screen map and the captures. Posts the clicks to the window, so the
    mouse pointer does not move. Returns what it did."""
    import time
    found = find_window(kind)
    if not found:
        return {"ok": False, "error": f"no {kind} window open"}
    hwnd, (w, h), img = found
    if kind == "display":
        x0, y0, x1, y1 = picture_box(img)
        x, y = x0 + fx * (x1 - x0), y0 + fy * (y1 - y0)
    else:
        x, y = fx * w, fy * h
    win = wt.RECT()
    user32.GetWindowRect(hwnd, ctypes.byref(win))
    target = _render_widget(hwnd) or hwnd
    pt = wt.POINT(int(win.left + x), int(win.top + y))
    user32.ScreenToClient(target, ctypes.byref(pt))
    lp = (pt.y & 0xFFFF) << 16 | (pt.x & 0xFFFF)
    user32.PostMessageW(target, WM_MOUSEMOVE, 0, lp)
    time.sleep(0.03)
    user32.PostMessageW(target, WM_LBUTTONDOWN, MK_LBUTTON, lp)
    time.sleep(hold_ms / 1000)
    user32.PostMessageW(target, WM_LBUTTONUP, 0, lp)
    return {"ok": True, "window": kind, "at": [round(fx, 4), round(fy, 4)], "client": [pt.x, pt.y],
            "widget": target != hwnd}


def capture_png(kind):
    """PNG of that window. The display comes back cropped to the Gen 4 picture, so screen-map boxes
    line up whatever size the trainee made the window."""
    for hwnd, title, size, hung in app_windows():
        if hung:
            continue
        img = capture(hwnd, size)
        if classify(img) == kind:
            if kind == "display":
                img = crop(img, picture_box(img))
            return to_png(img)
    return None
