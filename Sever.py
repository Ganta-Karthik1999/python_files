import socket

HOST='10.110.136.198'
PORT=9999

server=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind((HOST,PORT))

server.listen(5)


while True:
    comm_socket,address=server.accept()
    print("Connected to the Address {address}")
    message= comm_socket.recv(1024).decode('utf-8')
    print(f"Message form the Client is : {message} ")
    comm_socket.send(("Got your message").encode('utf-8'))
    comm_socket.close()
    print("Connection has been treminated !!!!")