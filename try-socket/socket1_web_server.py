from socket import *
serverName='127.0.0.1'
serverPort=22323
serverSocket=socket(AF_INET,SOCK_STREAM)
serverSocket.bind((serverName,serverPort))
serverSocket.listen(1)
print('The server is ready to receive.')
while True:
    print('waiting to connect...')
    connectSocket, addr = serverSocket.accept()
    print('connected from',addr)
    try:
        message=connectSocket.recv(1024)
        message=str(message,'utf-8')
        fi=message.split()[-1]
        print(fi)
        text=open(str(fi),'r')
        print(text)
        lines=text.readlines()
        head=len(lines)
        print(head)
        connectSocket.send(bytes(str(head),'utf-8'))
        for i in lines:
            connectSocket.send(bytes(i,'utf-8'))
    except FileNotFoundError:
        head='404 not Found'+'\n'
        head+str('documents not found')
        connectSocket.send(bytes(head,'utf-8'))
    connectSocket.close()
serverSocket.close()

