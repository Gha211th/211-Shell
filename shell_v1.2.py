import os 
import subprocess
import shlex
import platform
import getpass

# i'm make the shell can detect the OS
OS_type = platform.system()
if OS_type == "darwin":
    OS_type = "macos"

USER = getpass.getuser()


# color code
RESET = "\033[0m"
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
CYAN = "\033[36m"
MAGENTA = "\033[35m"

print(rf"""{MAGENTA}
  ___  ___  __    __      _____ _          _ _ 
 |__ \|__ \|  |  |  |    / ____| |        | | |
    ) |  ) |  |  |  |   | (___ | |__   ___| | |
   / /  / /|  |  |  |    \___ \| '_ \ / _ \ | |
  / /_ / /_|  |__|  |    ____) | | | |  __/ | |
 |____|____(_)____(_)   |_____/|_| |_|\___|_|_|
 
            Welcome to 211 Shell v1.2
            Detected OS   : {OS_type}
            USER          : {USER}
           Type {RED}"exit"{RESET} {BLUE}to leave the shell.{RESET}
------------------------------------------------
""")

def main():
    while True:
        current = os.getcwd()
        command = input(f"{GREEN}{USER}@{OS_type} {BLUE}{current}$> {RESET}")
        if command == 'exit':
            print(fr"""{YELLOW}
    ____                   _ ____             
    / ___| ___   ___   ___| | __ )  _   _  ___ 
    | |  _ / _ \ / _ \ / __  |  _ \ | | | |/ _ \
    | |_| | (_) | (_) | (_|  | |_) || |_| |  __/
    \____|\___/ \___/ \___|_|____/  \__, |\___|
                                    |___/      
                
            Thank's for use "211 shell!"
                {BLUE}@Gha211th.2k25{RESET}
    {YELLOW}-----------------------------------------------{RESET}
            {RESET}""")
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
                print(f"{RED}>> File not found{RESET}")
            except PermissionError:
                print(f"{RED}>> You don't have any permission to open this file{RESET}")
            except NotADirectoryError:
                print(f"{RED}>> Directory not found{RESET}")
            continue
        try:
            subprocess.run(command, shell=True)
        except Exception as e:
            print(f"Error {e}")

# RUN PROGRAM
main()