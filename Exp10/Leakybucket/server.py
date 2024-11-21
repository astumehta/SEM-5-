import socket
import time

class Leaky:
    def __init__(self, max_rate):
        self.current_rate = max_rate
        self.packet_loss_threshold = 5

    def adjust_rate(self, feedback):
        if feedback == "congested":
            self.current_rate = max(1, self.current_rate - 1)
        elif feedback == "underutilized":
            self.current_rate += 1

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind(('localhost', 12345))
    leaky = Leaky(max_rate=10)
    
    print("Leaky Server is listening on port 12345...")
    while True:
        data, addr = server_socket.recvfrom(1024)
        print(f"Received packet: {data.decode()} from {addr}")
        
        feedback = "congested" if len(data) > leaky.packet_loss_threshold else "underutilized"
        leaky.adjust_rate(feedback)

if __name__ == "__main__":
    start_server()
