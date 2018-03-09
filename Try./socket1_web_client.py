from socket import *
host='127.0.0.1'
port=22323
clientsocket=socket(AF_INET,SOCK_STREAM)
clientsocket.connect((host,port))

try:
    sentence = input('input the name of the package:')
    clientsocket.send(bytes(sentence, 'utf-8'))
    lens = int(str(clientsocket.recv(1024), 'utf-8'))
    print('From server:')
    print(lens)
    for i in range(lens):
        receive = clientsocket.recv(1024)
        print(str(receive, 'utf-8'))
except Exception as e:
    clientsocket.close()

