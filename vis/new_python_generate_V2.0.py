import pandas as pd
import numpy as np
import random as rd
import seaborn as sns
import matplotlib.pyplot as plt
import statsmodels.api as sm
a = pd.read_csv('ping_data.csv')


c=[11111,22222,33333,44444]
cc=['Tor','local','Core', 'supercore', 'interdc']



#40*40 / 1600 picture
for i in range(1600):
    new = []
    AB=pd.DataFrame(None).T
    new.append(4+i)
    new.append(1523263580577353)
    new.append('10.2.96.'+str(50+int(i%40)))
    new.append(rd.choice(c))
    new.append('10.2.96.'+str(50+(int(i/40))%40))
    new.append(rd.choice(c))
    new.append('TCP')
    new.append('ToR')
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
    pp=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'
        ,'0','1','2','3','4','5','6','7','8','9','A','B','C','D']
    for i,j in enumerate(srcip):
        if j not in d:
            d[str(j)]=pp[-1]
            pp=pp[:-1]
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


#FIRST HEATMAP
a=transformer(a[3:])
temp=a.loc[3:]
b=temp.pivot('SrcIPname','DstIPname','RTT')



plt.figure("pingmesh")
ax = plt.subplot(2,1,1)
#cmap = sns.cubehelix_palette(start = 1, rot = 3, gamma=0.8, as_cmap = True)
pic=sns.heatmap(b,annot=True,ax=ax,linewidths=0.15, linecolor='white',annot_kws={"color":"black","size":1})
for text in pic.texts:
    text.set_size(1)
    if int(text.get_text())> int(50):
        text.set_size(12)
        text.set_weight('bold')
        text.set_style('italic')


#sns.heatmap(b,mask=b<40,ax=ax,cbar=False,annot=True,annot_kws={"weight": "bold","color":"blue","size":10})


ax.set_title('Pingmesh Heatmap')

ax.set_xlabel('Servername')
ax.set_ylabel('Servername')
#plt.savefig("40*40_{}.png".format(i+1))



#Second cdf;pdf
a=pd.read_csv('1.csv')
a=a[3:].pivot("SrcIP","DstIP","RTT")
c=(a.pop("10.2.96.51"))
t=[]
for i in c:
    t.append(i)


x=t
ax0=plt.subplot(2,2,3)
ax0.hist(x, 20, normed=1, histtype='bar', facecolor='yellowgreen', alpha=0.75)
ax0.set_title('Server{n}_pdf'.format(n="10.2.96.51"))
ax1=plt.subplot(2,2,4)
ax1.hist(x, 20, normed=1, histtype='bar', facecolor='pink',rwidth=1, cumulative=True,alpha=0.75)
ax1.set_title('Server{n}_cdf'.format(n="10.2.96.51"))
ecdf=sm.distributions.ECDF(x)
z=np.linspace(min(x),max(x))
y=ecdf(z)
plt.step(z,y)


plt.show()

