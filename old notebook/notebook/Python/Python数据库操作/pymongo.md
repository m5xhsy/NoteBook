## pymongo的使用

```python
import pymongo
import json
mongoClick = pymongo.MongoClient(host="192.168.239.128", port=27017,)
Mongodb = mongoClick["m5xhsy"]	# 使用数据库

############ 查找 ############
res = Mongodb.user.find()		# 查找所有
print(res)
for item in res:		
    print(item)
    item["_id"] = str(item.get("_id"))	# 查询出来的_id为对象，需要转换成str才可用序列化
    s = json.dumps(item)
    print()

# 指定查询字段
res = Mongodb.user.find_one({},{"_id":0})	# 0表示不显示_id
print(res)
    
    
res = Mongodb.user.find({}).skip(2),limit(5)	# 跳过2条查5条
res = Mongodb.user.find({}).sort("age",pymongo.ASCENDING)  # 后面也可用直接写1 或者 -1， pymongo.DESCENDING  倒序

# _id查找
from bson import ObjectId
s = ObjectID("5a4sd5a6s5d46a5s4d65a4sd65a4sd")
res = Mongodb.user.find_one({"_id":s})
############ 增加 ############
res = Mongodb.user.insert_one({"age":55,"name":"adslasd"})
print(res, type(res), res.inserted_id)

res = Mongodb.user.insert_many([{"age":565,"name":"adslasd"},{"age":5,"name":"adslasd"}])
print(res, type(res), res.inserted_ids)
############ 更新 ############
Mongodb.user.update_one({"age":55},{"$set":{"name":"asdasda"}})
Mongodb.user.update_many({"age":55},{"$set":{"name":"asdasdsada"}})

############ 删除 ############
res = Mongodb.user.delete_one({"age":55})
res = Mongodb.user.delete_many({})
```

