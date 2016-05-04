#!/usr/bin/env python
# coding=utf-8

from socket import *
from time import ctime

HOST = ''
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST, PORT)

tcpServSock = socket(AF_INET, SOCK_STREAM)
tcpServSock.bind(ADDR)
tcpServSock.listen(5)

while True:
    print 'waiting for connection...'

    tcpCliSock, addr = tcpServSock.accept()
    print 'connection from: ', addr

    while True:
        data = tcpCliSock.read(BUFSIZ)

        if not data:
            break;

        tcpCliSock.send('[%s] %s' % ctime(), data)

        tcpCliSock.close()

tcpServSock.close()
