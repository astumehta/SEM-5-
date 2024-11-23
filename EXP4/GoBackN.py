import time
import random

window_size = 4
total_frames = 10
sent_frames = 0
ack_received = 0

while ack_received < total_frames:
    for i in range(window_size):
        if sent_frames < total_frames:
            print(f"Sending frame {sent_frames}")
            sent_frames += 1
            time.sleep(1)

    for i in range(window_size):
        if ack_received < total_frames:
            ack = random.choice([True, False]) 
            if ack:
                print(f"ACK received for frame {ack_received}")
                ack_received += 1
            else:
                print(f"Frame {ack_received} lost, resending from this frame")
                sent_frames = ack_received
                break