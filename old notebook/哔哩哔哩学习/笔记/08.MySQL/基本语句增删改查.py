'''
数据库操作
    use db1;                                            使用数据库
    select database()；                                 查看当前使用数据库
    create database db1 charset utf-8;                  创建utf8的数据库
    show create database db1;                           查看当前创建的数据库如何创建
    show databases;                                     查看所有数据库
                                                            information_schema： 虚拟库，不占用磁盘空间，存储的是数据库启动后的一些参数，如用户表信息、列信息、权限信息、字符信息等
                                                            performance_schema： MySQL 5.5开始新增一个数据库：主要用于收集数据库服务器性能参数，记录处理查询请求时发生的各种事件、锁等现象
                                                            mysql： 授权库，主要存储系统用户的权限信息
                                                            test： MySQL数据库系统自动创建的测试数据库
    alter database db1 chaeset gbk;                     修改数据库编码
    drop database db1;                                  删除数据库

表操作
    create table b1 select * from db2.a1;               复制db2.a1的表结构和记录
    create table b2 select * from db2.a1 where 1>5;     在db2数据库下新创建一个b2表，给一个where条件，条件要求不成立，条件为false，只拷贝表结构
    create table b3 like db2.a1;                        (只拷贝表结构，不拷贝记录)
    create table t1(id int,name char(50));              创建表
    show create table t1;                               查看当前这张t1表
    show tables;                                        查看所有表
    desc t1;                                            查看t1表详细信息
    alter table t1 modify name char(60);                修改name格式 (modify 修改)
    alter table t1 change name NAMA char(60);           修改name格式
    drop table t1;                                      删除t1表

表内容操作
    insert t1(id,name) values(1,'xx'),(2,'jj');         插入一条数据
    select id from db1.t1;                              查找db1数据库中t1表中的所有id
    select id,name from db1.t1 where id=2;              查找id=2的多个值
    select * from db1.t1;                               查找所有值
    delete from t1;                                     删除t1表
    delete from t1 where id=2;                          删除t1表中id=2的数据

数据操作补充
    一、插入数据
        1.插入完整数据（顺序插入）
        语法一：insert into 表名(字段1, 字段2, 字段3…字段n) values(值1, 值2, 值3…值n);

        语法二：insert into 表名 values(值1, 值2, 值3…值n);

        2.指定字段插入数据
        语法： insert into 表名(字段1, 字段2, 字段3…) values(值1, 值2, 值3…);

        3.插入多条记录
        语法：  insert into 表名 values
                (值1, 值2, 值3…值n),
                (值1, 值2, 值3…值n),
                (值1, 值2, 值3…值n);

        4.插入查询结果
        语法：insert into 表名(字段1, 字段2, 字段3…字段n) select(字段1, 字段2, 字段3…字段n) from 表2 where 条件;

    二、更新数据
        语法：
        update 表名 set 字段1 = 值1,字段2 = 值2, where 条件;
        示例：
        update mysql.user set password = password(‘123’) where user =’root’ and host =’localhost’;
        update m5xhsy.emp set name='xxx',age=15 where eid=8;

    三、删除数据
        语法：
        delete from 表名 where 条件;
        示例：
        delete from mysql.user where password =’’;