#  getWindows.py
# Get List of open windows applications.
# https://pywinauto.readthedocs.io/en/latest/getting_started.html
import os
import getpass
import platform
import psutil
import subprocess
import win32gui

def winEnumHandler( hwnd, windows ):
    if win32gui.IsWindowVisible( hwnd ):
        window = win32gui.GetWindowText( hwnd )
        if len(window) > 0:
            windows.append(window)

def getProcesses():
    processes = {}
    for proc in psutil.process_iter():
        processName = proc.name()
        processID = proc.pid
        processes[processName] = processID
    return processes

def parseWindows(activeWindows):
    windowsRaw = []
    for window in activeWindows:
        windowsRaw += window.split()
    windows = []
    for w in windowsRaw:
        if len(w) > 3:
            windows.append(w)
    return windows

def isApplication(processes, windows):   
    for win in windows:
        for key in processes.keys():
            if win.lower() in key.lower():
                # print(key)
                pass

def stopApplication():
    userInput = input("Enter a process to kill: ")
    for proc in psutil.process_iter():
        if userInput in proc.name():
            print(f'Killing {proc.name()}.')
            proc.kill()

def initializeAppPaths():
    user = getpass.getuser()
    applications = {}
    applications["cmd"] = f"C:\\WINDOWS\\system32\\cmd.exe"   
    applications["cmder"] = f"C:\Applications\Cmder\Cmder.exe"
    applications["chrome"] = f"C:\\Users\\{user}\\AppData\\Local\\Google\\Chrome\\Application\\chrome.exe"
    applications["teams"] = f"C:\\Users\{user}\\AppData\\Local\\Microsoft\\Teams\\current\\Teams.exe"
    applications["word"] = f"C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE"
    applications["excel"] = f"C:\\Program Files\\Microsoft Office\\root\\Office16\\EXCEL.EXE"
    return applications

def startApplication(applications):
    print("Select an application to start:")
    while True:
        for app in applications.keys():
            print(app)
        userInput = input("Enter an app to start: ")
        subprocess.Popen(applications.get(userInput))


def main():
    windows = []
    win32gui.EnumWindows( winEnumHandler, windows )
    processes = getProcesses()
    windows = parseWindows(windows)
    isApplication(processes, windows)
    # stopApplication()
    applications = initializeAppPaths()
    startApplication(applications)

if __name__ == "__main__":
    main()

