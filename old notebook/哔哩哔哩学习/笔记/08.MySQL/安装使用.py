'''
(一) 安装步骤:
        1.解压
        2.添加环境变量到bin目录
        3.初始化                                mysqld --initialize-insecure
        4.启动MySQL服务                         mysqld
        5.启动MySQL客户端并连接MySQL服务器      mysql -uroot -p

(二) 启动服务器终端被阻塞，将MySQL服务做成windows服务即可解决
        mysqld --install        制作MySQL服务(管理员方式运行)
        mysqld --remove         移除MySQL服务
        net start mysql         启动MySQL服务
        net stop mysql          关闭MySQL服务
        补充 关闭进程
            tasklist | findstr mysql  # 查找带MySQL字符串的进程
            taskkill /F /PID 3288  # 结束PID为3288的进程

(三) 设置密码
        select user()                           查看当前登录用户
        $ mysqladmin -uroot -p password "123"     设置root密码为123
        mysql -uroot -p123                      登录账号
        set password = PASSWORD('redhat123');

(四) 破解密码(或者在my.ini里面加 --skip-grant-tables，改完密码再删除)
        (1) 先关掉之前的MySQL服务器
        (2) 跳过授权表开启MySQL的服务端    mysqld --skip-grant-tables
        (3) 客户端链接                     mysql -uroot -p
        (4) 更改密码                       updata mysql.user set authentication_string =password('') where User='root';
        (5) 刷新权限                       flish privileges;

(五) 用户统一编码
    配置文件 my.ini
        [mysqld]
        # 设置mysql的安装目录 **后面的路径一定是安装sql的目录（自己电脑的）**
        basedir=B:\MySQL
        # 设置mysql数据库的数据的存放目录，必须是data
        datadir=B:\MySQLdata
        sql_mode=NO_ENGINE_SUBSTITUTION,STRICT_TRANS_TABLES
        # mysql端口
        port=3306
        # 字符集
        [mysqld]
        character-set-server=utf8
        collation-server=utf8_general_ci
        [client]
        default-character-set=utf8
        [mysql]
        default-character-set=utf8


常用命令:
    客户端
        \s；                     查看配置
        use db1;                                                 #使用数据库
        create table t1(id int,name char(10));                  #创建一个t1表
        drop table t1;                                           #删除t1表
        select * from t1;                                       #查看t1表中所有内容
        select id from t1；                                      #查看t1中所有id
        show tables;                                             #显示所有表
        show databases;                                         #显示所有
        create database db1;                                    #创建db1
        mysql -uroot -p                                         #root用户登录，密码默认为空
        insert into t1(id,name) values(1,'xxx'),(2,'bbb');      #插入内容
        select user();                                          #查看用户
    服务端
        net start mysql     #开启服务端
        net stop mysql      #关闭服务端
        mysqld      #开启服务端
        mysqld --initialize-insecure        #初始化，生成data文件


###补充
    tasklist | findstr mysql  # 查找带MySQL字符串的进程
    taskkill / F / PID 3288  # 结束PID为3288的进程



数据库: 数据库是一些关联表的集合。.
数据表: 表是数据的矩阵。在一个数据库中的表看起来像一个简单的电子表格。
列: 一列(数据元素) 包含了相同的数据, 例如邮政编码的数据。
行：一行（=元组，或记录）是一组相关的数据，例如一条用户订阅的数据。
冗余：存储两倍数据，冗余降低了性能，但提高了数据的安全性。
主键：主键是唯一的。一个数据表中只能包含一个主键。你可以使用主键来查询数据。
外键：外键用于关联两个表。
复合键：复合键（组合键）将多个列作为一个索引键，一般用于复合索引。
索引：使用索引可快速访问数据库表中的特定信息。索引是对数据库表中一列或多列的值进行排序的一种结构。类似于书籍的目录。
参照完整性: 参照的完整性要求关系中不允许引用不存在的实体。与实体完整性是关系模型必须满足的完整性约束条件，目的是保证数据的一致性。


