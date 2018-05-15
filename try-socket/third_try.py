from socket import *
HOST='localhost'
PORT=21557
BUFSIZE=1024
ADDR=(HOST,PORT)
while True:
    tcpCliSock=socket(AF_INET,SOCK_STREAM)
    tcpCliSock.connect(ADDR)
    data=input('>')
    if not data :
        break
    tcpCliSock.send(bytes('%s \r\n' %data,'utf-8'))
    data=tcpCliSock.recv(BUFSIZE)
    if not data:
        break
    print (data.strip())
    tcpCliSock.close()


