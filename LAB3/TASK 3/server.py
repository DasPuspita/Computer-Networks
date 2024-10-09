# -*- coding: utf-8 -*-
"""
Created on Mon Nov 13 21:30:29 2023

@author: Lenovo
"""

import socket
import threading

HEADER= 64
FORMAT= 'utf-8'
SERVER= socket.gethostbyname(socket.gethostname())    
PORT= 5050
DISCONNECT_MSG= 'End'
ADDR= (SERVER, PORT)

server= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)
print('Server is starting......')

server.listen()
print('Server is listening ON', SERVER)

def handle_clients(conn, addr): 
    #conn, addr= server.accept() 
    print('Connected To', addr)
    connected= True
    while connected:
        msg_length= conn.recv(HEADER).decode(FORMAT)
        if msg_length: 
            msg_length= int(msg_length)
            msg= conn.recv(msg_length).decode(FORMAT)
            if msg== DISCONNECT_MSG:
                connected= False
                conn.send(f'Terminating the connection with {addr}'.encode(FORMAT))
            else:
                vowels= 'aeiouAEIOU'
                count= 0
                
                for elem in msg:
                    if elem in vowels:     
                        count+=1
                        
                if count==0:
                    conn.send("Not enough vowels".encode(FORMAT))
                    
                elif count<=2:
                    conn.send("Enough vowels I guess".encode(FORMAT))
                    
                else:
                    conn.send("Too many vowels".encode(FORMAT))
                    
                    
                    
                    
    conn.close()
    
while True:
    conn, addr= server.accept() 
    thread= threading.Thread(target= handle_clients, args=(conn, addr))
    thread.start()
              