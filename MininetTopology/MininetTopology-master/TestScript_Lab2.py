import socket
import os,sys
import struct

MULTICAST_TTL = 2
MCAST_GRP = sys.argv[1]
MESSAGE = b'Hello, Multicast!'

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, MULTICAST_TTL)

counter = 0
while(counter < 200):
	sock.sendto(MESSAGE, (MCAST_GRP, 50000))
	counter += 1
