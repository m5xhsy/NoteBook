import random
#取随机整数
random.randint(x,y)         #顾头顾尾
random.randrange(x,y,z)       #顾头不顾尾加步长
#取随机小数
random.random()             #取0-1之间的小数
random.uniform(x,y)          #取一个范围之间的小数
#从一个列表中随机取值
random.choice(lit)          #在列表中随机抽取一个值
random.sample(lit,x)        #在列表中随机抽取x个值
#打乱一个列表
random.shuffle(lis)         #在原来列表基础上打乱列表，没有返回值
