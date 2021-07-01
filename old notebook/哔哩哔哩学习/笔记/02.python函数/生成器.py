def func():         #生成器函数
    print(1)
    yield          #相当于return，都可以返回数据,但是不会彻底中断函数，分段执行
    print(2)
    print(2)
    yield

gen=func()          #获取生成器，不执行函数
print(func().__next__())
print(gen.__next__())



#####################send()和_next_一样可以执行下一个yield,并且可以给上一个yield传值
def func():
    print(1)
    a=yield 1
    print(2)
    b=yield 2
    print(3)
    yield 3 #最后一个yield不能传值
gen=func()
print(gen.__next__())   #第一个只能用——next()
print(gen.send('1.1'))  #send()必须传值
print(gen.send(2.2))

#####################
for i in func():#for内部有_next_()
    print(i)

print(list(func()))#内部有_next_()





# 对比yield 与 yield from
def func():
    lst = ['卫龙','老冰棍','北冰洋','牛羊配']
    yield lst
g = func()
print(g)
print(next(g))  # 只是返回一个列表
def func():
    lst = ['卫龙','老冰棍','北冰洋','牛羊配']
    yield from lst
g = func()
print(g)
print(next(g))# 他会将这个可迭代对象(列表)的每个元素当成迭代器的每个结果进行返回。
print(next(g))
print(next(g))
print(next(g))



#典型例题
def add(a,b):
    ruturn a+b
def test():
    for i in range(4):
        yeild i
g =test()
for n in [5,10]
    g=(add(n,i) for i in g)
print(list(g))

分析
def add(a,b):
    ruturn a+b
def test():
    for i in range(4):#i=0,1,2,3
        yeild i
g =test()#获取生成器
for n in [5,10]             #只记录代码，不取值
    g=(add(n,i) for i in g)   #g=(add(n,i) for i in add(n,i) for i in g) 最后执行时取10
print(list(g))
