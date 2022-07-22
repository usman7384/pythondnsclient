from dataclasses import dataclass
from header import *
import struct

@dataclass
class Question():

    url : str
    query_type : int


    def build_question(self):
        query_packet = "".encode()
        for i in self.url.split("."):
            encoded = i.encode()
            bytelen = len(i)
            query_packet += struct.pack(f"! {bytelen+1}B", bytelen, *encoded)
        query_packet += struct.pack(
            ">B2H", 0, self.query_type, 1 # End of String,# Query Type,# Query Class
        )  
        return query_packet

    def parse_question(self,data):
        self.url=self.parse_hostname(data)
        self.query_type=self.parse_query_type(data)
        query_class = self.parse_query_class(data)
        return f"\nDomain : {self.url}      Query Type :  {query_class}    Query Class :  {self.query_type}"


    def parse_hostname(self, data_recieved):
        url = []
        chunk_size = data_recieved[12]
        index = 13
        while chunk_size != 0:
            for i in range(chunk_size):
                url.append(data_recieved[index])
                index += 1
            url.append(46)
            chunk_size = data_recieved[index]
            index += 1
        hostname = ""
        for i in url:
            hostname += chr(i)
        return hostname

    def parse_query_type(self, data_recieved):
        index = 12
        while data_recieved[index] != 0:
            index += 1
        index += 1
        query_type = ""
        query_type_list = list(data_recieved[index : index + 2])
        index += 2
        if (query_type_list[0] * 10 + query_type_list[1] * 1) == 1:
            query_type += "  A   "
        return query_type

    def parse_query_class(self,data_recieved):
        index = 12
        while data_recieved[index] != 0:
            index += 1
        index += 3
        query_class = ""
        class_list = list(data_recieved[index : index + 2])
        if (class_list[0] * 10 + class_list[1] * 1) == 1:
            query_class += " IN "
        return query_class


