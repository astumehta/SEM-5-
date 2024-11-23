import time
import random

total_frames = 5
timeout = 2
current_frame = 0

def send_frame(frame):
    print(f"Frame {frame} sent.")
    time.sleep(1)

def ack_receive(frame):
    choice = random.choice([True, False])
    if choice:
        print(f"Acknowledgement received for Frame {frame}.")
    else:
        print(f"No acknowledgement for Frame {frame}")
    return choice

while current_frame < total_frames:
    send_frame(current_frame)

    t = time.time()
    ack = False

    while time.time() - t < timeout:
        ack = ack_receive(current_frame)
        break

    if ack:
        current_frame += 1
    else:
        print(f"Timeout! Retransmitting frame {current_frame}...")

print("All frames sent and acknowledged successfully!")
