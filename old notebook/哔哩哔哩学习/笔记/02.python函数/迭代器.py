# d = 'abcd'
# l = d.__iter__()  # 生成迭代器
# print(l.__next__())  # 打印下一个迭代器元素
# print(l.__next__())  # 打印下一个迭代器元素
# print(l.__next__())  # 打印下一个迭代器元素
# print(l.__next__())
# print(l.__next__())

# c=123
# d='abcd'
# i=d.__iter__()
#
# while 1:
#     try:                        #尝试执行
#         ed=i.__next__()
#         print(ed)
#     except StopIteration:       #处理错误
#         break

lis = list("asdas")
# print(lis)

#
# c ="123"
# c = c.__iter__()
# print('_iter_' in dir(lis))               #好像不能用了
# print('_iter_' in dir(c))

i = "123"
j = i.__iter__()
# 官方查询方案
from _collections_abc import Iterable        #可迭代对象
from _collections_abc import Iterator        #迭代器
print(isinstance(i,Iterable))           #判断是否是可迭代对象
print(isinstance(i,Iterator))           #判断是否是迭代器
print(isinstance(j,Iterable))
print(isinstance(j,Iterator))

# 迭代多个数组
# from itertools import chain
# for item in chain([1,5,6,3,2],[1,5,6,3,8,1],[1,5,9,6,2]):
#     print(item)
