import socket
import time

HOST='127.0.0.1'
PORT=5001

client_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client_socket.connect((HOST,PORT))

while True:
    message=input("enter the data here..")
    client_socket.sendall(message.encode())
    if message=='end':
        break
    data=client_socket.recv(1024)
    time.sleep(2)
    print(data.decode())
    
print("ended the connection")
client_socket.close()