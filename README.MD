# Get window information with ctypes 

```python
pip install ctypes-window-info
```

```python

from ctypes_window_info import get_window_infos
get_window_infos()


[WindowInfo(pid=624, title='Default IME', hwnd=66212, length=12, tid=628, status='invisible', coords_client=(0, 0, 0, 0), dim_client=(0, 0), coords_win=(0, 0, 0, 0), dim_win=(0, 0)),
 WindowInfo(pid=624, title='EPPCCMON', hwnd=66210, length=9, tid=628, status='invisible', coords_client=(0, 1424, 0, 728), dim_client=(1424, 728), coords_win=(182, 1622, 182, 949), dim_win=(1440, 767)),
 WindowInfo(pid=1004, title='Default IME', hwnd=131798, length=12, tid=3912, status='invisible', coords_client=(0, 0, 0, 0), dim_client=(0, 0), coords_win=(0, 0, 0, 0), dim_win=(0, 0)),
 WindowInfo(pid=1032, title='Administrator:  ', hwnd=262166, length=17, tid=940, status='invisible', coords_client=(0, 705, 0, 45), dim_client=(705, 45), coords_win=(0, 738, 0, 84), dim_win=(738, 84)),
 WindowInfo(pid=1324, title='Default IME', hwnd=66174, length=12, tid=8332, status='invisible', coords_client=(0, 0, 0, 0), dim_client=(0, 0), coords_win=(0, 0, 0, 0), dim_win=(0, 0)),
 WindowInfo(pid=1324, title='Default IME', hwnd=66178, length=12, tid=10192, status='invisible', coords_client=(0, 0, 0, 0), dim_client=(0, 0), coords_win=(0, 0, 0, 0), dim_win=(0, 0)),
 WindowInfo(pid=1324, title='Default IME', hwnd=66186, length=12, tid=9656, status='invisible', coords_client=(0, 0, 0, 0), dim_client=(0, 0), coords_win=(0, 0, 0, 0), dim_win=(0, 0)),
 WindowInfo(pid=1324, title='VBoxPowerNotifyClass', hwnd=66184, length=21, tid=9656, status='invisible', coords_client=(0, 98, 0, 98), dim_client=(98, 98), coords_win=(-200, -100, -200, -100), dim_win=(100, 100)),
 WindowInfo(pid=1324, title='VBoxUsbLibClass', hwnd=66176, length=16, tid=10192, status='invisible', coords_client=(0, 98, 0, 98), dim_client=(98, 98), coords_win=(-200, -100, -200, -100), dim_win=(100, 100)),
 WindowInfo(pid=1324, title='VirtualBox Interface', hwnd=66172, length=21, tid=8332, status='invisible', coords_client=(0, 0, 0, 0), dim_client=(0, 0), coords_win=(-200, -199, -200, -199), dim_win=(1, 1)),
....
```
