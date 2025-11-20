import os 
import subprocess
import shlex
import platform

# i'm make the shell can detect the OS
OS_type = platform.system()

print(rf"""
  ___  ___  __    __      _____ _          _ _ 
 |__ \|__ \|  |  |  |    / ____| |        | | |
    ) |  ) |  |  |  |   | (___ | |__   ___| | |
   / /  / /|  |  |  |    \___ \| '_ \ / _ \ | |
  / /_ / /_|  |__|  |    ____) | | | |  __/ | |
 |____|____(_)____(_)   |_____/|_| |_|\___|_|_|
 
            Welcome to 211 Shell v1.2
            Detected OS: {OS_type}
           Type "exit" to leave the shell.
------------------------------------------------
""")

while True:
    current = os.getcwd()
    command = input(f"{current}>> ")
    if command == 'exit':
        print(r"""
   ____                   _ ____             
  / ___| ___   ___   ___| | __ )  _   _  ___ 
 | |  _ / _ \ / _ \ / __  |  _ \ | | | |/ _ \
 | |_| | (_) | (_) | (_|  | |_) || |_| |  __/
  \____|\___/ \___/ \___|_|____/  \__, |\___|
                                   |___/      
              
        Thank's for use "211 shell!"
              @Gha211th.2k25
-----------------------------------------------
        """)
        break

    if command.startswith('cd'):
        parts = shlex.split(command)
        if len(parts) == 1:
            home = os.path.expanduser("~")
            os.chdir(home)
            continue
        target = parts[1]
        try:
            os.chdir(target)
        except FileNotFoundError:
            print(">> File not found")
        except PermissionError:
            print(">> You don't have any permission to open this file")
        except NotADirectoryError:
            print(">> Directory not found")
        continue
    try:
        subprocess.run(command, shell=True)
    except Exception as e:
        print(f"Error {e}")