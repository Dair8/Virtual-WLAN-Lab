#! /usr/bin/env python
##

import os, sys
from socket import *
from fcntl import ioctl
from select import select
import getopt, struct
import json
from NetScheme import NetScheme

#Json's parsing functions
def _decode_list(data):
    rv = []
    for item in data:
        if isinstance(item, unicode):
            item = item.encode('utf-8')
        elif isinstance(item, list):
            item = _decode_list(item)
        elif isinstance(item, dict):
            item = _decode_dict(item)
        rv.append(item)
    return rv
def _decode_dict(data):
    rv = {}
    for key, value in data.iteritems():
        if isinstance(key, unicode):
            key = key.encode('utf-8')
        if isinstance(value, unicode):
            value = value.encode('utf-8')
        elif isinstance(value, list):
            value = _decode_list(value)
        elif isinstance(value, dict):
            value = _decode_dict(value)
        rv[key] = value
    return rv

#Help function
def usage(status=0):
    print "Usage: controller.py -t [ipTarget1,ipTarget2,...,ipTargetn]"
    print "You need to have a valid json in the same folder than controller.py"
    sys.exit(status)

#Global variables
MAGIC_WORD = "VirtualWLANLab"
PORT = 10000
socketList = [0] * 256
peer = [0] * 256
ip=["10.0.0.1/24","10.0.0.2/24","10.0.0.3/24","10.0.0.4/24","10.0.0.5/24","10.0.0.6/24","10.0.0.7/24"]

#Parsing the arguments
opts = getopt.getopt(sys.argv[1:],"t:h")

for opt,optarg in opts[0]:
    if opt == "-h":
        usage()
    elif opt == "-t":
        target = optarg.split(",")

with open('data.json') as data_file:    
    data = json.load(data_file, object_hook=_decode_dict)

scheme=NetScheme(data["hosts"],data["neighbors"])


#Preparing the peers list and the sockets using the hosts in the scheme provided
j=0
for i in scheme.netList.keys():
    socketList[i] = socket(AF_INET, SOCK_DGRAM)
    peer[i]=(target[j],PORT)
    print (peer[i])
    j+=1

#Establishing conecctions with the hosts
try:
    j=0
    for i in scheme.netList.keys():
	socketList[i].sendto(MAGIC_WORD, peer[i])
	word,peer[i] = socketList[i].recvfrom(1500)
	if word != MAGIC_WORD:
		print "Bad magic word for %s:%i" % peer[i]
		sys.exit(2)
        ##Sending IP to the host's new interface
        socketList[i].sendto(ip[j], peer[i])
        print "Connection with %s:%i established" %peer[i]
    	j+=1
    print("Controller ready")

    #Starting the wireless emulator functions (controller side)
    while 1:
        inp,outp,exc = select(socketList,[],[])
	inp=inp[0]
	buf,p = inp.recvfrom(1500)
	i=0
	while inp!=socketList[i]:
		i+=1
	aux=scheme.getNeighbors(i)[0]
	for j in aux:
		socketList[j].sendto(buf,peer[j])

except KeyboardInterrupt:
    print "Stopped by user."

