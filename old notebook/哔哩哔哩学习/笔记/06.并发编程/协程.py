# 由程序员创造的操作系统中不存在的东西，可以认为是微线程
# import sys
# sys.path.append(r'c:\python3.8\lib\site-packages')
# def func1():
#     print(11)
#     gr2.switch()
#     print(22)
#     gr2.switch()
#
# def func2():
#     print(33)
#     gr1.switch()
#     print(44)
#
# gr1=greenlet.greenlet(func1)
# gr2=greenlet.greenlet(func2)
# gr1.switch()



#####################协程+遇到IO就切换
import sys
sys.path.append(r'c:\python3.8\lib\site-packages')
sys.path.append(r'')
import greenlet             #协程模块
import requests
from gevent import monkey
monkey.patch_all()          #代码中遇到IO自动切换

def get_page(url):
    ret=requests.get(url)
    print(url,ret.text)

greenlet([
    greenlet.spawn(get_page,'http://tianqi.sogou.com/?tid=101250101'),
    greenlet.spawn(get_page,'http://time.tianqi.com/'),

])







#也可以通过yield来写协程