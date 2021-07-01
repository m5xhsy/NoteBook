逻辑查询    select * from t1,t2 where t1.id = t2.t1_id;
MySQL提供方法:
    多表链接查询:
        SELECT 字段列表
            FROM 表1 INNER|LEFT|RIGHT JOIN 表2
            ON 表1.字段 = 表2.字段;
        （1）先看第一种情况交叉连接：不适用任何匹配条件。生成笛卡尔积
        （2）内连接：只连接匹配的行
        （3）外链接-左连接：优先显示左表全部记录
        （3）外链接-左连接：优先显示左表全部记录

    符合条件连接查询:
        select employee.name,department.name from employee inner join department
    　　  on employee.dep_id = department.id
    　　  where age > 25;
    子查询:
        #1：子查询是将一个查询语句嵌套在另一个查询语句中。
        #2：内层查询语句的查询结果，可以为外层查询语句提供查询条件。
        #3：子查询中可以包含：IN、NOT IN、ANY、ALL、EXISTS 和 NOT EXISTS等关键字
        #4：还可以包含比较运算符：= 、 !=、> 、<等
        （1）带in关键字的子查询
        （2）带比较运算符的子查询
        （3）带EXISTS关键字的子查询
            #EXISTS关字键字表示存在。在使用EXISTS关键字时，内层查询语句不返回查询的记录。而是返回一个真假值。True或False
            #当返回True时，外层查询语句将进行查询；当返回值为False时，外层查询语句不进行查询
            #department表中存在dept_id=203，Ture
            mysql> select * from employee  where exists (select id from department where id=200);




            select id,name from department
            where id in
                (select dep_id from employee group by dep_id having avg(age) > 25);