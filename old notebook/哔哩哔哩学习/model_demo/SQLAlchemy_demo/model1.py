from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,String,Integer,ForeignKey
from sqlalchemy.orm import relationship
Base = declarative_base()

class Student(Base):
    __tablename__ = "student"
    id = Column(Integer,primary_key=True)
    name = Column(String(32))
    school_id = Column(Integer,ForeignKey("school.id"))
    stu2sch = relationship("School",backref="sch2stu")
    # 如果Student中查看School,直接.Stu2sch,School中查看Student,直接.sch2Stu

class School(Base):
    __tablename__ = "school"
    id = Column(Integer,primary_key=True)
    name = Column(String(32))

from sqlalchemy import create_engine
engine = create_engine("mysql+pymysql://root:Ass078678@192.168.239.128:3306/m5xhsy?charset=utf8")


Base.metadata.create_all(engine)