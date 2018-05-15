import os
a0=os.popen("sudo hping3 -V -c 4 -i u1000 192.168.2.100").read()
a1=os.popen("sudo hping3 -V -c 4 -i u1000 192.168.2.101").read()
a2=os.popen("sudo hping3 -V -c 4 -i u1000 192.168.2.202").read()
aa=a0+a1+a2
a=aa.split("\n")
for f in a:
    print(f)



