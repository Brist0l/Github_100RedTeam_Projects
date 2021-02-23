import socket

HOST = socket.gethostbyname(socket.gethostname())  # gets the ip-address of a machine
PORT = 8080  # port number
bind = (HOST, PORT)

s = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)  # ipv4 with TCP
s.bind(bind)
s.listen(1)
while True:
    connection, address = s.accept()
    print(f"Connected by {address}")
    while True:
        data = connection.recv(1024)
        if not data:
            break
        else:
            while True:
                print(f"U have send:{data.decode()}")
                break
    connection.close()