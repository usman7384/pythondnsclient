from dataclasses import dataclass
from header import *
from question import *

@dataclass
class queryBuilder:

    header: Header
    question: Question

    def build_packet(self):
        packet=self.header.pack_header()
        packet+=self.question.build_question()
        return packet

    def unpack(self, data):
        data_len = len(data)
        data_recieved = struct.unpack(f"!{data_len}B", data)
        return data_recieved









