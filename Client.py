import socket

HOST='localhost'
PORT=9999


while True:
    server=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.connect((HOST, PORT))

    server.send("Hi".encode('utf-8'))
    print(server.recv(1024))
 