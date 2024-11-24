import time
import random

window_size = 4
total_frames = 10
sent_frames = 0
ack_received = [False] * total_frames 
waiting_for_ack = []  

while False in ack_received:
    while sent_frames < total_frames and len(waiting_for_ack) < window_size:
        print(f"Sending frame {sent_frames}")
        waiting_for_ack.append(sent_frames) 
        sent_frames += 1
        time.sleep(1)

    for i in waiting_for_ack: 
        ack = random.choice([True, False]) 
        if ack:
            print(f"ACK received for frame {i}")
            ack_received[i] = True
            waiting_for_ack.remove(i)  
        else:
            print(f"ACK lost for frame {i}, resending it")
            time.sleep(1) 
