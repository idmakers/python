import win32api, win32con , win32gui ,time


def click(x,y):
  win32api.SetCursorPos((x,y))
  win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
  win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)

flags, hcursor, (x,y) = win32gui.GetCursorInfo()
print(x,y)
click(1513,734)
time.sleep(2)
click(1705,705)
time.sleep(2)
click(1705,705)
time.sleep(2)
click(1705,705)
time.sleep(2)
