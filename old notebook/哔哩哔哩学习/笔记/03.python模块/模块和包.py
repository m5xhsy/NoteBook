'''
#什么是模块
        #已经写好的一组功能的集合(别人写好的函数，变量，方法放在一个文件里，这个文件可以被我们直接使用，这个文件就是模块)
        #py文件  all文件  zip文件

#如何自己写一个模块
        #创建一个py文件，起一个符合变量命名规则的名字，这个就是模块名

#模块的导入
        #先导入内置模块，再导入第三方模块，最后导入自定义模块。(python规则)
        #导入一个模块就是执行一个模块

#import
        #import被导入的过程中发生了什么事
            #1找到这个模块
            #2判断这个模块是否被导入
            #3没有被导入就创造这个模块的命名空间
            #4让这个模块的名字指向这个命名空间
            #5执行这个模块的代码
        #命名空间
            #模块和当前文件在不同的命名空间
        #为模块起别名
            #import my_moddule as m         #找my_module,找到后给my_module起一个命名空间叫m，起了别名之后使用这个模块只能用别名调
            #例如：
                #def func(dic,t='json')
                #   if t=='json':
                #       import json as aaa
                #   elif t=='pickle':
                #       import pickle as aaa
                #returm aaa.dumps(dic)
        #一行导入多个模块       #建议多行导入
            #import os,time
            #import os as o,time as t

#from import
        #from import导入的过程中发生了什么事
            #1找到要导入的模块
            #2判断这个模块是否被导入过
            #3如果这个模块没有被导入过
                #创建一个属于这个模块的命名空间
                #执行这个文件
                #找到你要导入的变量
                #给你要导入的变量创建一个引用，指向要导入的变量
            #4如果这个模块已经被导入过
                #找到你要导入的变量
                #给你要导入的变量创建一个引用，指向要导入的变量
        #命名空间
            #模块和当前文件在不同的命名空间
        #为变量起别名
            #from my_module import read1 as r1,read2 as r2
        #一行导入多个名字
            #from my_module import read1,read2
        #*和_all_的关系
            #form my_module import *    #在当前文件命名空间创建了模块中的变量指向模块的命名空间，指向关系可破坏
            #_all_和import *的关系：*会参靠_all_变量，约束了*导入的变量的内容
            #_all_=['name','read1','read2']  #只约束*的导入方式
    #模块引用中的情况
        #模块的循环利用
            #一个纯的 函数组成的 多个模块之间不能循环使用
        #模块的加载与修改
            #已经被导入的模块再去修改，不会影响当前文件的引用
            #要想修改的模块被正在运行的程序感知，要重新运行程序
        #把模块当作脚本来执行
            #在cmd或者pycharm里面执行  脚本执行
            #导入这个文件              模块执行
            一个文件中的_name_变量
                #当这个文件被当作脚本执行的时候，_name_=='_main_'
                #当这个文件被当成模块执行的时候，_name_=='模块名'
                #if __name__ == '__main__':     #输入main再按Tab自动生成
        #模块的搜索路径
            # import sys
            # path=r'A:'
            # sys.path.append(path)
            # import a


#包:文件夹下面有一个_init_.py的包，是几个模块的集合
    #导入模块
        #import 文件夹1.文件夹2.py文件名  as 别名          #不用别名，调用函数的话就要写成： 文件夹1.文件夹2.py文件名.函数
        #from 文件夹1.文件夹.py文件名 import 函数名        #调用不用写那么长，py文件名.函数()就可以调用
        #from 文件夹1.文件夹 import py文件名               #import不能有带点的
    #导入包
        #绝对导入
            #制定_init_
            #缺点如果当前导入包的文件和被导入包的位置关系发生了调整，那么_init_文件里面位置也要发生改变
            #所有的导入都要从根目录下往后去解释文件之间的关系
            #这个脚本以及和这个脚本同级的模块中都只能用绝对导入
            #包和当前文件永远在同级目录下，不会发生改变就可以用绝对导入
        #相对导入
            #含有相对导入的文件不能被直接执行
            #不需要反复的修改路径，只要一个包中的所有文件夹和文件的相对位置不发生改变
            #也不要去关心当前这个包和被执行文件之间的层级关系
            #from . import
            #只能在包里去用
            #含有相对导入的py文件不能被直接执行，必须要放在包中被导入才能被调用


如果我们希望导入包的时候，能够顺利把模块也导入进来，需要设计_init_文件



#创建目录代码
import os
os.makedirs('glance/api')
os.makedirs('glance/cmd')
os.makedirs('glance/db')
l = []
l.append(open('glance/__init__.py','w'))
l.append(open('glance/api/__init__.py','w'))
l.append(open('glance/api/policy.py','w'))
l.append(open('glance/api/versions.py','w'))
l.append(open('glance/cmd/__init__.py','w'))
l.append(open('glance/cmd/manage.py','w'))
l.append(open('glance/db/models.py','w'))
map(lambda f:f.close() ,l)



################目录结构
glance/                   #Top-level package

├── __init__.py      #Initialize the glance package

├── api                  #Subpackage for api

│   ├── __init__.py

│   ├── policy.py

│   └── versions.py

├── cmd                #Subpackage for cmd

│   ├── __init__.py

│   └── manage.py

└── db                  #Subpackage for db

    ├── __init__.py

    └── models.py



##################文件内容###模拟，实际按自己需求写

#policy.py
def get():
    print('from policy.py')

#versions.py
def create_resource(conf):
    print('from version.py: ',conf)

#manage.py
def main():
    print('from manage.py')

#models.py
def register_models(engine):
    print('from models.py: ',engine)

#################绝对导入
glance/

├── __init__.py      from glance import api
                             from glance import cmd
                             from glance import db

├── api

│   ├── __init__.py  from glance.api import policy
                              from glance.api import versions

│   ├── policy.py

│   └── versions.py

├── cmd                 from glance.cmd import manage

│   ├── __init__.py

│   └── manage.py

└── db                   from glance.db import models

    ├── __init__.py

    └── models.py

#################相对导入
glance/

├── __init__.py      from . import api  #.表示当前目录
                     from . import cmd
                     from . import db

├── api

│   ├── __init__.py  from . import policy
                     from . import versions

│   ├── policy.py

│   └── versions.py

├── cmd              from . import manage

│   ├── __init__.py

│   └── manage.py    from ..api import policy
                     #..表示上一级目录，想再manage中使用policy中的方法就需要回到上一级glance目录往下找api包，从api导入policy

└── db               from . import models

    ├── __init__.py

    └── models.py














'''