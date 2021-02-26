import os
import socket
import tqdm

SEPARATOR = "<SEPARATOR>"
BUFFER_SIZE = 4096

HOST = socket.gethostbyname(socket.gethostname())
PORT = 8080
filename = input("enter ur file location:").strip('"')
fileSize = os.path.getsize(filename=filename)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
s.send(f"{filename}{SEPARATOR}{fileSize}".encode())

progress = tqdm.tqdm(range(fileSize), f"Sending{filename}", unit="B", unit_scale=True, unit_divisor=1024)
with open(filename, 'rb') as f:
    while True:
        byte = f.read(BUFFER_SIZE)
        if not byte:
            break
        s.sendall(byte)
        progress.update(len(byte))
s.close()
