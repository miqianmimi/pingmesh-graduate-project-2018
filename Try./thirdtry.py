from socketserver import (TCPServer as TCP, StreamRequestHandler as SRH)
from time import ctime
HOST=''
PORT=21557
ADDR=(HOST,PORT)

class MYRequestHandler(SRH):
    def handle(self):
        print ('...connected from:',self.client_address)
        print(ctime())
        self.wfile.write(bytes('[%s] %s' % (ctime(),self.rfile.readline().decode('utf-8')),'utf-8'))
tcpServ=TCP(ADDR,MYRequestHandler)
print('waiting for connection...')
tcpServ.serve_forever()

