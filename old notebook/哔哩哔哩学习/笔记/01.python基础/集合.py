'''
#*****集合操作*****
创建集合
    set1={a,b,c}
    set1=set({a,b,c})

增
    set1.add('a')
    set1.update('a')

删
    set1.remove('a')                                #按元素删除
    set1.pop()                                      #随机删除
    set1.clear()                                    #全部删除
    del set1                                        #删除集合

关系测试
交集
    print(set1&set2)
    print(set.intersection(set2))
并集
    print(set1|set2)
    print(set1.union(set2))
反交集
    print(set1^set2)
    print(ser1.symmetric_difference(set2))
差集
    print(set1-set2)
    print(set1.difference(set2))
子集
    print(set1<set2)
    print(set1.issubset(set2))
超集
    print(set2>set1)
    print(set2.issuperset)
'''