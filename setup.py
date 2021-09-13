# A minimilastic setup file for python projects 
try:
    import pyfiglet
    import subprocess
    from subprocess import Popen
    import os
    import re
    import sys
    from colorama import * 
    import platform
    from tkinter import*
    from tkinter.ttk import*


except ImportError:
    os.system("pip3 install pyfiglet", shell=True)
    os.system("pip3 install coloroma", shell=True)

# Replace all [INSERT... with your own
os.system("cls")

ascii_banner = pyfiglet.figlet_format("[INSERT APP NAME]")
print(ascii_banner)
init()
print(Fore.GREEN + " [+] [INSERT COMPANY NAME (OPTIONAL)]")
print(' ')
print(Fore.GREEN + " [+] Setting up [INSERT APP NAME]")
print(Fore.RED + "-----------------------------------------------------")
print(Fore.WHITE + "App Version : [INSERT APP VERSION]")
print(Fore.WHITE + "Detected OS: " + platform.system())
print(Fore.WHITE + "OS Release: " + platform.release())
print(Fore.RED + "-----------------------------------------------------")
print(Fore.GREEN + "Developer : [INSERT DEVELOPER NAME]")

input('\n [=] Press Enter to download modules')
print("Please wait")
# Make a list of modules in module = [] that need to be installed via pip
module = []
for i in module :
    os.system('pip install ' + i)
root=Tk()
root.title("Setup")
def starty():
    # Insert File name which need to be run at the end of setup
    Popen('[INSERT FILE]', shell=True)


label1=Label(root,text="Setup Completed .  You can start your app now\nby clicking on the button below").pack()
buttonstart=Button(root, text="Start App",command=starty).pack()
root.mainloop()

#print(Style.RESET_ALL)
