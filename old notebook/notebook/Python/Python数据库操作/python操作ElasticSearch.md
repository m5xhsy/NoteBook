# ElasticSearch

## 关于ES的操作

- **结果过滤：**对于返回结果做过滤，主要是优化返回内容

- **ElasticSearch对象：**直接操作es对象，处理简单的索引信息
- **Indices：**关于索引的细节操作，比如mappings
- **Cluster：**集群操作
- **Nodes：**节点操作
- **Cat API：**换一种查询方式，一般返回json类型，cat提供简介的返回
- **Snapshot：**快照相关，快照是从正在运行的Elasticsearch集群中获取的备份。我们可以拍摄单个索引或整个群集的快照，并将其存储在共享文件系统的存储库中，并且有一些插件支持S3，HDFS，Azure，Google云存储等上的远程存储库。

- **Task Management API：**任务管理API是新的，仍应被视为测试版功能。API可能以不向后兼容的方式更改。

## 连接

```
from elasticsearch import Elasticsearch

es = Elasticsearch()   # 默认本地
es = Elasticsearch(["127.0.0.1:9200"]) 
es = Elasticsearch(
	["192.168.239.128","192.168.239.129","192.168.239.130"],  # 集群
    sniff_on_start=True,            # 连接前测试
    sniff_on_connection_fail=True,  # 节点无响应时刷新节点
    sniff_timeout=60                # 超时时间
)
es = Elasticsearch(['127.0.0.1:9200'],ignore=400)  # 忽略返回的400状态码
es = Elasticsearch(['127.0.0.1:9200'],ignore=[400, 405, 502])  # 以列表的形式忽略多个状态码
```

## ES对象操作

### es.index

```
es.index(index="pyes", body={"name":"xxx","age":18})	   # 这里不指定id的话，会随机生成字符串作为id	
es.index(index="pyes", id=1, body={"name":"xxx","age":18}) # es7以前版本需要指定doc_type参数，由于es8要删除类型，所以不用写了
```

### es.get

```
es.get(index="pyes", id=1)		# 获取指定id的数据
```

### es.search

```
body={
	"query":{
		"match":{
			"name":"orz"
		}
	}
}
es.search(index="pyes")								# 返回所有
es.search(index="pyes", body=body) 					# 按条件查询
es.search(index="pyes",_source=["name"])			# _source中允许返回的字段
es.search(index="pyes",_source_includes=["name"])	# 效果和上面这个一样
es.search(index="pyes",_source_excludes=["name"])	# _source中排除的字段
es.search(index="pyes", body=body, filter_path=["hits.hits","hits.ti*"])	# 返回json数据中包含列表中点出的数据
```

### es.get_source

```
es.get_source(index="pyes", id=1, _source=["name"])		# 根据索引和id直接返回结果字典，也可以使用_source_excludes和_source_includes
```

### es.count

```
body={
	"query":{
		"match":{
			"name":"orz"
		}
	}
}
es.count(index="pyes", body=body)		# 根据条件查看有多少条数据(返回字典)
es.count(index="pyes")["count"]			# 获取index中所有数据的条数
```

### es.create

```
es.create(index="pyes", id=1, body={"name":"orz","age":18})	 #创建索引并增加数据，如果存在就只加数据，对应id数据如果存在就会报错
```

### es.delete

```
es.delete(index="pyes", id=1) 	# 删除指定id的字段，但是不能删索引
```

### es.delete_by_query

```
body={
    "query":{
        "match":{
            "name":"m5xhsy"
        }
    }
}
es.delete_by_query(index="pyes",body=body)		#根据条件查询出来的结果
```

### es.exists

```
es.exists(index="pyes",id=1)	# 查询是否存在对应id的文档，返回bool值
```

### es.info

```
es.info()	# 获取当前集群基本信息
```

### es.ping

```
es.ping()	# 查看当前集群是否启动，返回bool值
```

## Indices操作

### 创建映射es.indices.create

使用的比较多的方法创建mappings

```
body = {
	"mappings":{
		"dynamic":"strict",
		"properties":{
			"name":{
				"type":"text"
			},
			"nickname":{
				"type":"text"
			},
			"age":{
				"type":"long"
			}
		}
	}
}
es.indices.create(index="ind",body=body)
```

### 查看分词es.indices.analyze

返回分词结果

```
es.indices.analyze(body={"analyzer":"ik_max_word","text":"python是世界上最好的语言"})
```

### 删除索引es.indices.delete

```
es.indices.delete(index="ind") # 删除指定索引
```

### 索引别名es.indices.put_alias

```
es.indices.put_alias(index="ind",name="alipip")				# 索引取别名
es.indices.put_alias(index=["ind", "pyes"],name="alipip") 	# 多个索引取同一个别名，用于联查
```

