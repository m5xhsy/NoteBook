# Mongodb

## 安装

### yum安装

1. ### 配置程序包管理系统（`yum`）

   创建一个`/etc/yum.repos.d/mongodb-org-4.4.repo`文件，以便您可以使用`yum`以下命令直接安装MongoDB ：

   ```
   [mongodb-org-4.4]
   name=MongoDB Repository
   baseurl=https://repo.mongodb.org/yum/redhat/$releasever/mongodb-org/4.4/x86_64/
   gpgcheck=1
   enabled=1
   gpgkey=https://www.mongodb.org/static/pgp/server-4.4.asc
   ```

2. ### 安装MongoDB软件包

   要安装最新的稳定版MongoDB，请发出以下命令：

   ```shell
   $ sudo yum install -y mongodb-org
   ```

   或者，要安装特定版本的MongoDB，请分别指定每个组件包，并将版本号附加到包名中，如以下示例所示：

   ```shell
   $ sudo yum install -y mongodb-org-4.4.1 mongodb-org-server-4.4.1 mongodb-org-shell-4.4.1 mongodb-org-mongos-4.4.1 mongodb-org-tools-4.4.1
   ```

### 直接安装

1. ###  官网找包

   ```shell
   https://www.mongodb.com/download-center#community
   ```

2. ### 下载tgz压缩包解压

   ```
   wget https://fastdl.mongodb.org/linux/mongodb-linux-x86_64-ubuntu1604-4.2.8.tgz    # 下载
   tar -zxvf mongodb-linux-x86_64-ubuntu1604-4.2.8.tgz                                    # 解压
   mv mongodb-src-r4.2.8  /opt/mongodb                          # 将解压包拷贝到指定目录
   ```

3. ### 将bin目录添加环境

   ```shell
   $ vim /etc/profile
   ######
   PATH=$PATH:/opt/mongodb/bin
   ######
   $ source /etc/profile
   ```

## Mongodb启动配置

```
--logpath 日志文件路径
--master 指定为主机器
--slave 指定为从机器
--source 指定主机器的IP地址
--pologSize 指定日志文件大小不超过64M.因为resync是非常操作量大且耗时，最好通过设置一个足够大的oplogSize来避免resync(默认的 oplog大小是空闲磁盘大小的5%)。
--logappend 日志文件末尾添加
--port 启用端口号
--fork 在后台运行
--only 指定只复制哪一个数据库
--slavedelay 指从复制检测的时间间隔
--auth 是否需要验证权限登录(用户名和密码)
 
 
-h [ --help ]             show this usage information
--version                 show version information
-f [ --config ] arg       configuration file specifying additional options
--port arg                specify port number
--bind_ip arg             local ip address to bind listener - all local ips
                           bound by default
-v [ --verbose ]          be more verbose (include multiple times for more
                           verbosity e.g. -vvvvv)
--dbpath arg (=/data/db/) directory for datafiles    指定数据存放目录
--quiet                   quieter output   静默模式
--logpath arg             file to send all output to instead of stdout   指定日志存放目录
--logappend               appnd to logpath instead of over-writing 指定日志是以追加还是以覆盖的方式写入日志文件
--fork                    fork server process   以创建子进程的方式运行
--cpu                     periodically show cpu and iowait utilization 周期性的显示cpu和io的使用情况
--noauth                  run without security 无认证模式运行
--auth                    run with security 认证模式运行
--objcheck                inspect client data for validity on receipt 检查客户端输入数据的有效性检查
--quota                   enable db quota management   开始数据库配额的管理
--quotaFiles arg          number of files allower per db, requires --quota 规定每个数据库允许的文件数
--appsrvpath arg          root directory for the babble app server 
--nocursors               diagnostic/debugging option 调试诊断选项
--nohints                 ignore query hints 忽略查询命中率
--nohttpinterface         disable http interface 关闭http接口，默认是28017
--noscripting             disable scripting engine 关闭脚本引擎
--noprealloc              disable data file preallocation 关闭数据库文件大小预分配
--smallfiles              use a smaller default file size 使用较小的默认文件大小
--nssize arg (=16)        .ns file size (in MB) for new databases 新数据库ns文件的默认大小
--diaglog arg             0=off 1=W 2=R 3=both 7=W+some reads 提供的方式，是只读，只写，还是读写都行，还是主要写+部分的读模式
--sysinfo                 print some diagnostic system information 打印系统诊断信息
--upgrade                 upgrade db if needed 如果需要就更新数据库
--repair                  run repair on all dbs 修复所有的数据库
--notablescan             do not allow table scans 不运行表扫描
--syncdelay arg (=60)     seconds between disk syncs (0 for never) 系统同步刷新磁盘的时间，默认是60s
 
Replication options:
--master              master mode 主复制模式
--slave               slave mode 从复制模式
--source arg          when slave: specify master as <server:port> 当为从时，指定主的地址和端口
--only arg            when slave: specify a single database to replicate 当为从时，指定需要从主复制的单一库
--pairwith arg        address of server to pair with
--arbiter arg         address of arbiter server 仲裁服务器，在主主中和pair中用到
--autoresync          automatically resync if slave data is stale 自动同步从的数据
--oplogSize arg       size limit (in MB) for op log 指定操作日志的大小
--opIdMem arg         size limit (in bytes) for in memory storage of op ids指定存储操作日志的内存大小
 
Sharding options:
--configsvr           declare this is a config db of a cluster 指定shard中的配置服务器
--shardsvr            declare this is a shard db of a cluster 指定shard服务器
```

