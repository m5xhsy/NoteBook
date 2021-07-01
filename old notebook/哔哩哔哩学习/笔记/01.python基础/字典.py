'''
*****字典操作*****
增
    dic['1']='a'					    			#增加，也是强制修改
    dic.setdefault('1','a')

删
    dic.pop('1') 						    		#删除，有返回值，为键所带的值，没有则会报错
    dic.clear()								    	#清空
    del dic['1']								    #删除

改
    dic['1']='a'	    							#修改
    dic.updata(dic1)	    						#更新，将dic1添加进dic，有则修改，无则添加

查
    for 循环				    					#for i in dic:    输出的是键
                                                    #     print(i)
    print(dic['1'])					    			#输出值，没有则报错
    print(dic.get('1','没有'))			    		#输出值，如果没有则输出“没有”
    print(dic.setdefault('1'))				    	#也可以查，没有输出None

其他方法
    print(dic.keys())							    #拿到所有的键，组成一个列表
    print(dic.values())						    	#拿到所有的值，组成一个列表
    print（dic.items())							    #拿到所有的键值对，组成一个列表

创建字典
    dic=dict.formkeys([1,2,3],'alex')               #dic={1:'alex',2:'alex',3:'alex'}
    dic={1:'alex'}
    dic=dict({1:'alex'})
'''

dic=dict()
dic.setdefault('a',1)


# 如果字典有这个key，不设置，没有则设置默认值

