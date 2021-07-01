from elasticsearch import Elasticsearch

# es = Elasticsearch()
es = Elasticsearch(["127.0.0.1:9200"])
# es = Elasticsearch(
#     ["192.168.239.128","192.168.239.129","192.168.239.130"],
#     sniff_on_start=True,            # 连接前测试
#     sniff_on_connection_fail=True,  # 节点无响应时刷新节点
#     sniff_timeout=60                # 超时时间
#
# )

# es = Elasticsearch(['127.0.0.1:9200'],ignore=400)  # 忽略返回的400状态码
# es = Elasticsearch(['127.0.0.1:9200'],ignore=[400, 405, 502])  # 以列表的形式忽略多个状态码

# print(es.index(index="ppd",id=1,body={"name":"orz","age":10}))
# print(es.get(index="ppd",id=1))


# es.indices.close("agg")
# es.indices.open("agg")