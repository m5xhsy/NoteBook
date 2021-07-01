# Redis

redis是一个key-value存储系统。和Memcached类似，它支持存储的value类型相对更多，包括string(字符串)、list(链表)、set(集合)、zset(sorted set --有序集合)和hash（哈希类型）。这些数据类型都支持push/pop、add/remove及取交集并集和差集及更丰富的操作，而且这些操作都是原子性的。在此基础上，redis支持各种不同方式的排序。与memcached一样，为了保证效率，数据都是缓存在内存中。区别的是redis会周期性的把更新的数据写入磁盘或者把修改操作写入追加的记录文件，并且在此基础上实现了master-slave(主从)同步。

## 下载安装

### Windows

```
https://github.com/microsoftarchive/redis/releases/tag/win-3.0.503
```

下载msi格式安装，在windows服务里面重启，可以添加环境变量

### Linux

```shell
$ wget http://download.redis.io/releases/redis-6.0.8.tar.gz
$ tar xzf redis-6.0.8.tar.gz -C /opt
$ cd /opt/redis-6.0.8
$ make && make install
或者
$ yum install redis
```

## redis启动

### 启动服务

```shell
$ redis-server		
```

### 启动客户端

```shell
$ redis-cli -h 127.0.0.1 -p 6379 -a Ass078678
或者
$ redis-cli -h 127.0.0.1 -p 6379
> auth Ass078678
```

## 设置密码

设置密码有两种方式。

### 命令行设置

1. 运行cmd切换到redis根目录，先启动服务端

   ```shell
   $ redis-server
   ```

2. 另开一个cmd切换到redis根目录，启动客户端

   ```shell
   $ redis-cli -h 127.0.0.1 -p 6379
   ```

3. 客户端使用config get requirepass命令查看密码

   ```redis
   > config get requirepass
   1)"requirepass"
   2)""    //默认空
   ```

4. 客户端使用config set requirepass yourpassword命令设置密码

   ```shell
   > config set requirepass 123456
   ```

5. 一旦设置密码，必须先验证通过密码，否则所有操作不可用

   ```shell
   >config get requirepass
   (error)NOAUTH Authentication required
   ```

   命令行设置的密码在服务重启后失效，所以一般不使用这种方式。

### 配置文件设置

#### Window

1. 在redis根目录下找到redis.windows.conf配置文件，搜索requirepass，找到注释密码行，添加密码如下：

   ```shell
   # requirepass foobared
   requirepass Ass078678    //注意，行前不能有空格
   ```

2. 重启服务后，客户端重新登录后发现密码还是空？

   ```shell
   >config get requirepass
   1)"requirepass"
   2)""
   ```

3. 网上查询后的办法：创建redis-server.exe 的快捷方式， 右键快捷方式属性，在目标后面增加redis.windows.conf， 这里就是关键，你虽然修改了.conf文件，但是exe却没有使用这个conf，所以我们需要手动指定一下exe按照修改后的conf运行，就OK了。所以，这里我再一次重启redis服务(指定配置文件)

   ```shell
   $ redis-server redis.windows.conf		# 未添加环境变量需要指定文件夹
   ```

4. 客户端再重新登录，OK了。

   ```shell
   $ redis-cli -h 127.0.0.1 -p 6379 -a 123456
   >config get requirepass
   1)"requirepass"
   2)"123456"
   ```

#### Linux

1. redis解压包里找到redis.conf文件

   ```shell
   $ vim /opt/redis-6.0.8/redis.conf
   ```

2. 搜索requirepass行                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         

   ```shell
   # requirepass foobared
   requirepass Ass078678    //注意，行前不能有空格
   ```

3. 此时修改网不能直接使用redis-server

   ```shell
   $ redis-server /opt/redis-6.0.8/redis.conf				# 使用redis-server加配置文件
   或者
   $ echo "alias redis-server='redis-server /opt/redis-6.0.8/redis.conf'" >> /etc/bashrc # 取别名方法
   ```

