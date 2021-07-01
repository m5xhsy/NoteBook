'''
    删除索引        drop index 索引名 on 表名
    显示索引        show index from 表名
- 普通索引  仅有一个加速查找
    建表添加
        index 索引名(列名(4))        表示前4个字符创建索引
    后续添加
        create index 索引名 on 表名(列名)

- 唯一索引  加速查找和唯一约束（可含null）
    建表创建
        unique  index  索引名(列名)
    后续添加
        create unique index 索引名 on 表名(列名)

- 主键索引  加速查找和唯一约束（不含null）
    建表创建
        列名 类型 not null,
        unique index 索引名(列名)
    后续添加
        alter table 表名 add primary key(列名);
    删除索引
        alter table 表名 drop primary key;
        alter table 表名  modify  列名 int, drop primary key;

- 联合索引（多列）
   - 联合主键索引
　 - 联合唯一索引 　　
   - 联合普通索引



- 组合索引最左前缀
    如果组合索引为：(name,email)
    name and email       -- 使用索引
    name                 -- 使用索引
    email                -- 不使用索引
    对于同时搜索n个条件时，组合索引的性能好于多个单列索引



(1)避免使用select *
(2)count(1)或count(列)代替count(*)
(3)创建表时尽量使用char代替varchar
(4)表的字段顺序固定长度的字段优先
(5)组合索引代替多个单列索引（经常使用多个条件查询时）
(6)尽量使用短索引 （create index ix_title on tb(title(16));特殊的数据类型text类型）
(7)使用连接（join）来代替子查询
(8)连表时注意条件类型需一致
(9)索引散列（重复少）不适用于建索引，例如：性别不合适



- like
    '%xx'select * from userinfo where name like '%al';
- 使用函数
    select * from userinfo where reverse(name) = 'alex333';
- or
    select * from userinfo where id = 1 or email = 'alex122@oldbody';
    特别的：当or条件中有未建立索引的列才失效，以下会走索引
        select * from userinfo where id = 1 or name = 'alex1222';
        select * from userinfo where id = 1 or email = 'alex122@oldbody' and name = 'alex112'
- 类型不一致
    如果列是字符串类型，传入条件是必须用引号引起来，不然...
    select * from userinfo where name = 999;
- !=
    select count(*) from userinfo where name != 'alex'
    特别的：如果是主键，则还是会走索引
        select count(*) from userinfo where id != 123
- >
    select * from userinfo where name > 'alex'
    特别的：如果是主键或索引是整数类型，则还是会走索引
        select * from userinfo where id > 123
        select * from userinfo where num > 123
- order by
    select email from userinfo order by name desc;
        当根据索引排序时候，选择的映射如果不是索引，则不走索引
        特别的：如果对主键排序，则还是走索引：
            select * from userinfo order by nid desc;
- 组合索引最左前缀
    如果组合索引为：(name, email)
        name and email - - 使用索引
        name - - 使用索引
        email - - 不使用索引









explain + 查询SQL - 用于显示SQL执行信息参数，根据参考信息可以进行SQL优化
select_type：
    查询类型
        SIMPLE          简单查询
        PRIMARY         最外层查询
        SUBQUERY        映射为子查询
        DERIVED         子查询
        UNION           联合
        UNION RESULT    使用联合的结果
table：
    正在访问的表名
type：
    查询时的访问方式，性能：all < index < range < index_merge < ref_or_null < ref < eq_ref < system / const
    ALL     全表扫描，对于数据表从头到尾找一遍
            select * from userinfo;
            特别的：如果有limit限制，则找到之后就不在继续向下扫描
            select * from userinfo where email = 'alex112@oldboy'
            select * from userinfo where email = 'alex112@oldboy' limit 1;
            虽然上述两个语句都会进行全表扫描，第二句使用了limit，则找到一个后就不再继续扫描。

INDEX ：    全索引扫描，对索引从头到尾找一遍
            select nid from userinfo;
RANGE：     对索引列进行范围查找
            select * from userinfo where name < 'alex';
            PS:
                between and
                in
                > >= < <= 操作
                注意： != 和 > 符号
INDEX_MERGE：    合并索引，使用多个单列索引搜索
                 select * from userinfo where name = 'alex' or nid in (11, 22, 33);
REF：       根据索引查找一个或多个值
            select * from userinfo where name = 'alex112';
EQ_REF：    连接时使用primary key 或unique类型
            select userinfo2.id, userinfo.name from userinfo2 left join tuserinfo on userinfo2.id = userinfo.id;
CONST：     常量
            表最多有一个匹配行, 因为仅有一行, 在这行的列值可被优化器剩余部分认为是常数, const表很快, 因为它们只读取一次。
            select id from userinfo where id = 2;
SYSTEM：系统
            表仅有一行( = 系统表)。这是const联接类型的一个特例。
            select * from (select id from userinfo where id = 1) as A;
possible_keys：  可能使用的索引
key：            真实使用的
key_len：　　    MySQL中使用索引字节长度
rows：           mysql估计为了找到所需的行而要读取的行数 - ----- 只是预估值
extra：
        该列包含MySQL解决查询的详细信息
        “Using index”
            此值表示mysql将使用覆盖索引，以避免访问表。不要把覆盖索引和index访问类型弄混了。
        “Using where”
            这意味着mysql服务器将在存储引擎检索行后再进行过滤，许多where条件里涉及索引中的列，当（并且如果）它读取索引时，就能被存储引擎检验，因此不是所有带where子句的查询都会显示“Using where”。有时“Using where”的出现就是一个暗示：查询可受益于不同的索引。
        “Using temporary”
            这意味着mysql在对查询结果排序时会使用一个临时表。
        “Using filesort”
            这意味着mysql会对结果使用一个外部索引排序，而不是按索引次序从表里读取行。mysql有两种文件排序算法，这两种排序方式都可以在内存或者磁盘上完成，explain不会告诉你mysql将使用哪一种文件排序，也不会告诉你排序会在内存里还是磁盘上完成。
        “Range checked for each record(index map: N)”
            这个意味着没有好用的索引，新的索引将在联接的每一行上重新估算，N是显示在possible_keys列中索引的位图，并且是冗余的






慢日志
    (1) 进入MySql 查询是否开了慢查询
             show variables like 'slow_query%';
             参数解释：
                 slow_query_log 慢查询开启状态  OFF 未开启 ON 为开启
            slow_query_log_file 慢查询日志存放的位置（这个目录需要MySQL的运行帐号的可写权限，一般设置为MySQL的数据存放目录）

    （2）查看慢查询超时时间
           show variables like 'long%';
           ong_query_time 查询超过多少秒才记录   默认10秒

    （3）开启慢日志（1）（是否开启慢查询日志，1表示开启，0表示关闭。）
               set global slow_query_log=1;
    （4）再次查看
                  show variables like '%slow_query_log%';

    （5）开启慢日志（2）：（推荐）
             在my.cnf 文件中
             找到[mysqld]下面添加：
               slow_query_log =1
       　　　　 slow_query_log_file=C:\mysql-5.6.40-winx64\data\localhost-slow.log
        　　　  long_query_time = 1

        参数说明：
            slow_query_log 慢查询开启状态  1 为开启
            slow_query_log_file 慢查询日志存放的位置
            long_query_time 查询超过多少秒才记录   默认10秒 修改为1秒


分页
    （1）只有上一页和下一页
            做一个记录：记录当前页的最大id或最小id
            下一页：
            select * from userinfo where id>max_id limit 10;

            上一页：
            select * from userinfo where id<min_id order by id desc limit 10;


      (2) 中间有页码的情况
               select * from userinfo where id in(
                   select id from (select * from userinfo where id > pre_max_id limit (cur_max_id-pre_max_id)*10) as A order by A.id desc limit 10
               );