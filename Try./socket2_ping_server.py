#server
from socket import *
serverport=20003
serverSocket=socket(AF_INET,SOCK_DGRAM)
serverSocket.bind(('127.0.0.1',serverport))
print('server is ok')
while True:
    message,addr=serverSocket.recvfrom(1024)
    print (message)
    print(addr)
    print('receive message from %s',addr)
    if str(message,'utf-8')=='ping':
        serverSocket.sendto(bytes('pong','utf-8'),addr)
serverSocket.close()
