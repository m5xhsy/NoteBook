######常用方法####使用方法查看线程
- join
- deamon
- name
- multiprocessing.current_process()
- multiprocessing.current_process().ident/pid





import multiprocessing
######windows下运行的方法一：
def test(arg):
    print(arg)

if __name__ == '__main__':
    for i in range(20):
        p=multiprocessing.Process(target=test,args=(i,))
        p.start()

######windows下运行的方法二：
def test(arg):
    print(arg)

def func():
    for i in range(20):
        p = multiprocessing.Process(target=test, args=(i,))
        p.start()

if __name__ == '__main__':
    func()


#####linux或者mac下运行
def test(arg):
    print(arg)


for i in range(20):
    p = multiprocessing.Process(target=test, args=(i,))
    p.start()





##########################数据不共享
import multiprocessing
lst_data=[]
def func(arg):
    lst_data.append(arg)
    print(lst_data)
if __name__ == '__main__':
    for i in range(20):
        p=multiprocessing.Process(target=func,args=(i,))
        p.start()
############################数据共享
########队列
import multiprocessing,time
q=multiprocessing.Queue()
def func(arg,q):
    q.put(arg)
    # print('当前进程',arg,q.get())

if __name__ == '__main__':
    for i in range(20):
        p=multiprocessing.Process(target=func,args=(i,q))       #windows下得把q传进去
        p.start()
    time.sleep(3)
    while True:
        x=q.get()
        print(x)
########字典
import multiprocessing,time
def test(arg,dic):
    dic[arg]=100

if __name__ == '__main__':
    m = multiprocessing.Manager()

    dic = m.dict()
    for i in range(20):
        p = multiprocessing.Process(target=test, args=(i,dic,))     #windows得传参
        p.start()
    time.sleep(1)
    print(dic)
    p.is_alive()                #判断怕是否执行完毕




##############################类继承方式

import multiprocessing
class Myprocess(multiprocessing.Process):
    pass

def run(i):
        print(i)

if __name__ == '__main__':
    for i in range(20):
        p=Myprocess(target=run,args=(i,))
        p.start()