### 删除别名es.indices.delete_alias

```
es.indices.delete_alias(index="ind",name="alipip")				# 删除一个
es.indices.delete_alias(index=["ind", "pyes"], name="alipip")	# 删除多个
```

### 映射定义es.indices.get_mapping

```
es.indices.get_mapping(index="ind")			# 相当于执行 GET ind 返回结果的mappings部分
```

### 设置定义es.indices.get_settings

```
es.indices.get_settings(index="ind")		# 相当于执行 GET ind 返回结果的settings部分
```

### 索引状态es.indices.get

```
es.indices.get(index="ind")					# 相当于get_settings加上get_mappings返回的结果
es.indices.get(index=["ind","map"])
```

### 别名状态es.indices.get_alias

```
es.indices.get_alias(index="ind")			# 查看一个索引对应的别名状态(有没有都返回json数据)
es.indices.get_alias(index=["ind","map"])	# 查看多个索引对应的别名状态
```

### 字段映射信息es.indices.get_field_mapping

```
es.indices.get_field_mapping(index="ind",fields="name")		# 查看指定字段对应的映射信息
es.indices.get_field_mapping(index="ind",fields=["name","nickname"])	# 查看多个字段对应的映射信息
```

### 索引是否存在es.indices.exists

```
es.indices.exists(index="ind") # 查看索引是否存在,返回bool值
```

### 刷新索引es.indices.flush

```
es.indices.flush(index="ind")
```

### 开启索引es.indices.open

```
es.indices.open(index="ind") # 打开一个封闭的索引以使其可用于搜索。
```

### 关闭索引es.indices.close

```
es.indices.close(index="ind") # 关闭索引以从群集中删除它的开销。封闭索引被阻止进行读/写操作# 
```

### 清除索引缓存es.indices.clear_cache

```
es.indices.clear_cache(index="ind") # 清除与一个或多个索引关联的所有缓存或特定缓存
```

### 监控索引升级es.indices.get_uprade

```
es.indices.get_uprade(index="ind")
```

### 检索模板es.indices.get_template

```
es.indices.get_template() 	# 按名称检索索引模板
```

### 特定映射定义es.indices.put_mapping

```
es.indices.put_mapping(			# 注册特定类型的特定映射定义。
    body,
    index=None,
    doc_type=None,
    params=None,
    headers=None,
)
```

### 更改索引级别es.indices.put_settings

```
es.indices.put_settings(body, index=None, params=None, headers=None) # 实时更改特定索引级别设置。
```

### 创建索引模板es.indices.put_template

```
es.indices.put_template(name, body, params=None, headers=None)	# 创建一个索引模板，该模板将自动应用于创建的新索引。
```

### 索引转移es.indices.rollover

```
es.indices.rollover(
    alias,
    body=None,
    new_index=None,
    params=None,
    headers=None,
)
# 当现有索引被认为太大或太旧时，翻转索引API将别名转移到新索引。API接受单个别名和条件列表。别名必须仅指向单个索引。如果索引满足指定条件，则创建新索引并切换别名以指向新别名
```

### 索引低级别段信息es.indices.segments

```
es.indices.segments(index=None, params=None, headers=None)    # 提供构建Lucene索引（分片级别）的低级别段信息。
```

## Cluster集群

### 集群设置es.cluster.get_settigns

```python
es.cluster.get_settings()  # 获取集群设置。
```

### 集群状态es.cluster.health

```python
es.cluster.health() # 获取有关群集运行状况的非常简单的状态。
```

### 综合信息es.cluster.state

```python
es.cluster.state()  #获取整个集群的综合状态信息
```

### 节点信息es.cluster.stats

```python
es.cluster.stats()  # 返回群集的当前节点的信息
```

## Node节点相关

### es.nodes.info，返回集群中节点的信息。

```python
es.nodes.info()  # 返回所节点
es.nodes.info(node_id='node1')   # 指定一个节点
es.nodes.info(node_id=['node1', 'node2'])   # 指定多个节点列表
```

### es.nodes.stats，获取集群中节点统计信息。

```python
es.nodes.stats()
es.nodes.stats(node_id='node1')
es.nodes.stats(node_id=['node1', 'node2'])
```

### es.nodes.hot_threads，获取指定节点的线程信息。

```python
es.nodes.hot_threads(node_id='node1')
es.nodes.hot_threads(node_id=['node1', 'node2'])
```

### es.nodes.usage，获取集群中节点的功能使用信息。

```python
es.nodes.usage()
es.nodes.usage(node_id='node1')
es.nodes.usage(node_id=['node1', 'node2'])
```

## Cat（一种查询方式）

### 返回别名信息 es.cat.aliases

