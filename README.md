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
| :--- | :----: | 
| 1 |定义数据格式Log   |
| 2    | 实现python pingmesh10v10可视化 +latency cdf图     |
| 3 | 实现Python pingmesh40V40可视化        |
| 4 |构造自动生成数据程序          |

[✅latency可视化](https://queue.acm.org/detail.cfm?id=1809426)
[✅Seaborn教程](https://python-graph-gallery.com/91-customize-seaborn-heatmap/ )
[✅Seaborn颜色调整](https://seaborn.pydata.org/tutorial/color_palettes.html#building-color-palettes)


### 2018/04/11:
* pingagent -> 1.0 [socket server client ping each other on localhost](/pingagent_socket/version1/client.cpp), my first c++ ⁄(⁄ ⁄•⁄ω⁄•⁄ ⁄)⁄

### 2018/04/12:
* pingagent.socket 
*  ->[version1 本地1V1手动](/pingagent_socket/version1/)
*  ->[version2 自动1V1服务器](/pingagent_socket/version2/)
*  ->[version3 服务器1V1自动计时打印IP](/pingagent_socket/version3/)

### 2018/04/13:
* pingagent.socket
* ->[version4 服务器1v1自动保存日志](/pingagent_socket/version4/)
* ->[version5 shell自动打印ping的rtt: nc ping hping](/pingagent_socket/version5/)

### 2018/04/16:
* pingagent.socket
* ->[version6 shell 自动获取日志](/pingagent_socket/version6/)
* ->[version7 得到json日志](/pingagent_socket/version7/)
* ->[version8 服务器1vn 多链接](/pingagent_socket/version8/)
* ->[version9 服务器1vn 保存json日志](/pingagent_socket/version9/)
* ->[version10 服务器1vn 3s请求自动发送 保存日志](/pingagent_socket/version10/)

### 2018/04/17:
* pingagent.socket
* ->[version11 完成一个shell 在服务器后台运行一次 一体化保存数据](/pingagent_socket/version11/)

### 2018/04/19:
* pingagent.socket
* ->[version12 初始demo完成,shell联通,C++PING,python画图一体化，以两个server为例](/pingagent_socket/version12/)
