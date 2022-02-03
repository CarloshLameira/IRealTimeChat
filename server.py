import socket
HOST = 'localhost'
PORT = 8001

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.bind((HOST, PORT))

sock.listen(5)

chats =  {''}

while True:
        novoSock, _ = sock.accept()
        sala = novoSock.recv(1024).decode()
        
        novoSock.send(b'ok')
    