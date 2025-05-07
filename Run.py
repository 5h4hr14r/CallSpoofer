# Encoded by Shahriar Shawon
# Life is Locked
# Simple as Fu#ck

# ---------------- Imports
import os
import shutil
import zipfile
from time import sleep
from getpass import getpass
from colorama import Fore

# Install necessary packages if missing
try:
    import colorama
except ImportError:
    _ = os.system('pip install colorama' if os.name == 'nt' else 'pip3 install colorama')

# ---------------- Colors
r = "\033[1;31m"
g = "\033[1;32m"
y = "\033[1;33m"
b = "\033[1;34m"
d = "\033[2;37m"
R = "\033[1;41m"
Y = "\033[1;43m"
B = "\033[1;44m"
w = "\033[1;37m"
g = "\033[0;90m"
red = r  # Rename to avoid confusion

# ------------------ Banners
logo = Fore.RED + """
  
                                              SHAHRIAR SHAWON
  
            """ + Fore.YELLOW + """>>> """ + Fore.GREEN + """5h4hr14r""" + Fore.YELLOW + """ <<<

"""

def banner():
    print(logo)

def cls_clear_func():
    os.system('cls' if os.name=='nt' else 'clear')

def existing_directory_file(file):
    if os.path.exists(file):
        os.remove(file)

def designprint(shawon):
    print(red + "└─> " + w + shawon)

def front_design():
    cls_clear_func()
    banner()

front_design()

class Setup:
    def __init__(self, user):
        self.data = user

    def mainFile(self):
        self.save = self.data
        try:
            # Use standard zipfile module without encryption
            with zipfile.ZipFile('Zork/callspoofv3.zip', 'r') as extracted_zip:
                extracted_zip.extractall()  # No password needed
            designprint('Password Correct !')  # If the file is extracted successfully
            sleep(2.3)
            front_design()
            designprint('Successfully Unzipped file.')
            sleep(3.0)
            existing_directory_file('callspoofv3.zip')
            cls_clear_func()
            banner()
            os.system('python main.py' if os.name=='nt' else 'python3 main.py')
        except Exception as shawon:
            designprint('Error: ' + str(shawon))
            sleep(0.5)
            os.system('python Run.py' if os.name=='nt' else 'python3 Run.py')

try:
    user_ezip_unzipping = getpass(red + "└─" + w + "Enter the password of Zipfile : " + red).strip()
except:
    pass

if __name__ == '__main__':
    existing_directory_file('main.py')
    main_start = Setup(user_ezip_unzipping)
    main_start.mainFile()
