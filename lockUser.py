# lockUser.py
# Gets the current logged in user and locks their computer.
# Sam Eakin
import getpass
import ctypes
import psutil
import time

def getUser():
    print(getpass.getuser())
    # TODO: have to figure out how to unlock. User authentication is needed for this.
    # pw = getpass.getpass() # https://docs.python.org/3/library/getpass.html#getpass.getuser
    # print(pw) 

def isLocked():
    for proc in psutil.process_iter():
        if proc.name() == "LogonUI.exe":
            print("Computer is already locked.")
            return True
        else:
            return False

def lock():
    if isLocked():
        exit
    else:
        print("Locking workstation...")
        time.sleep(1)
        ctypes.windll.user32.LockWorkStation()

def main():
    getUser()
    lock()

if __name__ == "__main__":
    main()