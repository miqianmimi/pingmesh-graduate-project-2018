from pandas import DataFrame
import numpy as np
import random as rd
import seaborn as sns
import matplotlib.pyplot as plt
import statsmodels.api as sm
import json
from collections import defaultdict


a=open('pinglist.txt')
mmm=0
for i in a:
    mmm+=1
print(mmm)

li=[]
for i in range(mmm):
    li.append(i*(mmm-1)+1)
print(li)

RTT = []
SERVER = []
CLIENT = []
TIME = []
NUM = []
dictMerged={}
for m,n in enumerate(li):
    temp=[]
    with open('./'+"result/"+str(n)+'/resultabcd.json',encoding='utf-8')as f: #./100/resultabc.json #./101/resultabc.json
        try:
            while True:
                fp = f.readline()
                c = json.loads(fp)
                temp.append(c)
            else:
                break
        except:
            #print(temp)
            f.close()
            print("第%s个result已经处理"%n)
        for i in range(4*(mmm-1)):
            if i==0:
                #print("初始化")
                dictMerged = dict(temp[i])
                for i in dictMerged.items():
                    if i[0]!='entries':
                        dictMerged[str(i[0])]= [dictMerged[str(i[0])]]
                #print(dictMerged)

            else:
                for b in temp[i].items():
                    #print(b)
                    if b[0] != 'entries':
                        dictMerged[b[0]].append(b[1])
                    else:
                        dictMerged[b[0]].append(b[1][0])
                #print(dictMerged)

        #print(dictMerged)
        TIME.append([])
        SERVER.append([])
        CLIENT.append([])
        RTT.append([])
        NUM.append([])
        for i in dictMerged['num']:
            NUM[m].append(i)
        for di in dictMerged['entries']:
            TIME[m].append(di[0])  # timestamp
            SERVER[m].append(di[1])  # server
            CLIENT[m].append(di[3])  # client
            RTT[m].append(di[-2])  # RTT


        print(" ***********************  ***********************  ***********************  ***********************")
        print(" ***********************  ***********************  ***********************  ***********************")
        print(" ***********************  ***********************  ***********************  ***********************")


j=int(input("你想画第几个时间段的图片：CHOOSE FROM "+str(NUM[0][0])+","+str(NUM[0][mmm-1])+","+str(NUM[0][2*mmm-2])+","+str(NUM[0][3*mmm-3])+":  "))


NEWTIME=[]
NEWSERVER=[]
NEWCLIENT=[]
NEWRTT=[]
for p in range(mmm):
    for q in range(len(NUM[0])):
        if NUM[p][q]==j:
            NEWTIME.append(TIME[p][q])
            NEWSERVER.append (SERVER[p][q].split(".")[-1])
            NEWCLIENT.append (CLIENT[p][q].split(".")[-1])
            NEWRTT.append (RTT[p][q]*100000)


data={'time':NEWTIME,'server':NEWSERVER,'client':NEWCLIENT,'rtt':NEWRTT}
df=DataFrame(data)
print(df)
b = df.pivot('server', 'client', 'rtt')
print(b)

plt.figure(str(j)+"pingmesh")
ax = plt.subplot(2, 1, 1)
# cmap = sns.cubehelix_palette(start = 1, rot = 3, gamma=0.8, as_cmap = True)
# vmin=0,vmax=40,robust=True
# YlGnBu
#PIYG
#Paired_r

cc=sns.diverging_palette(148, 0, s=75, l=65, n=20,center='light',as_cmap=True)
#pic=sns.heatmap(b,vmin=0,vmax=60,cmap=cc,center=25,annot=True,ax=ax,linewidths=1.5, linecolor='white',annot_kws={"size":7})

pic = sns.heatmap(b, vmin=0, vmax=100, center=20, cmap='YlGnBu', annot=True, ax=ax, linewidths=1.5,linecolor='white', annot_kws={"size": 7})
for text in pic.texts:
    text.set_size(7)
    if int(float(text.get_text())) >int(50):
        text.set_size(12)
        text.set_weight('bold')
        text.set_style('italic')

# sns.heatmap(b,mask=b<40,ax=ax,cbar=False,annot=True,annot_kws={"weight": "bold","color":"blue","size":10})


ax.set_title('Pingmesh Heatmap rtt*10^-5')

ax.set_xlabel('Server_name')
ax.set_ylabel('Client_name')
# plt.savefig("40*40_{}.png".format(i+1))



# Second cdf;pdf


awk=int(input("请输入你想要的服务器的RTT图的序号序号:Choose From" +str(NEWSERVER[0])+","+str(NEWSERVER[mmm-1])+","+str(NEWSERVER[2*mmm-2])+","+str(NEWSERVER[3*mmm-3])+","+str(NEWSERVER[4*mmm-4])+","+str(NEWSERVER[5*mmm-5])+","+str(NEWSERVER[6*mmm-6])+","+str(NEWSERVER[7*mmm-7])+":   "))
t=[]
name=[]
for ii in range(len(SERVER)):
    for jj in range(len(SERVER[0])):
        print(SERVER[ii][jj])
        if SERVER[ii][jj] == "192.168.1."+str(awk):
            t.append(RTT[ii][jj]*100000)
            name.append(CLIENT[ii][jj])


print(t)


x = t
ax0 = plt.subplot(3, 2, 5)
ax0.hist(x, 20, normed=1, histtype='bar', facecolor='pink', alpha=0.6)
ax0.set_title('Server{n} pdf'.format(n=str('192.168.1.'+str(awk))))
ax1 = plt.subplot(3, 2, 6)
ax1.hist(x, 20, normed=1, histtype='bar', facecolor='lightblue', alpha=0.5, rwidth=1, cumulative=True)
ax1.set_title('Server{n} cdf'.format(n=str('192.168.1.'+str(awk))))
ecdf = sm.distributions.ECDF(x)
z = np.linspace(min(x), max(x))
y = ecdf(z)
plt.step(z, y, 'lightpink')
plt.show()


