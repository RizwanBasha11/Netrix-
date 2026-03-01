import socket
import random
from config import LOSS_RATE, BUFFER_SIZE

class UDPSocket:
    def __init__(self, port):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.bind(("localhost", port))

    def send(self, data, addr):
        if random.random() < LOSS_RATE:
            print("Packet dropped (simulated)")
            return
        self.sock.sendto(data, addr)

    def receive(self):
        data, addr = self.sock.recvfrom(BUFFER_SIZE)
        return data, addr