其他配置参数含义

| --quiet                | # 安静输出                                                   |
| ---------------------- | ------------------------------------------------------------ |
| --port arg             | # 指定服务端口号，默认端口27017                              |
| --bind_ip arg          | # 绑定服务IP，若绑定127.0.0.1，则只能本机访问，不指定默认本地所有IP |
| --logpath arg          | # 指定MongoDB日志文件，注意是指定文件不是目录                |
| --logappend            | # 使用追加的方式写日志                                       |
| --pidfilepath arg      | # PID File 的完整路径，如果没有设置，则没有PID文件           |
| --keyFile arg          | # 集群的私钥的完整路径，只对于Replica Set 架构有效           |
| --unixSocketPrefix arg | # UNIX域套接字替代目录,(默认为 /tmp)                         |
| --fork                 | # 以守护进程的方式运行MongoDB，创建服务器进程                |
| --auth                 | # 启用验证                                                   |
| --cpu                  | # 定期显示CPU的CPU利用率和iowait                             |
| --dbpath arg           | # 指定数据库路径                                             |
| --diaglog arg          | # diaglog选项 0=off 1=W 2=R 3=both 7=W+some reads            |
| --directoryperdb       | # 设置每个数据库将被保存在一个单独的目录                     |
| --journal              | # 启用日志选项，MongoDB的数据操作将会写入到journal文件夹的文件里 |
| --journalOptions arg   | # 启用日志诊断选项                                           |
| --ipv6                 | # 启用IPv6选项                                               |
| --jsonp                | # 允许JSONP形式通过HTTP访问（有安全影响）                    |
| --maxConns arg         | # 最大同时连接数 默认2000                                    |
| --noauth               | # 不启用验证                                                 |
| --nohttpinterface      | # 关闭http接口，默认关闭27018端口访问                        |
| --noprealloc           | # 禁用数据文件预分配(往往影响性能)                           |
| --noscripting          | # 禁用脚本引擎                                               |
| --notablescan          | # 不允许表扫描                                               |
| --nounixsocket         | # 禁用Unix套接字监听                                         |
| --nssize arg (=16)     | # 设置信数据库.ns文件大小(MB)                                |
| --objcheck             | # 在收到客户数据,检查的有效性，                              |
| --profile arg          | # 档案参数 0=off 1=slow, 2=all                               |
| --quota                | # 限制每个数据库的文件数，设置默认为8                        |
| --quotaFiles arg       | # number of files allower per db, requires --quota           |
| --rest                 | # 开启简单的rest API                                         |
| --repair               | # 修复所有数据库run repair on all dbs                        |
| --repairpath arg       | # 修复库生成的文件的目录,默认为目录名称dbpath                |
| --slowms arg (=100)    | # value of slow for profile and console log                  |
| --smallfiles           | # 使用较小的默认文件                                         |
| --syncdelay arg (=60)  | # 数据写入磁盘的时间秒数(0=never,不推荐)                     |
| --sysinfo              | # 打印一些诊断系统信息                                       |
| --upgrade              | # 如果需要升级数据库                                         |

 Replicaton 参数

| --fastsync      | # 从一个dbpath里启用从库复制服务，该dbpath的数据库是主库的快照，可用于快速启用同步 |
| --------------- | ------------------------------------------------------------ |
| --autoresync    | # 如果从库与主库同步数据差得多，自动重新同步，               |
| --oplogSize arg | # 设置oplog的大小(MB)                                        |

主/从参数

| --master         | # 主库模式                   |
| ---------------- | ---------------------------- |
| --slave          | # 从库模式                   |
| --source arg     | # 从库 端口号                |
| --only arg       | # 指定单一的数据库复制       |
| --slavedelay arg | # 设置从库同步主库的延迟时间 |

 \* Replica set(副本集)选项：

| --replSet arg | # 设置副本集名称 |
| ------------- | ---------------- |
|               |                  |

 Sharding(分片)选项

| --configsvr      | # 声明这是一个集群的config服务,默认端口27019，默认目录/data/configdb |
| ---------------- | ------------------------------------------------------------ |
| --shardsvr       | # 声明这是一个集群的分片,默认端口27018                       |
| --noMoveParanoia | # 关闭偏执为moveChunk数据保存                                |

