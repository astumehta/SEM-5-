import socket

class Leaky:
    current_rate = 10
    packet_loss_threshold = 5 

    def adjust_rate(self, feedback):
        if feedback == "congested":
            self.current_rate = max(1, self.current_rate - 1)
        elif feedback == "underutilized":
            self.current_rate += 1

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind(('localhost', 12345))
leaky = Leaky()

print("Leaky Server is listening on port 12345...")

while True:
    data, addr = server_socket.recvfrom(1024)
    print(f"Received packet: {data.decode()} from {addr}")
    
    feedback = "congested" if len(data) > leaky.packet_loss_threshold else "underutilized"
    leaky.adjust_rate(feedback)
