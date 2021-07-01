



## 一对一

### 创建表

```python
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,Integer,String
from sqlalchemy import  create_engine
# 创建ORM模型基类
Base = declarative_base()

# 创建ORM对象
class User(Base):
    __tablename__ = "user"
    id = Column(Integer,primary_key=True)    # 是否主键
    name = Column(String(32),index=True)        # 是否创建索引
    age = Column(Integer)

# 创建数据库连接
engine = create_engine("mysql+pymysql://root:Ass078678@192.168.239.128/m5xhsy?charset=utf8")

# 去数据库创建与user对应的表
Base.metadata.create_all(engine)
```

### 使用表

```python
from model import User,engine 

# 创建会话，打开数据库连接
from sqlalchemy.orm import sessionmaker
Session = sessionmaker(engine)

# 打开会话窗口
db_session = Session()		# 通过会话窗口进行增删改查

"""
######对此进行增删改查操作
"""

# 执行提交会话窗口中的所有操作(查询不用提交)
db_session.commit()
# 关闭
db_session.close()
```

### 操作表

1. #### 增加

   ```python
   # 增加数据
   db_session.add(User(name="撒旦",age=18))
   # 批量增加数据    也可以用多个add()
   db_session.add_all([
       User(name="Ass",age=18),
       User(name="Bss",age=19),
       User(name="Css",age=20),
       User(name="Dss",age=21),
       User(name="Ess",age=22),
   ])
   ```

2. #### 删除

   ```python
   db_session.query(User).filter(User.id==1).delete()
   ```

3. #### 修改

   ```shell
   db_session.query(User).filter_by(id=4).update({"age":128})
   db_session.query(User).filter(User.id<=3).update({"age":0})
   ```

   

4. #### 查找

   ```python
   # 不加.all()或者.first()可查看sql语句
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
   ```

## 一对多

### 创建表