4. 配置文件其他配置

   ```shell
   bind 127.0.0.1  							# 绑定ip，如需要远程访问，需要填写服务器ip 0.0.0.0
   port 6363									# 端口，redis启动端口
   daemonize yes								# 守护进程方式运行
   dbfilename dump.rdb							# rdb数据文件
   dir /var/lib/redis/							# 数据文件存放路径
   logfile /var/log/redis/redis-server.log		# 日志文件
   slaveof										# 主从复制
   
   补充:
   ################################## NETWORK #####################################
   bind 127.0.0.1 #绑定的ip
   protected-mode yes #保护模式
   port 6379 #端口
   
   ################################# GENERAL #####################################
   daemonize yes #后台运行, 默认是no
   pidfile /var/run/redis_6379.pid #后台运行时需要的pid文件
   
   # 日志级别
   # Specify the server verbosity level.
   # This can be one of:
   # debug (a lot of information, useful for development/testing)
   # verbose (many rarely useful info, but not a mess like the debug level)
   # notice (moderately verbose, what you want in production probably)
   # warning (only very important / critical messages are logged)
   loglevel notice
   logfile "" #日志的文件名
   
   databases 16 #默认数据库的数量
   
   ################################ SNAPSHOTTING  ################################
   # rdb持久化规则
   save 900 1 #在900秒内, 至少有1个key发生了变动, 则进行持久化操作
   save 300 10
   save 60 10000
   
   stop-writes-on-bgsave-error yes #持久化失败后, 是否继续工作
   
   rdbcompression yes #是否压缩rdb文件
   rdbchecksum yes #保存rdb文件时, 是否校验
   rdb-del-sync-files no #rdb文件是否删除同步锁
   dir ./ #drb文件保存目录
   
   ################################## SECURITY ###################################
   requirepass 123456 #设置密码, 默认无
   
   ############################## MEMORY MANAGEMENT ################################
   # 在内存达到上限后的处理策略
   # volatile-lru：只对设置了过期时间的key进行LRU
   # allkeys-lru ： 删除lru算法的key   
   # volatile-random：随机删除即将过期key   
   # allkeys-random：随机删除   
   # volatile-ttl ： 删除即将过期的   
   # noeviction ： 永不过期，返回错误
   #maxmemory-policy noeviction 默认是noeviction
   
   ############################## APPEND ONLY MODE ###############################
   # aof持久化规则
   appendonly no #是否开启, 默认持久化方式为rdb
   appendfilename "appendonly.aof" #aof文件名
   
   # appendfsync always #每次修改同步一次
   appendfsync everysec #每秒同步一次
   # appendfsync no #从不
   ```

## 发布订阅

1. 发布者

   ```redis
   > PUBLISH 频道名 信息		# 发布消息
   ```

2. 订阅者

   ```redis
   > SUBSCRIBE 频道名			 # 订阅频道
   > PSUBSCRIBE 频道名*		 # 订阅所有能匹配上频道*的			
   ```

3. 频道

## 持久化

RDB和AOF同时开启只会同步AOF

### RDB持久化

```shell
$ vim /opt/redis-6.0.8/redis.conf 		 	# 配置文件

dbfilename dump.rdb							# rdb数据文件
dir /var/lib/redis/							# 数据保存位置

save 900 1									# 900秒1条操作
save 300 10									# 300秒10条操作
save 60 10000								# 60秒10000条操作
```

### AOF持久化

```shell
$ vim /opt/redis-6.0.8/redis.conf 		 	# 配置文件

appendonly yes								# 开启AOF
appendfilename "appendonly.aof"				# 保存路径
appendfsync  always    						# 总是修改类的操作
             everysec   					# 每秒做一次持久化
             no     						# 依赖于系统自带的缓存大小机制
```

### 不重启切换RDB到AOF

1. 备份RDB数据

   ```shell
   $ cp /data/redis/dump.rdb /data/redis/dump.1.rdb
   ```

2. 执行命令临时开启AOF关闭RDB

   ```shell
   > config set appendonly yes  	 #开启AOF功能
   > config set save ""  			#关闭RDB功能
   ```

3. 修改配置永久生效

   ```shell
   vim /opt/redis-6.0.8/redis.conf
   ##########	其他配置参考前面
   appendonly yes
   save ""				
   ```

4. 验证数据完整性

## 主从复制

### 主从配置

1. 进入文件夹

   ```shell
   $ cd /opt/redis-6.0.8/					
   ```

2. 批量创建配置文件

   ```shell
   $ touch redis-{6079..6381}.conf
   ```

3. 编辑主库配置文件

   ```shell
   $ vim redis-6079.conf					
   #############
   port 6379
   daemonize yes
   pidfile /data/redis/6379/redis.pid
   loglevel notice
   logfile "/data/redis/6379/redis.log"
   dbfilename dump.rdb
   dir /data/redis/6381
   protected-mode no
   ```

4. 编辑从库配置文件

   ```shell
   $ sed "s/6379/6380/g" redis-6079.conf > redis-6080.conf && echo "slaveof 127.0.0.1 6379" >> redis-6080.conf	
   $ sed "s/6379/6381/g" redis-6079.conf > redis-6081.conf && echo "slaveof 127.0.0.1 6379" >> redis-6081.conf
   ## "slaveof 127.0.0.1 6379"指向主库
   ```

5. 启动所有redis并测试

   ```shell
   $ redis-server /opt/redis-6.0.8/redis-6379.conf
   $ redis-server /opt/redis-6.0.8/redis-6380.conf
   $ redis-server /opt/redis-6.0.8/redis-6381.conf
   # 开启主从配置后从库只能读，不能写(可用做读写分离)
   ```

