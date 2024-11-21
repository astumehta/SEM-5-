import time
import random

class SelectiveRepeat:
    def __init__(self, window_size, total_frames):
        self.window_size = window_size
        self.total_frames = total_frames
        self.sent_frames = [None] * total_frames
        self.ack_received = [False] * total_frames
        self.current_frame = 0

    def send_frame(self, frame_num):
        if self.sent_frames[frame_num] is None:
            print(f"Sending frame {frame_num}")
            self.sent_frames[frame_num] = True
            time.sleep(1)

    def receive_ack(self, frame_num):
        ack = random.choice([True, False])
        if ack:
            print(f"ACK received for frame {frame_num}")
            self.ack_received[frame_num] = True
        else:
            print(f"NACK for frame {frame_num}")

    def send_frames(self):
        while not all(self.ack_received):
            for i in range(self.window_size):
                frame_num = (self.current_frame + i) % self.total_frames
                if not self.ack_received[frame_num]:
                    self.send_frame(frame_num)

            for i in range(self.window_size):
                frame_num = (self.current_frame + i) % self.total_frames
                if not self.ack_received[frame_num]:
                    self.receive_ack(frame_num)

            for i in range(self.window_size):
                frame_num = (self.current_frame + i) % self.total_frames
                if self.ack_received[frame_num]:
                    self.current_frame = (self.current_frame + 1) % self.total_frames
                    break

sr = SelectiveRepeat(window_size=4, total_frames=10)
sr.send_frames()
