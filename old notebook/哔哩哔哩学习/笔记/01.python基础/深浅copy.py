'''
#*****深浅copy*****
深copy
    import copy                                     #copy模块
    ll.copy.deepcopy()
浅copy
    11.copy                                         #切片是浅copy,l2=l1[:]
'''

dic = dict.fromkeys(["张三", "李四"], ["足球", "篮球"])
print(dic)  # {'张三': ['足球', '篮球'], '李四': ['足球', '篮球']}
dic["张三"].append("游泳")
print(dic)  # {'张三': ['足球', '篮球', '游泳'], '李四': ['足球', '篮球', '游泳']}
