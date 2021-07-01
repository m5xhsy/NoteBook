#######获取错误的堆栈信息
import traceback

def func():
    try:
        a=a+1
    except Exception as e:
        error_msg=traceback.format_exc()
        print(error_msg)
func()

######else和finall
try:
    print('aaaa')#给某某发邮件
except ValueError:
    print('ValueError')#某某错误
except IndexError:
    print('IndexError')#某某错误
except Exception as e:
    print('Exception')#万能
else:
    print('发送成功')#没发生错误就执行
finally:
    print('')#无论如何都执行，即使return遇到finally也会先执行finall中的代码（网络连接，数据库连接，关闭文件句柄）

#try...except...
#try...finally
#try...except...else
#try...except...finally
#try...except...else...finally

######主动抛异常
raise ValueError
raise ValueError(未知错误)#给程序员用，对用户不能主动抛异常

######断言
assert 1==2  #程序满足的先决条件,一般不会用到，看源码会用到
相当于
if 1==int(input()):
    pass
else:
    assert AssertionError


######多步异常处理
lst=[5,3]
while 1:
    print('————————————————————\n\t1.薯片\n\t2.可乐')
    xx=input('请输入你要购买的商品:')
    try:
        print('\t{}元'.format(lst[int(xx)-1]))
        continue
    except ValueError:
        print('请输入正确的数字!')
        continue
    except IndexError:
        print('请输入正确的选项!')
        continue


######多步合并异常处理
lst=[5,3]
while 1:
    print('————————————————————\n\t1.薯片\n\t2.可乐')
    xx=input('请输入你要购买的商品:')
    try:
        print('\t{}元'.format(lst[int(xx)-1]))
        continue
    except (ValueError,IndexError):
        print('请输入合法的选项!')
        continue


######万能异常处理
###1
lst=[5,3]
while 1:
    print('————————————————————\n\t1.薯片\n\t2.可乐')
    xx=input('请输入你要购买的商品:')
    try:
        print('\t{}元'.format(lst[int(xx)-1]))
        continue
    except Exception as e:
        print(e.args)
        print('请输入合法的选项!')
        continue

###2
lst=[5,3]
while 1:
    print('————————————————————\n\t1.薯片\n\t2.可乐')
    xx=input('请输入你要购买的商品:')
    try:
        print('\t{}元'.format(lst[int(xx)-1]))
        continue
    except:         #也相当于except Exception as e:
        print('请输入合法的选项!')
        continue




#也可以先写多分支异常再写万能异常

#########自定义异常
# 1111111111111111111111111111111111111111111111
import os
class ExistsError(Exception):
    pass

class KeyInvalidError(ExistsError):
    pass

def func(path,prev):
    error_dic={'code'='None','msg'='None'}
    try:
        if not os.path.exists(path):            #主动抛出异常
            raise ExistsError()
        if not prev:
            raise KeyInvalidError()
        pass
    except ExistsError as e:                    #自己捕获异常
        error_dic['code']=1001
        error_dic['msg']='文件不存在'
    except KeyInvalidError as e:
        error_dic['code'] = 1002
        error_dic['msg'] = '关键字不存在'
    except Exception as e:
        error_dic['code'] = 1003
        error_dic['msg'] = '未知错误'
    return error_dic

#222222222222222222222222222222222222222222
import os
class ExistsError(Exception):
    def __init__(self,code,msg):
        self.code=code
        self.msg=msg

class KeyInvalidError(ExistsError):
    def __init__(self, code, msg):
        self.code = code
        self.msg = msg

def func(path,prev):
    error_dic={'code':None,'msg':None}
    try:
        if not os.path.exists(path):            #主动抛出异常
            raise ExistsError(1001,'文件不存在')
        if not prev:
            raise KeyInvalidError(1002,'关键字不存在')
        pass
    except ExistsError as obj1:                    #自己捕获异常，实例化
        print(obj1.code,obj1.msg)
    except KeyInvalidError as obj2:
        print(obj2.code, obj2.msg)
    except Exception as e:
        print(1003,'未知错误')
    return error_dic