6. 查看主从库信息

   ```shell
   $ redis-cli -p 6379 info Replication
   # Replication#########################
   role:master
   connected_slaves:2
   slave0:ip=127.0.0.1,port=6380,state=online,offset=252,lag=1
   slave1:ip=127.0.0.1,port=6381,state=online,offset=252,lag=0
   master_replid:f8863d3d3f76da1e1f7bf919661835aa11ed6d45
   master_replid2:0000000000000000000000000000000000000000
   master_repl_offset:252
   second_repl_offset:-1
   repl_backlog_active:1
   repl_backlog_size:1048576
   repl_backlog_first_byte_offset:1
   repl_backlog_histlen:252
   
   $ redis-cli -p 6380 info Replication
   # Replication#########################
   role:slave
   master_host:127.0.0.1
   master_port:6379
   master_link_status:up
   master_last_io_seconds_ago:9
   master_sync_in_progress:0
   slave_repl_offset:252
   slave_priority:100
   slave_read_only:1
   connected_slaves:0
   master_replid:f8863d3d3f76da1e1f7bf919661835aa11ed6d45
   master_replid2:0000000000000000000000000000000000000000
   master_repl_offset:252
   second_repl_offset:-1
   repl_backlog_active:1
   repl_backlog_size:1048576
   repl_backlog_first_byte_offset:1
   repl_backlog_histlen:252
   
   $ redis-cli -p 6381 info Replication
   # Replication#########################
   role:slave
   master_host:127.0.0.1
   master_port:6379
   master_link_status:up
   master_last_io_seconds_ago:1
   master_sync_in_progress:0
   slave_repl_offset:266
   slave_priority:100
   slave_read_only:1
   connected_slaves:0
   master_replid:f8863d3d3f76da1e1f7bf919661835aa11ed6d45
   master_replid2:0000000000000000000000000000000000000000
   master_repl_offset:266
   second_repl_offset:-1
   repl_backlog_active:1
   repl_backlog_size:1048576
   repl_backlog_first_byte_offset:1
   repl_backlog_histlen:266
   ```

   

### 主库故障

#### 手动切换

1. 杀死主库6379模拟故障

2. 登录6380，去除从库身份

   ```shell
   $ slaoveof no one
   ```

3. 登录6381，生成新的从库身份

   ```shell
   $ slaveof 127.0.0.1 6381
   ```

4. 测试新的主从测试数据同步

#### redis哨兵.

> 保护redis主从集群正常运转，当主库挂掉后，自动的在从库中挑选新的主库，并修改配置文件
>
> 如果之前主库重启，会自动变成从库，并自动修改配置文件

1. 准备3个redis数据库

2. 进入文件夹

   ```shell
   $ cd /opt/redis-6.0.8/
   ```

3. 准备3个哨兵配置文件

   ```shell
   $ touch redis-sentinel-{26379..26381}.conf
   ```

4. 编辑配置文件

   ```shell
   $ vim redis-sentinel-26379.conf
   //######################################
   // Sentinel节点的端口
   port 26379  
   dir /data/redis/data/
   logfile "26379.log"
   daemonize yes
   // 当前Sentinel节点监控 192.168.119.10:6379 这个主节点
   // 2代表判断主节点失败至少需要2个Sentinel节点同意
   // mymaster是主节点的别名
   sentinel monitor mymaster 127.0.0.1 6379 2
   
   //每个Sentinel节点都要定期PING命令来判断Redis数据节点和其余Sentinel节点是否可达，如果超过30000毫秒30s且没有回复，则判定不可达
   sentinel down-after-milliseconds mymaster 30000
   
   //当Sentinel节点集合对主节点故障判定达成一致时，Sentinel领导者节点会做故障转移操作，选出新的主节点，原来的从节点会向新的主节点发起复制操作，限制每次向新的主节点发起复制操作的从节点个数为1
   sentinel parallel-syncs mymaster 1
   
   //故障转移超时时间为180000毫秒
   sentinel failover-timeout mymaster 180000
   ```

5. 配置好其他俩个文件夹

   ```shell
   $ sed "s/26379/26380/g" redis-sentinel-26379.conf > redis-sentinel-26380.conf 
   $ sed "s/26379/26380/g" redis-sentinel-26379.conf > redis-sentinel-26381.conf 
   ```

6. 启动哨兵

   ```shell
   $ redis-sentinel /opt/redis-6.0.8/redis-sentinel-26379.conf
   $ redis-sentinel /opt/redis-6.0.8/redis-sentinel-26380.conf
   $ redis-sentinel /opt/redis-6.0.8/redis-sentinel-26381.conf
   ```

