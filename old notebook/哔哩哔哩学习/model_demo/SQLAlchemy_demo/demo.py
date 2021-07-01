from model_demo.SQLAlchemy_demo.model import User,engine

# 创建会话，打开数据库连接
from sqlalchemy.orm import sessionmaker
Session = sessionmaker(engine)

# 打开会话窗口
db_session = Session()

# 增
"""
# 1.增加数据
db_session.add(User(name="撒旦",age=18))

# 2.批量增加数据    也可以用多个add()
db_session.add_all([
    User(name="Ass",age=18),
    User(name="Bss",age=19),
    User(name="Css",age=20),
    User(name="Dss",age=21),
    User(name="Ess",age=22),
])
"""

# 查
""" # 不加.all()或者.first()可查看sql语句
# 查询所有数据
user_list = db_session.query(User).all()
print(user_list)                     # 列表
print(user_list[0].name)
print(db_session.query(User))       # sql语句

# 查询一条数据
user_obj = db_session.query(User).first()
print(user_obj.name, user_obj.age)

# 条件查询  
user_list = db_session.query(User).filter(User.id==4).all()
print(user_list[0].name)
user_list = db_session.query(User).filter(User.id>=4).all()
print([item.name for item in user_list])

user_obj = db_session.query(User).filter_by(id=4).first()
print(user_obj.name)
"""

# 改
"""
db_session.query(User).filter_by(id=4).update({"age":128})
db_session.query(User).filter(User.id<=3).update({"age":0})
"""

# 删
"""
db_session.query(User).filter(User.id==1).delete()
"""
db_session.query(User).filter(User.id==3).delete()
# 执行提交会话窗口中的所有操作
db_session.commit()
# 关闭
db_session.close()