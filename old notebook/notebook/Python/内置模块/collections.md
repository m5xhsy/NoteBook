# Collections

## 统计元素

可迭代对象中元素出现次数

```
from collections import Counter

st = "ABCJABCBABCDBCBC"
Counter(st) 		# Counter({5: 3, 1: 1, 2: 1, 62: 1, 8: 1})
```

## 默认字典

defaultdict实例化时传可执行对象,如果取值时没有这个值，返回可执行对象的返回值，并设置进去

```python
from  collections import defaultdict

dic = defaultdict(lambda :"null")
print(dic) # defaultdict(<function <lambda> at 0x00000236AA483C10>, {})
dic["aaa"]
print(dic) # defaultdict(<function <lambda> at 0x00000236AA483C10>, {'aaa': 'null'})
```

## 可迭代对象

```python
from collections.abc import Iterable,Iterator

i = "123"
j = i.__iter__()
print(isinstance(i,Iterable))   # True         #判断是否是可迭代对象
print(isinstance(i,Iterator))   # False        #判断是否是迭代器
print(isinstance(j,Iterable)) 	# True
print(isinstance(j,Iterator))	# True
```

## 命名元组

```python
from collections import namedtuple

point = namedtuple("struct",["year","month","day"])
p = point(2020,10,31)
print(p)      # struct(year=2020, month=10, day=31)
print(p.year) # 2020
```

## 双向队列

```python
from collections import deque # 双向队列

q = deque() 
q.append("A")  		# ["A"]
q.append("B")  		# ["A","B"]
q.appendleft("C") 	# ["C","A","B"]
print(q.pop())		# B
print(q.popleft())  # C
```

