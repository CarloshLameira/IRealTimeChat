import socket
import threading

HOST = '127.0.0.1'
PORT = 8001

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

chats = {}

def broadcast(room, mensage):
    for i in chats[room]:
        if isinstance(mensage, str):
            mensage = mensage.encode()

        i.send(mensage)

def enviarMensagem(name, room, client):
    while True:
        mensage = client.recv(1024)
        mensage = f"{name}: {mensage.decode()}\n"
        broadcast(room, mensage)

while True:
    client, addr = server.accept()
    client.send(b'SALA')
    room = client.recv(1024).decode()
    name = client.recv(1024).decode()
    if room not in chats.keys():
        chats[room] = []
    chats[room].append(client)
    print(f'{name} se conectou na sala {room}! INFO {addr}')
    broadcast(room, f'{name}: Entrou na sala!\n')
    thread = threading.Thread(target=enviarMensagem, args=(name, room, client))
    thread.start()