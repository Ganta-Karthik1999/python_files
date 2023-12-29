import socket
import time


while True:
    c=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    c.connect(('192.168.0.100',8000))
    id=input("please enter your PSID: ")
    c.send(bytes(id,'utf-8'))
    time.sleep(1)


#print(c.recv(1024).decode())
