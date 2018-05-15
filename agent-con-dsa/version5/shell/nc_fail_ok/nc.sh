#!本脚本实现功能有：用ping命令得到1v3:server之间icml的Ping的rtt时间，存入log之中
#!用nc命令得到1v3:server之间的rtt时间，存入log之中.
#!101是大server

cat/ip-ports.txt | while read line
do
  nc -w 10 -v -z $line >/dev/null 2>&1
  if [$? -eq 0]
  then
    echo $line:ok
  else
    echo $line:fail
  fi
done






