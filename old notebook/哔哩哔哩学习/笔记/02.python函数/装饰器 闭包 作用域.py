#*****作用域*****
'''
globals()                                              #查看全局作用域
locals()                                                  #查看当前作用域
globals a                                              #全局中a引用到函数
                                                       #全局中没有a则创建
nonlocal a                                             #找函数外面一层离他最近的变量




#****闭包*****内层函数应用了外层函数的环境变量，这种函数叫做闭包函数
print(inner._closure_)                                  #判断函数是否闭包，否则为None
                                                        # def ct():
                                                        #     a=1
                                                        #     def kc():
                                                        #         print(a)
                                                        #     print(kc.__closure__)
                                                        #     return kc
                                                        #ct()



def foo():
    x = 2
    y = 2
    def func():
        z = 3
        print(x)
        print(z)
    return func

fun = foo()
print(fun.__closure__[0].cell_contents)         #2
'''



# #################装饰器#############
# L:
# E:
# G:
# B:内置
#基于封闭原则
'''
def index():

    print('this is index')
def login():
    user = input('user>>>')
    pswd = input('pswd>>>')
    if user == 'm5xhsy' and pswd == '123':
        print('登录成功!')
        index()
    else:
        print('登录失败!')
login()
'''
###基于开放原则
'''
def login(func):
    user = input('user>>>')
    pswd = input('pswd>>>')
    if user == 'm5xhsy' and pswd == '123':
        print('登录成功!')
        func()
    else:
        print('登录失败!')

def index():
    print('this is index')

def home():
    print('this is home')

login(index)
login(home)
'''
#基于开放封闭原则
'''
def login(func):        #func为外部函数的环境变量  login是装饰器函数
    def inner():
        user = input('user>>>')
        pswd = input('pswd>>>')
        if user == 'm5xhsy' and pswd == '123':
            print('登录成功!')
            func()
        else:
            print('登录失败!')
    return inner        
@login          # 相当于index = login(index)        #index指向inner
def index():
    print('this is index')

index()
'''

#举例
import time
def times(func):
    def inner():
        now = time.time()
        func()
        print(time.time() - now)
    return inner

@times
def add():
    ret = 1
    for i in range(30000000):
        ret = ret + i
    print(ret)

add()





##############
import functools
def wai(func, *args, **kwargs):
    @functools.wraps(func)      # 保留原始属性
    def session_wai():
        if not request.cookies:
            return redirect('/login')
        return func()
    return session_wai