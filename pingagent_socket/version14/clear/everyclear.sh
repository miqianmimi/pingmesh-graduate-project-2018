#clearforeach

echo "开始清除空间"
rm -rf *
for ((i=$1; i<$[$2+$1-1]; i ++))  
do  
	echo $i;
	#rm -rf $i;
	mkdir $i ;
done  
echo "清除完成，退出."
if [ $1 -ge 30 ]; then 
	echo "要跳回去么46貌似有点毛病？"
	#ssh yiqing@143.89.191.114
	#cd pingmesh
fi
killall -u yiqing
