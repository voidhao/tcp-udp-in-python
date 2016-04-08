import socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
for data in ['hao', 'voidhao', 'clemon']:
    s.sendto(data, ('127.0.0.1', 8080))
    print s.recv(1024)
s.close()
