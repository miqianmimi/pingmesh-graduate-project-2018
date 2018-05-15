 import socket
from socket import *
from time import ctime

# tcpSock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# tcpSock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
tcpSock = socket(AF_INET, SOCK_STREAM)
HOST = '127.0.0.1'
PORT = 21563
BUFFSIZE = 1024
ADDR=(HOST, PORT)

tcpSerSock = socket(AF_INET, SOCK_STREAM)
tcpSerSock.bind(ADDR)
tcpSerSock.listen(5)

while True:
    print('waiting for connection...')
    tcpCliSock, addr = tcpSerSock.accept()
    print('...connected from:', addr)

    while True:
        data = tcpCliSock.recv(BUFFSIZE)
        if not data:
            break

        tcpCliSock.send(bytes('[%s] %s' % (ctime(), data.decode('utf-8')), 'utf-8'))
tcpSerSock.close()
