# Pingmesh reimplementation
Author: Yiqing Ma

## Log format
The log file consist of many lines, each line in log file is a json object and is formatted like below
```json
{"Host": "10.2.96.50", "Timestamp": 1523263580577352, "Num": 1, "Entries": [[Timestamp, SrcIP, SrcPort, DstIP, DstPort, Protocol, ProbingType, MsgLen, RTT, ErrCode], ...]}
```

For example
```json
{"Host":"10.2.96.50","Timestamp":1523263581577352,"Num":2,"Entries":[[1523263580577352,"10.2.96.50",11111,"10.2.96.51",22222,"tcp","tor",1024,201,0],[1523263580677352,"10.2.96.50",11111,"10.2.96.52",22223,"tcp","tor",0,158,0]]}
{"Host":"10.2.96.52","Timestamp":1523263582123455,"Num":1,"Entries":[[1523263580577353,"10.2.96.52",33333,"10.2.96.50",44444,"tcp","tor",1024,199,0]]}
```

# 毕设参考文档及每日进展：

### 2018/04/10:
* visualize -> 2.0 [data generate and picture generate](/vis/new_python_generate_V2.0.py), [latency cdf and server picture](/vis/pingmesh.png)

| Series | Done | 
| :--- | :---- | 
| 1 |定义数据格式Log   |
| 2    | 实现python pingmesh10v10可视化 +latency cdf图     |
| 3 | 实现Python pingmesh40V40可视化        |
| 4 |构造自动生成数据程序          |

[✅latency可视化](https://queue.acm.org/detail.cfm?id=1809426)
[✅Seaborn教程](https://python-graph-gallery.com/91-customize-seaborn-heatmap/ )
[✅Seaborn颜色调整](https://seaborn.pydata.org/tutorial/color_palettes.html#building-color-palettes)


### 2018/04/11:
* pingagent -> 1.0 [socket server client ping each other on localhost](/pingagent_socket/version1/client.cpp), ⁄(⁄ ⁄•⁄ω⁄•⁄ ⁄)⁄

| Series | Done | 
| :--- | :---- | 
| 1 |第一个C++程序   |
| 2    | 实现socket 简易版通讯     |
| 3 | 实现socket 人机交互版通讯   |

[✅如何写Ping程序](https://blog.csdn.net/appleyuchi/article/details/78123752)
[✅Socket c++](http://c.biancheng.net/cpp/html/3029.html)



### 2018/04/12:
* pingagent.socket 
*  ->[version1 本地1V1手动](/pingagent_socket/version1/)
*  ->[version2 自动1V1服务器](/pingagent_socket/version2/)
*  ->[version3 服务器1V1自动计时打印IP](/pingagent_socket/version3/)

| Series | Done | 
| :--- | :---- | 
| 1 | 实现Server加个time的ping    |
| 2    | 实现两台服务器之间的ping     |
| 3 | 实现自动计时  |
| 4 | 得到log数据  |

[✅服务器配置](https://github.com/HKUST-SING/Equipment-SINGLab)
[✅两台服务器上ping](https://blog.csdn.net/u011353822/article/details/39370849)
[✅不同的服务器之间的跳转](http://linuxtools-rst.readthedocs.io/zh_CN/latest/tool/scp.html)
[✅socket+linux](https://www.kancloud.cn/wizardforcel/linux-c-book/134964)


### 2018/04/13:
* pingagent.socket
* ->[version4 服务器1v1自动保存日志](/pingagent_socket/version4/)
* ->[version5 shell自动打印ping的rtt: nc ping hping](/pingagent_socket/version5/)

| Series | Done | 
| :--- | :---- | 
| 1 | 完成log输出 Timestamp, SrcIP, SrcPort, DstIP, DstPort, Protocol, ProbingType, MsgLen, RTT, ErrCode   |
| 2    | 完成shell脚本/python模拟shell脚本，记录nc,ping的时间，得到baseline   |
| 3 | 参考goaccess做log文档直接分析可视化监控  |

[✅重要APUE.16 chapter](http://www.cnblogs.com/0xcafebabe/p/4478824.html)
[✅改用输出到printf](https://blog.csdn.net/u010368556/article/details/79182521)
[✅重要ping;nc文档](http://dbaplus.cn/blog-57-680-1.html)
[✅linux net 命令大全(好东西)](https://linux.cn/article-5461-1.html)
[✅Goaccess](https://goaccess.io/download#distro)
[✅nc命令构造http请求;重要](https://www.jianshu.com/p/84c374c48837)


### 2018/04/16:
* pingagent.socket
* ->[version6 shell 自动获取日志](/pingagent_socket/version6/)
* ->[version7 得到json日志](/pingagent_socket/version7/)
* ->[version8 服务器1vn 多链接](/pingagent_socket/version8/)
* ->[version9 服务器1vn 保存json日志](/pingagent_socket/version9/)
* ->[version10 服务器1vn 3s请求自动发送 保存日志](/pingagent_socket/version10/)

| Series | Done | 
| :--- | :---- | 
| 1 | json格式输出   |
| 2    | 改成:server ping 多次 client 多次 fork   |
| 3 | 改成文件储存版本，并且存到server端 |
| 4 |设定时间3S一发送 |

[✅C语言语法](https://www.kancloud.cn/digest/clearning/149690)
[✅Tcp server 1ping n client](https://blog.csdn.net/shine_journey/article/details/72641313)


### 2018/04/17:
* pingagent.socket
* ->[version11 完成一个shell 在服务器后台运行一次 一体化保存数据](/pingagent_socket/version11/)

| Series | Done | 
| :--- | :---- | 
| 1 | expect 和 spawn 和 key-generate 免除钥匙自动登录   |
| 2 | &实现后台操作的shell  |
| 3 | shell自动化操作 |

[✅如何写shell并行所有程序](https://www.zhihu.com/question/53122087)
[✅shell登录多台服务器](http://www.jb51.net/article/34250.htm)
[✅免密码](配置公共钥匙 https://broqiang.com/posts/30)
[✅自动输入密码](https://blog.csdn.net/zhangjikuan/article/details/51105166)
[✅expect 和 spawn自动登录](https://blog.csdn.net/donglynn/article/details/51536212)
[✅伪终端](http://www.cnblogs.com/wangcp-2014/p/6691445.html)
[✅argv](https://blog.csdn.net/eastmount/article/details/20413773)

### 2018/04/19:
* pingagent.socket
* ->[version12 初始demo完成,shell联通,C++PING,python画图一体化，以两个server为例](/pingagent_socket/version12/)

| Series | Done | 
| :--- | :---- | 
| 1 | 初始demo,shell读数据C++PING,python画图一体化，以两个server为例   |
| 2 | 读出文件到python;用json画图 |
| 3 | 写了clear.sh，调出了不对等的bug |

[✅python解析json文件](https://zhuanlan.zhihu.com/p/27917664)
