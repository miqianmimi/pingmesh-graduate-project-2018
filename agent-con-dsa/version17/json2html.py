import json


a = open('pinglist.txt')
server_how_many = 0
for i in a:
    server_how_many += 1
print(server_how_many)

li = []
for i in range(server_how_many):
    li.append(i*(server_how_many-1)+1)
print(li)

RTT = []
SERVER = []
CLIENT = []
TIME = []
NUM = []
dictMerged = {}
for m,n in enumerate(li):
    temp = []
    with open('./'+"result/"+str(n)+'/resultabcd.json')as f:#,encoding='utf-8'
        try:
            while True:
                fp = f.readline()
                c = json.loads(fp)
                temp.append(c)
            else:
                break
        except:
            # print(temp)
            f.close()
            print("%s result ok" % n)
        for i in range(4 * (server_how_many - 1)):  # timestamp = 4!
            if i == 0:
                dictMerged = dict(temp[i])
                for i in dictMerged.items():
                    if i[0] != 'entries':
                        dictMerged[str(i[0])] = [dictMerged[str(i[0])]]
            else:
                for b in temp[i].items():
                    if b[0] != 'entries':
                        dictMerged[b[0]].append(b[1])
                    else:
                        dictMerged[b[0]].append(b[1][0])
        # print(dictMerged)
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

print(len(TIME[0]))
print(TIME[1])
print(TIME[2])
print(TIME[3])
print(server_how_many )
# what i want now : first a data.json (RTT) second a server.json (SERVER NAME) last a timestamp.json( TIME STAMP ) the add one is the rtt.json(rtt)


server=[]
for i in range(len(SERVER)):
    server.append("\""+str(SERVER[i][0])+"\"")


timestamp_how_many = int(len(RTT[0]) / (server_how_many - 1))
ans = []
for m in range(timestamp_how_many):
    ans.append([])

for m in range(timestamp_how_many):
    for i in range(len(RTT)):
        count = 0
        #import pdb; pdb.set_trace()
        for j in range(server_how_many):
            if i == j :
                ans[m].append([i,j,0])
                j = j + 1
                count = 1
            else :
                ans[m].append([i, j, int( 100000 * RTT[i][j + m * (server_how_many - 1) - count])])
#print(ans)
#print(len(ans[0]))
rtt=[]

for i in range(server_how_many): #8
    rtt.append ([])
    for t in range(len(ans)): #4
        for j in range(server_how_many):
            if j != i:
                rtt[i].append(ans[t][j + i * (server_how_many)][2])

rtt.append([])
for i in range(len(rtt[0])):
    sum = 0
    for j in range(len(rtt)-1):# 1,2,3,4,5,6,7,8
        sum += rtt[j][i]
    p = int(sum / (len(rtt) - 1))
    rtt[-1].append(p)

print(rtt[-1])

#for i in range(int(len(TIME[0])/(server_how_many - 1))):
#    b = 0
#    for j in range(len(ans[i])):
#        b = b + ans[i][j][2]
#        a = int(b/(len(ans[0])-server_how_many))
#    rtt[-1].append(a)

output = open('/tmp/server.json', 'w')
output.write("var server = ")
output.write("{\n")
output.write("\"server\":[\n")
output.write("[")

for i in range(len(server)):
    output.write(str(server[i]))
    if i != len(server) - 1:
        output.write(",")
output.write("]")
output.write('\n')
output.write("]")
output.write('\n')
output.write("};")
output.close()


output2 = open('/tmp/data.json', 'w')
output2.write("var data = {\n")

output2.write("\"data\":[\n")
for i in range(len(ans)):
    output2.write(str(ans[i]))
    if i != len(ans) - 1:
        output2.write(',\n')
output2.write("\n")
output2.write("]\n")
output2.write("};")

output2.close()


output3 = open('/tmp/timestamp.json','w')
output3.write("var timestamp = {\n")
output3.write("\"timestamp\":[\n ")
output3.write("[")
for i in range(int(len(TIME[0])/(server_how_many-1))):
    output3.write(str(TIME[0][i*(server_how_many-1)]))
    if i != len(TIME[0])/(server_how_many-1) - 1:
        output3.write(",")
output3.write("]")
output3.write('\n')
output3.write("]")
output3.write('\n')
output3.write("};")
output3.close()

output4 = open('/tmp/rttaverage.json','w')
output4.write("var rtt = {\n")
output4.write("\"rtt\":[\n ")
for i in range(len(rtt)):
    output4.write(str(rtt[i]))
    if i != len(rtt) - 1:
        output4.write(',\n')
output4.write("\n")
output4.write("]\n")
output4.write("};")
output4.close()


print(" ")
print(" ")
print(" ***********************  data prepare for pic over ************************")