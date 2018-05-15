#include<iostream>
#include<string.h>
#include<sys/types.h>
#include<sys/socket.h>
#include<netinet/in.h>
#include<arpa/inet.h>
#include<stdlib.h>
#include<unistd.h>
#include<netdb.h>
#include <chrono>
#include<cstdio>
#include <stdio.h>
#include<string>
#include<sstream>
using namespace std;
long int unix_timestamp()
{
	time_t t = std::time(0);
	long int now = static_cast<long int> (t);
	return now;
}
int main()
{
	FILE *fp=fopen("*.txt","w"); 
	int client, server;
	int portNum=1239; //note the server and clients I
	bool isExit=false;
	int bufsize=1024;
	char buffer[bufsize];
	char str[INET_ADDRSTRLEN];
	long int now;
    const char *ip = "127.0.0.1";

	struct sockaddr_in server_addr;
	



    // init socket
	client= socket(AF_INET,SOCK_STREAM,0);
	if (client<0)
	{
		cout<<"\nError creating socket..."<<endl;
		exit(1);
	}
	cout<<"\n=>Client Socket Created"<<endl;
	server_addr.sin_family=AF_INET;
	server_addr.sin_addr.s_addr = inet_addr("192.168.2.101");  //具体的IP地址
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
		
	auto start = std::chrono::high_resolution_clock::now();
	
	int cc=0;
	do {

		cc=cc+1;

		int count=0;
		do{
			cout<<"Client: send hello *\n";
			strcpy(buffer,"send hello *");
			count=count+1;
			send(client,buffer,bufsize,0);
			if (*buffer=='#')
			{
				send(client,buffer,bufsize,0);
				*buffer='*';
				isExit=true;
			}
		}while (count<1);
		
		count=0;
		do{		
			cout<<"Server: ";
			recv(client,buffer,bufsize,0);
			cout<<buffer<<' ';
			count=count+1;
			if (*buffer=='#')
			{
				*buffer='*';
				isExit=true;
			}
    		cout<<"\n"<<endl;

    		//get IP get connection.
			printf("received from %s at PORT %d\n",
		       inet_ntop(AF_INET,  &server_addr.sin_addr, str, sizeof(str)),
		       ntohs(server_addr.sin_port));
			

			char hname[128];
    		struct hostent *hent;
    		int i;
   			gethostname(hname, sizeof(hname));
    		hent = gethostbyname(hname);
   			printf("SrcIp: %s/naddress list: ", hent->h_name);
   			for(i = 0; hent->h_addr_list[i]; i++) {
        		printf("%s/t", inet_ntoa(*(struct in_addr*)(hent->h_addr_list[i])));
    		}
    		cout<<"\n"<<endl;

			//[1]get dstip dstport
			printf("1.DistIp: %s\n",inet_ntop(AF_INET,  &server_addr.sin_addr, str, sizeof(str)));
			printf("2.DistPort: %d\n",ntohs(server_addr.sin_port));

			//[2]get srcip srcport

			printf("3.SrcIp:%s\n", hent->h_name);
    		printf("4.SrcPort:%d\n",portNum);

    		//[3] get ProbingType
			printf("5.ProbingType:tor\n");
			//[4] get Protocol
			printf("6.Protocol:TCP Socket\n");
			//[5] get MsgLen
			int amm=strlen(buffer);
			printf("7.MsgLen:%d",amm );
			
			//[6]get timestamp, get rtt
			auto end = std::chrono::high_resolution_clock::now();
			std::chrono::duration<double> elapsed_seconds = end-start;
			std::time_t end_time = std::chrono::system_clock::to_time_t(end);

			stringstream ss;
			int ii=1;
			ss<<"{\"host\":\"";
			ss<<inet_ntop(AF_INET, &server_addr.sin_addr, str, sizeof(str));
			ss<<"\",";
			ss<<"\"timestamp\":"; 
			now = unix_timestamp();
			ss<<to_string(now);
			ss<<",\"num\":";
			ss<<to_string(ii);
			ss<<",\"entries\":[[";
			ss<<to_string(now);
			ss<<",\"";
			ss<<inet_ntop(AF_INET,  &server_addr.sin_addr, str, sizeof(str));
			ss<<"\",";
			ss<<to_string(ntohs(server_addr.sin_port));
			ss<<",\"";


			string pp= hent->h_name;
			unsigned int iSize = pp.length();
       			string b;
	        for (int tt=3;tt<iSize;tt++)
	        {
	        	if('-' != pp[tt])
	        	{
	        		b+=pp[tt];
	        	}
	        	if('-'==pp[tt])
	        	{
				b+='.';	
	        	}
	        }

			ss<<b;
			ss<<"\",";
			ss<<portNum;
			ss<<",\"tcp\",";
			ss<<"\"tor\",";
			ss<<to_string(amm);
			ss<<",";
			ss<<to_string(elapsed_seconds.count());
			ss<<",0]]}";
			std::string mm ;
			mm=ss.str();

			fprintf(fp,"%s\n", mm.c_str());

    		printf("8.Timestamp:%s",std::ctime(&end_time));
		    printf("9.Rtt:");
		    cout<<elapsed_seconds.count() <<endl;
			cout<<mm<<endl;

		}while(count<1);
	}while(cc<1);
	cout<<endl;

	cout<<"=>Connection terminated..."<<endl;
	cout<<"Goodbye"<<endl;
	close(client);
	
  
	fclose(fp);
	return 0;

	} 
