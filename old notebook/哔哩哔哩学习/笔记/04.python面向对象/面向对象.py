面向对象三大特性：多态，继承，封装
######面向对象的格式：

#普通用法
    定义1
        class 类名:               #定义了一个类
            def 函数名(self,参数1,参数2):     #在类中定义了一个方法
                pass
    调用
        obj=类名()                 #创建了一个对象/实例化一个对象#obj称为类的对象或者类的实例
        obj.函数名(参数1,参数2)               #通过对象调用其中的方法



#构造方法
    定义
        class 类名:
            def __init__(self,参数1,参数2):  # 特殊方法(构造方法)进行数据初始化
                self.n1=参数1     #实例对象
                self.n2=参数2     #将数据封装在
            def 函数1(self):
                pass
            def 函数2(self):
                pass
    调用
        x1 = 类名(参数1,参数2)       #类名加括号引出特殊方法
        x1.函数1()                    #类的内部也可以调用，self.函数1()
        x2.函数2()
 


#打包
def func(arg):
    print(arg.k1)
    print(arg.k2)
    print(arg.k3)

class Foo:
    def __init__(self,k1,k2,k3):
        self.k1 = k1
        self.k2 = k2
        self.k3 = k3

obj=Foo(111,222,333)
func(obj)

#
class Files:
    def __init__(self,path):
        self.path=path
        self.f=open(self.path,'w')
    def xx1(self):
        pass
    def xx2(self):
        pass
obj=Files(path)
obj.xx1()
obj.xx2()
obj.f.close()


######如何写
方法一：归类+提取公共值
方法二：在指定类中编写和当前类相关的所有代码+提取公共值