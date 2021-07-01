from model_demo.SQLAlchemy_demo.model2 import engine,User,Hobby
from sqlalchemy.orm import sessionmaker

Session = sessionmaker(engine)
db_session = Session()


# 增加
# 正向
# user_obj = User(name="m5xhsy",user2hobby=[Hobby(name="足球"),Hobby(name="篮球"),Hobby(name="游泳")])
# db_session.add(user_obj)
# 反向
# hobby_obj = Hobby(name="游泳")
# hobby_obj.hobby2user = [User(name="Ass"),User(name="Bss"),User(name="Css")]
# db_session.add(hobby_obj)


user_list = db_session.query(User).all()
print([(user_obj.name,[item.name for item in user_obj.user2hobby]) for user_obj in user_list])
# [('Ass', ['游泳']), ('Bss', ['游泳']), ('Css', ['游泳']), ('m5xhsy', ['篮球', '游泳', '足球'])]

hobby_list = db_session.query(Hobby).all()
print([(hobby_obj.name,[item.name for item in hobby_obj.hobby2user]) for hobby_obj in hobby_list])
# [('游泳', ['m5xhsy']), ('游泳', ['Ass', 'Bss', 'Css']), ('篮球', ['m5xhsy']), ('足球', ['m5xhsy'])]


db_session.commit()
db_session.close()