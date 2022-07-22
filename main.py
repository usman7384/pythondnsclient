from MyParser import *
from MySocket import *
from queryBuilder import *
from answer import *
from dnslib import DNSRecord, DNSHeader, DNSQuestion, QTYPE, RR, A


def main(hostname,QueryType):

    flags=Flags()
    header=Header(flags)
    question= Question(hostname,QueryType)

    query=queryBuilder(header,question)
    query_packet=query.build_packet()

    sock = MySocket()
    sock.mysend(query_packet)
    query_packet, address = sock.myreceive()
    sock.sock.close()


    answer=Answer()
    head=header.parse_header(query_packet)
    ques=question.parse_question(query_packet)
    resp=answer.parse_answer(query_packet)

    print(head,ques,resp)


if __name__ == "__main__":
    HOST_NAME = "app.carbonteq-livestream.ml"
    QueryType=1
    main(HOST_NAME,QueryType )
