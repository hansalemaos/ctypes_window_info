from collections import namedtuple
from ctypes import wintypes, byref
import ctypes
from ctypes import WinDLL

windll = ctypes.LibraryLoader(WinDLL)
user32 = windll.user32
kernel32 = windll.kernel32

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
    wintypes.HWND,
    wintypes.LPARAM,
)
WindowInfo = namedtuple(
    "WindowInfo",
    "pid title windowtext hwnd length tid status coords_client dim_client coords_win dim_win class_name path",
)


def get_window_infos(hwnd=None):
    r"""
    This function utilizes the Windows API to retrieve information about windows.

    Args:
        hwnd (int or None): The handle of the window for which to retrieve the text, defaults to None (all windows).

    Returns:
        namedtuple: A named tuples with - pid title windowtext hwnd length tid status coords_client dim_client coords_win dim_win class_name path

    Note:
        This function uses the `GetWindowTextW` function from the `user32` library to retrieve the window text.
        It is intended for use on Windows operating systems and relies on the ctypes library to interface with the Windows API.

    Examples:
        from ctypes_window_info import get_window_infos

        get_window_infos()

        [[WindowInfo(pid=88, title='Base_PowerMessageWindow', windowtext='', hwnd=197614, length=1, tid=9668, status='invisible', coords_client=(0, 0, 0, 0), dim_client=(0, 0), coords_win=(0, 0, 0, 0), dim_win=(0, 0), class_name='Base_PowerMessageWindow', path='C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe'),
         WindowInfo(pid=88, title='Chrome_StatusTrayWindow', windowtext='', hwnd=197592, length=1, tid=9668, status='invisible', coords_client=(0, 0, 0, 0), dim_client=(0, 0), coords_win=(0, 0, 0, 0), dim_win=(0, 0), class_name='Chrome_StatusTrayWindow', path='C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe'),
         WindowInfo(pid=88, title='Chrome_SystemMessageWindow', windowtext='', hwnd=197600, length=1, tid=9668, status='invisible', coords_client=(0, 130, 0, 10), dim_client=(130, 10), coords_win=(0, 136, 0, 39), dim_win=(136, 39), class_name='Chrome_SystemMessageWindow', path='C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe'),
         WindowInfo(pid=88, title='Chrome_WidgetWin_0', windowtext='', hwnd=197580, length=1, tid=9668, status='invisible', coords_client=(0, 0, 0, 0), dim_client=(0, 0), coords_win=(0, 0, 0, 0), dim_win=(0, 0), class_name='Chrome_WidgetWin_0', path='C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe'),
         WindowInfo(pid=88, title='Chrome_WidgetWin_0', windowtext='', hwnd=197606, length=1, tid=9668, status='invisible', coords_client=(0, 1424, 0, 728), dim_client=(1424, 728), coords_win=(182, 1622, 182, 949), dim_win=(1440, 767), class_name='Chrome_WidgetWin_0', path='C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe'),
         WindowInfo(pid=88, title='Chrome_WidgetWin_1', windowtext='', hwnd=2492886, length=1, tid=9668, status='invisible', coords_client=(0, 64, 0, 64), dim_client=(64, 64), coords_win=(-1, 63, 1028, 1092), dim_win=(64, 64), class_name='Chrome_WidgetWin_1', path='C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe'),
         ....

         get_window_infos(197614)
         [WindowInfo(pid=88, title='Base_PowerMessageWindow', windowtext='', hwnd=197614, length=1, tid=9668, status='invisible', coords_client=(0, 0, 0, 0), dim_client=(0, 0), coords_win=(0, 0, 0, 0), dim_win=(0, 0), class_name='Base_PowerMessageWindow', path='C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe')]

    """

    result = []

    @WNDENUMPROC
    def enum_proc(hWnd, lParam):
        if hwnd is not None:
            if hWnd != hwnd:
                return True
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
            kernel32.CloseHandle(coa)
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


