from pandas import DataFrame
import numpy as np
import random as rd
import seaborn as sns
import matplotlib.pyplot as plt
import statsmodels.api as sm
import json

a=[100,101]
d=[]
for i,j in enumerate(a):
    d.append([])
    with open('./'+str(j)+'/resultabcd.json',encoding='utf-8')as f: #./100/resultabc.json #./101/resultabc.json
        try:
            while True:
                fp = f.readline()
                c = json.loads(fp)
                d[i].append(c)
            else:
                break
        except:
            f.close()

print(d)

RTT=[]
SERVER=[]
CLIENT=[]
TIME=[]
for di in d:
    print(di)
    for i,j in enumerate(di):
        if di==d[0]:
            TIME.append([])
            SERVER.append([])
            CLIENT.append([])
            RTT.append([])
        else:
            print("添加数据")

        TIME[i].append(j['entries'][0][0]) #timestamp
        SERVER[i].append(j['entries'][0][1]) #server
        CLIENT[i].append(j['entries'][0][3]) #client
        RTT[i].append(j['entries'][0][-2]) #RTT
print(TIME,SERVER,CLIENT,RTT)

print(len(TIME))



#这里的i表示timestamp
i=int(input("你想画第几个时间段的图片："))

#for i in range(len(TIME)):
data={'time':TIME[i],'server':SERVER[i],'client':CLIENT[i],'rtt':RTT[i]}
df=DataFrame(data)
print(df)
b = df.pivot('server', 'client', 'rtt')
print(b)

plt.figure(str(TIME[i])+"pingmesh")
ax = plt.subplot(2, 1, 1)
# cmap = sns.cubehelix_palette(start = 1, rot = 3, gamma=0.8, as_cmap = True)
# vmin=0,vmax=40,robust=True
# YlGnBu
pic = sns.heatmap(b, vmin=-50, vmax=60, center=20, cmap='PiYG', annot=True, ax=ax, linewidths=1.5,
                  linecolor='white', annot_kws={"size": 7})
for text in pic.texts:
    text.set_size(7)
    if int(float(text.get_text())*100000) >int(50):
        text.set_size(12)
        text.set_weight('bold')
        text.set_style('italic')

# sns.heatmap(b,mask=b<40,ax=ax,cbar=False,annot=True,annot_kws={"weight": "bold","color":"blue","size":10})


ax.set_title('Pingmesh Heatmap'+str(TIME[i]))

ax.set_xlabel('Servername')
ax.set_ylabel('Servername')
# plt.savefig("40*40_{}.png".format(i+1))



# Second cdf;pdf
t=[]
for ii in range(len(RTT[0])):
    t .append([])
    for j in range(len(RTT)):
        t[ii].append(RTT[j][ii])
name=[]
for iii in range(len(SERVER[0])):
    name.append(SERVER[0][iii])
print(name)

m=int(input("请输入你想要的服务器的RTT图的序号序号:(0,1中选)"))
#for m in range(len(t)):

x = t[m]
ax0 = plt.subplot(2, 2, 3)
ax0.hist(x, 20, normed=1, histtype='bar', facecolor='lightgreen', alpha=0.5)
ax0.set_title('Server{n} pdf'.format(n=str(name[m])))
ax1 = plt.subplot(2, 2, 4)
ax1.hist(x, 20, normed=1, histtype='bar', facecolor='lightpink', alpha=0.5, rwidth=1, cumulative=True)
ax1.set_title('Server{n} cdf'.format(n=str(name[m])))
ecdf = sm.distributions.ECDF(x)
z = np.linspace(min(x), max(x))
y = ecdf(z)
plt.step(z, y, 'pink')
plt.show()


