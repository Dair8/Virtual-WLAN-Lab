#! /usr/bin/env python

import os, sys
from socket import *
from fcntl import ioctl
from select import select
import getopt, struct
import subprocess

#Help function
def usage(status=0):
    print "Usage: host.py"
    sys.exit(status)

#Global variables
MAGIC_WORD = "VirtualWLANLab"
TUNSETIFF = 0x400454ca
IFF_TAP   = 0x0002
TUNMODE = IFF_TAP
PORT = 10000

#Parsing the arguments
opts = getopt.getopt(sys.argv[1:],"h")

for opt,optarg in opts[0]:
    if opt == "-h":
        usage()

#Creating the new interface
f = os.open("/dev/net/tun", os.O_RDWR)
ifs = ioctl(f, TUNSETIFF, struct.pack("16sH", "tun%d", TUNMODE))
ifname = ifs[:16].strip("\x00")

#Preparing socket
s = socket(AF_INET, SOCK_DGRAM)

#Establishing connection with the controller
try:
    s.bind(("", PORT))
    while 1:
        word,peer = s.recvfrom(1500)
        if word == MAGIC_WORD:
            break
        print "Bad magic word for %s:%i" % peer(i)
    s.sendto(MAGIC_WORD, peer)
    #Retreiving IP from the controller and assign it to the new interface
    ip,peer = s.recvfrom(1500)
    print "Assigned to interface %s" %ifname + " the IP address: %s" %ip
    os.system("ifconfig %s" %ifname + " %s" %ip)
    print "Connection with %s:%i established" % peer
    
    #Starting the emulator functions  (host side)
    while 1:
        r = select([f,s],[],[])[0][0]
        if r == f:
            s.sendto(os.read(f,1500),peer)
        else:
            buf,p = s.recvfrom(1500)
            os.write(f, buf)
except KeyboardInterrupt:
    print "Stopped by user."
