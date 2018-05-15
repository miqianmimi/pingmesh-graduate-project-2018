# Pingmesh reimplementation
Author: Yiqing Ma

idea from: [郭传雄](https://www.youtube.com/watch?v=qPkQSH1iNqc) SIGCOMM

✅的表示参考文档，表格内是进展，* 后表示代码更新处 

## Log format:
The log file consist of many lines, each line in log file is a json object and is formatted like below
```json
{"Host": "10.2.96.50", "Timestamp": 1523263580577352,"Entries": ["timestamp", "src", "Dst", "protocol", "RTT"], ...]}
```

## Example:
result.json 
```json
{"host":"192.168.1.1","timestamp":1524502747,"num":1,"entries":[[1524502747,"192.168.1.1",8910,"192.168.1.41",8910,"tcp","tor",0,0.000823,0]]}
```
分成三块Json：

1.data.json 
```json
var data = {
"data":[
[[0, 0, 0], [0, 1, 82], [0, 2, 57], [0, 3, 74], [0, 4, 70], [0, 5, 66], [0, 6, 65], [0, 7, 64], [1, 0, 179]...]...]};
```
2.timestamp.json
```json
var timestamp = {
"timestamp":[[1524502747,1524502750,1524502753,1524502756]]};
```

3.server.json
```json
var server = {
"server":[["192.168.1.1","192.168.1.40","192.168.1.41","192.168.1.42","192.168.1.46","192.168.1.48","192.168.1.49","192.168.1.50"]]};
```


## 毕设参考文档及每日进展：

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
* pingagent.socket->[version11 完成一个shell 在服务器后台运行一次 一体化保存数据](/pingagent_socket/version11/)

| Series | Done | 
| :--- | :---- | 
| 1 | expect 和 spawn 和 key-generate 免除钥匙自动登录   |
| 2 | &实现后台操作的shell  |
| 3 | shell自动化操作 |

[✅如何写shell并行所有程序](https://www.zhihu.com/question/53122087)
[✅shell登录多台服务器](http://www.jb51.net/article/34250.htm)
[✅免密码配置公共钥匙]( https://broqiang.com/posts/30)
[✅自动输入密码](https://blog.csdn.net/zhangjikuan/article/details/51105166)
[✅expect 和 spawn自动登录](https://blog.csdn.net/donglynn/article/details/51536212)
[✅伪终端](http://www.cnblogs.com/wangcp-2014/p/6691445.html)
[✅argv](https://blog.csdn.net/eastmount/article/details/20413773)

### 2018/04/19:
* pingagent.socket->[version12 初始demo完成,shell联通,C++PING,python画图一体化，以两个server为例](/pingagent_socket/version12/)

| Series | Done | 
| :--- | :---- | 
| 1 | 初始demo,shell读数据C++PING,python画图一体化，以两个server为例   |
| 2 | 读文件到python;用json画图 |
| 3 | 写clear.sh，调出2个bug |

[✅python解析json文件](https://zhuanlan.zhihu.com/p/27917664)


## 第一版demo的操作指南

* 准备部分：
需要的文件在version12里面：bb.sh(main); clear.sh; s12.cpp; c12.cpp ;vis.py

* 代码部分：把这些文件全部放到v11内,运行下面部分代码，可以得到实时的ping的值，输入绘图参数，得到热力图和Latency_cdf结果 
```
ssh yiqing@192.168.2.254
cd pingmesh/v11
mkdir 100
mkdir 101
bash bb.sh
```
[✅APUE](http://www.apuebook.com/)
[✅经典必看 socket有关的编程项目](https://notes.shichao.io/unp/)

### 2018/04/21:
* pingagent.socket->[version13 修改为多个server](/pingagent_socket/version13/)

| Series | Done | 
| :--- | :---- | 
| 1 |  添加clearmy.sh，实现pingmesh之后复原工作  |
| 2 |  添加automatickey.sh，实现pingmesh自动配网关到服务器之间秘钥  |


### 2018/04/23:
* pingagent.socket->[version14 修改为任意n\*nserver之间的pingmesh系统](/pingagent_socket/version14/)

| Series | Done | 
| :--- | :---- | 
| 1 |  第二版demo,shell读数据，clean，key作用，C++PING,python画图一体化，以两个server为例 |
| 2 |  后台双向并行，使得同时获得同一时刻所有数据  |
| 3 |  根据pinglist中server个数，自动实现获取服务器两两ping的数据  |

[✅Linux如何读取文件保存到数组](https://fukun.org/archives/01282174.html)

## 第二版demo的操作指南

* 准备部分：
需要的文件在version13里面：main.sh; clearmy.sh;

* 代码部分：把这些文件全部放到v13内,运行下面部分代码，可以得到实时的ping的值 
```
ssh yiqing@143.89.191.114
cd pingmesh
bash main.sh
每次运行完毕后需要
bash clearmy.sh
```

* 结构图：
![Structure](https://github.com/miqianmimi/pingmesh-graduate-project-2018/blob/master/middle-result/%E7%BB%93%E6%9E%84%E5%9B%BE.png)
* 包含文件内容图
![Contain](https://github.com/miqianmimi/pingmesh-graduate-project-2018/blob/master/middle-result/%E6%89%80%E5%90%AB%E5%86%85%E5%AE%B9%E6%96%87%E4%BB%B6%E5%9B%BE.png)


### 2018/04/24:
* pingagent.socket ->[version14 配合画图实现一体化 N SERVER PING RESULT ](/pingagent_socket/version14/)

| Series | Done | 
| :--- | :---- | 
| 1 |  8*8 服务器server client； 4个Timestamp图 |
| 2 |  Python采用automatic动图；能够生成不同timestamp下的图  |
| 3 |  完成毕设中期进展，中期答辩PPT，demo2， 结构图，待提高  |

[✅python动图](https://zhuanlan.zhihu.com/p/31323002)
* 待提高点：
![Imrovement](https://github.com/miqianmimi/pingmesh-graduate-project-2018/blob/master/middle-result/%E5%BE%85%E6%8F%90%E9%AB%98.png)

### 2018/05/09:
* pingagent.socket ->[version15 将vis改成Echarts网页版 heatmap1 ](/pingagent_socket/version15/version1.png)

| Series | Done | 
| :--- | :---- | 
| 1 | 将vis改成html形式，Echarts添加服务器真实数据，画好heatmap |

[✅Echarts学习](http://echarts.baidu.com/echarts2/doc/start.html)
[✅Echarts timestamp](http://www.echartsjs.com/gallery/editor.html?c=scatter-life-expectancy-timeline)
[✅javascript 输出数据](http://www.runoob.com/js/js-output.html)

### 2018/05/10:
* pingagent.socket ->[version15 添加time轴，heatmap1 -> heatmap 2 ](/pingagent_socket/version15/version2.png)

| Series | Done | 
| :--- | :---- | 
| 1 | 将Echarts合并timestamp,可变动的pingmesh图 |

[✅html语言入门](http://www.w3school.com.cn/b.asp)
[✅Echarts文档](http://echarts.baidu.com/option.html#series-heatmap.data)
[✅Echarts TimeLine 教程](http://echarts.baidu.com/option.html#timeline)

### 2018/05/11:
* pingagent.socket ->[version15 添加vismap, heatmap 2 -> heatmap 3 ](/pingagent_socket/version15/version3.png)
* pingagent.socket ->[version15 添加涟漪特效, heatmap 3 -> heatmap 4 ](/pingagent_socket/version15/heatmap4.html)

| Series | Done | 
| :--- | :---- | 
| 1 | 改进vismap 彩色坐标标轴 |
| 2 | 添加涟漪特效：对于latency延误在前3位的数字 |
| 3 | 合并另一个Latency图 |

* 可视化新效果
![New Pingmesh visulization](https://github.com/miqianmimi/pingmesh-graduate-project-2018/blob/master/agent-con-dsa/version15/version4.png)

[✅Echarts高亮](http://echarts.baidu.com/option.html#calendar)
[✅网页切块](http://blog.51cto.com/wuwei5460/1324543)
[✅好看的分割线](https://blog.csdn.net/alex8046/article/details/51917069)
[✅画latency的图](http://echarts.baidu.com/examples/editor.html?c=candlestick-brush&theme=light)

### 2018/05/12:
* pingagent.socket ->[version15 添加Latency Bar, heatmap 4 -> heatmap 5 ](/pingagent_socket/version15/heatmap5.html)

| Series | Done | 
| :--- | :---- | 
| 1 | 正确显示latency	 |
| 2 | 添加zoom可缩放条+animation特效 |
| 3 | 合并两个container到一张图 |

* 可视化完整效果
![New Pingmesh visulization](https://github.com/miqianmimi/pingmesh-graduate-project-2018/blob/master/agent-con-dsa/version15/version5(2).png)

[✅多条线段](http://echarts.baidu.com/examples/editor.html?c=line-stack)
[✅分段色彩](http://echarts.baidu.com/examples/editor.html?c=line-aqi)
[✅ datazoom](http://echarts.baidu.com/option.html#dataZoom)
