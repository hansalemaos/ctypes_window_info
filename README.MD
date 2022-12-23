# Get window information with ctypes 

```python
pip install ctypes-window-info
```

```python

from ctypes_window_info import get_window_infos
get_window_infos()


[[WindowInfo(pid=88, title='Base_PowerMessageWindow', windowtext='', hwnd=197614, length=1, tid=9668, status='invisible', coords_client=(0, 0, 0, 0), dim_client=(0, 0), coords_win=(0, 0, 0, 0), dim_win=(0, 0), class_name='Base_PowerMessageWindow', path='C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe'),
 WindowInfo(pid=88, title='Chrome_StatusTrayWindow', windowtext='', hwnd=197592, length=1, tid=9668, status='invisible', coords_client=(0, 0, 0, 0), dim_client=(0, 0), coords_win=(0, 0, 0, 0), dim_win=(0, 0), class_name='Chrome_StatusTrayWindow', path='C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe'),
 WindowInfo(pid=88, title='Chrome_SystemMessageWindow', windowtext='', hwnd=197600, length=1, tid=9668, status='invisible', coords_client=(0, 130, 0, 10), dim_client=(130, 10), coords_win=(0, 136, 0, 39), dim_win=(136, 39), class_name='Chrome_SystemMessageWindow', path='C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe'),
 WindowInfo(pid=88, title='Chrome_WidgetWin_0', windowtext='', hwnd=197580, length=1, tid=9668, status='invisible', coords_client=(0, 0, 0, 0), dim_client=(0, 0), coords_win=(0, 0, 0, 0), dim_win=(0, 0), class_name='Chrome_WidgetWin_0', path='C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe'),
 WindowInfo(pid=88, title='Chrome_WidgetWin_0', windowtext='', hwnd=197606, length=1, tid=9668, status='invisible', coords_client=(0, 1424, 0, 728), dim_client=(1424, 728), coords_win=(182, 1622, 182, 949), dim_win=(1440, 767), class_name='Chrome_WidgetWin_0', path='C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe'),
 WindowInfo(pid=88, title='Chrome_WidgetWin_1', windowtext='', hwnd=2492886, length=1, tid=9668, status='invisible', coords_client=(0, 64, 0, 64), dim_client=(64, 64), coords_win=(-1, 63, 1028, 1092), dim_win=(64, 64), class_name='Chrome_WidgetWin_1', path='C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe'),
 ....
```
