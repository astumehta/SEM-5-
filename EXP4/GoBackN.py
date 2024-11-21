import time
import random

class GoBackN:
    def __init__(self, window_size, total_frames):
        self.window_size = window_size
        self.total_frames = total_frames
        self.sent_frames = 0
        self.ack_received = 0

    def send_frames(self):
        while self.ack_received < self.total_frames:
            for i in range(self.window_size):
                if self.sent_frames < self.total_frames:
                    print(f"Sending frame {self.sent_frames}")
                    self.sent_frames += 1
                    time.sleep(1)

            for i in range(self.window_size):
                if self.ack_received < self.total_frames:
                    ack = random.choice([True, False])
                    if ack:
                        print(f"ACK received for frame {self.ack_received}")
                        self.ack_received += 1
                    else:
                        print(f"Frame {self.ack_received} lost, resending from this frame")
                        self.sent_frames = self.ack_received
                        break

gbn = GoBackN(window_size=4, total_frames=10)
gbn.send_frames()
