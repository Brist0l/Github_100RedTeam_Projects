import socket

UDP_HOST = '192.168.51.1'
UDP_PORT = 8080
to = (UDP_HOST, UDP_PORT)

s = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
s.bind(to)

while True:
    data, addrs = s.recvfrom(1024)
    print(f"recived:{data.decode()}")
