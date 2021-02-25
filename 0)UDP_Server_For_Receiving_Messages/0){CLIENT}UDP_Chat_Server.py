import socket

UDP_HOST = socket.gethostbyname(socket.gethostname())
UDP_PORT = 8080
to = (UDP_HOST, UDP_PORT)
while True:
    message = bytes(input('>'), 'utf-8')

    s = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
    s.sendto(message, to)
