from collections import namedtuple
from ctypes import wintypes
import ctypes
from ctypes import windll

user32 = ctypes.WinDLL("user32")
GetWindowRect = windll.user32.GetWindowRect
GetClientRect = windll.user32.GetClientRect


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
    "pid title hwnd length tid status coords_client dim_client coords_win dim_win",
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

        result.append(
            (
                WindowInfo(
                    pid.value,
                    title.value,
                    hWnd,
                    length,
                    tid,
                    status,
                    coords_client,
                    dim_client,
                    coords_win,
                    dim_win,
                )
            )
        )
        return True

    user32.EnumWindows(enum_proc, 0)
    return sorted(result)
