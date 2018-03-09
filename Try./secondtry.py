import socket
from socket import *
from time import ctime

# tcpSock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# tcpSock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
tcpSock = socket(AF_INET, SOCK_STREAM)
HOST = '127.0.0.1'
PORT = 21561
BUFFSIZE = 1024
ADDR=(HOST, PORT)

udpSerSock = socket(AF_INET, SOCK_DGRAM)
udpSerSock.bind(ADDR)

while True:
    print('waiting for connection...')
    data, addr = udpSerSock.recvfrom(BUFFSIZE)
    udpSerSock.sendto(bytes('[%s] %s' % (ctime(), data.decode('utf-8')), 'utf-8'),addr)
    print('...received from and returned to:', addr)
udpSerSock.close()
