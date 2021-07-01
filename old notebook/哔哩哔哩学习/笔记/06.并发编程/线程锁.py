import threading,time
# ############################lock=threading.Lock               #同步锁，锁一个放一个

# 方法和递归锁一样


############################### lock=threading.RLock                #递归锁
# import threading,time
# lst=[]
# lock=threading.RLock()
# def func(i):
#     lock.acquire()
#     v=threading.current_thread()
#     time.sleep(1)
#     name=v.getName()
#     lst.append(name)
#     print(i,lst[-1])
#     lock.release()
# for i in range(100):
#     t=threading.Thread(target=func,args=(i,))
#     t.setName(str(i))
#     t.start()


################################# lock =threading.BoundedSemaphore(n)  一次锁n个
# import time
# lock =threading.BoundedSemaphore(3)
# def func(arg):
#     lock.acquire()
#     time.sleep(3)
#     print(arg)
#     lock.release()
#
# for i in range(20):
#     t=threading.Thread(target=func,args=(i,))
#     t.start()



################################### lock = threading.Condition()        条件锁
# lock = threading.Condition()
# def ifs():
#     input()
#     return True
#
# def func(arg):
#     lock.wait_for(ifs)    #加锁
#     print(arg)
#
# for i in range(20):
#     t = threading.Thread(target=func, args=(i,))
#     t.start()



###########################lock=threading.Event()
# lock=threading.Event()
# def func(arg):
#     print('线程')
#     lock.wait()
#     print(arg)
#
# for i in range(20):
#     t=threading.Thread(target=func,args=(i,))
#     t.start()
#
# input('>>>')
# lock.set()                      #全部释放
# input('>>>')
# lock.clear()                    #再次锁住


# 线程安全  (用空间换时间，线程id执行数据)

import threading,time
from threading import local


class Ass(local):
    pass


foo = Ass()


def func(args):
    foo.name = args
    time.sleep(3)
    print(str(args)+'>'+str(foo.name)+'>'+str(threading.current_thread().ident))


for i in range(20):
    th = threading.Thread(target=func, args=(i,))
    th.start()