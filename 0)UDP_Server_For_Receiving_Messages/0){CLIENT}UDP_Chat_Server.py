import socket

UDP_HOST = ''#run the code which is present at the end of the script
UDP_PORT = 8080
to = (UDP_HOST, UDP_PORT)
while True:
    message = bytes(input('>'), 'utf-8')

    s = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
    s.sendto(message, to)
    
#print(socket.gethostbyname(socket.gethostname()))
