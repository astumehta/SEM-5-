import socket
import threading
import time

bucket_token_list = []
MAX_BUCKET_SIZE = 10
TIME_LAPSE = 3
lock = threading.Lock()

def create_server_socket():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('127.0.0.1', 50003))
    server_socket.listen(5)
    print("Server started on 127.0.0.1:50003")
    return server_socket

def add_token_to_bucket():
    while True:
        with lock:
            if len(bucket_token_list) < MAX_BUCKET_SIZE:
                bucket_token_list.append(1)
        time.sleep(TIME_LAPSE)

def handle_client(client_socket):
    while True:
        data = client_socket.recv(1024).decode()
        if not data:
            continue
        print(f"Received: {data}")
        with lock:
            if bucket_token_list:
                bucket_token_list.pop(0)
                print(f"Token used, bucket: {bucket_token_list}")
            else:
                client_socket.send("Token not available, wait.".encode())
                print("No token available")
    client_socket.close()

def start_server():
    server_socket = create_server_socket()
    threading.Thread(target=add_token_to_bucket, daemon=True).start()
    while True:
        client_socket, addr = server_socket.accept()
        print(f"Connection from {addr}")
        threading.Thread(target=handle_client, args=(client_socket,), daemon=True).start()

start_server()
