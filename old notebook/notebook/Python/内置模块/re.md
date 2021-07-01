# Re模块

## 基本使用

- **re.findall()**

  (正则表达式，带匹配的字符串，flag)  匹配结果是列表

  ```python
  ret = re.findall("\d","1a2b")
  print(ret) # ['1', '2']
  ```

- **re.search()**

  (正则表达式，带匹配的字符串)只匹配从左到右第一个，获取迭到的是内存地址，用.group()获取结果

  ```python
  ret = re.search("\d","1a2b")
  if ret:   
      print(ret.group()) # 1
  ```

- **re.match()**

  从头匹配，相当于search()中的正则表达式前面添加^

  ```python
  ret = re.match("\d","1a2b") 
  if ret:   
      print(ret.group())	# 1
  ```

- **re.split()**

  返回列表，按照正则表达式里面的内容切割，匹配到的内容会被切割掉,正则表达式加括号会保留正则表达式里面的内容

  ```python
  res = re.split("(\d)","1a2b") 
  print(res)		# ['', '1', 'a', '2', 'b']
  
  ret = re.split("\d","1a2b")
  print(ret)  	# ['', 'a', 'b']
  ```

- **re.sub() **

  按照正则规则去寻找要被替换的内容(要替换的表达式，替换的内容，字符串)

  ```python
  ret = re.sub("\d","c","1a2b")
  print(ret) 		# cacb
  ```

- **re.subn()**

  和sub一样，会返回元组，第二元素是替换次数

  ```python
  ret = re.subn("\d","c","1a2b")          
  print(ret)  # ('cacb', 2)
  ```

- **re.compile()**

  把正则表达式编译成字节码，节省编译时间，可以用findall,finditer,search

  ```python
  res=re.compile("\d")
  ret = res.findall("1a2b")
  print(ret)   # ['1', '2']
  ```

- **re.finditer()**

  返回一个迭代器，用.group()获取,节省使用正则表达式的空间/内存

  ```python
  ret = re.finditer("\d","1a2b")
  print(next(ret).group()) # 1
  print(next(ret).group()) # 2
  ```

## 分组

- **()**

  ```python
  import re
  s='<a>web</a>'
  ret=re.search('<(\w+)>(\w+)</(\w+)>',s)
  print(ret.group(0))   # <a>wab</a>
  print(ret.group(1))   # a
  print(ret.group(2))   # web
  print(ret.group(3))   # a
  ```

- **(?: )**

  ```python
  s='<a>wab</a>'
  ret1=re.findall('>(\w+)<',s)   
  ret2=re.findall('>(?:\w+)<',s) # 括号里面的是一个整体但不存储
  ret3=re.findall('(\w+)',s)
  print(ret1)  # ['wab']
  print(ret2.) # ['>wab<']
  print(ret3)   # ['a', 'wab', 'a']
  ```

- **(?P<name>)**

  ```python
  s = '<a>wab</a>'
  ret4=re.search('>(?P<lcc>\w+)<',s)          #()内加?P<name>可以给分组取名，通过group('name')获取值
  print(ret4.group('lcc'))  # wab
  ```

- **(?P<name>) (?P=name)**

  ```python
  ret=re.search('<(?P<name>\w+)>(\w+)</(?P=name)>',s)
  #用?P=name可让匹配前后数值一样r'<(\w+)>(\w+)</(\1)>'或者'<(\w+)>(\w+)</(\\1)>'用\1取第一组的值
  print(ret.group("name"))  # a
  print(ret.group(2))       # web
  ```

- **(\w)xxx(\1)**

  ```python
  ret=re.search('<(\w+)>(\w+)</(\\1)>',s)   # r'<(\w+)>(\w+)</(\1)>'或者'<(\w+)>(\w+)</(\\1)>'用\1取第一组的值
  print(ret.group(1))        # a
  print(ret.group(2))       # web
  ```

## 补充

```python
k='(1.2+5)*(2.4+65)-1256+12.5'
ret6=re.findall('\d+',k)
ret7=re.findall('\d+\.\d+|\d+',k)    # 优先匹配小数
ret8=re.findall('\d+|\d+\.\d+',k)    # 优先匹配整数(小数匹配不到)
ret9=re.findall('(\d+\.\d+)|\d+',k)         # 只匹配小数
print(ret6)  # ['1', '2', '5', '2', '4', '65', '1256', '12', '5']
print(ret7)  # ['1.2', '5', '2.4', '65', '1256', '12.5']
print(ret8)  # ['1', '2', '5', '2', '4', '65', '1256', '12', '5']
print(ret9)  # ['', '5', '', '65', '1256', '']
```



