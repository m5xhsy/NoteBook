
成员分三类
1.变量
    -实例变量(字段)       #实例变量(字段)访问时，使用对象访问，即：obj1.name
        -公有实例变量(字段)
        -私有实例变量(字段)
    -类变量(静态字段)      #类变量(静态字段)访问时，使用类访问，即：Ass.country
        -公有类变量(静态字段)
        -私有类变量(静态字段)
        例如：
            class Ass:
                country = '中国'  # 类变量，不同的对象共用
                __city = '长沙'  # 私有类变量，内部能访问，外部不能，加双下划线表示私有         #派生类也访问不到私有变量，但是可以通过基类的函数访问到

                def __init__(self, name):
                    self.name = name  # 公有实例变量，不同的对象值不同
                    self.__age = 21  # 私有实例变量，内部能访问，外部不能，加双下划线表示私有

                def func(self):
                    print(self.__age)  # 私有实例变量可通过函数间接执行
                    print(Ass.__city)  # 私有类变量可通过函数间接执行
            obj1 = Ass('张三')
            obj2 = Ass('李四')
            obj1.func()
            print(obj1.country)
            print(obj2.country)
            obj1.country = '美国'  # 修改实例变量，先找自己的内存有没有country，没有就创一个，并赋值
            print(obj1.country)
            print(obj2.country)
            Ass.country = '法国'  # 修改类变量，obj1已经被修改过一次所以，这条语句 只修改了李四的
            print(obj1.country)
            print(obj2.country)

2.方法                #在函数前面加__属于私有方法，规则和私有变量一样
    -实例方法
    -静态方法
    -类方法
        例如:
            class Ass:
                def __init__(self, name):
                    self.name = name
                    self.age=10

                def func1(self):    # 实例方法
                    print(self.name)

                @staticmethod       # 静态方法，如果没调用__init__中的内容，可以用静态方法，函数前加@ststicmthod
                def func2(x1,x2):
                    print(666,x1,x2)

                @classmethod        #类方法，需要借用类，但不想传参的函数         函数前面加@classmethod
                def func3(cls,x1,x2):
                    print(x1)
                    print(x2)
                    print(cls)

            obj = Ass('王烁')       #实例方法的调用
            obj.func1()

            Ass.func2(777,888)       #静态方法的调用，推荐用类调用
            obj.func2(777,888)

            Ass.func3('abc','123')  #类方法的调用，推荐用类调用
            obj.func3('abc','123')

3.属性                            #也有私有属性和公有属性，规则和前面的一样
    class Ass:
        def __init__(self):
            pass
        """
        # 与下面@property一样
        def ass(self):
            return 123
        
        ass = property(ass)
        """
        @property               #属性  函数前面加@property
        def func(self):         #参数只有一个self
            pass
            return 123
    obj = Ass()
    print(obj.func)             #调用时无需加括号，当无需传参且有返回值时可以用属性



class Ass():
    @property
    def user(self):
        return self._user

    @user.setter
    def user(self, value):
        print("set user")
        self._user = value

    @user.deleter
    def user(self):
        print("del user")
        del self._user

p1 = Ass()
p1.user = "m5xhsy"
print(p1.user)
del p1.user