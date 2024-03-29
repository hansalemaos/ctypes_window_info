# Get window information with ctypes 


## pip install ctypes-window-info


```python

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

```
