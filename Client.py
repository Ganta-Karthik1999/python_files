import socket

HOST='10.110.136.198'
PORT=8888

server=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.connect((HOST, PORT))

server.send("Hi".encode('utf-8'))
print(server.recv(1024))
 