from email import header
from flags import *
from random import randint
import struct
from dataclasses import dataclass

@dataclass
class Header:
    

    flags   : Flags
    QDCOUNT : int  = 1

    id      : ClassVar = randint(0, 255)
    ANCOUNT : ClassVar = 0
    NSCOUNT : ClassVar = 0
    ARCOUNT : ClassVar = 0        
    

    def isCorrect(self,data):
        length = len(data)
        return (length >= 12)

    def pack_header(self):
        header_packet = struct.pack(
            "!6H",
            self.id,
            self.flags.pack_flags(),
            self.QDCOUNT,
            self.ANCOUNT,
            self.NSCOUNT, # NSCOUNT
            self.ARCOUNT, # ARCOUNT
        )
        return header_packet

    def parse_header(self,data_recieved):
        flag_response=''
        if self.isCorrect(data_recieved):
            self.id=self.parseID(data_recieved)
            flag_response=self.flags.parseFlags(data_recieved)
            self.ANCOUNT=self.parseAN(data_recieved)
            self.QDCOUNT=self.parseQD(data_recieved)
            self.NSCOUNT=self.parseNS(data_recieved)
            self.ARCOUNT=self.parseAR(data_recieved)
            return f"Flags: {flag_response};  Query: {self.QDCOUNT},  Answer: {self.ANCOUNT},  Authority: {self.NSCOUNT},  Additional: {self.ARCOUNT}"
        return "MALICIOUS PACKET"


    def parseID(self,data_recieved):
        id = [str(i) for i in data_recieved[:2] if i > 0]
        return ";;ID = " + "".join(id) if len(id) > 0 else "ID = 0"

    def parseQD(self,data_recieved):
        query_count_list = list(data_recieved[4:6])
        query_count = query_count_list[0] * 10 + query_count_list[1] * 1
        return query_count

    def parseAN(self,data_recieved):
        answer_count_list = list(data_recieved[6:8])
        answer_count = answer_count_list[0] * 10 + answer_count_list[1] * 1
        return answer_count

    def parseNS(self,data_recieved):
        authority_list = list(data_recieved[8:10])
        authority = authority_list[0] * 10 + authority_list[1] * 1
        return authority

    def parseAR(self,data_recieved):
        additional_list = list(data_recieved[10:12])
        additional = additional_list[0] * 10 + additional_list[1] * 1
        return additional

