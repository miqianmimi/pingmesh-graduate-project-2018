#! /bin/bash
{ 	
	ssh yiqing@192.168.2.101  'rm -fr 1/; rm -fr 2/ ; mkdir 1; mkdir 2 ; killall -u yiqing'
} &

sleep 1 &
wait $!

{
	ssh yiqing@192.168.2.100  'rm -fr 1/; rm -fr 2/ ; mkdir 1; mkdir 2 ; killall -u yiqing'
} &



{
	rm -fr 100/; rm -fr 101/; mkdir 100 ; mkdir 101
} &

sleep 3 &
wait $!

{
	killall -u yiqing
} & 

sleep 1 &
wait $!
{	
	ssh yiqing@143.89.191.40 ; cd pingmesh/v11/
} &


