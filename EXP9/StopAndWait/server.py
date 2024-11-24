import socket
import time

HOST='127.0.0.1'
PORT=5001

server_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_socket.bind((HOST,PORT))
server_socket.listen()

print(f"the server is listening on {HOST}:{PORT}")
conn,address=server_socket.accept()
print(f"connected by {address}")

def generate_ack(conn):
    while True:
        data=conn.recv(1024)
        if not data:
            break
        received_data=data.decode()
        time.sleep(2)
        print(f"the data which is received is: {received_data}")
        if received_data=='end':
            break
        ack=f"sending the acknowledgement of: {received_data}"
        conn.sendall(ack.encode())
    conn.close()

generate_ack(conn)

server_socket.close()
