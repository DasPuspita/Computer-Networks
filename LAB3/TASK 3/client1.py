# -*- coding: utf-8 -*-
"""
Created on Mon Nov 13 21:54:54 2023

@author: Lenovo
"""

import socket
 
HEADER= 64
FORMAT= 'utf-8'
SERVER= socket.gethostbyname(socket.gethostname())  
PORT= 5050
DISCONNECT_MSG= 'End'
ADDR= (SERVER, PORT)

client= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send(msg):
    message= msg.encode(FORMAT)
    msg_length= len(msg)
    send_length= str(msg_length).encode(FORMAT)
    send_length+= b" "*(HEADER- len(send_length))
    client.send(send_length)
    client.send(message)
    
    print(client.recv(2048).decode(FORMAT))
    
    
#msg= f"The Hostname of client is {socket.gethostname()} and the IP is {SERVER}"
#send(msg)
#send(DISCONNECT_MSG) 

while True:
    user_msg= input('Please enter: ')
    if user_msg== DISCONNECT_MSG:
        send(user_msg)
        break
    else:
        send(user_msg)
    


    
    