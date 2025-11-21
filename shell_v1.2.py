# i'm made the v1.3!

import os
import shlex
import subprocess
import platform
import getpass
import shutil

# for Os type
OS_name = platform.system()

# for name User
User_name_device = getpass.getuser()

# color *is from Ai
RESET = "\033[0m"
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
CYAN = "\033[36m"
MAGENTA = "\033[35m"

# for opening logo
banner = rf"""{CYAN}
  _______  ____   ____     _______  __   __  _______  ___      ___     
|       ||    | |    |   |       ||  | |  ||       ||   |    |   |    
|____   | |   |  |   |   |  _____||  |_|  ||    ___||   |    |   |    
 ____|  | |   |  |   |   | |_____ |       ||   |___ |   |    |   |    
| ______| |   |  |   |   |_____  ||       ||    ___||   |___ |   |___ 
| |_____  |   |  |   |    _____| ||   _   ||   |___ |       ||       |
|_______| |___|  |___|   |_______||__| |__||_______||_______||_______|
 
                    Welcome to 211 Shell v1.2
                    Detected OS   : {OS_name}
                    USER          : {User_name_device}
                Type {RED}"exit"{RESET} {BLUE}to leave the shell.{RESET}
{CYAN}______________________________________________________________________{RESET}
"""

# for closing
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

# print the logo for when the shell start
print(banner)

while True:
    current = os.getcwd()
    command = input(f"{GREEN}{User_name_device}&{OS_name}{RESET} {BLUE}{current}${RESET} ")

    # for exit the program
    if command == 'exit':
        print(closing)
        break
    elif command == '':
        continue
    elif command == 'funfetch':
        print(banner)
        continue
    elif len(command) == 2 and command[1] == ':':
        drive_path = command.upper() + '\\'
        try:
            os.chdir(drive_path)
        except Exception:
            print(f"{RED}>> {command} not found!{RESET}")

    if command.startswith('cd'):
        parts = shlex.split(command)
        if len(parts) == 1:
            home = os.path.expanduser('~')
            os.chdir(home)
            continue
        target = parts[1]

        try:
            os.chdir(target)
        except FileNotFoundError:
            print(f">> {RED}file {target} Is not found{RESET}")
        except NotADirectoryError:
            print(f">> {RED}Directory {target} Is not found{RESET}")
        except PermissionError:
            print(f">> {RED}{target} Can't be opened{RESET}")
        continue

    parts_rm = shlex.split(command)
    if parts_rm[0] == 'rm':
        if len(parts_rm) < 2:
            print(f">>{RED} Usage: rm <file_directory>{RESET}")
            continue
        
        target_rm = parts_rm[1]
        target_path = os.path.join(current, target_rm)

        if os.path.isfile(target_path):
            try:
                os.remove(target_path)
                print(f">> {BLUE}file {target_rm} has successfuly removed!{RESET}")
            except Exception as e:
                print(f'>> {RED}Error {e}{RESET}')
        elif os.path.isdir(target_path):
            try:
                shutil.rmtree(target_path)
                print(f">> {BLUE}Directory {target_rm} has successfuly removed!{RESET}")
            except Exception as e:
                print(f">> {RED}Error {e}{RESET}")
        else:
            print(f">> {RED}Can't Find: {RESET}{BLUE}{target_rm}{RESET}")

    try:
        subprocess.run(command, shell=True)
    except Exception as e:
        print(f"Error {e}")