##########线程锁
# import threading,time
# lock=threading.RLock()
# n=10
# def func(arg):
#     global n
#     print('这段代码不加锁',arg)
#     lock.acquire()          #加锁                                保护线程锁中的内容
#     print('当前线程:',arg,'读取的全局变量值:',n)
#
#     n=i
#     time.sleep(1)
#     print('当前线程:',arg,'修改后全局变量值:',n)
#     lock.release()          #释放锁
#
# for i in range(n):
#     t=threading.Thread(target=func,args=(i,))
#     t.start()
#
#





###########基本格式
# import threading
# import time
# def test(a):
#     time.sleep(5)
#     print(a)
#
# while 1:
#     a=input('>>>')
#     server=threading.Thread(target=test,args=(a))           #创建一个线程
#     server.start()                                              #执行test

############内容

import threading
import time
def func(arg):
    time.sleep(arg)
    t=threading.current_thread()        #获取当前线程
    name= t.getName()                   #获取名字
    id =threading.get_ident()           #获取线程唯一id值
    print(name,arg,id)

f1=threading.Thread(target=func,args=(2,))  #子线 程1
f1.setName('子线程1')          #设置名字
f1.setDaemon(True)
f1.start()

f2=threading.Thread(target=func,args=(4,))  #子线程2
f2.setName('子线程2')
f2.setDaemon(True)
f2.start()
# f2.join(2)                  #让主线程在这等两秒，无论是否执行完毕，会继续往下走
# f2.join()                   #让主线程在这等，直到这个线程执行完毕才往下走

f3=threading.Thread(target=func,args=(9,))  #子线程3
f3.setName('子线程2')
f3.setDaemon(True)          #主线程执行完直接关闭，不等子线程
f3.start()

time.sleep(5)                               #主线程
print(5)


#############面向对象相关
# import threading
# class my_threading(threading.Thread):
#     pass
#
# def func(arg):
#      print(arg)
#
# t1=my_threading(target=func,args=('111',))
# t1.start()



#########服务器相关
# ######客户端
# import socket
# client=socket.socket()
# client.connect(('192.168.121.1',8808))
# while 1:
#     res=input('>>>')
#     client.send(res.encode('utf8'))
#     if res=='exit':
#         break
#     else:
#         fs=client.recv(1024).decode('utf8')
#         print(fs)
# client.close()
#
# ######服务器
# import socket
# import threading
#
# def test(conn,server):
#     while 1:
#         try:
#             rst = conn.recv(1024)
#             if rst==b'exit':
#                 break
#             else:
#                 conn.send(rst+b'sb')
#         except ConnectionResetError:
#             print('用户异常中断')
#             return
#     conn.close()
#     print('用户退出')
#
#
# server=socket.socket()
# server.bind(('192.168.121.1',8808))
# server.listen(5)
# while 1:
#     try:
#         conn,addr=server.accept()
#         threading_server=threading.Thread(target=test,args=(conn,server,))
#         print(addr[0],'接入')
#         threading_server.start()
#     except OSError:
#         pass
