# Hashlib

## md5加密

```python
import hashlib

obj = hashlib.md5(b"123") 				# 加盐
obj.update("abcd".encode("utf-8"))
obj.update("ecfg".encode("utf-8"))
# obj.update("abcdecfg".encode("utf-8"))	上面步结果和这一步是一样的
s = obj.hexdigest() # '70433b519d1576728182a97532733935'

补充:
    md5加密的字符串一般不能作为字典的key或者数据库主键，但是一种情况例外，文件上传服务器时，通过md5加密后字符串可判断服务器是否存在这个文件，如果存在就不用上传，直接引用
```

## sha1加密

```python
import hashlib

obj = hashlib.sha1(b"123")
# obj.update(b'aaaa')
# obj.update(b'bbbb')
obj.update(b'aaaabbbb') # 85bf468daade3745d505894dc05223a162c95ecc
print(obj.hexdigest())
```

