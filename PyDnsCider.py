#!/usr/bin/python
import time
import socket
from netaddr import IPNetwork
print "Enter your /CIDR notation for Reverse DNS"
cidr = raw_input("> ")
for ip in IPNetwork(cidr):
    try:
        ptr = socket.gethostbyaddr(str(ip))
        print '%s,%s' % (ip,ptr[0])
    except socket.herror:
        print '%s,N/a' % ip
    time.sleep(.1)
