import socket
import time
import pandas as pd


host='192.168.0.100'
port=8000
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((host,port))
s.listen(5)
print("Socket Created")

print('Waiting for the connection')

try:
    while True:
        c,address=s.accept()
        print("In the Loop:")
        #print(c.recv(1024).decode())
        demo=c.recv(4096).decode()
        print(demo)
        f=open("demo.txt","a")
        f.write(str(demo)+str(","))
        f.close()
        print("client connected :",address)
        print("=====================================")
        #c.send(bytes('Welcome to the server','utf-8'))
        #time.sleep(5)
        c.close()

except KeyboardInterrupt:
    pass
    # account=pd.read_csv("text.txt",delimiter=',')
    # account.to_csv('employ_data.csv',index=None)




    