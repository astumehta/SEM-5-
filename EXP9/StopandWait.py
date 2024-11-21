import random
import time

def unreliable_network(packet, loss_prob=0.3, corruption_prob=0.2):
   if packet is None:
       return None
   if random.random() < loss_prob:
       return None
   if random.random() < corruption_prob:
       packet['corrupt'] = True
   return packet

class Sender:
   def __init__(self):
       self.frame_num = 0

   def send(self):
       print(f"Sending Frame {self.frame_num}")
       return {'frame_num': self.frame_num}

   def receive_ack(self, ack):
       if ack is None:
           print(f"Timeout occurred for Frame {self.frame_num}. Retransmitting...\n")
           return False
       elif 'corrupt' in ack:
           print(f"Corruption detected in ACK for Frame {self.frame_num}. Retransmitting...\n")
           return False
       elif ack['ack_num'] == self.frame_num:
           print(f"Acknowledgment received for Frame {self.frame_num}\n")
           self.frame_num += 1
           return True

class Receiver:
   def __init__(self):
       self.expected_frame_num = 0

   def receive(self, packet):
       if packet is None:
           print(f"Frame lost during transmission!\n")
           return None
       if 'corrupt' in packet:
           print(f"Corruption detected in Frame {packet['frame_num']}. Discarding packet.\n")
           return None
       if packet['frame_num'] == self.expected_frame_num:
           ack = {'ack_num': self.expected_frame_num}
           self.expected_frame_num += 1
           return ack
       else:
           return None

def stop_and_wait_arq(sender, receiver, frame_count):
   for _ in range(frame_count):
       ack_received = False
       while not ack_received:
           packet = sender.send()
           packet = unreliable_network(packet)
           ack = receiver.receive(packet)
           ack = unreliable_network(ack)
           ack_received = sender.receive_ack(ack)
           time.sleep(1)

   print("All frames sent successfully.")

if __name__ == "__main__":
   sender = Sender()
   receiver = Receiver()
   frame_count = 5
   stop_and_wait_arq(sender, receiver, frame_count)
