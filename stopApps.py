# stopApps.py
# Start Applications on a user system. Currently the application options are hard-coded.
# Sam Eakin
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
                print(key)
                

def stopApplication():
    userInput = input("Enter a process to kill: ")
    for proc in psutil.process_iter():
        if userInput in proc.name():
            print(f'Killing {proc.name()}.')
            proc.kill()

def main():
    windows = []
    win32gui.EnumWindows( winEnumHandler, windows )
    processes = getProcesses()
    windows = parseWindows(windows)
    isApplication(processes, windows)
    stopApplication()

if __name__ == "__main__":
    main()

