######封装
封装：
    将相关功能封装到一个类中：
    class Mssage:
        def email(self):pass
        def wechat(self):pass
        def msg(self):pass
    将数据封装到一个对象中
    class Person:
        def __init__(self,name,age,gender):
            self.name=name
            self.age=age
            self.gender=gender
    obj=Person('张三','18','男')
继承： #一对一或一对多
    class Ass:          #父类/基类(相对而言)
        def fa(self):
            print('fa')
    class Bss(Ass):     #子类/派生类(相对而言)
        def fb(self):
            print('fb')
    class Css(Bss):
        def fc(self):
            print('fc')
    obj=Css()
    obj.fa()
    obj.fb()
    obj.fc()
    #先在自己类中找，没有就去父类#提高代码重用性
多继承  #只有python支持
    class Ass:  # 父类/基类(相对而言)
        def fa(self):
            print('fa')
    class Bss(Ass):  # 子类/派生类(相对而言)
        def f(self):
            print('fb')
    class Css(Bss,Ass):     #优先左边的Bss
        pass
    obj =Css()
    obj.fa()

多态  #多种形态或多种状态
    #python原生支持多态，所以没有什么特殊性
    #鸭子模型
    #由于python传参时无序指定类型
