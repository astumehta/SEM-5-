import socket
import time
import random

HOST = '127.0.0.1'
PORT = 5001

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen()

print(f"The server is listening on {HOST}:{PORT}")
conn, address = server_socket.accept()
print(f"Connected by {address}")

def generate_ack(conn):
    while True:
        data = conn.recv(1024)
        if not data:
            break
        received_data = data.decode()
        time.sleep(2)
        print(f"The data which is received is: {received_data}")
        
        if received_data == 'end':
            break
        
        # Simulate ACK loss
        if random.random() < 0.3:
            print(f"Simulating lost ACK for: {received_data}")
            continue
        
        # Send ACK if not dropped
        ack = f"ACK for: {received_data}"
        conn.sendall(ack.encode())
    conn.close()

generate_ack(conn)
server_socket.close()
