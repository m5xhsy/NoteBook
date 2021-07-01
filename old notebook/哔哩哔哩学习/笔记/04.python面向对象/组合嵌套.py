###嵌套
class School(object):
    def __init__(self,name,site):
        self.name=name
        self.site=site

    def teach(self):
        print('讲课')

class Teacher(object):
    def __init__(self,name,age,salary):
        self.name=name
        self.age=age
        self.__salary=salary
        self.school=None

obj1=School('湖南理工学院','湖南岳阳')
obj2=School('长沙理工学院','湖南长沙')

teacher1=Teacher('王屁屁',18,10000)
teacher2=Teacher('张屁屁',20,12000)

teacher1.school=obj1        #School嵌套到Teacher里面
teacher2.school=obj2

teacher2.school.teach()