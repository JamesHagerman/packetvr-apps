#!/usr/bin/env python

# import dpkt

# f = open('test.pcap')
# pcap = dpkt.pcap.Reader(f)

# for ts, buf in pcap:
#     eth = dpkt.ethernet.Ethernet(buf)
#     ip = eth.data
#     tcp = ip.data

#     if tcp.dport == 80 and len(tcp.data) > 0:
#         http = dpkt.http.Request(tcp.data)
#         print http.uri

# f.close()

import sys
import struct

import pcap
import dpkt

pc = pcap.pcap(name="en1", timeout_ms=10000, immediate=True)
pc.setfilter('tcp')

def __packet_handler(ts, pkt):
    eth = dpkt.ethernet.Ethernet(pkt)
    if eth.type != dpkt.ethernet.ETH_TYPE_IP:
        # skip non-IP packets
        return
    ip = eth.data
    # Grab the source IP off of the packet.
    # It's returned as 4 byte string, e.g. '\x01\x02\x03\x04'
    # This gives you the IP as an integer, not in dotted decimal form.
    src_ip = struct.unpack("<L", ip.src)[0]
    #print str(src_ip)

    tcp = ip.data

    if tcp.dport == 80 and len(tcp.data) > 0:
        http = dpkt.http.Request(tcp.data)
        print http.uri

pc.loop(0, __packet_handler)



