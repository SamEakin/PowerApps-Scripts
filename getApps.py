import platform
import psutil
import subprocess
import os

def main():
    getOS()
    getProcesses()
    # startApplication()
    stopApplication()

def getOS(): 
    print(platform.system())

def getProcesses():
    for proc in psutil.process_iter():
        processName = proc.name()
        processID = proc.pid
        if isBackgroundProcess(processName):
            pass
        else:
            print(processName," ::: ", processID)
        # getPath(proc.pid)
        # print(os.path.abspath("notepad.exe"))


def isBackgroundProcess(processName):
    backgroundProcesses = ["svchost"]
    for bgProc in backgroundProcesses:
        if bgProc in processName:
            return True
    return False


def stopApplication():
    userInput = input("Enter a process to kill: ")
    for proc in psutil.process_iter():
        if userInput in proc.name():
            print(f'Killing {proc.name()}.')
            proc.kill()

def startApplication():
    print("Starting notepad...")
    # print(os.path.abspath("chrome.exe"))
    subprocess.run("notepad.exe")

if __name__ == "__main__":
    main()



# def getPath(pID):
#     p = psutil.Process(pID)
#     print(p.exe()) # NO PERMISSIONS