from pandas import DataFrame
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import statsmodels.api as sm
import json
import sys
from matplotlib.animation import FuncAnimation
from collections import defaultdict
import random as rd



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





def printheat():
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

    TT=NEWTIME[0]
    data={'time':NEWTIME,'server':NEWSERVER,'client':NEWCLIENT,'rtt':NEWRTT}
    df=DataFrame(data)
    print(df)
    b = df.pivot('server', 'client', 'rtt')
    print(b)

    plt.figure(str(j)+"pingmesh",figsize=(10,8))

    ax = plt.subplot(2, 1, 1)


    # cmap = sns.cubehelix_palette(start = 1, rot = 3, gamma=0.8, as_cmap = True)
    # vmin=0,vmax=40,robust=True
    # YlGnBu
    #PIYG
    #Paired_r

    #cc=sns.diverging_palette(148, 0, s=75, l=65, n=20,center='light',as_cmap=True)
    #pic=sns.heatmap(b,vmin=0,vmax=60,cmap=cc,center=25,annot=True,ax=ax,linewidths=1.5, linecolor='white',annot_kws={"size":7})

    pic = sns.heatmap(b, vmin=0, vmax=120, center=23, cmap='YlGnBu', annot=True, ax=ax, linewidths=1.5,linecolor='white', annot_kws={"size": 7})

    for text in pic.texts:
        text.set_size(11)
        if int(float(text.get_text())) >int(50):
            text.set_size(13)
            text.set_weight('bold')
            text.set_style('italic')

    # sns.heatmap(b,mask=b<40,ax=ax,cbar=False,annot=True,annot_kws={"weight": "bold","color":"blue","size":10})

    ax.set_title('Pingmesh Heatmap timestamp: %s' % TT,fontsize=15)
    #ax.set_xticklabels(ax.get_xticklabels(), rotation=-90)
    #1ax.xaxis.tick_top()
    ax.set_xlabel('Server_name',fontsize=10)
    ax.set_ylabel('Client_name',fontsize=10)
    # plt.savefig("40*40_{}.png".format(i+1))


def printcdf():

    # Second cdf;pdf
    a=open('pinglist.txt')
    t = []
    for l in range(mmm):
        awk=SERVER[l][0]
        t.append([])
        for ii in range(len(SERVER)):
            for jj in range(len(SERVER[0])):
                print(SERVER[ii][jj] == awk)
                if SERVER[ii][jj] == awk:
                    t[l].append(RTT[ii][jj]*100000)
    print(t)
    x=[]
    for j in range(len(t[0])):
        sum=0
        for i in range(mmm):
            sum=sum+t[i][j]
        sum=sum/mmm
        x.append((float)(round(sum*100))/100)


    print(len(x))


    ax0 = plt.subplot(2,2,3)
    ax0.set_title('Server{n} pdf'.format(n=str('_average')))
    sns.distplot(x,bins=20, rug=True,color='lightgreen')
    plt.grid(True)


    ax1 = plt.subplot(2,2,4)
    ax1.hist(x, 20, normed=1, histtype='bar', facecolor='lightpink', alpha=0.5, rwidth=1, cumulative=True)
    ax1.set_title('Server{n} cdf'.format(n=str('_average')))
    ecdf = sm.distributions.ECDF(x)
    z = np.linspace(min(x), max(x))
    y = ecdf(z)
    plt.step(z, y, 'lightpink')
    plt.grid(True)
    plt.twinx()


plt.close()  # clf() # 清图 cla() # 清坐标轴 close() # 关窗口
#fig = plt.figure(figsize=(10,10)) # 设置图像显示的时候XY轴比例

plt.ion()  # interactive mode on

print('开始仿真')
try:
    for i in range(4):
        # 障碍物船只轨迹
        printheat()
        printcdf()

        plt.pause(2)
        plt.clf()
except Exception as err:
    print(err)




