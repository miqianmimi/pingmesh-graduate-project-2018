import pandas as pd
import numpy as np
import random as rd
import seaborn as sns
import matplotlib.pyplot as plt
a = pd.read_csv('ping_data.csv')


c=[11111,22222,33333,44444]
cc=['Tor','local','Core', 'supercore', 'interdc']



#10*10 /100图
for i in range(1000):
    new = []
    AB=pd.DataFrame(None).T
    new.append(4+i)
    new.append(1523263580577353+int(i/100))
    new.append('10.2.96.'+str(50+int(i%10)))
    new.append(rd.choice(c))
    new.append('10.2.96.'+str(50+(int(i/10))%10))
    new.append(rd.choice(c))
    new.append('Tcp')
    new.append('Tor')
    new.append(1024)
    new.append(int(np.random.normal(20,20,2000)[i]))
    new.append(0)
    print(new)
    AB=pd.DataFrame(new).T
    AB.columns=a.columns
    a= pd.concat([a,AB], ignore_index=True)

a.to_csv(r'./1.csv')
a = pd.read_csv('1.csv')


def IP2name(srcip,c):
    d={}
    pp=list(range(1000,c,-1))
    for i,j in enumerate(srcip):
        if j not in d:
            d[str(j)]=pp.pop()
    print(d)
    newlist=[]
    for i in srcip:
        newlist.append(str(d[i]))
    print(newlist)
    return newlist

def transformer(a):
    SrcIP=a.pop('SrcIP')
    DstIP=a.pop('DstIP')
    print(SrcIP)
    print(DstIP)
    SrcIP=list(SrcIP)
    DstIP=list(DstIP)
    d=IP2name(SrcIP,0)
    e=IP2name(DstIP,0)
    a.insert(0,'SrcIPname',d)
    a.insert(1,'DstIPname',e)
    print(a)
    return(a)

a=transformer(a[3:])
plt.figure("pingmesh")

for i in range(10):
    temp=a.loc[3+i*(100):102+i*(100)]
    b=temp.pivot('SrcIPname','DstIPname','RTT')
    print(b)
    ax = sns.heatmap(b,annot=True)
   # plt.savefig("a{}.png".format(i+1))
    plt.subplot(3,4,i+1)

plt.show()

