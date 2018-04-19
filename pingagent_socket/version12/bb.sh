#! /bin/bash
#在254上v10里面部署client;server两个文件的代码1.
#在254上运行采集数据的bb.sh的代码2.运行后得到数据
#在254上放置python画图的代码3.
#在254上放置json转成画图格式的代码4.

#ssh yiqing@143.89.191.40
#cd pingmesh/v10


{
	scp s11.cpp yiqing@192.168.2.101:1/  
	ssh -t -t yiqing@192.168.2.101  'cd 1/; g++ s11.cpp -o s11 -std=c++11; ./s11'
	echo "++++++++++101 as server is over++++++++++."
} & 

##{ scp s11.cpp yiqing@192.168.2.101:~/; ssh yiqing@192.168.2.101; g++ s11.cpp -o s11 -std=gnu++11; ./s11 192.168.2.101; } &

sleep 5 &
wait $!
#expect expect_scp.sh 192.168.2.254  yiqing  yiqingma result.txt  ~/

#用expect来传输文件代替scp
#scp result.txt yiqing@192.168.2.254:~/
#或者从254直接Pull

#另一者也在后台执行：

{	scp c11.cpp yiqing@192.168.2.100:1/
	ssh -t -t yiqing@192.168.2.100 'cd 1/; g++ c11.cpp -o c11 -std=c++11 ;./c11 192.168.2.101'
	echo "++++++++++100 as client is over++++++++++."
} &
#sleep 20 &
#wait $!


#一者在后台执行：


{	scp s11.cpp yiqing@192.168.2.100:2/
	ssh -t -t yiqing@192.168.2.100  'cd 2/; g++ s11.cpp -o s11 -std=gnu++11 ; ./s11 '
	echo "++++++++++100 as server is over++++++++++."
	
} &

#另一者也在后台执行：

{	scp c11.cpp yiqing@192.168.2.101:2/
	ssh -t -t yiqing@192.168.2.101 'cd 2/; g++ c11.cpp -o c11 -std=gnu++11 ;./c11 192.168.2.100' 
	echo "++++++++++101 as client is over+++++++++++++++."
} &
#然后数据存到了254里面
#打开json转格式文件，读出文件。
#就可以疏通到python画图软件中

#运行本程序bash jj.sh
sleep 20 &
wait $!
#回到192.168.2.254上：远程读取数据为了画图


scp yiqing@192.168.2.101:1/resultabcd.json 101/
scp yiqing@192.168.2.100:2/resultabcd.json 100/
echo "get data"
echo "draw the picture"

#python vis.py





