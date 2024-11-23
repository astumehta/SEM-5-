import time
import random
class StopAndWait:
    def _init_(self, total_frames):
        self.total_frames = total_frames  
        self.current_frame = 0           
        self.timeout = 2                 

    def send_frame(self, frame):
        print(f"Sending frame {frame}...")
        time.sleep(0.5) 

    def receive_ack(self, frame):
        ack = random.choice([True, False])  
        if ack:
            print(f"Acknowledgment received for frame {frame}.")
        else:
            print(f"Acknowledgment lost for frame {frame}.")
        return ack

    def simulate(self):
        while self.current_frame < self.total_frames:
            self.send_frame(self.current_frame)

            start_time = time.time()
            ack_received = False

            while time.time() - start_time < self.timeout:
                ack_received = self.receive_ack(self.current_frame)
                if ack_received:
                    break

            if ack_received:
                self.current_frame += 1
            else:
                print(f"Timeout! Retransmitting frame {self.current_frame}...")

        print("All frames sent and acknowledged successfully!")

protocol = StopAndWait(total_frames=5) 
protocol.simulate()