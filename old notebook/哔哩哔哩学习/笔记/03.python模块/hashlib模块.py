import hashlib

#实例化对象
obj=hashlib.md5(b'123')         #加盐

#写入要加密的字节
obj.update('asdjowefiosnssada'.encode('utf-8'))

#获取密文
v=obj.hexdigest()
print(v)

