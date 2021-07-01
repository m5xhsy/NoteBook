'''
*****字符操作*****
    name.bit_length()     							#计算i转换为二进制的位数
    name.capitalize()  								#首字母大写其余小写
    name.upper()									#全部大写
    name.lower()									#全部小写
    name.center(20,'*')         					#字符串居中前后填充自定义字符
    name.startswith('e',1,4)						#判断字符串是否以e开头,1-4切片
    name.endswith('e',1,4)							#判断字符串是否以结尾,1-4切片
    name.swapcase()									#字母大小写翻转
    name.title()               	 					#非字母隔开处大写
    name.find('a',1,5)  							#在1-5切片，元素a找索引，没有则返回-1
    name.index('a',1,5)								#在1-5切片，元素a找索引，没有则报错
    name.strip('*da34')								#去除前后指定元素或空格，前后用lstrip()或rstrip()
    name.split('，'，1)								#将字符串以“，”分割成列表，分割一次。默认时空格在前不作为分割元素前后用lsplit()或rsplit()
    '*'.join(name)									#将字符分割以*链接起来
    name.replace('a','A'，1)						#将字符串中a用A替换1次
    name.count('a',1-5)								#1-5切片，字符a出现了多少次
    len(name)										#字符串长度
    '我叫{}，{}'.format('xx','xx')
    '我叫{0}，{1},{0}'.format('yy','xx')
    '我叫{name}，{age}'.format(name='yy',age='xx')	#格式输出
    is系列
    name.isalnum()									#判断是否数字字母组成
    name.isdigit()									#判断是否数字组成
    name.isalpha()									#判断是否字母组成
'''