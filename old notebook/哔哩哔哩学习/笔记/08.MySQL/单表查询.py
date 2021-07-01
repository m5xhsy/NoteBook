'''
语法
    select 字段1,字段2... from 表名
                      where 条件
                      group by 字段
                      having 筛选
                      order by 字段
                      limit 限制条数


from                1.找到表:from
where               2.拿着where指定的约束条件，去文件/表中取出一条条记录
                            where子句中可以使用
                            1.比较运算符：>、<、>=、<=、<>、!=
                            2.between 80 and 100 ：值在80到100之间
                            3.in(80,90,100)值是10或20或30
                            4.like 'xiaomagepattern': pattern可以是%或者_。%小时任意多字符，_表示一个字符
                            5.逻辑运算符：在多个条件直接可以使用逻辑运算符 and or not
group by            3.将取出的一条条记录进行分组group by，如果没有group by，则整体作为一组
                            例如： select count(1) age from group by age;     查看不同年龄人数
                            分组发生在where之后
                            由于没有设置ONLY_FULL_GROUP_BY,也可以有结果，默认都是组内的第一条记录，但其实这是没有意义的
                            如果想分组，则必须要设置全局的sql的模式为ONLY_FULL_GROUP_BY
                            继续验证通过group by分组之后，只能查看当前字段,如果想查看组内信息，需要借助于聚合函数   count(1)或者count(*)查看个数
having              4.将分组的结果进行having过滤
                            HAVING与WHERE不一样的地方在于
                            #！！！执行优先级从高到低：where > group by > having
                            #1. Where 发生在分组group by之前，因而Where中可以有任意字段，但是绝对不能使用聚合函数。
                            #2. Having发生在分组group by之后，因而Having中可以使用分组的字段，无法直接取到其他字段,可以使用聚合函数
select              5.执行select
distinct            6.去重
order by            7.将结果按条件排序：order by
                        按单列排序
                            select * from employee order by age;
                            select * from employee order by age asc;
                            select * from employee order by age desc;
                        按多列排序:先按照age升序排序，如果年纪相同，则按照id降序
                            select * from employee order by age asc,id desc;
limit               8.限制结果的显示条数
                    示例：
                        select * from employee order by salary desc limit 3;   #默认初始位置为0
                        select * from employee order by salary desc limit 0,5; #从第0开始，即先查询出第一条，然后包含这一条在内往后查5条
                        select * from employee order by salary desc limit 5,5; #从第5开始，即先查询出第6条，然后包含这一条在内往后查5条














