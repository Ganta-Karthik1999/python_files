import socket
import sys

#Create a socket to conect two computer
def create_socket():
    try:
        global host
        global port
        global soc
        host="" 
        port=7000
        soc=socket.socket()
    except socket.error as msg:
        print("An error occured while creating the socket"+str(msg))

#Binding  the socket and listing for the connections
def bind_socket():
    try:
        global host
        global port
        global soc
        print("Binding the port :"+str(port))
        soc.bind(host,port)
        soc.listen(5)

    except socket.error as msg:
        print("Socket binding error :" str(msg)+"\n"+"Retying")
        bind_socket() 

#Establish connect with a client

def socket_accept():
   con,address= soc.accept()
   print("Connection has bee established: "+"With the IP"+address+"and the Port"+str(address[1]))
   send_command(con)
   con.close()

#This is used send commands to the client 
def send_command(con):
    while True:
        cmd=input()
        if cmd=="quit":
            con.close()
            soc.close()
            sys.exit()
        if len(str.encode(cmd))>0:
            con.send(str.encode(cmd))
            client_response=str(con.recv(1024),"utf-8")
            print(client_response,end="")

def main():
    create_socket()
    bind_socket()
    socket_accept

main()



