from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,Integer,String

# 创建ORM模型基类
Base = declarative_base()

# 创建ORM对象
class User(Base):
    __tablename__ = "user"
    id = Column(Integer,primary_key=True,autoincrement=True)    # 是否主键以及自增长,新版本默认自增长
    name = Column(String(32),index=True)        # 是否创建索引
    age = Column(Integer)

# 创建数据库连接
from sqlalchemy import  create_engine
engine = create_engine("mysql+pymysql://root:Ass078678@192.168.239.128:3306/m5xhsy?charset=utf8")

# 去数据库创建与user对应的表
Base.metadata.create_all(engine)