import time
import random

window_size = 4
total_frames = 10
sent_frames = 0
ack_received = [False] * total_frames  # Track which frames have been acknowledged
waiting_for_ack = []  # List to track the frames that have been sent but not acknowledged

while any(not ack for ack in ack_received):  # Continue until all frames are acknowledged
    # Send new frames up to window size
    while sent_frames < total_frames and len(waiting_for_ack) < window_size:
        print(f"Sending frame {sent_frames}")
        waiting_for_ack.append(sent_frames)  # Add frame to the list of sent frames waiting for ACK
        sent_frames += 1
        time.sleep(1)

    # Process ACKs (or simulate loss)
    for frame in waiting_for_ack[:]:  # Iterate over frames that were sent but not acknowledged
        ack = random.choice([True, False])  # Simulate whether the ACK is received for the frame
        if ack:
            print(f"ACK received for frame {frame}")
            ack_received[frame] = True
            waiting_for_ack.remove(frame)  # Remove frame from the waiting list
        else:
            print(f"ACK lost for frame {frame}, resending it")
            # Frame is lost, re-add to the waiting list for retransmission
            time.sleep(1)  # Simulate some delay before retransmitting the lost frame
