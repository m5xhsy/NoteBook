import pymongo
import json
from bson import ObjectId
mongoClick = pymongo.MongoClient(host="192.168.239.128", port=27017, )
Mongodb = mongoClick["music"]
res = Mongodb.pop.find()
print(res)
for item in res:
    print(item)
    item["_id"] = str(item.get("_id"))
    s = json.dumps(item)


# res = Mongodb.user.find_one({},{"_id":0})
# print(res)

# res = Mongodb.user.insert_one({"age":55,"name":"adslasd"})
# print(res, type(res), res.inserted_id)
#
# res = Mongodb.user.insert_many([{"age":565,"name":"adslasd"},{"age":5,"name":"adslasd"}])
# print(res, type(res), res.inserted_ids)
#
# Mongodb.user.update_one({"age":55},{"$set":{"name":"asdasda"}})
#
# Mongodb.user.update_many({"age":55},{"$set":{"name":"asdasdsada"}})
#
# res = Mongodb.user.delete_one({"age":55})
#
# res = Mongodb.user.delete_many({})
#
# res = Mongodb.user.find({}).skip(2),limit(5)
#
# res = Mongodb.user.find({}).sort("age",pymongo.ASCENDING)  # 后面也可用直接写1 或者 -1
# # pymongo.DESCENDING  倒序
#
# s = ObjectID("5a4sd5a6s5d46a5s4d65a4sd65a4sd")
#
# res = Mongodb.user.find_one({"_id":s})