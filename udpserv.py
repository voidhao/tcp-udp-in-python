#!/usr/bin/python
# -*- coding: utf-8 -*-
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('127.0.0.1', 8080))
print 'bind UDP on 8080'
while True:
    data, addr = s.recvfrom(1024)
    print 'received from %s:%s' % addr
    s.sendto('hello, %s!' % data, addr)
