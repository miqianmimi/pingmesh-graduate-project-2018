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
		
		cp s.cpp result/$1/
		cd result/$1/
		scp s.cpp yiqing@$2:~
		echo " "
		cd ..
		cd ..
		sleep 3
		{
			ssh -t -t yiqing@$2  "bash server.sh $1 $2 "
		} &
		sleep 1
		#wait $!
	} &

}


pingagentclient(){
	#echo $1,$2,$3
    ##{ 
	#	ssh -t -t yiqing@$i
	#	mkdir -p $1
	#} &
	#wait $!
	#w=$($4-1)
	{
		echo " "
		echo "目标：实现client $2 启动"	
		echo " "
		#focus@@@@@
		#除了2需要调整外，别的都不需要调整
		#if [ $(($1%$w)) == 1 ] ; then 
		#	scp client.sh yiqing@$2:~
		#	echo " "
		#fi


		cp c.cpp result/$1/
		cd result/$1/
		scp c.cpp yiqing@$2:~
		echo " "
		cd ..
		cd ..
		sleep 3 
		{
			ssh -t -t yiqing@$2 "bash client.sh $1 $2 $3"
		} &

		wait $!
		echo " "
		scp yiqing@$3:$1/resultabcd.json result/$1	
		echo " "
		echo " "
		echo "已经成功的从$3ping$2中得到数据，并且($3 as server $2 as client)"
		echo " "
	} &

}

#Main function 调用函数，跑测试并获得程序，主函数在这里看过来

#先测两台！
ARRAY=($(awk '{print $0}' pinglist1.txt))
mmm=1
{
	for i in ${ARRAY[*]}
	do
		((mmm++))
		echo ${i}
		scp server.sh yiqing@$i:~
		echo " "
		scp client.sh yiqing@$i:~
		echo " "
	done
} & 
wait $!



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


for t in ${list[*]}
{
	echo $t;
} 




count=1
for j in ${list[*]}
do
	arr=(${j//,/ }) 

	tt=0;
	s=${arr[0]};
	c=${arr[1]};

	echo " "
	echo "这次要处理的是这两台服务器",$s,$c
	echo " "

	{
		pingagentserver $count $s ;
		sleep 4 &
		wait $!
		pingagentclient $count $c $s ;
	} &

	((count++))  
done

#gateway :143.89.191.114

