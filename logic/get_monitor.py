from win32api import GetSystemMetrics


monitor = f"{GetSystemMetrics(0)}x{GetSystemMetrics(1)}"
if monitor == "1280x720":
    from monitor_formats.f1280x720 import *
if monitor == "1920x1080":
    from monitor_formats.f1920x1080 import *
if monitor == "2560x1440":
    from monitor_formats.f2560x1440 import *
