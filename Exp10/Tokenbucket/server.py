import socket
import time

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

def server():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind(('localhost', 12345))
    bucket = TokenBucket(100, 10)
    while True:
        data, _ = s.recvfrom(1024)
        print(f"Received: {data.decode()}")

if __name__ == "__main__":
    server()
