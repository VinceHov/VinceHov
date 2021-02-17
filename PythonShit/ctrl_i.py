import win32com.client
import win32gui
import win32process
import  time
hwnd = win32gui.GetForegroundWindow()

_, pid = win32process.GetWindowThreadProcessId(hwnd)

shell = win32com.client.Dispatch("WScript.Shell")

shell.AppActivate('15644')
for i in range(787):
    shell.SendKeys('^i')
    time.sleep(0.01)
print('its over')
shell.AppActivate(pid)