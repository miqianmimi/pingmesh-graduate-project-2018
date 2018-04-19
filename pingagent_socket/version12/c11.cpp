#include <sys/types.h>  
#include <sys/socket.h>  
#include <stdio.h>  
#include <netinet/in.h>  
#include <arpa/inet.h>  
#include <unistd.h>  
#include <string.h>  
#include <stdlib.h>  
#include <fcntl.h>  
#include <sys/shm.h>  
#include <chrono>
#include <iostream>  
#include <sstream>
#include <netdb.h>
#include <unistd.h>
#include <string.h>

#define PORT  8910
#define BUFFER_SIZE 1024  

long int unix_timestamp()
{
    time_t t = std::time(0);
    long int now = static_cast<long int> (t);
    return now;
}

int main(int argc, char **argv)  
{  
    if(argc!=2)  
    {  
        printf("usage: client IP \n");  
        exit(0);  
    }  
  
    //定义IPV4的TCP连接的套接字描述符  
    int sock_cli = socket(AF_INET,SOCK_STREAM, 0);  
    struct sockaddr_in servaddr;  
    memset(&servaddr, 0, sizeof(servaddr));  
    servaddr.sin_family = AF_INET;  
    servaddr.sin_addr.s_addr = inet_addr(argv[1]);  
    servaddr.sin_port = htons(PORT);  //服务器端口  

    //错误点应该在这里
    //连接服务器，成功返回0，错误返回-1  
    if (connect(sock_cli, (struct sockaddr *)&servaddr, sizeof(servaddr)) < 0)  
    {  
        perror("connect");  
        exit(1);  
    }  
    printf("connect server(IP:%s).\n",argv[1]);  
  
    char sendbuf[BUFFER_SIZE];  
    char recvbuf[BUFFER_SIZE];  
    //客户端将控制台输入的信息发送给服务器端，服务器原样返回信息  
    int county= 1;
    int ii=1;

    while (1)  
    {  
        if (county==5)//为了让server端退出.
        { 
            sprintf(sendbuf,"exit");
        }
        if(county<5)
        {
            sprintf(sendbuf,"send hello%d", county);
        }
        county=county+1;
        auto start = std::chrono::high_resolution_clock::now();
        
        std::cerr<<"\n"<<std::endl;        
        std::cerr<<"client发送"<<std::endl;
        std::cerr<<sendbuf<<std::endl;
        std::cerr<<"\n"<<std::endl;

        send(sock_cli, sendbuf, strlen(sendbuf),0); ///发送  

        if(strcmp(sendbuf,"exit")==0)  
        {   
            printf("\n");  
            printf("client端退出了 exited.\n");  
            printf("\n");  
            break;  
        }  
        memset(sendbuf, 0, sizeof(sendbuf));  

        //printf("client receive:\n"); 
        recv(sock_cli, recvbuf, sizeof(recvbuf),0); ///接收  
        std::cerr<<"\n"<<std::endl;        
        std::cerr<<"client收到"<<std::endl;
        std::cerr<<recvbuf<<std::endl;
        std::cerr<<"\n"<<std::endl;

        memset(recvbuf, 0, sizeof(recvbuf)); 



        auto end = std::chrono::high_resolution_clock::now();
        std::chrono::duration<double> elapsed_seconds = end-start;
  
        std::stringstream ss;
        ss.clear();
        char stt[INET_ADDRSTRLEN];
        ss<<"{\"host\":\"";
        ss<<inet_ntop(AF_INET, &servaddr.sin_addr, stt, sizeof(stt));
        ss<<"\",";
        ss<<"\"timestamp\":"; 
        long int now = unix_timestamp();
        ss<<std::to_string(now);
        ss<<",\"num\":";
        ss<<std::to_string(ii);
        ii=ii+1;
        ss<<",\"entries\":[[";
        ss<<std::to_string(now);
        ss<<",\"";
        ss<<inet_ntop(AF_INET,  &servaddr.sin_addr, stt, sizeof(stt));
        ss<<"\",";
        ss<<std::to_string(ntohs(servaddr.sin_port));
        ss<<",\"";

        char hname[128];
        struct hostent *hent;
        gethostname(hname, sizeof(hname));
        hent = gethostbyname(hname);
        std::string pp= hent->h_name;
        unsigned int iSize = pp.length();
        //std::cout<<pp<<std::endl;
        std::string b;
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
        ss<<PORT;
        ss<<",\"tcp\",";
        ss<<"\"tor\",";
        int amm=strlen(sendbuf);
        ss<<std::to_string(amm);
        ss<<",";
        ss<<std::to_string(elapsed_seconds.count());
        ss<<",0]]}";
        std::string mm ;
        mm.clear();
        mm=ss.str();
        
        std::cerr<<"\n"<<std::endl;        
        std::cerr<<"client发送json"<<std::endl;
        std::cerr<<mm<<std::endl;
        std::cerr<<"\n"<<std::endl;


        send(sock_cli, mm.c_str(),mm.size(),0); 
        


        sleep(3) ;
    }  

    close(sock_cli );  
    return 0;  
}  
