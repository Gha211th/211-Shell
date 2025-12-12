import os
import subprocess
import shlex

print(r"""
  ___  ___  __    __      _____ _          _ _ 
 |__ \|__ \|  |  |  |    / ____| |        | | |
    ) |  ) |  |  |  |   | (___ | |__   ___| | |
   / /  / /|  |  |  |    \___ \| '_ \ / _ \ | |
  / /_ / /_|  |__|  |    ____) | | | |  __/ | |
 |____|____(_)____(_)   |_____/|_| |_|\___|_|_|
 
            Welcome to 211 Shell v1.1
           Type "exit" to leave the shell.
------------------------------------------------
""")

while True:
    current = os.getcwd()
    command = input(f"{current}>> ").strip()

    if command == "exit":
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

    if command.startswith("cd"):
        parts = shlex.split(command)
        if len(parts) == 1:
            print(">> cd: mising operand")
            continue
        try:
            os.chdir(parts[1])
        except FileNotFoundError:
            print(">> File not found")
        except NotADirectoryError:
            print(">> Directory not found")
        except PermissionError:
            print(">> Need permission To open file")
        continue
    try:
        subprocess.run(command, shell=True)
    except Exception as e:
        print(f"Error {e}")