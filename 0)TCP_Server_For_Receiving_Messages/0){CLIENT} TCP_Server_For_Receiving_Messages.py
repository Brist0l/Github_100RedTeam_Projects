import socket

HOST = ''#run the comannd written at the end and enter the value here
PORT = 8080
connect = (HOST, PORT)

s = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
try:
    s.connect(connect)
    while True:
        msg = input(">")
        msg = bytes(msg, 'utf-8')
        s.sendall(msg)
except:
    print("Server Down :(")

# print(socket.gethostbyname(socket.gethostname()))
