
class Ass(object):
    __slots__ = ("__storage__", "__ident_func__")  # 限定类只能有这2个属性
    '''注释文档'''
    def __init__(self,x1,x2):
        self.x1=x1
        self.x2=x2
        self.dict={'ccc':'cc'}

    def __call__(self,*args,**kwargs):
        print(args,kwargs)
        return 0

    def __getitem__(self, item):
        print(item)
        return 1

    def __setitem__(self, key, value):
        print(key,value)


    def __delitem__(self,key):
        print(key)

    def __add__(self, other):
        return  self.x1+other.x2

    def __enter__(self):
        print(258)
        return 456

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(369)

    def __str__(self):
        return '内存地址'

    def __iter__(self):
        #也可以是生成器
        # yield 'aa'
        # yield 'bb'
        # yield 'cc'
        return iter([11,22,33,55,66,66])#返回迭代器

    def __setattr__(self, key, value):
        pass

    def __getattr__(self, item):
        raise xxx       #属性未被找到执行
#1 类名() 自动执行 __init__
obj=Ass(666,888)
obj1=Ass(111,222)
#2 对象() 自动执行 __call__
print(obj(4,5,6,k=5))

#3 对象['xx'] 自动执行 __getitem__
print(obj['abc'])

#4 对象['xx']=11 自动执行 __setitem__
obj['aaa']='bbb'

#5 del 对象['xx'] 自动执行 __delitem__
del obj['ccc']

#6 对象+对象 自动执行 __add__
print(obj1+obj)

#7 with 对象 自动执行 __enter__和__exit__
with obj as f:      #__enter__有返回值
    print(f)
    print(147)      #258>456>147>369

#8  修改对象的内存地址变成字符串
print(obj,type(obj))

#9 获取注释文档
print(obj.__doc__)

#10 把类里面封装的数据以字典返回
print(obj1.__dict__)

#11__iter__将对象转换为可迭代对象，返回一个迭代器iter([11,22,33,44,])
for i in obj1:
    print(i)

#12
class Foo(object):
    def __init__(self,a1,a2):
        '''
        为空对象进行数据初始化
        :param a1:
        :param a2:
        '''
        print(1)
        self.a1=a1
        self.a2=a2

    def __new__(cls, *args, **kwargs):
        '''
        创建一个空对象,真正意义上的上的构造方法
        :param args:
        :param kwargs:
        '''
        print(2)
        return  object.__new__(cls)         #object.__new__(cls) ，内存地址和obj2一样，但是没有值，__init__是为其赋值

obj2=Foo(2,3)








#等等。。。。