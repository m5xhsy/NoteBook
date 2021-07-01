####################线程池
# from concurrent.futures import ThreadPoolExecutor           #只有python3有
# import time
# def func(args,test):
#     time.sleep(2)
#     print(str(args)+str(test))
#
# #创建一个线程池（最多五个线程）
# pool = ThreadPoolExecutor(5)
#
# for i in range(20):
#     #线程池中获取20个线程，只有5个，所以 每次执行5个
#     pool.submit(func,i,'666')

#####################进程池
# from concurrent.futures import ProcessPoolExecutor
# import time
# def task(arg):
#     time.sleep(2)
#     print(arg)
#
# if __name__ == '__main__':
#     pool=ProcessPoolExecutor(max_workers=5)
#     for i in range(20):
#         pool.submit(task,i)


###################map使用方法
# from concurrent.futures import ThreadPoolExecutor,ProcessPoolExecutor
#
# import os,time,random
# def task(n):
#     print('%s is runing' %os.getpid())
#     time.sleep(random.randint(1,3))
#     return n**2
#
# if __name__ == '__main__':
#
#     executor=ThreadPoolExecutor(max_workers=3)
#
#     # for i in range(11):
#     #     future=executor.submit(task,i)
#
#     executor.map(task,range(1,12)) #map取代了for+submit






######################回调函数
# from concurrent.futures import ThreadPoolExecutor,ProcessPoolExecutor
#
# import requests
# import json
# import os
#
# def get_page(url):
#     print('<进程%s> get %s' %(os.getpid(),url))
#     respone=requests.get(url)
#     if respone.status_code == 200:
#         return {'url':url,'text':respone.text}
#
# def parse_page(res):
#     res=res.result()
#     print(res)
#     print('<进程%s> parse %s' %(os.getpid(),res['url']))
#     parse_res='url:<%s> size:[%s]\n' %(res['url'],len(res['text']))
#     with open('d.txt','a') as f:
#         f.write(parse_res)
#
#
# if __name__ == '__main__':
#     urls=[
#         'https://www.baidu.com',
#         'https://www.python.org',
#         'https://www.openstack.org',
#         'https://help.github.com/',
#         'http://www.sina.com.cn/'
#     ]
#     p=ProcessPoolExecutor(3)
#     for url in urls:
#         p.submit(get_page,url).add_done_callback(parse_page) #parse_page拿到的是一个future对象obj，需要用obj.result()拿到结果

###################################################

    # from multiprocessing import Pool
    # p=Pool(3)
    # for url in urls:
    #     p.apply_async(get_page,args=(url,),callback=parse_page)   # 这里回调函数拿到的是返回的值
    # p.close()
    # p.join()





from multiprocessing.dummy import Pool
pool = Pool(5)

def func(a):
    return a*a

x = pool.map(func,[1,2,3,4,5])      # map相当于for循环+apply_async
print(x)
