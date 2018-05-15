#192.168.2.101打开监听
#nc -k -l 1567
#-k表示一直保持

#!/bin/bash
Num=1000
IPADDR="192.168.2.101"
PORT="1234"
for ((i=0; i<1000; i++))
do nc $IPADDR $PORT < /dev/null 
  if [ $? -ne "0" ]
  then  
    echo "*" 
  fi 
done


##command in 192.168.2.100
#time bash caculate.sh >rttt.log
#scp rttt.log yiqing@192.168.2.254:~