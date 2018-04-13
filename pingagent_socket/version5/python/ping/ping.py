import os
a0=os.popen("ping -c 3 -q 192.168.2.100").read()
a1=os.popen("ping -c 3 -q 192.168.2.101").read()
a2=os.popen("ping -c 3 -q 192.168.2.202").read()
aa=a0+a1+a2
a=aa.split("\n")
for f in a:
    print(f)


b0=os.popen("ping -c 3 -q -s 63000 192.168.2.100").read()
b1=os.popen("ping -c 3 -q -s 63000 192.168.2.101").read()
b2=os.popen("ping -c 3 -q -s 63000 192.168.2.202").read()
bb=b0+b1+b2
b=bb.split("\n")
for c in b:
    print(c)
