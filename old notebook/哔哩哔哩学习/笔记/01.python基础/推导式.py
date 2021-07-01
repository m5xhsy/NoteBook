######1
# 原式
lst = []
for i in range(1, 16):
    if i % 2 == 0:
        lst.append('python' + str(i))
print(lst)
# 推导式        #语法#lis=[结果 for循环 判断]
lst = ['python' + str(i) for i in range(1, 16) if i % 2 == 0]
print(lst)

######2
# 原式
if 3 > 2:
    print(3)
else:
    print(2)
# 推导式        #语法#  执行语句 if 判断条件 else 执行语句
print(3 if 3 > 2 else 2)

######3
# 原式
dic = {}
lis = [00, 11, 22]
for i in range(0, len(lis)):
    dic[i] = lis[i]
print(dic)
# 推导式        #语法#dic={k:v for循环 条件筛选}
lis = [00, 11, 22]
dic = {i: lis[i] for i in range(0, len(lis))}
print(dic)