7. 查看状态

   ```shell
   [root@localhost ~]#redis-cli -p 26379 info Sentinel
   # Sentinel
   sentinel_masters:1
   sentinel_tilt:0
   sentinel_running_scripts:0
   sentinel_scripts_queue_length:0
   sentinel_simulate_failure_flags:0
   master0:name=mymaster,status=ok,address=127.0.0.1:6379,slaves=2,sentinels=3
   [root@localhost ~]#redis-cli -p 26380 info Sentinel
   # Sentinel
   sentinel_masters:1
   sentinel_tilt:0
   sentinel_running_scripts:0
   sentinel_scripts_queue_length:0
   sentinel_simulate_failure_flags:0
   master0:name=mymaster,status=ok,address=127.0.0.1:6379,slaves=2,sentinels=3
   [root@localhost ~]#redis-cli -p 26381 info Sentinel
   # Sentinel
   sentinel_masters:1
   sentinel_tilt:0
   sentinel_running_scripts:0
   sentinel_scripts_queue_length:0
   sentinel_simulate_failure_flags:0
   master0:name=mymaster,status=ok,address=127.0.0.1:6379,slaves=2,sentinels=3
   ```

   

## redis-cluster

> redis每秒可生成10万条数据但是如果业务需要每秒100万条数据呢？这时就有了redis-cluster官方3.0版本后的集群方案。redis3.0集群采用P2P模式，完全去中心化，将redis所有的key分成了16384个槽位，每个redis实例负责一部分slot，集群中的所有信息通过节点数据交换而更新。redis实例集群主要思想是将redis数据的key进行散列，通过hash函数特定的key会映射到指定的redis节点上。

### 使用方法

1. 创建6个配置文件

   ```shell
   $ cd /opt/redis/
   $ touch redis-{6379..6384}.conf
   ```

2. 写入配置文件

   ```shell
   $ vim redis-6379.conf
   #######################
   port 7000
   daemonize yes
   dir "/data/redis/6379"
   logfile "6379.log"
   dbfilename "dump-6379.rdb"
   cluster-enabled yes   #开启集群模式
   cluster-config-file nodes-6379.conf　　#集群内部的配置文件
   cluster-require-full-coverage no　#redis cluster需要16384个slot都正常的时候才能对外提供服务，换句话说，只要任何一个slot异常那么整个cluster不对外提供服务。 因此生产环境一般为no
   ```

3. 创建数据保存位置

   ```shell
   $ mkdir /data/redis/{6379..6380}
   ```

4. 配置其他文件

   ```shell
   $ sed "s/6379/6380/g" redis-6379.conf > redis-6380.conf
   $ sed "s/6379/6381/g" redis-6379.conf > redis-6381.conf
   $ sed "s/6379/6382/g" redis-6379.conf > redis-6382.conf
   $ sed "s/6379/6383/g" redis-6379.conf > redis-6383.conf
   $ sed "s/6379/6384/g" redis-6379.conf > redis-6384.conf
   ```

5. 启动redis服务

   ```shell
   $ redis-server redis-6379.conf
   $ redis-server redis-6380.conf
   $ redis-server redis-6381.conf
   $ redis-server redis-6382.conf
   $ redis-server redis-6383.conf
   $ redis-server redis-6384.conf
   ```

6. 检查服务启动

   ```shell
   $ netstat -tunlp|grep redis
   $ ps -ef|grep redis
   ```

7. 开启集群

   ```shell
   $ redis-cli --cluster create 127.0.0.1:6379 127.0.0.1:6380 127.0.0.1:6381 127.0.0.1:6382 127.0.0.1:6383 127.0.0.1:6384 --cluster-replicas 1
   # redis5.0以前是下载ruby用redis/src/redis-trib.rb开启的，现在是c语言写的，用redis-cli开启
   # 集群自动为6个redis分配主从状态
   ```

8. 查看集群状态

   ```shell
   redis-cli -p 6379 cluster info 
   redis-cli -p 6379 info replication
   redis-cli -p 6379 cluster nodes  					#等同于查看nodes-6379.conf文件节点信息
   redis-cli -p 6379 cluster nodes | grep master		# 集群主节点状态
   redis-cli -p 6379 cluster nodes | grep slave		# 集群从节点状态
   ```

9. 测试写入数据(登录要加 -c 表示集群模式)

   ```shell
   ## 根据key名算法处理后定向到某个节点中的槽位中
   $ redis-cli -c -p 6381				# 登录主节点6381	
   > set name m5xhsy					# 设置key-value
   -> Redirected to slot [3300] located at 127.0.0.1:6379		# 数据设置到6379的3300插槽
   $ redis-cli -c -p 6380				# 登录主节点6380
   > get name
   -> Redirected to slot [3300] located at 127.0.0.1:6379		# 数据从6379的3300插槽读取过来的
   "m5xhsy"
   ```

   

   