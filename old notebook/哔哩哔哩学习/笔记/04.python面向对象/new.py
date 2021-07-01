class Singleton(object):
    def __new__(cls, *args, **kwargs):  # new方法分配空间，创建对象
        if not hasattr(cls, "_instance"):
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance


class MyClass(Singleton):
    def __init__(self, name):
        if name is not None:
            self.name = name


a = MyClass('a')
print(a.name, a)  # a <__main__.MyClass object at 0x000001F75F97AA60>

b = MyClass("b")

print(a.name, a)  # b <__main__.MyClass object at 0x000001F75F97AA60>

print(b.name, b)  # b <__main__.MyClass object at 0x000001F75F97AA60>
