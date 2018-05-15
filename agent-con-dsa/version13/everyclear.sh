#clearforeach

echo "开始清除空间"
rm -rf *
for ((i=$1; i<=$[7+$1]; i ++))  
do  
	mkdir $i ;
done  
echo "清除完成，退出."
killall -u yiqing
