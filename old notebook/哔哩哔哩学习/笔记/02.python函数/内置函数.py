(68个)sorted() filter()map()
#反射#4
    setattr()                       #根据字符串为参数，去动态的设置一个成员(内存)  setattr(xx,'func',lambda x:x+1)
    delattr()                       #根据字符串为参数，去动态的删除一个成员(内存)  delattr(xx,'func')
    getattr()                       #根据字符串为参数，找到模块中与之同名的成员
    hasattr()                       #根据字符串为参数，判断模块中有没有与之同名的成员(函数或者变量)
                                    #模块
                                         # form types import FunctionType    #输入参数执行模块中的函数或者变量
                                         # form module
                                         # val=input('请输入')
                                         # if hasattr(module,val):
                                         #     func=getattr(module,val)
                                         #     if isinstance(func,FunctionType):
                                         #         func()
                                         #     else
                                         #         print(func)
                                         # else:
                                         #     print('没有这个成员')
                                    #类  #class Ass:
                                         #    def aaa(self):
                                         #        print('aaa')
                                         # obj=Ass()
                                         # v=getattr(obj,'aaa')#方法
                                         # v=getattr(Ass,'aaa')#函数
面向对象#9
    issubclass()                    #(子类， 父类)判断参数1是不是参数二的子类，或者子类的子类
    type()                          #获取当前对象是由哪个类创建的   type(obj)==Ass
    isinstance()                    #(对象，类)判断第一个参数(对象)是不是第二个参数(类/类的父类)的实例,和type类似，但是type只判断一级
                                        #from types import MethodType,FunctionType      #判断是方法还是函数
                                        # def check(arg):
                                        #    if isinstance(arg,MethodType)
                                        #         print('这是一个方法')
                                        #    elif isinstance(arg,FunctionType)
                                        #         print('这是一个函数')
                                        #    else:
                                        #         print('不知道是什么')
    callable()                      #判断是否可以被调用

#作用#2
#迭代器生成器#3
    iter()                          #n._iter_()等于iter(n)
    next()                          #n._next_()等于next(n)
    range()
#基础数据类型#38
    #和数字相关的
        #数据类型
            bool()                  #数据类型转换成bool类型
            int()                   #数据类型转换成int类型
            float()                 #数据类型转换为float类型(浮点)
            complex()               #数据类型转换为complex类型(复数)格式：a=1+0j
        #进制转换
            bin()                   #求二进制(0b00)
            oct()                   #求八进制(0o00)
            hex()                   #求十六进制(0x00)
        #数学运算
            abs()                   #求绝对值
            divmod()                #计算商和余数divmod(除数,被除数)   结果(商,余)
            round()                 #四舍五入round(求的数字，保留小数点后位数，默认1位)
            pow()                   #求次幂pow(a,3,b)等于a**a**a%b  二的三次方取余
            sum()                   #求和sun([a,b,c],d),a+b+c后再加d
            min()                   #求最小值min(a,b,c,d)
            max()                   #求最大值max(a,b,c,d)
    #和数据结构相关的
        #序列
            #元组和列表
                list()              #将数据类型转换成列表
                tuple()             #将数据类型转换成元组
            #字符串
                str()               #数据类型转换成str类型
                format()            #格式化输出
                                    #字符#format(s,'^20')拉长到20，居中    和center(20,' ')一样
                                        #format(s,'<20')拉长到20，左对齐
                                        #formar(s,'>20')拉长到20，又对齐
                                    #数据#format(3,'b')二进制
                                        #format(97,'c')unicode
                                        #format(11,'d')十进制
                                        #format(11,'o')八进制
                                        #format(11,'X')十六进制(大写)
                                        #format(11,'x')十六进制(小写)
                                        #format(11,'n')十进制
                                        #formar(11)十进制
                                    #浮点#format(123456789,'e')科学记数法，保留六位小数
                                        #format(123456789,'0.2e')科学记数法，保留两位小数(小写)
                                        #format(123456789,'0.2E')科学记数法，保留两位小数(大写)
                                        #format(1.23456789,'f')小数点计数法，保留六位小数
                                        #format(1.23456789,'0.2f')小数点计数法，保留两位小数
                                        #format(1.23456789e+10000,'F')小数点计数法
                bytes()             #转换为字节
                bytearray()         #返回一个新字节数组，这个数组里面元素是可变的，并且范围是[0,256]例bytearray('asdf',encoding='utf-8')
                memoryview()        #查看内存
                ord()               #输入字符，找到字符的编码位置 例如a-97,A-65
                chr()               #输入编码位置，找到字符 例如97-a,65-A
                ascii()             #判断是否属于ascii码，是就输出该字符，不是就输出unicode
                repr()              #原样输出字符串,也可以用r'abcd'
            #序列相关内置函数
                reversed()          #翻转，返回一个迭代器
                slice()             #切片s=lis[slice(开始，结尾，步长)]
        #数据集合
            #字典
                dict()              #字典
            #集合
                set()               #集合
                frozenset()         #s=frozenset({})不可变集合，可哈希
        #数据结构相关的内置函数
            len()                   #计算长度
            sorted()                #排序函数
                                        #key:排序方案，sorted函数内部会把可迭代对象中的每一个元素拿出来交给后面的key
                                        #后面的key算出来一个数字，作为当前这个元素的权重，整个函数根据权重进行排序
                                        #例如：
                                        #lst=[11,22,546,256,321,8781]
                                        #def func(n)
                                        #   return len(n)
                                        #ll=sorted(lst,key=func，reverse=True)#将lst中的每一个元素根据func算出字符长短，按顺序排序
                                        #print(ll)                              #reverse=Ture为反向排序
            enumerate()             #枚举 for i,j in enumerate(l,100)
            all()                   #and的意思  print(all([1,1,1,1]))里面东西都为真则真
            any()                   #or的意 思 print(any([1,1,1,1]))里面东西一个为真则真
            zip()                   #a=zip(lst1,lst2,lst3)将3个列表一一对应，输出迭代器，数组长度不统一，则过滤
            filter()                #过滤函数
                                        #lis=['王烁','张三','李四']
                                        # def func(fn):
                                        #     if fn[0]=='张':
                                        #         return False
                                        #     else:
                                        #         return True
                                        # h=filter(func,lis)#判断条件加数组，返回迭代器/或者funk可用/lambda el:el[0]!='张'/替代/
                                        # print(list(h))    #通过list()获取
            map()                   #映射函数
                                        # lst1=[1,2,3,4,5,6,7,8,9]
                                        # lst2=[1,2,3,4,5,6,7,8,9]#将可迭代对象中的每一个元素进行映射，
                                        # def func(fn,fp):        #分别去执行function，并建立一个新列表
                                        #     return fn+fp
                                        # h=map(func,lst1,lst2)    #或者#h=map(lambda el,ef:el+ef,lst1,lst2)
                                        # print(list(h))
