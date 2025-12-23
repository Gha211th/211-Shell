import os
import subprocess

print(fr"""
  ___  ___  __    __      _____ _          _ _ 
 |__ \|__ \|  |  |  |    / ____| |        | | |
    ) |  ) |  |  |  |   | (___ | |__   ___| | |
   / /  / /|  |  |  |    \___ \| '_ \ / _ \ | |
  / /_ / /_|  |__|  |    ____) | | | |  __/ | |
 |____|____(_)____(_)   |_____/|_| |_|\___|_|_|
 
                Welcome to 211 Shell
           Type "exit" to leave the shell.
------------------------------------------------
""")

while True:
    current = os.getcwd()
    command = input(f"{current}>> ").strip()

    if command == 'exit':
        print("==============================================")
        print("================== GOOD BYE ==================")
        print("==============================================\n")
        break

    if command.startswith("cd"):
        parts = command.split()
        if len(parts) == 1:
            print(">> What do you looking for?")

        try:
            target = command.split()[1]
            os.chdir(target)
        except FileNotFoundError:
            print(">> File not found btw~")
        except NotADirectoryError:
            print(">> Can't found directory btw~")
        except PermissionError:
            print(">> You don't have any permission btw~")
        continue
    try:
        subprocess.run(command, shell=True)
    except Exception as e:
        print(f"Error {e}")