import platform
import os


def system_command():
    print("===== System Information =====")
    print(f"Operating System : {platform.system()}")
    print(f"OS Version       : {platform.release()}")
    print(f"Python Version   : {platform.python_version()}")
    print(f"Current Directory: {os.getcwd()}")