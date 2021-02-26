import socket
import threading

HOST = socket.gethostbyname(socket.gethostname())
PORT = 8080

server = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()
print("Listening....")

clients = []
nicknames = []


def broadcast(message):
    for client in clients:
        client.send(message)


def handle(client):
    while True:
        try:
            message = client.recv(1024)
            broadcast(message)
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nickname = nicknames[index]
            broadcast(f"{nickname} left the chat".encode('ascii'))
            nicknames.remove(nickname)
            break


def receive():
    while True:
        client, address = server.accept()
        print(f"connected with{address}")
        client.send("NICK".encode('ascii'))
        nickname = client.recv(1024).decode('ascii')
        nicknames.append(nickname)
        clients.append(client)
        print(f"nickname:{nickname},client:{client}")
        broadcast(f"{nickname} joined the chat".encode('ascii'))
        client.send(f"connected to the server".encode('ascii'))
        thread = threading.Thread(target=handle, args=(client,))
        thread.start()


receive()
