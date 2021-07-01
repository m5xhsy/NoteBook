from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.engine import create_engine
from sqlalchemy import String,Integer,Column,ForeignKey,Table
from sqlalchemy.orm import relationship
Base = declarative_base()


relevance_obj = Table(
    "relevance",
    Base.metadata,
    Column("user_id",Integer, ForeignKey("user.id")),
    Column("hobby_id",Integer,ForeignKey("hobby.id")),
)

class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True)
    name = Column(String(32),index=True)
    user2hobby = relationship("Hobby",secondary=relevance_obj,backref="hobby2user") # 2张关联表任意一张创建

class Hobby(Base):
    __tablename__ = "hobby"
    id = Column(Integer,primary_key=True)
    name = Column(String(32),index=True)

engine = create_engine("mysql+pymysql://root:Ass078678@192.168.239.128:3306/m5xhsy?charset=utf8")


Base.metadata.create_all(engine)







