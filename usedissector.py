import json
from dissector import Dissector
from dissector import *

"""
this file is a test unit for a pcap library (mainly dissector.py
and its associated protocols classes). This library uses and
depends on Scapy library.
"""
# instance of dissector class
dissector = Dissector()

# sending the pcap file to be dissected
pkts = dissector.dissect_pkts("/root/Desktop/irc.cap")

# iterating the dissected packets
for pkt in pkts :
    print(pkt)
print(pkts["irc"])
#print(json.dumps(pkts["http"], indent=4))
f = open("/root/Desktop/file.txt", "w")
#AAAAA = pkts["http"][17]
#print(pkts["http"][17]["message-body"])

f.write(json.dumps(pkts["irc"], indent=4))

#f.write(pkts[26])
#print(pkts["http"][17])
# print (pkts["http"])