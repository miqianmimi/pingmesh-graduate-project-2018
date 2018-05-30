import Tkinter as tk
import os
import paramiko
import sys
import subprocess
import shlex
import commands

# utf-8#utf-8#utf-8# utf-8#utf-8#utf-8
class UnicodeStreamFilter:
    def __init__(self, target):
        self.target = target
        self.encoding = 'utf-8'
        self.errors = 'replace'
        self.encode_to = self.target.encoding

    def write(self, s):
        if type(s) == str:
            s = s.decode("utf-8")
        s = s.encode(self.encode_to, self.errors).decode(self.encode_to)
        self.target.write(s)


if sys.stdout.encoding == 'cp936':
    sys.stdout = UnicodeStreamFilter(sys.stdout)
# utf-8#utf-8#utf-8# utf-8#utf-8#utf-8




window = tk.Tk()
window.title('Pingmesh system')
window.geometry('200x500')

# function:
def input_list():
    var = e.get()
    f = open(str(var)+'.txt')
    for i in f.readlines():
        j =i.split('\n')
        #print(j)
        t.insert('insert',j[0])
        t.insert('insert', '\n')

def send_automate_key():
    var = e.get()

    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect('143.89.191.114',username='yiqing',password='yiqing')
    cmd = 'cd pingmesh; bash automatekey.sh '+str(var)+'.txt'
    stdin, stdout, stderr = ssh.exec_command(cmd)
    for i in stdout.readlines():
        print (i)
    for j in stderr.readlines():
        print(j)
#    os.system('bash automatekey.sh pinglist.txt')
#    os.system('ssh yiqing@143.89.191.114 -tt')
#    os.system('bash automatekey.sh pinglist.txt')

def clear_my_env():
    var = e.get()
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect('143.89.191.114',username='yiqing',password='yiqing')
    cmd = 'cd pingmesh; bash clearmy.sh '+str(var)+'.txt'
    stdin, stdout, stderr = ssh.exec_command(cmd)
    for i in stdout.readlines():
        print (i)
    for j in stderr.readlines():
        print(j)

def test_pingmesh():
    var = e.get()
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect('143.89.191.114', username='yiqing', password='yiqing')
    cmd = 'cd pingmesh; bash main.sh ' + str(var) + '.txt'
    stdin, stdout, stderr = ssh.exec_command(cmd)
    for i in stdout.readlines():
        print (i)
    for j in stderr.readlines():
        print(j)

def take_back():
    print('start')
    a=os.popen('scp -r yiqing@143.89.191.114:/home/yiqing/pingmesh/result/ ~/Desktop/')
    print(a)
    c=os.popen('rm -rf result')
    print(c)
    b=os.popen('mv -f ~/Desktop/result/ ~/Desktop/Simple-Server-and-Chat-Program-master/Version17GUI_tkinter/')
    print(b)
    print('result is back to local_dir')
    print('end')


def draw_pic():
    print('start')
    a = os.popen('python json2html.py')
    print(a)
    b = os.popen('open heatmap5.html')
    print('result is back to local_dir')
    print('end')



# button # for input the pinglist
b1 = tk.Button(window,text = 'show ping_list',command = input_list)
b1.pack()

b2 = tk.Button(window,text = 'send automate_key',command = send_automate_key)
b2.pack()

b3 = tk.Button(window,text = 'clear my environment',command = clear_my_env)
b3.pack()

b4 = tk.Button(window,text = 'Test pingmesh ',command = test_pingmesh)
b4.pack()

b5 = tk.Button(window,text = 'take back result',command = take_back)
b5.pack()

b6 = tk.Button(window,text = 'draw heatmap',command = draw_pic)
b6.pack()
#  Radiobutton()



# Entry # for pinglist input
e = tk.Entry(window,text='please input the server list',show=None,width=15)
e.pack()

# Text #for pinglist display
t = tk.Text(window,height=10)
t.pack()

window.mainloop()
