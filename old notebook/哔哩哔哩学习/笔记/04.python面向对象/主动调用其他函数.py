######方式一##与继承无关
class Ass(object):
    def func(self):
        print('Ass')

class Bss(object):
    def func(self):
        print('Bss')
        Ass.func(self)          #需要手动传self
obj=Bss()
obj.func()

######方式二##按照当前类的继承顺序往上找
例1：
class Ass(object):
    def func(self):
        print('Ass')

class Bss(Ass):
    def func(self):
        print('Bss')
        super().func()          #按照执行顺序找下一个

obj=Bss()
obj.func()


例2
class Ass(object):
    def func(self):
        print('Ass')

class Bss(object):
    def func(self):
        super().func()  # 按照执行顺序找下一个,Css>Bss>Ass,所以先找Css,再找Bss
        print('Bss')

class Css(Bss, Ass):
    pass

obj = Css()
obj.func()