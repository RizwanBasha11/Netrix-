import time
import threading
from config import RETRANSMIT_TIMEOUT

class ReliableSender:
    def __init__(self, udp_socket):
        self.udp = udp_socket
        self.seq = 0
        self.pending = {}
        self.lock = threading.Lock()

    def send(self, packet, addr):
        with self.lock:
            self.seq += 1
            packet["seq"] = self.seq
            self.pending[self.seq] = (packet, addr, time.time())

        self.udp.send(packet["raw"], addr)

    def ack_received(self, seq):
        with self.lock:
            if seq in self.pending:
                del self.pending[seq]
                print("ACK received:", seq)

    def retransmit_loop(self):
        while True:
            time.sleep(1)

            with self.lock:
                for seq in list(self.pending.keys()):
                    packet, addr, ts = self.pending[seq]

                    if time.time() - ts > RETRANSMIT_TIMEOUT:
                        print("Resending:", seq)
                        self.pending[seq] = (packet, addr, time.time())
                        self.udp.send(packet["raw"], addr)
