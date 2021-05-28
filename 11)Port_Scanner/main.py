import socket

target = input("enter the target:")
start_port = input("enter the starting port number:")
end_port = input("enter the ending port number:")
try:
    for port in range(int(start_port), int(end_port)):
        s = socket.socket()
        socket.setdefaulttimeout(1)
        result = s.connect_ex((str(target), int(port)))
        if result == 0:
            print(f"{port} is open")
        s.close()
except KeyboardInterrupt:
    print("Exiting..")
    exit()
except socket.gaierror:
    print("Hostname Could Not Be Resolved !!!!")
    exit()
except socket.error:
    print("Server not responding !!!!")
    exit()
