#语法  a=lambda 参数：返回值////////如果返回值是2个则返回值应用元组//函数只能一行//返回值可以是任意数据类型//函数名是<lambda>
a=lambda n:n*n                #相当于#def func(n):
print(a(5))                         #return n*n
                                    #print(func(5))




print(fn._name_)              #可查看真实的函数名

def func(n):
    print(n)
    pass
c=func
b=c
print(b.__name__)