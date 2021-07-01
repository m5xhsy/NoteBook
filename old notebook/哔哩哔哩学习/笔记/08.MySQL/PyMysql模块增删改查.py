###增/删/改
'''
import pymysql
user = input('账号：').strip()
pswd = input('密码：').strip()
conn = pymysql.connect(
    host='127.1.1.1',
    user='root',
    password="Ass078678",
    database='study',
    port=3306,
    charset='utf8'
)
try:
    cur = conn.cursor()
    # #增
    # sql = 'insert into userinfo(username,password) values(%s,%s)'
    # ret = cur.execute(sql, [user, pswd])
    # 删
    # sql = 'delete from userinfo where username = %s'
    # ret = cur.execute(sql,[user])
    #改
    sql = 'update userinfo set password = %s where username = %s'
    ret = cur.execute(sql, [pswd,user])
    conn.commit()               #提交
    print(ret)
    if ret:
        print('成功')
    else:
        print('失败')
except pymysql.err.IntegrityError:
    print('失败')
    conn.rollback()     # 出现错误，数据回滚
conn.close()
cur.close()
'''

###查
import pymysql
conn = pymysql.connect(
    host='127.1.1.1',
    user='root',
    password="Ass078678",
    database='study',
    port=3306,
    charset='utf8'
)
cur = conn.cursor(cursor=pymysql.cursors.DictCursor)
sql = 'select * from userinfo'
cur.execute(sql)
# cur.scroll(2,mode='relative')  # 相对当前位置移动（移动）
# cur.scroll(2,mode='absolute') # 相对绝对位置移动

result1 = cur.fetchone()        #获取下一行，第一次为首行
result2 = cur.fetchmany(2)      #获取2行
result3 = cur.fetchall()        #获取所有
print(result1)
print(result2)
print(result3)




######
conn.commit()       # 数据提交
conn.rollback()     # 数据回滚
