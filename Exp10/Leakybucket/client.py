import socket
import time
import random
#current rate,feedback,packetsize
class Leaky:
    current_rate = 10
    def adjust_rate(self, feedback):
        if feedback == "congested":
            self.current_rate = max(1, self.current_rate - 1)
        elif feedback == "underutilized":
            self.current_rate += 1


client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
leaky = Leaky()
while True:
    packet_size = random.randint(1, 20)
    message = f"Packet of size {packet_size}"
    client_socket.sendto(message.encode(), ('localhost', 12345))
    print(f"Sent: {message}")

    feedback = "congested" if packet_size > 10 else "underutilized"
    leaky.adjust_rate(feedback)

    time.sleep(1)
