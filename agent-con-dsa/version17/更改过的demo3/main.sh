#test

#打印内容，个数
printserverinfo(){
	echo ${ARRAY[*]}
	echo ${#ARRAY[@]}
}

###测试循环传文件
trasmissiontest(){
 	for i in ${ARRAY[*]}
	{
		scp s.cpp yiqing@$i:~
		scp c.cpp yiqing@$i:~
	}
}

###测试循环读取,号前后数据
pirntpinglist(){
	for j in ${list[*]}
	{
		arr=(${j//,/ })  
		for i in ${arr[*]}
		do
			echo $i 
		done
	}
}


#ping的函数
pingagentserver(){


	#echo $1,$2
	#$1代表count $2代表server号
	{
	    echo " "
	    echo "目标：实现server $2 启动"	
	    echo " "
		#开文件已经完成
		##{
		#	ssh -t -t yiqing@$2
		#	mkdir -p $1
		#} &
		#wait $!
		#发送文件打开server
		#z=$($3-1)
		
		#focus@@@@@
		#除了2需要调整外，别的都不需要调整
		#if [ $(($1%z)) == 1 ] ; then 
		#scp server.sh yiqing@$2:~
		#echo " "
		#fi  
		

		{
			echo " "
			echo "我开启了新后台,来设置$2 server" 
			echo " "
			ssh -t -t yiqing@$2  "bash server.sh $1 $2 "
		} &
		sleep 1
		#wait $!
	} &

}


pingagentclient(){
	#echo $1,$2,$3,$4
    ##{ 
	#	ssh -t -t yiqing@$i
	#	mkdir -p $1
	#} &
	#wait $!
	#w=$($4-1)
	##{
	echo " "
	echo "目标：实现client $2 启动"	
	echo " "
	#focus@@@@@
	#除了2需要调整外，别的都不需要调整
	#if [ $(($1%$w)) == 1 ] ; then 
	#	scp client.sh yiqing@$2:~
	#	echo " "
	#fi



	sleep 5
	{
		echo " "
		echo "我开启了新后台,来链接$3" 
		echo " "
		ssh -t -t yiqing@$2 "bash client.sh $1 $2 $3 $4"
	} &
	wait $!
	echo " "

    #103这也可以拿数据
	scp yiqing@$3:$4/resultabcd.json result/$1	
	echo " "
	echo " "
	echo "已经成功的从$3ping$2中得到数据，并且($3 as server $2 as client)"
	echo " "
	#} &

}

#Main function 调用函数，跑测试并获得程序，主函数在这里看过来

#先测两台！
ARRAY=($(awk '{print $0}' $1))
{
	for i in ${ARRAY[*]}
	do
		echo ${i}
		scp server.sh yiqing@$i:~
		echo " "
		scp client.sh yiqing@$i:~
		echo " "
	done
} &  
wait $!
#！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！#！！
#！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！#！！
#！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！#！！
#！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！#！！
#！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！#！！
#！！！！！！！！！！！！！#并发就不要用来计数 mmm会出错！！！！！！！！！！！！！#！！
#！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！#！！
#！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！#！！
#！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！#！！
#！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！#！！
#！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！#！！


MMM=0
ARRAY=($(awk '{print $0}' $1))
for i in ${ARRAY[*]}
do
	((mmm=mmm+1))
done

echo "";
echo "这次一共" $mmm "台服务器";
echo "";


#创建ping的数组队列，,号隔开，前面server，后面client :并创建对应文档用于记录ping数据。
idd=1
for m in ${ARRAY[*]}
{
	for n in ${ARRAY[*]}
	do
		#mkdir -p $idd 
		if [ $m != $n ];then
			#echo $m,$n
			#echo $idd
			list[idd]="$m,$n"
			((idd++))
		fi
	done
}

#传文件
for t in ${ARRAY[*]}
{	
	w=1;
	for ((i=w;i<`expr $w+$mmm-1`;i++));
	do 
		echo $t;		
		cp s.cpp result/$i/
		cd result/$i/
		scp s.cpp yiqing@$t:~
		echo " "
		cd ..
		cd ..
		cp c.cpp result/$i/
		cd result/$i/
		scp c.cpp yiqing@$t:~
		echo " "
		cd ..
		cd ..
	done
	w=`expr $w+$mmm-1`;

} 




pingthesame(){
	for ((i=$1;i<`expr $1+$mmm-1`;i ++)) ;
	do  
		count=$i  #count = 1,2;3,4;5,6
		j=${list[$i]} # j = 列表
		arr=(${j//,/ }) # arr = 分隔开
		s=${arr[0]}; # s = server部分 
		#echo "这边输出的s应该都一样"; 
		c=${arr[1]};  	#c= client部分
		
		if [ $count == $1 ]; then #当count=1，3，5的时候启动server
			pingagentserver $count $s ; #给server的有count 和server的IP
			sleep 2
		fi
		{
			pingagentclient $count $c $s $1 ; #给client的有count 和client和server的，还有1，3，5用于读数据
		} &
	done  
}
#！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！#！！
#！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！#！！
#！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！#！！
#！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！#！！
#！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！#！！
#！！！！！！！！！！！！！#$1用来取我们的数据！！！！！！！！！！！！！！！！！！#！！
#！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！#！！
#！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！#！！
#！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！#！！
#！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！#！！
#！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！#！！		
		#} &
 		#sleep 100 &
		#wait $! 
#！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！#！！
#！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！#！！
#！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！#！！
#！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！#！！
#！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！#！！
#！！！！！！！！！！！！！#调试用的睡眠:现在可以实现并行！！！！！！！！！！！！！#！！
#！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！#！！
#！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！#！！
#！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！#！！
#！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！#！！
#！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！#！！


tt=`expr $mmm \* $(($mmm - 1))`;
ddd=1;
while [ $ddd -lt $tt ]
do 
	{	
		pingthesame $ddd
	} &
	#sleep 25 &
	#wait $!

	((ddd=ddd+mmm-1));
done

#最后再发一回拿结果
#for t in ${ARRAY[*]}
##{	
#	w=1;
#	for ((i=w;i<`expr $w+$mmm-1`;i++));
#	do 
#		scp yiqing@$t:$w/resultabcd.json result/$w
#	done
#	w=`expr $w+$mmm-1`;
#
#} 



#gateway :143.89.191.114
#起一个s,同时两个client链接他
#同时起三个s
