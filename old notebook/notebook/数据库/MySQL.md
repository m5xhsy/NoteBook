# MySQL

## 安装MySQL

- CentOS 8安装mariadb

```shell
$ yum install -y mariadb-server			# 安装mariadb数据库服务
$ systemctl start mariadb.service		# 启动服务
$ systemctl enable mariadb.service		# 设置开机自启动
$ mysql -u root -p -h 192.168.239.128	# 连接MySQL  (-h为远程连接)
```

- 如果配置的源安装版本过低，则配置官方源安装

  - 配置mariadb官方yum源(baseurl去http://yum.mariadb.org/找合适版本的)

    ```shell
    $ tee /etc/yum.repos.d/mariadb.repo <<-'EOF'
    [mariadb]
    name = MariaDB
    baseurl = http://yum.mariadb.org/10.5/centos8-amd64/
    gpgkey=https://yum.mariadb.org/RPM-GPG-KEY-MariaDB
    gpgcheck=1
    EOF
    ```

  - 安装

    ```shell
    $ yum install MariaDB-server		# 官方安装大写
    ```


## 初始化

```shell
$ mysql_secure_installation

Enter current password for root (enter for none)		# 输入当前root密码(默认为空)	
Set root password? [Y/n] 								# 设置密码
Remove anonymous users? [Y/n] 							# 删除匿名测试用户(Y)
Disallow root login remotely? [Y/n] 					# 不允许root远程登录(n)
Remove test database and access to it? [Y/n] 			# 删除测试数据库(Y)
Reload privilege tables now? [Y/n] 						# 刷新权限表(Y)
```

## 开启密码验证

```mysql
> update user set plugin = 'mysql_native_password' where user = 'root';
> flush privileges
```

## 配置编码格式

```shell
$ vim /etc/my.cnf.d/mariadb-server.cnf
# 配置编码
[mysqld]
character-set-server=utf8
collation-server=utf8_general_ci
init-connect = SET NAMES utf8
log-error=/var/log/mysqld.log
[client]
default-character-set=utf8
[mysql]
default-character-set=utf8
```

## 修改密码

```shell
$ mysqladmin -uroot -p password "123"		# 这个命令不需要进入mysql
set password = PASSWORD('redhat123');		# 登录MySQL后修改
```

## 创建用户

```mariadb
> create user 'm5xhsy'@'127.0.0.1' identified by 'Ass078678'; 	# 创建用户m5xhsy只能在127.0.0.1的IP地址登录，%可代表所有
```

## 权限相关

```mariadb
> grant all privileges on *.* to root@'%' identified by 'Ass078678'  # 给用户授予所有权限并且验证密码是Ass078678
> flush privileges								# 刷新权限 
```

## 数据库备份

```shell
$ mysqldump -u root -p --all-databases > /data/db.dump		# 备份数据库
$ mysql -uroot -p < /data/db.dump							# 恢复数据库
> source /data/db.dump										# 登录后导入
```

## MySQL主从复制

1. 原理

  1. 主库数据发生变动，并记录到日志中
  2. 从库开启线程读取主库的日志，并写入自己的日志中
  3. 从库根据读取的日志重复主库的操作

2. 主从配置

  - 主服务器

    1. 查看并停止主服务器MySQL服务状态

      ```shell
      $ systemctl status mariadb
      $ systemctl stop mariadb
      ```

    2. 配置主服务器配置

       ```shell
       $ vim /etc/my.cnf.d/mariadb-server.cnf
       ######	主库配置文件
       [mysqld]
       server-id=1
       log-bin=mysql-bin		# 数据库操作日志会记录到mysql-bin中
       ```

    3. 启动主服务器MySQL

       ```shell
       $ systemctl start mariadb			# 启动MySQL服务
       ```

    4. 进入MySQL查看配置

       ```shell
       $ mysql -uroot -p					# 进入MySQL
       > show master status;				# 查看配置
       +------------------+----------+--------------+------------------+
       | File             | Position | Binlog_Do_DB | Binlog_Ignore_DB |
       +------------------+----------+--------------+------------------+
       | mysql-bin.000001 |      645 |              |                  |
       +------------------+----------+--------------+------------------+
       1 row in set (0.000 sec)
       ```

    5. 创建用于主从配置的用户并授权

       ```shell
       > create user 'm5xhsy'@'%' identified by "Ass078678";		# 创建用户
       > grant replication slave on *.* to 'm5xhsy'@'%';			# 授予复制权限
       > flush privileges;											# 刷新权限
       ```

    6. 查看用户

       ```shell
       > select user,host from mysql.user;
       +--------+-----------------------+
       | user   | host                  |
       +--------+-----------------------+
       | m5xhsy | %                     |
       | root   | %                     |
       | root   | 127.0.0.1             |
       | root   | ::1                   |
       | root   | localhost             |
       | root   | localhost.localdomain |
       +--------+-----------------------+
       6 rows in set (0.000 sec)
       ```

  - 从服务器

    1. 查看并停止从服务器MySQL服务状态

       ```shell
       $ systemctl status mariadb
       $ systemctl stop mariadb
       ```

    2. 配置从服务器配置

       ```shell
       $ vim /etc/my.cnf.d/mariadb-server.cnf
       ######	主库配置文件
       [mysqld]
       server-id=2		# id与主服务器不同
       ```

    3. 启动从服务器MySQL

       ```shell
       $ systemctl start mariadb			# 启动MySQL服务
       ```

  - 同步数据

    1. 锁定主服务器

       ```mariadb
       > flush table with read lock;
       ```

    2. 导出数据库文件

       ```shell
       $ mysqldump -u root -p --all-databases > /data/db.dump
       ```

    3. 通过xshell导出并同步到从服务器

       ```shell
       $ mysql -uroot -p < /data/db.dump			# 也可以登录MySQL后> source /data/db.dump
       ```

    4. 从服务器配置同步参数

       ```mariadb
       change master to master_host='192.168.239.128',
       master_user='m5xhsy',
       master_password='Ass078678',
       master_log_file='mysql-bin.000003',			
       master_log_pos=783;
       # user和pswd是之前主服务器创建的用户
       # file和pos在主服务器通过> show master status; 查看
       ```

    5. 启动从服务器的主从同步进程

       ```mariadb
       > start slave;
       补充：
       > stop slave;reset slave; 		# 清除主从同步参数
       ```

    6. 检查状态

       ```mariadb
       > show slave status \G
       *************************** 1. row ***************************
                       Slave_IO_State: Waiting for master to send event
                          Master_Host: 192.168.239.128
                          Master_User: m5xhsy
                          Master_Port: 3306
                        Connect_Retry: 60
                      Master_Log_File: mysql-bin.000003
                  Read_Master_Log_Pos: 342
                       Relay_Log_File: mariadb-relay-bin.000002
                        Relay_Log_Pos: 555
                Relay_Master_Log_File: mysql-bin.000003
                     Slave_IO_Running: Yes		# 这个需要为Yes	
                    Slave_SQL_Running: Yes		# 这个也为Yes
       ```

    7. 关闭主服务器锁并测试

       ```mariadb
       > unlock tables;
       ```

    8. 配置从库的只读模式

       ```shell
       $ vim /etc/my.cnf.d/mariadb-server.cnf
       ###### root 用户无法做到只读
       [mysqld]
       read-only=true
       ```

  - 从库备份

    1.首先暂停从服务器的复制进程

    ```
    > mysqladmin -uroot -p stop-slave
    ```

    2.使用mysqldump导出全部或部分的数据库

    ```
    > mysqldump --all-databases > /data/db.dump
    ```

    3.在导出数据库后，重启复制进程

    ```
    > mysqladmin -uroot -p start-slave
    ```

  - 解决方案

    1. 从服务器上ping主服务器看看能不能通
    2. 查看主服务器用户是否存在以及是否具有权限
    3. 检查从服务器配置同步参数，host，pos，file是否正确
    4. 关闭服务器防火墙，或者添加端口
    5. selinux
    6. 从服务器远程登录主服务器