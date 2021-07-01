#序列化：str,bytes
#序列：元组，列表，str，bytes
json模块
import json
json.dumps()        #序列化  有默认值取消ascii编码以及格式化 ensure_ascii=False
json.loads()        #反序列化
#json能够处理的数据类型比较有限：字符串，列表，字典，数字
#字典中的可以，只能是字符串
#在所有的语言都通用
json.dump()         #(字典，文件句柄f)直接写入文件
json.load()         #(文件句柄f)直接读取文件

pickle模块
import pickle
pickle.dumps()
pickle.locds()
pickle.dump()
pickle.locd()
#基本和json一样，转换的是特殊编的码字节，以b模式录入和读取，支持的数据类型比较全面
#可以多次dump和locd，用
while True:
    try:
        pickle.dumps()
    except StopIteration:
