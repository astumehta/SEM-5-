import socket

def create_client_socket():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('127.0.0.1', 50003))
    print("Connected to server")
    return client_socket

def communicate_with_server(client_socket):
    while True:
        data = input("Enter data (or 'exit' to quit): ")
        if data == "exit":
            break
        client_socket.send(data.encode())
    client_socket.close()

def start_client():
    client_socket = create_client_socket()
    communicate_with_server(client_socket)

start_client()
