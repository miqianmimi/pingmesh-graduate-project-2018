import numpy as np
import random
from numpy.linalg import cholesky
print(" ***********************  ***********************  ***********************  ***********************")
print(" ***********************  ***********************  ***********************  ***********************")
print(" ***********************  ***********************  ***********************  ***********************")

#initialize:
timestamp_how_many = 10 #1.
server_how_many = 100 #2.
sampleNo = (server_how_many) * (timestamp_how_many)
mu = 40
sigma = 1
mu1 = 78
sigma1 = 10
np.random.seed(0)
RTT = []
for i in range(server_how_many):
    RTT.append([])
    RTT[i] = np.random.normal(mu, sigma, sampleNo)

for i in range(server_how_many):
    if i == 10:
        RTT[i] =np.random.normal(mu1, sigma1, sampleNo)

for i in range(server_how_many):
    for j in range(server_how_many):
        for m in range(timestamp_how_many):
            if j == 10:
                RTT[i][j+(server_how_many - 1) *m] = random.randint(70,90)

for i in range(server_how_many):
    for j in range(server_how_many):
        for m in range(timestamp_how_many):
            if i == j :
                RTT[i][j+(server_how_many - 1) *m] =0



TIME = []
for i in range(timestamp_how_many):
    TIME.append("15245027"+str(random.randint(0,9))+str(random.randint(0,9)))


server=[]
for i in range(server_how_many):
    server.append("\"" + str(i) + "\"")

ans = []
for m in range(timestamp_how_many):
    ans.append([])

for m in range(timestamp_how_many):
    for i in range(len(RTT)):
        for j in range(server_how_many):
            ans[m].append([i, j, int(RTT[i][j + m * (server_how_many - 1) ])])


rtt=[]
for i in range(server_how_many):  # 100
    rtt.append([])
    for t in range(timestamp_how_many):  # 10
        for j in range(server_how_many):   # 100
            if j != i:
                rtt[i].append(ans[t][j + i * (server_how_many)][2])

rtt.append([])
for i in range(len(rtt[0])):
    sum = 0
    for j in range(len(rtt)-1):# 10
        sum += rtt[j][i]
    p = int(sum / (len(rtt) - 1))
    rtt[-1].append(p)



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
for i in range(timestamp_how_many):
    output3.write(str(TIME[i]))
    if i != timestamp_how_many - 1:
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
