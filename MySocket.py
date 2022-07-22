import socket
from typing import ClassVar


class MySocket:

    DNS_IP : ClassVar = "8.8.8.8"  # Google public DNS server IP.
    DNS_PORT : ClassVar = 53  # DNS server port for queries.
    READ_BUFFER : ClassVar = 1024
    address : ClassVar = (DNS_IP, DNS_PORT)


    def __init__(self, sock=None):
        if sock is None:
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        else:
            self.sock = sock

    def mysend(self, data):
        sent = self.sock.sendto(data,self.address)
        if sent == 0:
            raise RuntimeError("socket connection broken")

    def myreceive(self):
            data, self.address = self.sock.recvfrom(self.READ_BUFFER)
            if data == b"":
                raise RuntimeError("socket connection broken")
            return data,self.address
