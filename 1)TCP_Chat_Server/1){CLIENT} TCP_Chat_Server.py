import socket
import threading

HOST = ''#run the command at the end
PORT = 8080
connect = (HOST, PORT)

nickname=input("enter ur nickname:")

client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(connect)

def receinve():
    while True:
        try:
            message=client.recv(1024).decode('ascii')
            if message=='NICK':
                client.send(nickname.encode('ascii'))

            else:
                print(message)
        except :
            print("An error occured")
            client.close()
            break

def write():
    while True:
        text=input("enter ur msg:")
        message=f'{nickname}:{text}'
        client.send(message.encode('ascii'))

recv_thread=threading.Thread(target=receinve)
recv_thread.start()
write_thread=threading.Thread(target=write)
write_thread.start()

#print(socket.gethostbyname(socket.gethostname))
