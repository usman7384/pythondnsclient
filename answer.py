from dataclasses import dataclass
from header import *
import struct

@dataclass
class Answer():

    IP : ClassVar 
    TTL: ClassVar


    def parse_ttl(self, data_recieved):
        ttl_list = list(data_recieved[-10:-6])
        ttl = 0
        for i in range(3):
            ttl += (
                ttl_list[i] * 256
            )  # one byte can represent a decimal number between 0(00) and 255.
        ttl += ttl_list[3]
        return ttl

    def parse_ip(self, data_recieved):
        ip_address_list = list(data_recieved[-4:])
        ip_address = []
        for i in ip_address_list:
            ip_address.append(str(i))
        return ".".join(ip_address)


    def parse_answer(self, data):
        IP = self.parse_ip(data)
        TTL = self.parse_ttl(data)
        return (
            f" TTL : {TTL}    IP : {IP}"
        )