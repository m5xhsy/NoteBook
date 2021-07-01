'''
默认值;
    default             设置默认值
是否为空:
    not null            不可以为空
    null                可以为空,默认为空

是否唯一:
    单列唯一
        id unique
    多列唯一
        unique(id),unique(name)
    联合唯一(组合唯一)
        unique(id,name)     (只要一列不同就可以插入数据)

设置主键:
    primary key             (做查询优化，但是not null unique 不能做)
        在MySQL的一个表中只有唯一的一个主键，不能有多列主键，但可以有复合主键
        一个表中可以：
        单列做主键
        多列做主键（复合主键）     primary key(id,name)
        约束：等价于 not null unique,字段的值不为空且唯一
        存储引擎默认是（innodb）:对于innodb存储引擎来说，一张表必须有一个主键。

自动增长:
    auto_increment
        delete from t1; #如果有自增id，新增的数据，仍然是以删除前的最后一样作为起始。
        truncate table t1;数据量大，删除速度比上一条快，且直接从零开始。
    查看可用的 开头auto_inc的词
    mysql> show variables like 'auto_inc%';
    +--------------------------+-------+
    | Variable_name            | Value |
    +--------------------------+-------+
    | auto_increment_increment | 1     |
    | auto_increment_offset    | 1     |
    +--------------------------+-------+
    rows in set (0.02 sec)
    # 步长auto_increment_increment,默认为1
    # 起始的偏移量auto_increment_offset, 默认是1

     # 设置步长 为会话设置，只在本次连接中有效
     set session auto_increment_increment=5;
     #全局设置步长 都有效。
     set global auto_increment_increment=5;
     # 设置起始偏移量
     set global  auto_increment_offset=3;

    #强调：If the value of auto_increment_offset is greater than that of auto_increment_increment, the value of auto_increment_offset is ignored.
    翻译：如果auto_increment_offset的值大于auto_increment_increment的值，则auto_increment_offset的值会被忽略

    # 设置完起始偏移量和步长之后，再次执行show variables like'auto_inc%';
    发现跟之前一样，必须先exit,再登录才有效。

    mysql> show variables like'auto_inc%';
    +--------------------------+-------+
    | Variable_name            | Value |
    +--------------------------+-------+
    | auto_increment_increment | 5     |
    | auto_increment_offset    | 3     |
    +--------------------------+-------+
    rows in set (0.00 sec)

    #因为之前有一条记录id=1
    mysql> select * from student;
    +----+---------+------+
    | id | name    | sex  |
    +----+---------+------+
    |  1 | xiaobai | male |
    +----+---------+------+
    row in set (0.00 sec)
    # 下次插入的时候，从起始位置3开始，每次插入记录id+5
    mysql> insert into student(name) values('ma1'),('ma2'),('ma3');
    Query OK, 3 rows affected (0.00 sec)
    Records: 3  Duplicates: 0  Warnings: 0

    mysql> select * from student;
    +----+---------+------+
    | id | name    | sex  |
    +----+---------+------+
    |  1 | xiaobai | male |
    |  3 | ma1     | male |
    |  8 | ma2     | male |
    | 13 | ma3     | male |
    +----+---------+------+
    auto_increment_increment和 auto_increment_offset


设置外键
    foreign key
        主表：被关联表
            create
            table dep(
            id int primary key auto_increment,
            name varchar(20) not null,
            des varchar(30) not null
            );

        从表：关联表
            create table emp(
            eid int primary key auto_increment,
            name char(10) not null,
            age int not null,
            dep_id int not null,
            constraint fk_dep foreign key(dep_id) references dep(id)
            on delete cascade
            on update cascade
            );

    外键的变种
        1.先站在右边表的角度 右表的多条记录对应左表的一条记录   成立
        2.先站在左边表的角度 左表的多条记录对应右表的一条记录   成立

        多对一或者一对多    1和2有一个成立
        多对多              1和2都成立 通过建立第三张表来建立多对多的关系
        一对一              1和2都不成立，给一个表的fk字段设置约束unique