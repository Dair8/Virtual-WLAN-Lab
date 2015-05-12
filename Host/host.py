#! /usr/bin/env python

import os, sys
from socket import *
from fcntl import ioctl
from select import select
import getopt, struct
import subprocess

MAGIC_WORD = "asd"
TUNSETIFF = 0x400454ca
IFF_TAP   = 0x0002
TUNMODE = IFF_TAP

def usage(status=0):
    print "Usage: host.py [-t controllerip:port]"
    sys.exit(status)

opts = getopt.getopt(sys.argv[1:],"t:h")

for opt,optarg in opts[0]:
    if opt == "-h":
        usage()
    elif opt == "-t":
        MODE = 2
        IP,PORT = optarg.split(":")
        PORT = int(PORT)
        peer = (IP,PORT)


f = os.open("/dev/net/tun", os.O_RDWR)
ifs = ioctl(f, TUNSETIFF, struct.pack("16sH", "tun%d", TUNMODE))
ifname = ifs[:16].strip("\x00")


s = socket(AF_INET, SOCK_DGRAM)

try:
    s.sendto(MAGIC_WORD, peer)
    word,peer = s.recvfrom(1500)
    if word != MAGIC_WORD:
        print "Bad magic word for %s:%i" % peer
        sys.exit(2)    
    ip,peer = s.recvfrom(1500)
    print "Ejecutando comando: " + "ifconfig %s" %ifname + " %s" %ip
    os.system("ifconfig %s" %ifname + " %s" %ip)
    print "Connection with %s:%i established" % peer
    
    while 1:
        r = select([f,s],[],[])[0][0]
        if r == f:
            s.sendto(os.read(f,1500),peer)
        else:
            buf,p = s.recvfrom(1500)
            if p != peer:
                print "Got packet from %s:%i instead of %s:%i" % (p+peer)
                continue
            os.write(f, buf)
except KeyboardInterrupt:
    print "Stopped by user."
