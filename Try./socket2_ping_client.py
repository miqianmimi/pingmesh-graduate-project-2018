#client
from socket import *
import time
clientsocket=socket(AF_INET,SOCK_DGRAM)
host='127.0.0.1'
port=20003
message=bytes('ping','utf-8')
for i in range(10):
    print("send ping")
    clientsocket.sendto(message,(host,port))
    receve,addr=clientsocket.recvfrom(1024)
    print(receve)
    if str(receve,'utf-8')=='pong':
        print('The {i} ping is arrived at{j}'.format(i=i+1,j=time.ctime()))
clientsocket.close()

