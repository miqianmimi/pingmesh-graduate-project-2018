#include<iostream>
#include<string.h>
#include<sys/types.h>
#include<sys/socket.h>
#include<netinet/in.h>
#include<arpa/inet.h>
#include<stdlib.h>
#include<unistd.h>

using namespace std;

int main()
{
	int client, server;
	int portNum=1234;
	bool isExit=false;
	int bufsize=1024;
	char buffer[bufsize];
	struct sockaddr_in server_addr;
	socklen_t size;

	//init socket
	client=socket(AF_INET,SOCK_STREAM, IPPROTO_TCP);

	if (client<0)
	{
		cout << "\nError establishing connection." << endl;
		exit(1);
	}
	cout << "\n=>Server Socket connection created..." << endl;

	server_addr.sin_family = AF_INET;
	server_addr.sin_addr.s_addr=inet_addr("127.0.0.1");
	server_addr.sin_port =htons(portNum);
	//binding socket
	//将套接字和IP、端口绑定

	if (bind(client,(struct sockaddr*)&server_addr,sizeof(server_addr))<0)
	{
		cout << "=> Error binding socket ..." << endl;
		exit(1);
	}
	size = sizeof(server_addr);
	cout<< "=> Looking for clients..." << endl;

	// listening socket
	//进入监听状态，等待用户发起请求

	listen(client,20);
	// accept client
	//接收客户端请求

	server=accept(client,(struct sockaddr*)&server_addr, &size);

	if (server < 0)
	{
		cout<<"=> Error on accepting..."<< endl;
		exit(1);
	}
	//向客户端发送数据

	while (server > 0)
	{
		strcpy(buffer, "=> Server connected...\n");
		send(server,buffer,bufsize,0);
		cout<<"=> Connected  with client...." <<endl;
		cout<<"\n=>Enter # to end the connection" <<endl;
		
		cout<<"Client: ";
		do{
			recv(server,buffer,bufsize,0);
			cout<<buffer<<"  ";
			if (*buffer=='#')
			{
				*buffer='*';
				isExit=true;
			}
		}while (*buffer !='*');

		do{
			cout<<"\nServer: ";
			do{
				cin>>buffer;
				send(server,buffer,bufsize,0);
				if (*buffer=='#')
				{
					send(server,buffer,bufsize,0);
					*buffer = '*';
					isExit= true;
				}
			} while (*buffer != '*');
			cout<<"Clinet: ";
			do {
				recv(server,buffer,bufsize,0);
				cout<<buffer<<" ";
				if (*buffer=='#')
				{
					*buffer='*';
					isExit=true;
				}

			}while(*buffer != '*' );
		}while(!isExit);
		cout<<"\n\n=> Connection terminated...." <<endl;
		cout<<"\nGoodbye..."<<endl;
		isExit=false;
		exit(1);
	}
	close(client);
	return 0;	

}
