from dataclasses import dataclass
from sre_parse import FLAGS
import struct
from sys import flags
from typing import ClassVar

@dataclass
class Flags:

    qr : bool =0
    aa : bool =0
    tc : bool =0
    rd : bool =1
    ra : bool =0

    qr_mask : ClassVar = 0x8000
    aa_mask : ClassVar = 0x0400
    tc_mask : ClassVar = 0x0200
    rd_mask : ClassVar = 0x0100
    ra_mask : ClassVar = 0x0080
    z_mask   : ClassVar = 0x0070
    rcode_mask : ClassVar = 0x000F



    def pack_flags(self):
        byte = 0
        z=2
        byte |= z << 4  
        if self.qr:
            byte |= self.qr_mask
        if self.aa:
            byte |= self.aa_mask
        if self.tc:
            byte |= self.tc_mask
        if self.rd:
            byte |= self.rd_mask
        if self.ra:
            byte |= self.ra_mask
        return byte 
        

    def parseFlags(self,data):
        (byte,) = struct.unpack("! H", data[2:4])
        self.qr=(self.qr_mask & byte) >> 15
        self.rd=(self.rd_mask & byte) >> 8
        self.ra=(self.ra_mask & byte) >> 7
        flags = ""
        flags += "qr " if (self.qr) == 1 else ""
        flags += "rd " if (self.rd) == 1 else ""
        flags += "ra" if (self.ra) == 1 else ""
        flags += self.parse_Rcode(data)
        return flags

    def parse_Rcode(self, data):
        (byte,) = struct.unpack("! H", data[2:4])
        rd =(self.rcode_mask & byte)
        if(rd ==  0):
            return "\nStatus : NOERROR"
