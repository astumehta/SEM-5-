import random
import time

def unreliable_network(packet, loss_prob=0.3, corruption_prob=0.2):
    if packet and random.random() < loss_prob:
        return None
    if packet and random.random() < corruption_prob:
        packet['corrupt'] = True
    return packet

class Sender:
    def __init__(self):
        self.frame_num = 0

    def send(self):
        print(f"Sending Frame {self.frame_num}")
        return {'frame_num': self.frame_num}

    def receive_ack(self, ack):
        if not ack:
            print(f"Timeout or lost ACK for Frame {self.frame_num}. Retransmitting...\n")
            return False
        if ack.get('corrupt'):
            print(f"Corruption detected in ACK for Frame {self.frame_num}. Retransmitting...\n")
            return False
        if ack.get('ack_num') == self.frame_num:
            print(f"Acknowledgment received for Frame {self.frame_num}\n")
            self.frame_num += 1
            return True

class Receiver:
    def __init__(self):
        self.expected_frame_num = 0

    def receive(self, packet):
        if not packet:
            print(f"Frame lost during transmission!\n")
            return None
        if packet.get('corrupt'):
            print(f"Corruption detected in Frame {packet['frame_num']}. Discarding packet.\n")
            return None
        if packet['frame_num'] == self.expected_frame_num:
            print(f"Frame {packet['frame_num']} received successfully.\n")
            ack = {'ack_num': self.expected_frame_num}
            self.expected_frame_num += 1
            return ack

def stop_and_wait_arq(sender, receiver, frame_count):
    for _ in range(frame_count):
        while True:
            packet = unreliable_network(sender.send())
            ack = unreliable_network(receiver.receive(packet))
            if sender.receive_ack(ack):
                break
            time.sleep(1)
    print("All frames sent successfully.")

if __name__ == "__main__":
    stop_and_wait_arq(Sender(), Receiver(), frame_count=5)