- name`要返回的以逗号分隔的别名列表。`format`Accept标头的简短版本，例如json，yaml

```python
es.cat.aliases(name='py23_alias')
es.cat.aliases(name='py23_alias', format='json')
```

### 分片使用情况 es.cat.allocation

返回分片使用情况。

```python
es.cat.allocation()
es.cat.allocation(node_id=['node1'])
es.cat.allocation(node_id=['node1', 'node2'], format='json')
```

### 文档计数的快速访问 es.cat.count

Count提供对整个群集或单个索引的文档计数的快速访问。

```python
es.cat.count()  # 集群内的文档总数
es.cat.count(index='py3')  # 指定索引文档总数
es.cat.count(index=['py3', 'py2'], format='json')  # 返回两个索引文档和
```

### fielddata的信息 es.cat.fielddata

基于每个节点显示有关当前加载的fielddata的信息。有些数据为了查询效率，会放在内存中，fielddata用来控制哪些数据应该被放在内存中，而这个`es.cat.fielddata`则查询现在哪些数据在内存中，数据大小等信息。

```python
es.cat.fielddata()
es.cat.fielddata(format='json', bytes='b')
```

`bytes`显示字节值的单位，有效选项为：`'b'，'k'，'kb'，'m'，'mb'，'g'，'gb'，'t'，'tb' ，'p'，'pb'`
`format`Accept标头的简短版本，例如json，yaml

### 集群健康信息 es.cat.health

从集群中`health`里面过滤出简洁的集群健康信息。

```python
es.cat.health()
es.cat.health(format='json')
```

### cat的帮助信息 es.cat.help

返回`es.cat`的帮助信息。

```python
print(es.cat.help())
```

### 索引的信息 es.cat.indices

返回索引的信息；也可以使用此命令进行查询集群中有多少索引。

```python
print(es.cat.indices())
print(es.cat.indices(index='py3'))
print(es.cat.indices(index='py3', format='json'))
print(len(es.cat.indices(format='json')))  # 查询集群中有多少索引
```

### 集群主节点IP es.cat.master

返回集群中主节点的IP，绑定IP和节点名称。

```python
print(es.cat.master())
print(es.cat.master(format='json'))
```

### 节点自定义属性 es.cat.nodeattrs

返回节点的自定义属性。

```python
print(es.cat.nodeattrs())
print(es.cat.nodeattrs(format='json'))
```

### 节点的拓扑 es.cat.nodes，

返回节点的拓扑，这些信息在查看整个集群时通常很有用，特别是大型集群。我有多少符合条件的节点？

```python
print(es.cat.nodes())
print(es.cat.nodes(format='json'))
```

### 节点插件信息 es.cat.plugins

返回节点的插件信息。

```python
print(es.cat.plugins())
print(es.cat.plugins(format='json'))
```

### 索引Lucene信息 es.cat.segments

返回每个索引的Lucene有关的信息

```python
es.cat.segments()
es.cat.segments(index='py3')
es.cat.segments(index='py3', format='json')
```

### 节点分片信息 es.cat.shards

返回哪个节点包含哪些分片的信息。

```python
es.cat.shards()
es.cat.shards(index='py3')
es.cat.shards(index='py3', format='json')
```

### 线程池信息 es.cat.thread_pool

获取有关线程池的信息。

```python
es.cat.thread_pool()
```

Snapshot（快照相关）

- es.snapshot.create，在存储库中创建快照。
  - `repository` 存储库名称。
  - `snapshot`快照名称。
  - `body`快照定义。
- es.snapshot.delete，从存储库中删除快照。
- es.snapshot.create_repository。注册共享文件系统存储库。
- es.snapshot.delete_repository，删除共享文件系统存储库。
- es.snapshot.get，检索有关快照的信息。
- es.snapshot.get_repository，返回有关已注册存储库的信息。
- es.snapshot.restore，恢复快照。
- es.snapshot.status，返回有关所有当前运行快照的信息。通过指定存储库名称，可以将结果限制为特定存储库。
- es.snapshot.verify_repository，返回成功验证存储库的节点列表，如果验证过程失败，则返回错误消息。

## Task（任务相关）

- es.tasks.get，检索特定任务的信息。
- es.tasks.cancel，取消任务。
- es.tasks.list，任务列表。

## 批量写入数据

```
import pandas as pd
from elasticsearch import Elasticsearch
from elasticsearch import helpers

es = Elasticsearch(hosts="127.0.0.1:9200")

df = pd.read_csv("./xxx.csv")

active = []
for i in range(len(df)):
    co = {
        '_index': 'news',
        '_source': {
            'title':df.iloc[i]["title"],
            "type":df.iloc[i]["type"],
            "src":df.iloc[i]["src"],
            "img_src":df.iloc[i]["img_src"],
            "content":df.iloc[i]["content"],
        }
    }
    active.append(co)
helpers.bulk(es,active)
```

