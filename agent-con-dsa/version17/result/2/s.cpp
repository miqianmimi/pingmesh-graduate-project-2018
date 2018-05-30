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
#include <fstream>
#include <iostream>

using namespace std;
#define PORT 8910
#define QUEUE_SIZE   10  
#define BUFFER_SIZE 1024  
  
//传进来的sockfd，就是互相建立好连接之后的socket文件描述符  
//通过这个sockfd，可以完成 [服务端]<--->[客户端] 互相收发数据  


//循环代码函数
void str_echo(int sockfd,struct sockaddr_in server_sockaddr)  
{  
    char buffer[BUFFER_SIZE];
    char buffer1[BUFFER_SIZE];
    char buffer2[BUFFER_SIZE];

    pid_t pid = getpid(); 
    while(1)  
    {  
        FILE *fp=fopen("resultabcd.json","a+"); 
        memset(buffer,0,sizeof(buffer));  
        int len = recv(sockfd, buffer, sizeof(buffer),0); 
        //cerr<<buffer<<endl;  
        std::cerr<<"\n"<<std::endl;
        std::cerr<<"server收到"<<std::endl;
        std::cerr<<buffer<<std::endl;
        std::cerr<<"\n"<<std::endl;

        if(strcmp(buffer,"exit")==0)  
        {  
            printf("\n");
            printf("server端一个退了,child process: %d exited.\n",pid);  
            printf("\n");   
            break;  
        }  


        //printf("pid:%d receive:\n",pid);  
        char ipv4_str_buf[INET_ADDRSTRLEN] = {0};
        //printf("received from %s at PORT %d\n",
        //                inet_ntop(AF_INET,  &server_sockaddr.sin_addr, ipv4_str_buf, sizeof(ipv4_str_buf)),
        //                ntohs(server_sockaddr.sin_port));

        
        strcpy(buffer1, "hi received *\n");
        send(sockfd,buffer1,BUFFER_SIZE,0);

        std::cerr<<"\n"<<std::endl;        
        std::cerr<<"server发送"<<std::endl;
        std::cerr<<buffer1<<std::endl;
        std::cerr<<"\n"<<std::endl;
        memset(buffer1,0,sizeof(buffer1));  


        memset(buffer2,0,sizeof(buffer2));  
        recv(sockfd,buffer2,sizeof(buffer2),0);
        if (strcmp(buffer2,"")!=0)  
        {
            std::cerr<<"\n"<<std::endl;        
            std::cerr<<"server收到json并写入库里面"<<std::endl;
            std::cerr<<buffer2<<std::endl;
            std::cerr<<"\n"<<std::endl;


            fprintf(fp,"%s\n",buffer2);
            memset(buffer2,0,sizeof(buffer2));  
        }


        fclose(fp);
    }  
    close(sockfd);  
   
}  
  
int main(int argc, char **argv)  
{  


    //定义IPV4的TCP连接的套接字描述符  
    int server_sockfd = socket(AF_INET,SOCK_STREAM, 0);  
    //定义sockaddr_in  
    struct sockaddr_in server_sockaddr;  
    server_sockaddr.sin_family = AF_INET;  
    server_sockaddr.sin_addr.s_addr = htonl(INADDR_ANY);  //inet_addr(argv[1]);  
    server_sockaddr.sin_port = htons(PORT);  
  
    //bind成功返回0，出错返回-1  
    if(bind(server_sockfd,(struct sockaddr *)&server_sockaddr,sizeof(server_sockaddr))==-1)  
    {  
        perror("bind");  
        exit(1);//1为异常退出  
    }  
    printf("bind success.\n");  
  
    //listen成功返回0，出错返回-1，允许同时帧听的连接数为QUEUE_SIZE  
    if(listen(server_sockfd,QUEUE_SIZE) == -1)  
    {  
        perror("listen");  
        exit(1);  
    }  
    printf("listen success.\n");  
  
    for(;;)  
    {  
        struct sockaddr_in client_addr;  
        socklen_t length = sizeof(client_addr);  
        //进程阻塞在accept上，成功返回非负描述字，出错返回-1  
        int conn = accept(server_sockfd, (struct sockaddr*)&client_addr,&length);  
        

        if(conn<0)  
        {  
            perror("connect");  
            exit(1);  
        }  
        printf("new client accepted.\n");  
        


        pid_t childid;  
        if(childid=fork()==0)//子进程  
        {   
            printf("child process: %d created.\n", getpid());  
            close(server_sockfd);//在子进程中关闭监听  
            str_echo(conn,server_sockaddr);//处理监听的连接  
            cout<<"+++++++++++++++++exit了解一下+++++++++++++++++"<<endl;
            //fclose(fp);
            exit(0);  
        }  
        //break;
        //fclose(fp);
    }  
  
    printf("closed.\n");  
    close(server_sockfd);  
    return 0;  
}  