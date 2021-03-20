import socket

import colorama

s = socket.socket()
colorama.init()
HOST = '127.0.0.1'
PORT = 8080
s.bind((HOST, PORT))
s.listen()
print(f"{colorama.Fore.BLACK}Listening....")
client, addr = s.accept()


def main():


    while True:
        client_input = client.recv(1024).decode()
        print(client_input)
        command = input(">")
        client.send(command.encode())
        data = client.recv(1024).decode()
        # if command == 'screen-mirror':
        #     s.close()
        #     from ScreenShare import Reciever
        #     Reciever.start(HOST,PORT)
        #     del Reciever.start(HOST,PORT)
        if command == 'exit':
            s.close()
            break
        print(data)
main()