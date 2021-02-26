import socket
import os
import tqdm

SEPARATOR = "<SEPARATOR>"
BUFFER_SIZE = 4096

HOST = socket.gethostbyname(socket.gethostname())
PORT = 8080

s = socket.socket()
s.bind((HOST, PORT))
s.listen(5)

client, addr = s.accept()

recv=client.recv(BUFFER_SIZE).decode()
filename,filesize=recv.split(SEPARATOR)
filename=os.path.basename(filename)
filesize=int(filesize)
progress = tqdm.tqdm(range(filesize), f"Receiving {filename}", unit="B", unit_scale=True, unit_divisor=1024)

with open(filename,'wb') as f:
    while True:
        bytes=client.recv(BUFFER_SIZE)
        if not bytes:
            break
        f.write(bytes)
        progress.update(len(bytes))
client.close()
s.close()