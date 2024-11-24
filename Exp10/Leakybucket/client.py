import socket, random, time

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    packet_size = random.randint(1, 5)
    message = str(packet_size)
    client_socket.sendto(message.encode(), ('localhost', 12345))
    print(f"Sent packet of size {packet_size}")
    
    time.sleep(1)
