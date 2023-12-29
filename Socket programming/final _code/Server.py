import socket
import time
import numpy as np
import pandas as pd
from openpyxl import workbook


def Creating_Socket():
    print("Socket Created")
    host='192.168.0.101'
    port=8855
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.bind((host,port))
    s.listen(5)
    return s


def receive_data(s):
    c,address=s.accept()
    print("Data has been recerived for the--->",str(address))
    demo=c.recv(4096).decode()
    print(demo)
    return demo

def update_file(demo):
    f=open("demo.txt","a")
    f.write(str(demo)+str(","))
    f.close()

def main(s):
    demo=receive_data(s)
    update_file(demo)
    return int(demo)


def file_genetraion(demo):
    df=pd.read_csv('All_employ.csv')
    print(df.columns)
    k=df[df['ID Number']==demo]
    lst=k.to_numpy()
    print(lst)
    df1 = pd.DataFrame(list(lst),columns=df.columns)
    print("=================")
    print(df1)
    print("================")
    lst2=list(lst[0])        
    print(lst2)
    with pd.ExcelWriter('entry.xlsx',mode='a',engine='openpyxl',if_sheet_exists='new') as writer:
            df1.to_excel(writer, sheet_name='employ_data')
            

    # with open('final_data.csv','w')as cs:
    #     kg=csv_writer(cs)
    #     kg.writerow(lst2)

    # for i in range(len(lst2)):
    #     f1=open("final_data.txt","a")
    #     f1.write(str(lst2[i])+str(","))
    #     f1.close
    


s=Creating_Socket()
while True:
    demo=main(s)
    file_genetraion(demo)
