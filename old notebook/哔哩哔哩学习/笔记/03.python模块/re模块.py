import os
#查找
re.findall()        #(正则表达式，带匹配的字符串，flag)匹配结果是列表
re.search()         #(正则表达式，带匹配的字符串)只匹配从左到右第一个，获取迭到的是内存地址，用.group()获取结果
                        #如果没有匹配到,用.group()会报错，只能用if ret:   print(ret.group())
re.match()          #从头匹配，相当于search()中的正则表达式前面添加^

re.split()          #返回列表，按照正则表达式里面的内容切割，匹配到的内容会被切割掉,正则表达式加括号会保留正则表达式里面的内容
re.sub()            #按照正则规则去寻找要被替换的内容(要替换的表达式，替换的内容，字符串)
re.subn()           #和sub一样，会返回元组，第二个字是替换次数

re.compile()        #把正则表达式编译成字节码，节省编译时间，可以用findall,finditer,search
                        #ret=re.compile('\d+)
                        #res=ret.findall('a+6sd5adsdd')
re.finditer()       #节省使用正则表达式的空间/内存
                        #返回一个迭代器，用.group()获取

"""                      
re.I #忽略大小写
re.M #多行匹配
re.S #单行匹配
"""
#############正则表达式在re模块中的使用##################
import re
s='<a>wab</a>'
ret=re.search('<(\w+)>(\w+)</(\w+)>',s)
print(ret.group(0))
print(ret.group(1))
print(ret.group(2))
print(ret.group(3))


ret1=re.findall('>(\W+)<')    # z
ret2=re.findall('>(?:\W+)<')  # 括号里面的是一个整体但不存储
ret3=re.findall('(\w+)')
print(ret1)
print(ret2)
print(ret3)

ret4=re.search('>(?P<lcc>\w+)<',s)          #()内加?P<name>可以给分组取名，通过group('name')获取值
print(ret4.group('lcc'))

ret5=re.search('<(?P<name>\w+)>(\w+)</(?P=name)>',s)#用?P=name可让匹配前后数值一样r'<(\w+)>(\w+)</(\1)>'或者'<(\w+)>(\w+)</(\\1)>'用\1取第一组的值
print(ret5)
print(ret5.group())


##########技巧#############
k='(1.2+5)*(2.4+65)-1256+12.5'
ret6=re.findall('\d+',k)
ret7=re.findall('\d+\.\d+|\d+',k)
ret8=re.findall('\d+\.\d+|\d+',k)
ret9=re.findall('\d+\.\d+|(\d+)',k)         #让整数优先显示
print(ret6)
print(ret7)
print(ret8)
print(ret9)
while 1:
    if '' in ret9:
        ret9.remove('')         #删除空的
    else:
        break
print(ret9)



