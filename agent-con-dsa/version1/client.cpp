#include<iostream>
#include<string.h>
#include<sys/types.h>
#include<sys/socket.h>
#include<netinet/in.h>
#include<arpa/inet.h>
#include<stdlib.h>
#include<unistd.h>
#include<netdb.h>

using namespace std;

int main()
{
	int client, server;
	int portNum=1234; //note the server and clients I
	bool isExit=false;
	int bufsize=1024;
	char buffer[bufsize];
    const char *ip = "127.0.0.1";

	struct sockaddr_in server_addr;
	
    // init socket
	client= socket(AF_INET,SOCK_STREAM,0);
	if (client<0)
	{
		cout<<"\nError creating socket..."<<endl;
		exit(1);
	}
	cout<<"\n =>Client Socket Created"<<endl;
	server_addr.sin_family=AF_INET;
	server_addr.sin_addr.s_addr = inet_addr("127.0.0.1");  //具体的IP地址
	server_addr.sin_port=htons(portNum);
	//connecting socket server

	if (connect(client,(struct sockaddr*)&server_addr,sizeof(server_addr))==0)
	{
		cout<<"=>Connecting to Server..." <<endl;
	}
	cout << "=> Awaiting confirmation from the server..." << endl; //line 40
	recv(client,buffer,bufsize,0);
	cout<<"=>Connection confirmed"<<endl;
	cout<<"\n\n=> Enter # to end the connection\n"<<endl;
	do{
		cout<<"Client: ";
		do{
			cin>>buffer;
			send(client,buffer,bufsize,0);
			if (*buffer=='#')
			{
				send(client,buffer,bufsize,0);
				*buffer='*';
				isExit=true;
			}
		}while (*buffer !=42);
		
		cout<<"Server: ";
		do{
			recv(client,buffer,bufsize,0);
			cout<<buffer<<' ';
			if (*buffer=='#')
			{
				*buffer='*';
				isExit=true;
			}
		}while(*buffer!=42);
		cout<<endl;
	}while(!isExit);
	cout<<"\n=>Connection terminated..."<<endl;
	cout<<"\nGoodbye\n"<<endl;
	close(client);
	return 0;

	} 
