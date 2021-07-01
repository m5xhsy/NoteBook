from model_demo.SQLAlchemy_demo.model1 import engine,School,Student
from sqlalchemy.orm import sessionmaker

Session = sessionmaker(engine)
db_session = Session()

# 添加
"""
# 普通添加
sch_obj = School(name="湖南理工学院")
db_session.add(sch_obj)
db_session.commit()

sch = db_session.query(School).filter(School.name == "湖南理工学院").first()
stu_obj = Student(name="m5xhsy",school_id=sch.id)
db_session.add(stu_obj)


# 正向添加
sch_obj = School(name="长沙理工大学")
sch_obj.sch2stu = [Student(name="Ass"),Student(name="Bss")]     # 一个学校有多个学生，为列表
db_session.add(sch_obj)

# 反向添加
stu_obj = Student(name="Css")
stu_obj.stu2sch = School(name="湖南大学")
db_session.add(stu_obj)
"""

# 查询
"""
stu = db_session.query(Student).all()
print([(item.stu2sch.name,item.name) for item in stu])
# [('湖南理工学院', 'm5xhsy'), ('长沙理工大学', 'Ass'), ('长沙理工大学', 'Bss'), ('湖南大学', 'Css')]

sch = db_session.query(School).all()
print([(item.name,[item.name for item in item.sch2stu]) for item in sch])
# [('湖南理工学院', ['m5xhsy']), ('长沙理工大学', ['Ass', 'Bss']), ('湖南大学', ['Css'])]
"""

# 修改
"""
db_session.query(Student).filter(Student.name == "m5xhsy").update({"school_id":2})
"""
# 删除
"""
db_session.query(Student).filter(Student.school_id == 2).delete()
"""

# 其他查询操作
"""
from sqlalchemy.sql import or_, and_, text
# 或
stu = db_session.query(Student).filter(or_(Student.school_id == 1,Student.name == "Css")).all()
print([item.name for item in stu])

# 且
stu = db_session.query(Student).filter(and_(Student.school_id == 1,Student.name == "屁屁")).all()
print([item.name for item in stu])

# 查询指定字段
stu = db_session.query(Student.name).first()
print(stu.name)

# 别名
stu = db_session.query(Student.id.label("nid"),Student.name.label("a")).first()
print(stu.nid,stu.a)

# 字符串匹配查询
stu = db_session.query(Student).filter(text("id<:value and school_id=:index")).params(value=13,index=3).all()
print([item.name for item in stu])

# 原生sql
stu = db_session.query(Student).from_statement(text("select * from student where name=:name")).params(name="屁屁").first()
print(stu.name,stu.stu2sch.name)

# 排序，默认正序.asc(),倒序.desc()
stu = db_session.query(Student).order_by(Student.school_id.desc()).all()
print([(item.school_id,item.name,item.stu2sch.name) for item in stu])
# [(1, '屁屁', '湖南理工学院'), (1, 'Ac', '湖南理工学院'), (1, 'Af', '湖南理工学院'), (1, 'Ae', '湖南理工学院'), (2, 'Ah', '长沙理工大学'), (2, 'Ag', '长沙理工大学'), (2, 'Ab', '长沙理工大学'), (3, 'Ad', '湖南大学'), (3, 'Aa', '湖南大学'), (3, 'Css', '湖南大学')]

# 区间
stu = db_session.query(Student).filter(~Student.id.between(5,9)).all()
print([item.name for item in stu])

# 不在列表中的 ~表示取反
stu = db_session.query(Student).filter(~Student.id.in_([8,9,6])).all()
print([item.name for item in stu])

# 组合查询
stu = db_session.query(Student).filter(
    or_(
        Student.id.in_([4,5]),
        and_(Student.school_id==1,Student.id>=9),
        Student.name != ""
    )
)
print([item.name for item in stu])

# 通配符
stu = db_session.query(Student).filter(~Student.name.like("A%"))
print([item.name for item in stu])

# 限制(切片)
stu = db_session.query(Student)[2:5]
print([item.name for item in stu])

# 原有基础上加或减
db_session.query(Student).filter(Student.school_id==3).update({Student.school_id:Student.school_id-1},synchronize_session="evaluate")

# 原有基础上字符串拼接
db_session.query(Student).filter(Student.school_id == 2).update({Student.name:Student.name+"长沙理工大学"},synchronize_session=True)
"""

db_session.commit()
db_session.close()