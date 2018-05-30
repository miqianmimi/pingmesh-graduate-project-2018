#automate key
key(){
	echo $1 $2
	if [ $2 == 1 ]; then
		{	echo "生成钥匙了"
			ssh-keygen -t rsa -P '' -f ~/.ssh/id_rsa
			sleep 1 #5
		} &
		wait $!
	fi
	echo "发送钥匙了,请输入密码!"
	scp -P 22 /home/yiqing/.ssh/id_rsa.pub yiqing@$1:~/
	sleep 1 #2
	
	echo "开始配置钥匙，请输入两次密码"
	scp everykey.sh yiqing@$1:~ #需要打印一次密码
	sleep 1 #2
	ssh -t -t yiqing@$1 "bash everykey.sh $2 "
	echo "钥匙配置已经完成"
}

ARRAY=($(awk '{print $0}' $1))
count=1
for i in ${ARRAY[*]}
do
	{
		key $i $count
	} &
	wait $!
	((count++))
done

