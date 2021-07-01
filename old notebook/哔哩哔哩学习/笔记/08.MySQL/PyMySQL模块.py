####登录示例
'''
import pymysql
user = input('请输入账号:').strip()
pswd = input('请输入密码:').strip()
#建立链接
conn = pymysql.connect(
    host='localhost',
    user='root',
    password="Ass078678",
    database='study',
    port=3306,
    charset='utf8',
)
#创建游标
cur = conn.cursor()
# sql = 'select * from userinfo where username = "%s" and password = "%s"'%(user,pswd)      #会被注释攻击
# res = cur.execute(sql)

# sql = 'select * from userinfo where username = %s and password = %s'
# res = cur.execute(sql,[user,pswd])          #也可以用元组

sql = 'select * from userinfo where username = %(user)s and password = %(pswd)s'
res = cur.execute(sql,{'user':user,'pswd':pswd})
#链接关闭
cur.close()
conn.close()
if res:
    print('登录成功')
else:
    print('登录失败')
'''