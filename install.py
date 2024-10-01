import os
import shutil
import subprocess
import sys

def get_user_profile():
    return os.path.expandvars(r"%USERPROFILE%")

def copy_executable_to_path():
    if hasattr(sys, '_MEIPASS'):
        exe_source = os.path.join(sys._MEIPASS, 'dsk.exe')
    else:
        exe_source = 'dsk.exe'

    target_dir = r"C:\Windows\System32"

    try:
        shutil.copy(exe_source, target_dir)
        print(f"dsk.exe copied at {target_dir}.")
    except Exception as e:
        print(f"Error when copying dsk.exe : {e}")

def create_alt_desktop_folder():
    alt_desktop = os.path.join(get_user_profile(), "Desktop_alt")

    try:
        if not os.path.exists(alt_desktop):
            os.makedirs(alt_desktop)
        else:
            print(f"The folder desktop_alt already exists.")
    except Exception as e:
        print(f"Error when creating the desktop_alt folder : {e}")

def main():
    copy_executable_to_path()
    create_alt_desktop_folder()
    print("Install Finished.")

if __name__ == "__main__":
    main()
