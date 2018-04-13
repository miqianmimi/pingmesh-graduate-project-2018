# Pingmesh reimplementation
author:yiqingma
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

### 2018/04/10:
* visualize -> 2.0 [data generate and picture generate](new_python_generate_V2.0.py), [latency cdf and server picture](pingmesh.png)


### 2018/04/11:
* pingagent -> 1.0 [socket server client ping each other on localhost](client.cpp), my first c++ ⁄(⁄ ⁄•⁄ω⁄•⁄ ⁄)⁄

### 2018/04/12:
* pingagent.socket 
*  ->[version1 本地1V1手动](/pingagent_socket/version1/)
*  ->[version2 自动1V1服务器](/pingagent_socket/version2/)
*  ->[version3 服务器1V1自动计时打印IP](/pingagent_socket/version3/)

### 2018/04/13:
* pingagent.socket
* ->[version4 服务器1v1自动保存日志](/pingagent_socket/version4/)
* ->[version5 shell自动打印ping的rtt: nc ping hping](/pingagent_socket/version5/)
