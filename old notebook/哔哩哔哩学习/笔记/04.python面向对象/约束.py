######约束
class Ass(object):  #用于约束Bss或者更多的子类
    def send(self):
        """
        必须继承Ass，然后必须编写send方法，用于完成业务逻辑
        """
        raise NotImplementedError("send()必须被重写")


class Bss(Ass):     #必须实现Ass中的功能，否则会主动抛异常
    pass
    def send(self):
        pass

obj=Bss()
obj.send()


######抽象类和抽象方法          #一般不用
from abc import ABCMeta,abstractstaticmethod,abstractmethod
class Ass(metaclass=ABCMeta):
    def f1(self):
        pass

    @abstractstaticmethod           #抽象方法
    def f2(self):
        pass
    @abstractmethod
    def f3(self):
        pass

class Bss(Ass):
    def f3(self):                   #必须继承Ass中的f2()
        print(123)

obj=Bss()
obj.f1()
obj.f2()




"""
######其他知识点
python：
        类：
            class Ass:
                pass

java/c#:
        接口：
            interface Ass:          #接口中的方法不能写代码，只能约束继承他的类必须实现接口中定义的所有方法。
                def f1(self,x1):pass

                def f2(self,x1):pass

            #如果类中继承了Ass，必学包含接口中定义的所有的方法
            #可以继承多个接口
        类：
            类：
                class Ass:
            抽象类：        #也可以做约束，约束继承他的派生类必须实现他的抽象方法
                abstract class Ass：
                    def f1():              #普通方法子类可以不写
                    abstract def f2():pass #不能写代码，抽象方法子类必须也有

"""