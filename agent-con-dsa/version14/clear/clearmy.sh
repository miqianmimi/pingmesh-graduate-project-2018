#! /bin/bash


#清除服务器端的文件夹重建
clearway(){
	{
		#echo $1,$2,$3
		echo "清除$1服务器上的残留文档，并创建$2到$[$2+$3]的文档"
		#$1，is the server ip
		#$2，is the start of the 目录
		scp everyclear.sh yiqing@$1:~ #需要打印一次密码
		#sleep 2
		ssh -t -t yiqing@$1 "bash everyclear.sh $2 $3 " #需要打印一次密码
	} 

}

#清除网关端的文件夹重建
cleargate(){
	#echo $1
	#mkdir -p result;
	cd result;
	rm -rf *;
	t=`expr $1 \* $(($1 - 1))`
	#echo $t
	for ((i=1;i<=$t;i ++)) ;
	do  
    	mkdir $i ;
	done  
}


#main
ARRAY=($(awk '{print $0}' pinglist.txt))
mmm=0
for i in ${ARRAY[*]}
do
	((mmm++))
done
#mmm代表有多少个Ping
echo $mmm

count=1



for i in ${ARRAY[*]}
do
	{
		clearway $i $count $mmm
	} &
	#sleep 3 &
	#wait $!
	count=$[ $count + $mmm - 1 ]
done

{
	cleargate $mmm

} &
sleep 1 &
wait $!

{
	killall -u yiqing
} & 




#ssh yiqing@143.89.191.114 
#cd pingmesh/


