from collections import namedtuple
from ctypes import wintypes, byref
import ctypes
from ctypes import windll

user32 = ctypes.WinDLL("user32")
kernel32 = ctypes.WinDLL("kernel32", use_last_error=True)

GetWindowRect = windll.user32.GetWindowRect
GetClientRect = windll.user32.GetClientRect


def get_window_text(hWnd):
    length = windll.user32.GetWindowTextLengthW(hWnd)
    buf = ctypes.create_unicode_buffer(length + 1)
    windll.user32.GetWindowTextW(hWnd, buf, length + 1)
    return buf.value


class RECT(ctypes.Structure):
    _fields_ = [
        ("left", ctypes.c_long),
        ("top", ctypes.c_long),
        ("right", ctypes.c_long),
        ("bottom", ctypes.c_long),
    ]


WNDENUMPROC = ctypes.WINFUNCTYPE(
    wintypes.BOOL,
    wintypes.HWND,  # _In_ hWnd
    wintypes.LPARAM,
)
WindowInfo = namedtuple(
    "WindowInfo",
    "pid title windowtext hwnd length tid status coords_client dim_client coords_win dim_win class_name path",
)


def get_window_infos():
    """Return a sorted list of visible windows."""
    result = []

    @WNDENUMPROC
    def enum_proc(hWnd, lParam):
        status = "invisible"
        if user32.IsWindowVisible(hWnd):
            status = "visible"

        pid = wintypes.DWORD()
        tid = user32.GetWindowThreadProcessId(hWnd, ctypes.byref(pid))
        length = user32.GetWindowTextLengthW(hWnd) + 1
        title = ctypes.create_unicode_buffer(length)
        user32.GetWindowTextW(hWnd, title, length)

        rect = RECT()
        GetClientRect(hWnd, ctypes.byref(rect))
        left, right, top, bottom = rect.left, rect.right, rect.top, rect.bottom
        w, h = right - left, bottom - top
        coords_client = left, right, top, bottom
        dim_client = w, h
        rect = RECT()
        GetWindowRect(hWnd, ctypes.byref(rect))
        left, right, top, bottom = rect.left, rect.right, rect.top, rect.bottom
        w, h = right - left, bottom - top
        coords_win = left, right, top, bottom
        dim_win = w, h

        length_ = 257
        title = ctypes.create_unicode_buffer(length_)
        user32.GetClassNameW(hWnd, title, length_)
        classname = title.value
        try:
            windowtext = get_window_text(hWnd)
        except Exception:
            windowtext = ""

        try:
            coa = kernel32.OpenProcess(0x1000, 0, pid.value)
            path = (ctypes.c_wchar * 260)()
            size = ctypes.c_uint(260)
            kernel32.QueryFullProcessImageNameW(coa, 0, path, byref(size))
            filepath = path.value
            ctypes.windll.kernel32.CloseHandle(coa)
        except Exception as fe:
            filepath = ""

        result.append(
            (
                WindowInfo(
                    pid.value,
                    title.value,
                    windowtext,
                    hWnd,
                    length,
                    tid,
                    status,
                    coords_client,
                    dim_client,
                    coords_win,
                    dim_win,
                    classname,
                    filepath,
                )
            )
        )
        return True

    user32.EnumWindows(enum_proc, 0)
    return sorted(result)
