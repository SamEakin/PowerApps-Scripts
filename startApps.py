#  startApps.py
# Get List of open windows applications.
# https://pywinauto.readthedocs.io/en/latest/getting_started.html
import os
import getpass
import platform
import psutil
import subprocess
import win32gui

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
    applications = initializeAppPaths()
    startApplication(applications)

if __name__ == "__main__":
    main()