#作用域#2
    globals()
    locals()
#其他#12
    #字符串类型代码
        eval()                      #k=eval('2+3*6')动态处理字符串,有返回值,字符串还原成字典，数组等
        exec()                      #可执行一个代码片段，没有返回值
        compile()                   #编译代码compile("要执行的代码段"，'文件名'，mode='模式')
                                        #3种模式
                                        # exec   存放流程语句
                                            code1='for i in range(10):print(i)'
                                            c1=compile(code1,''mode='exec')
                                            exec(c1)
                                        #exal   只放求值表达式
                                            code2='5+6'
                                            c2=compile(code2,'',mode='exal')
                                            a=exal(c2)
                                            print(a)
                                        # single 有交互是single
                                            code3="cont=inpt('请输入你的名字：')"
                                            c3=compile(code3,'',mode='single')
                                            exec(c3)
                                            print(cont)
    #输入输出
        print()                     #输出
                                        # file:  默认是输出到屏幕，如果设置为文件句柄，输出到文件
                                        # sep:   打印多个值之间的分隔符，默认为空格
                                        # end:   每一次打印的结尾，默认为换行符
                                        # flush: 立即把内容输出到流文件，不作缓存
                                        #例如：
                                            # import time
                                            # for i in range(0,101,2):
                                            #      time.sleep(0.1)
                                            #      char_num = i//2      #打印多少个'*'
                                            #      per_str = '\r%s%% : %s\n' % (i, '*' * char_num) if i == 100 else '\r%s%% : %s'%(i,'*'*char_num)
                                            #      print(per_str,end='', flush=True)
                                            # 打印进度条    \r 可以把光标移动到行首但不换行
        input()                     #输入
    #内存地址
        id()                        #算内存地址
        hash()                      #目的是为了储存，计算后是一个数字
    #文件操作
        open()
    #模块
        import                      #引用模块 _import_('os')
    #帮助
        help()                      #例help(str),帮助文档，比dir()多了注释
    #调用
        callable()                  #查看是否能被调用
    #内置属性
        dir()                       #查看内置属性
















abs()
dict()
help()
min()
setattr()
all()
dir()
hex()
next()
slice()
any()
divmod()
id()
object
sorted()
ascii()
enumerate
input()
oct()
staticmethod
bin()
eval()
int
open()
str
bool
exec
isinstance()
ord()
sum()
bytearray
filter()
issubclass()
pow()
super
bytes
float
iter()
print()
tuple
callable() 
format()
len()
property
type
chr()
frozenset
list
range
vars()
classmethod
getattr()
locals()
repr()
zip()
compile()
globals()
map()
reversed()
__import__()
complex
hasattr()
max()
round()
delattr()
hash()
memoryview
set