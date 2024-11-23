import time
import random

window_size = 4
total_frames = 10

sent_frames = [False] * total_frames
ack_received = [False] * total_frames


window_start = 0

while not all(ack_received):
    for i in range(window_start, min(window_start + window_size, total_frames)):
        if not sent_frames[i]:
            print(f"Sending frame {i}")
            sent_frames[i] = True
            time.sleep(1)

    for i in range(window_start, min(window_start + window_size, total_frames)):
        if not ack_received[i]:
            ack = random.random() < 0.7
            if ack:
                print(f"Received ACK for frame {i}")
                ack_received[i] = True
                time.sleep(1)
            else:
                print(f"Frame {i} lost. Will retransmit later.")
                sent_frames[i] = False
                time.sleep(1)

    while window_start < total_frames and ack_received[window_start]:
        window_start += 1

print(f"All {total_frames} frames sent and acknowledged.")