import socket
import time
import random

class TokenBucket:
    def __init__(self, capacity, rate):
        self.capacity = capacity
        self.rate = rate
        self.tokens = 0
        self.last_time = time.time()

    def update(self):
        elapsed = time.time() - self.last_time
        self.tokens = min(self.capacity, self.tokens + elapsed * self.rate)
        self.last_time = time.time()

    def can_send(self, size):
        self.update()
        if self.tokens >= size:
            self.tokens -= size
            return True
        return False

def client():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    bucket = TokenBucket(100, 10)
    while True:
        size = random.randint(1, 20)
        if bucket.can_send(size):
            s.sendto(f"Packet {size}".encode(), ('localhost', 12345))
            print(f"Sent: Packet {size}")
        else:
            print("Not enough tokens")
        time.sleep(1)

if __name__ == "__main__":
    client()
