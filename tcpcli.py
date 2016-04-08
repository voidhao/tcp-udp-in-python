#!/usr/bin/python
# -*- coding: utf-8 -*-
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('127.0.0.1', 8080))

print s.recv(1024)
for data in ['puhao', 'voidhao', 'clemon']:
    s.send(data)
    print s.recv(1024)
s.send('exit')
s.close()
