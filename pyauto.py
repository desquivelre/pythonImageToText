import subprocess

import pyautogui
import time


def execute_code_remotely(remote_pc, username, password, code_to_execute):
    # Connect to remote PC using RDP (using your preferred method)

    # Start the RDP session using the mstsc command
    subprocess.Popen(["mstsc", "/v:" + remote_pc], shell=True)

    # Wait for the remote desktop window to open
    time.sleep(5)  # Adjust the delay as needed

    # Use pyautogui to automate actions
    pyautogui.press("tab")
    pyautogui.typewrite(".\sesadmin")
    pyautogui.press("tab")
    pyautogui.typewrite("Dikk2137++")
    pyautogui.press("enter")



    # Simulate interactions to open a terminal/command prompt
    pyautogui.hotkey("win", "r")
    time.sleep(1)
    pyautogui.write("cmd")
    pyautogui.press("enter")
    time.sleep(2)

    # Type and execute the code on the remote machine
    pyautogui.write("d:")
    pyautogui.press("enter")

    pyautogui.write(r"cd D:\Diego\PERSONAL\Proyectos\pythonTomarFotoGNX\venv\Scripts")
    pyautogui.press("enter")

    pyautogui.write("activate.bat")
    pyautogui.press("enter")

    pyautogui.write(code_to_execute)
    pyautogui.press("enter")

    # Disconnect from the RDP session
    # ...

if __name__ == "__main__":
    remote_pc = "10.20.21.64"
    username = ".\sesadmin"
    password = "Dikk2137++"

    code_to_execute = "python -c \"print('Hello from remote machine')\""

    execute_code_remotely(remote_pc, username, password, code_to_execute)
