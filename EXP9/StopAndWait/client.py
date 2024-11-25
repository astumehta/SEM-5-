import socket
import time

HOST = '127.0.0.1'
PORT = 5001

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))

TIMEOUT = 5 

while True:
    message = input("Enter the data here: ")
    client_socket.sendall(message.encode())
    if message == 'end':
        break

    client_socket.settimeout(TIMEOUT)
    try:
        data = client_socket.recv(1024)
        print(data.decode())
    except socket.timeout:
        print(f"ACK not received for '{message}', retransmitting...")
        client_socket.sendall(message.encode())  # Retransmit the message

print("Ended the connection")
client_socket.close()
