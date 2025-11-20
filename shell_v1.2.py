# THIS IS MY FIRST SHELL THAT I EVER MADE
# kinda fun for me, cause when i run this 211 shell v1.2
# There's the color!

import os 
import subprocess
import shlex
import platform
import getpass

# i'm make the shell can detect the OS
OS_type = platform.system()
if OS_type == "darwin":
    OS_type = "macos"

# for detecting the username from laptop
USER = getpass.getuser()


# color code
RESET = "\033[0m"
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
CYAN = "\033[36m"
MAGENTA = "\033[35m"


# ascii opening logo
banner = rf"""{CYAN}
  _______  ____   ____     _______  __   __  _______  ___      ___     
|       ||    | |    |   |       ||  | |  ||       ||   |    |   |    
|____   | |   |  |   |   |  _____||  |_|  ||    ___||   |    |   |    
 ____|  | |   |  |   |   | |_____ |       ||   |___ |   |    |   |    
| ______| |   |  |   |   |_____  ||       ||    ___||   |___ |   |___ 
| |_____  |   |  |   |    _____| ||   _   ||   |___ |       ||       |
|_______| |___|  |___|   |_______||__| |__||_______||_______||_______|
 
                    Welcome to 211 Shell v1.2
                    Detected OS   : {OS_type}
                    USER          : {USER}
                Type {RED}"exit"{RESET} {BLUE}to leave the shell.{RESET}
{CYAN}______________________________________________________________________{RESET}
"""


closing = rf"""{YELLOW}
 _______  _______  _______  ______     _______  __   __  _______  __  
|       ||       ||       ||      |   |  _    ||  | |  ||       ||  | 
|    ___||   _   ||   _   ||  _    |  | |_|   ||  |_|  ||    ___||  | 
|   | __ |  | |  ||  | |  || | |   |  |       ||       ||   |___ |  | 
|   ||  ||  |_|  ||  |_|  || |_|   |  |  _   | |_     _||    ___||__| 
|   |_| ||       ||       ||       |  | |_|   |  |   |  |   |___  __  
|_______||_______||_______||______|   |_______|  |___|  |_______||__| 
{RESET}
                    {MAGENTA}Thank's for use "211 shell!"{RESET}
                        {BLUE}@Gha211th.2k25{RESET}
{YELLOW}====================================================================={RESET}

"""

print(banner)

def main():
    while True:
        current = os.getcwd()
        command = input(f"{GREEN}{USER}@{OS_type} {BLUE}{current}$> {RESET}")

        # when you type "typefetch"
        if command == "":
            continue

        # when you type "exit"it will be break the program / stop
        if command == 'exit':
            print(closing)
            break

        # kinda neofetch
        elif command == 'typefetch':
            print(banner)
            continue

        # for change the drive like C/D/E etc
        elif len(command) == 2 and command[1] == ":":
                drive_path = command.upper() + "\\"
                try:
                    os.chdir(drive_path)
                except Exception:
                    print(f"{RED}>> Drive not found{RESET}")
                continue
        
        # if the command start with "cd" it will be change the directory
        if command.startswith('cd'):
            parts = shlex.split(command)
            if len(parts) == 1:
                home = os.path.expanduser("~")
                os.chdir(home)
                continue
            target = parts[1]

            # if the target is false
            try:
                os.chdir(target)
            except FileNotFoundError:
                print(f"{RED}>> File not found{RESET}")
            except PermissionError:
                print(f"{RED}>> You don't have any permission to open this file{RESET}")
            except NotADirectoryError:
                print(f"{RED}>> Directory not found{RESET}")
            continue

        # for running the program
        try:
            subprocess.run(command, shell=True)
        except Exception as e:
            print(f"Error {e}")

# RUN PROGRAM
main()