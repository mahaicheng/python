#!/usr/bin/env python
# coding=utf-8

from socket import *
from time import ctime

HOST = ''
PORT = 21567
BUFSIZ = 1024

ADDR = (HOST, PORT)

udpSock = socket(AF_INET, SOCK_DGRAM)
udpSock.bind(ADDR)

while True:
    print 'waiting for message...'

    data, addr = udpSock.recvfrom(BUFSIZ)
    udpSock.sendto('[%s] %s' % (ctime(), data), addr)

    print '..received from and  returned to: ', addr

udpSock.close()