## 启动

- 数据存储目录：/var/lib/mongodb
- 日志文件目录：/var/log/mongodb

```shell
$ mongod --dbpath /var/lib/mongo --logpath /var/log/mongodb/mongod.log --fork
```

## 配置文件启动

进入bin的同级目录，建一个mongod.conf文件（编码格式为utf8无bom格式，否则会报错）作为mongodb的配置文件，内容如下

```shell
$ mongod -f mongo.conf  			# 配置文件方式启动

#数据库数据存放目录
dbpath=/usr/local/mongodb/data
#数据库日志存放目录
logpath=/usr/local/mongodb/logs/mongodb.log
#以追加的方式记录日志
logappend = true
#端口号 默认为27017
port=27017
#以后台方式运行进程
fork=true
#开启用户认证
auth=true
#关闭http接口，默认关闭http端口访问
#nohttpinterface=true
#mongodb所绑定的ip地址
#bind_ip = 127.0.0.1
#启用日志文件，默认启用
journal=true
#这个选项可以过滤掉一些无用的日志信息，若需要调试使用请设置为false
quiet=true
```

## 操作

### 数据库操作

```shell
use m5xhsy			# 切换或者创建数据库
db					# 查看当前使用数据库
show dbs			# 查看所有数据库
use m5xhsy			# 使用数据库
db.dropDatabase()	# 删除数据库
```

### 集合操作

```shell
# 创建集合
db.createCollection(name, { # name: 要创建的集合名称  参数二为可选参数, 指定有关内存大小及索引的选项
    capped : true, 			#  true，则创建固定集合，有着固定大小的集合，当达到最大值时，它会自动覆盖最早的文档。必须指定size
    autoIndexId : true, 	# 3.2 之后不再支持该参数。（可选）如为 true，自动在 _id 字段创建索引。默认为 false。
    size : 6142800, 		# 为固定集合指定一个最大值，即字节数。
    max : 10000 			# 指定固定集合中包含文档的最大数量。
})     	
									
# 查看集合
show collections

# 删除集合
db.collection.drop()		# collection为集合名称
```

### 增删改查操作

```shell
############ 插入数据 ############
db.user.insertOne({id:1,name:"m5xhsy"})
db.user.insertMany([{id:1,name:"m5xhsy"},{"id":2,name:"ass"}])

############ 删除数据 ############
db.user.remove({id:5})					 	# 删除所有匹配到的
db.user.remove({id:5},{justOne：true}) 	 	# 删除一条
# 3.2以后版本推荐
db.user.deleteOne({id:5})				# 删除一条
db.user.deleteMany({id:5})				# 删除多条

############ 修改数据 ############
db.collection.updateOne({id:1},{$set:{name:"xxx"}})
db.collection.updateMany({id:1},{$set:{name:"xxx"}})
# $修改器
db.collection.updateOne({id:1},{$unset:{name:"xxx"}})
db.collection.updateOne({id:1},{$push:{list:5}})			# list列表的最后添加元素
db.collection.updateOne({id:1},{$pull:{list:5}})			# list列表删除元素
db.collection.updateOne({id:1},{$pushAll:{list:[1,2,3]]}})	# list列表迭代添加原始
db.collection.updateOne({id:1},{$pop:{list:-1}})			# list列表删除第一个元素，-1为第一个，1为最后一个
db.collection.updateOne({list:5},{$set:{"list.$":6}})		# list列表中的5修改为6，其中list.$要用引号，只能改一个

 ############ 查找数据 ############
db.user.findOne()
db.user.find({}).skip(2).limit(5)  # 跳过2条查询五条
db.user.find({}).sort({age:-1})	# 反排序
如果三个都有，先排序，再跳过，最后选取+

# 且
db.user.find({id:1, name:"m5xhsy"})
# 或
db.user.find({$or:[{id:1}, {age:19}]})
# 子集
db.user.find({id:{$in:[5,6]}})
# 完全符合
db.user.find({list:{$all:[1,2,3]}}) # list列表完全符合[1,2,3]的
```

## 数据类型

```shell
Object  ID ：Documents 自生成的 _id

String： 字符串，必须是utf-8

Boolean：布尔值，true 或者false (这里有坑哦~在我们大Python中 True False 首字母大写)

Integer：整数 (Int32 Int64 你们就知道有个Int就行了,一般我们用Int32)

Double：浮点数 (没有float类型,所有小数都是Double)

Arrays：数组或者列表，多个值存储到一个键 (list哦,大Python中的List哦)

Object：如果你学过Python的话,那么这个概念特别好理解,就是Python中的字典,这个数据类型就是字典

Null：空数据类型 , 一个特殊的概念,None Null

Timestamp：时间戳

Date：存储当前日期或时间unix时间格式 
```





