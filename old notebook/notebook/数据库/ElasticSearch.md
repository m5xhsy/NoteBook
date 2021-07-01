# ElasticSearch

ElasticSearch是一个基于Lucene的搜索服务器。它提供了一个分布式多用户能力的全文搜索引擎，基于RESTful web接口。ElasticSearch是用Java开发的，并作为Apache许可条款下的开放源码发布，是当前流行的企业级搜索引擎。设计用于云计算中，能够达到准实时搜索、稳定、可靠、快速、安装使用方便

优点：

- 分布式：节点对外表现对等，加入节点自动均衡
- ElasticSearch完全支持Apache Lucene的接近实时的搜索
- 各节点组成对等的网络结构，当某个节点出现故障时会自动分配其他节点代替其进行工作
- 横向可扩展性，如果你需要增加一台服务器，只需要做点配置，然后启动就可以了

- 高可用：提供复制(replica)机制，一个分片可用设置多个复制，使得某台服务器宕机的情况下，集群仍然可用照常运行，并且会把由于服务器宕机丢失的复制到其他可用节点上，这点类似于HDFS的复制机制(HDFS中默认是3份复制)

缺点：

- 不支持事务
- 相对吃内存

## 安装

- 下载安装Java jdk

- Elastic Search官网下载ElasticSearch和Kibana

- 解压ElasticSearch到安装目录，进入Bin目录以管理员方式运行elasticsearch.bat

- 浏览器打开127.0.0.1:9200显示如下则安装成功

  ```json
  {
    "name" : "DESKTOP-5K97T47",
    "cluster_name" : "elasticsearch",
    "cluster_uuid" : "py_cHNqySuGiNvQ-GG7N0g",
    "version" : {
      "number" : "7.9.3",
      "build_flavor" : "default",
      "build_type" : "zip",
      "build_hash" : "c4138e51121ef06a6404866cddc601906fe5c868",
      "build_date" : "2020-10-16T10:36:16.141335Z",
      "build_snapshot" : false,
      "lucene_version" : "8.6.2",
      "minimum_wire_compatibility_version" : "6.8.0",
      "minimum_index_compatibility_version" : "6.0.0-beta1"
    },
    "tagline" : "You Know, for Search"
  }
  ```

- 解压Kibana到安装目录，进入Bin目录以管理员方式运行kibana.bat直到出现如下所示内容

  ```
  [Kibana][http] http server running at http://localhost:5601
  ```

- 进入127.0.0.1:5601查看到界面

- **注意：**安装路径不要有中文、空格

- **补充：**Kibana是一个为Elastic Search提供数据分析的web接口，可用它对日志进行高效的搜索、可视化、分析等操作

## ES的基本操作

### 增加

```
PUT user/doc/1       # 如果不存在则创建，存在则直接替换
{
  "name":"m5xhsy",
  "age":18,
  "hobby":[
    "篮球",
    "乒乓球",
    "羽毛球"
  ]
}
```
结果如下:

```
{ 
  "_index" : "user",
  "_type" : "doc",
  "_id" : "1",
  "_version" : 1,  # 修改一次
  "result" : "created", #创建
  "_shards" : {
    "total" : 2,
    "successful" : 1,
    "failed" : 0
  },
  "_seq_no" : 0,
  "_primary_term" : 1
}
```

### 删除

##### 只删一条

```
DELETE user/doc/1
```
结果如下:

```
{
  "_index" : "user",
  "_type" : "doc",
  "_id" : "1",
  "_version" : 2,
  "result" : "deleted",
  "_shards" : {
    "total" : 2,
    "successful" : 1,
    "failed" : 0
  },
  "_seq_no" : 1,
  "_primary_term" : 1
}
```

##### 删除索引

```
DELETE user
```

结果如下

```
{
  "acknowledged" : true
}
```

### 修改

```
POST user/doc/1/_update
{ 
  "doc":{   # 这里doc不是上面的那个doc
    "age":25
  }
}
```

结果如下

```
{
  "_index" : "user",
  "_type" : "doc",
  "_id" : "1",
  "_version" : 7,
  "result" : "updated",
  "_shards" : {
    "total" : 2,
    "successful" : 1,
    "failed" : 0
  },
  "_seq_no" : 6,
  "_primary_term" : 1
}
```

### 查询

#### 普通查询

##### 查看单个文档

```
GET a1/doc/1	
```

```
{
  "_index" : "user",
  "_type" : "doc",
  "_id" : "1",
  "_version" : 7,
  "_seq_no" : 6,
  "_primary_term" : 1,
  "found" : true,
  "_source" : {
    "name" : "m5xhsy",
    "age" : 25,
    "hobby" : [
      "篮球",
      "乒乓球",
      "羽毛球"
    ]
  }
}
```

##### 条件查询(一般不用)

```
GET user/doc/_search?q=age:18   # 不支持中文
```

```
{
  "took" : 67,
  "timed_out" : false,
  "_shards" : {
    "total" : 1,
    "successful" : 1,
    "skipped" : 0,
    "failed" : 0
  },
  "hits" : {
    "total" : {
      "value" : 1,
      "relation" : "eq"
    },
    "max_score" : 1.0,
    "hits" : [
      {
        "_index" : "user",
        "_type" : "doc",
        "_id" : "2",
        "_score" : 1.0,
        "_source" : {
          "name" : "m5xhsy",
          "age" : 18,
          "hobby" : [
            "足球",
            "游泳",
            "羽毛球"
          ]
        }
      }
    ]
  }
}

```

##### 查看所有文档

```
GET user/doc/_search
```

```
#! Deprecation: [types removal] Specifying types in search requests is deprecated.
{
  "took" : 0,
  "timed_out" : false,
  "_shards" : {
    "total" : 1,
    "successful" : 1,
    "skipped" : 0,
    "failed" : 0
  },
  "hits" : {
    "total" : {
      "value" : 2,
      "relation" : "eq"
    },
    "max_score" : 1.0,
    "hits" : [
      {
        "_index" : "user",
        "_type" : "doc",
        "_id" : "1",
        "_score" : 1.0,
        "_source" : {
          "name" : "m5xhsy",
          "age" : 25,
          "hobby" : [
            "篮球",
            "乒乓球",
            "羽毛球"
          ]
        }
      },
      {
        "_index" : "user",
        "_type" : "doc",
        "_id" : "2",
        "_score" : 1.0,
        "_source" : {
          "name" : "m5xhsy",
          "age" : 18,
          "hobby" : [
            "足球",
            "游泳",
            "羽毛球"
          ]
        }
      }
    ]
  }
}

```

##### 查看索引信息

```
GET _cat/indices?v
```

```
health status index                      uuid                   pri rep docs.count docs.deleted store.size pri.store.size
green  open   .kibana-event-log-7.9.3   -Hecl3M_QIyDDyrbKa0oCw   1   0          1            0      5.5kb           5.5kb
green  open   .apm-custom-link           NiJCi72dRv2lFY3ZlhwSGw   1   0          0            0       208b           208b
green  open   .kibana_task_manager_1     NmXXmDZRQCinz5r3v0u4yA   1   0          6          369    117.9kb        117.9kb
green  open   .apm-agent-configuration   R_NtNN5eT7aCZpLQAuRXpw   1   0          0            0       208b           208b
green  open   .kibana_1                  PjShozb2QAepE5OIYK4AwQ   1   0         21            8     10.4mb         10.4mb
yellow open   user                       1IRjOzphSPGK4kfxecmNsQ   1   1          2            6     30.7kb         30.7kb
```

##### 查看指定索引信息

```
GET user
```

```
{
  "user" : {
    "aliases" : { },
    "mappings" : {
      "properties" : {
        "age" : {
          "type" : "long"
        },
        "hobby" : {
          "type" : "text",
          "fields" : {
            "keyword" : {
              "type" : "keyword",
              "ignore_above" : 256
            }
          }
        },
        "name" : {
          "type" : "text",
          "fields" : {
            "keyword" : {
              "type" : "keyword",
              "ignore_above" : 256
            }
          }
        }
      }
    },
    "settings" : {
      "index" : {
        "creation_date" : "1604650449171",
        "number_of_shards" : "1",
        "number_of_replicas" : "1",
        "uuid" : "1IRjOzphSPGK4kfxecmNsQ",
        "version" : {
          "created" : "7090399"
        },
        "provided_name" : "user"
      }
    }
  }
}
```

##### 确认索引是否存在

```
HEAD user
```

```
200 - OK
```

#### match系列查询

##### 条件查询(match)

```
GET user/doc/_search
{
  "query":{
    "match":{
      "hobby":"篮球"    # 查询多个用逗号或空格分开，如"足球 篮球"
    }
  }
}
```

此处查询会进行分词，有bug，搜索足球所有带球的都查询到了

```
{
  "took" : 0,
  "timed_out" : false,
  "_shards" : {
    "total" : 1,
    "successful" : 1,
    "skipped" : 0,
    "failed" : 0
  },
  "hits" : {
    "total" : {
      "value" : 2,
      "relation" : "eq"
    },
    "max_score" : 0.95721513,
    "hits" : [
      {
        "_index" : "user",
        "_type" : "doc",
        "_id" : "1",
        "_score" : 0.95721513,
        "_source" : {
          "name" : "m5xhsy",
          "age" : 25,
          "hobby" : [
            "篮球",
            "乒乓球",
            "羽毛球"
          ]
        }
      },
      {
        "_index" : "user",
        "_type" : "doc",
        "_id" : "2",
        "_score" : 0.25548247,
        "_source" : {
          "name" : "m5xhsy",
          "age" : 18,
          "hobby" : [
            "足球",
            "游泳",
            "羽毛球"
          ]
        }
      }
    ]
  }
}
```

##### 短语查询(match_phrase)

- 列表中的元素为条件

    ```
    GET user/doc/_search
    {
      "query":{
        "match_phrase":{
          "hobby":"篮球"
        }
      }
    }
    ```

    ```
    {
      "took" : 73,
      "timed_out" : false,
      "_shards" : {
        "total" : 1,
        "successful" : 1,
        "skipped" : 0,
        "failed" : 0
      },
      "hits" : {
        "total" : {
          "value" : 1,
          "relation" : "eq"
        },
        "max_score" : 0.85222626,
        "hits" : [
          {
            "_index" : "user",
            "_type" : "doc",
            "_id" : "1",
            "_score" : 0.85222626,
            "_source" : {
              "name" : "m5xhsy",
              "age" : 25,
              "hobby" : [
                "篮球",
                "乒乓球",
                "羽毛球"
              ]
            }
          }
        ]
      }
    }
    ```

- 字段中包含了某个元素

  ```
  GET text/doc/_search
  {
    "query":{
      "match_phrase":{
        "title":"晓梦"
      }
    }
  }
  ```

  ```
  {
    "took" : 0,
    "timed_out" : false,
    "_shards" : {
      "total" : 1,
      "successful" : 1,
      "skipped" : 0,
      "failed" : 0
    },
    "hits" : {
      "total" : {
        "value" : 2,
        "relation" : "eq"
      },
      "max_score" : 0.65416455,
      "hits" : [
        {
          "_index" : "text",
          "_type" : "doc",
          "_id" : "2",
          "_score" : 0.65416455,
          "_source" : {
            "title" : "晓梦随疏钟，飘然蹑云霞"
          }
        },
        {
          "_index" : "text",
          "_type" : "doc",
          "_id" : "1",
          "_score" : 0.57191795,
          "_source" : {
            "title" : "庄生晓梦迷蝴蝶，望帝春心托杜鹃"
          }
        }
      ]
    }
  }
  ```

- 间隔模糊查询

    ```
    GET text/doc/_search
    {
      "query":{
        "match_phrase":{
          "title":{
            "query": "晓梦蝴蝶",
            "slop": 1   		# 间隔一个字符
          }
        }
      }
    }
    ```

    ```
    {
      "took" : 2,
      "timed_out" : false,
      "_shards" : {
        "total" : 1,
        "successful" : 1,
        "skipped" : 0,
        "failed" : 0
      },
      "hits" : {
        "total" : {
          "value" : 1,
          "relation" : "eq"
        },
        "max_score" : 1.5490112,
        "hits" : [
          {
            "_index" : "text",
            "_type" : "doc",
            "_id" : "1",
            "_score" : 1.5490112,
            "_source" : {
              "title" : "庄生晓梦迷蝴蝶，望帝春心托杜鹃"
            }
          }
        ]
      }
    }
    ```

    

##### 查询全部(match_all)

```
GET user/doc/_search
{
  "query":{
    "match_all":{}
  }
}
```

```
{
  "took" : 0,
  "timed_out" : false,
  "_shards" : {
    "total" : 1,
    "successful" : 1,
    "skipped" : 0,
    "failed" : 0
  },
  "hits" : {
    "total" : {
      "value" : 3,
      "relation" : "eq"
    },
    "max_score" : 1.0,
    "hits" : [
      {
        "_index" : "user",
        "_type" : "doc",
        "_id" : "1",
        "_score" : 1.0,
        "_source" : {
          "name" : "m5xhsy",
          "age" : 25,
          "hobby" : [
            "篮球",
            "乒乓球",
            "羽毛球"
          ]
        }
      },
      {
        "_index" : "user",
        "_type" : "doc",
        "_id" : "2",
        "_score" : 1.0,
        "_source" : {
          "name" : "m5xhsy",
          "age" : 18,
          "hobby" : [
            "足球",
            "游泳",
            "羽毛球"
          ]
        }
      },
      {
        "_index" : "user",
        "_type" : "doc",
        "_id" : "3",
        "_score" : 1.0,
        "_source" : {
          "name" : "屁屁",
          "age" : 18,
          "hobby" : [
            "跑步",
            "羽毛球"
          ]
        }
      }
    ]
  }
}
```

##### 最左前缀查询(match_phrase_prefix)

准备数据

```
PUT test/_doc/1
{
  "title":"to know full well"
}

PUT test/_doc/2
{
  "title":"to know no bounds"
}

PUT test/_doc/3
{
  "title":"to know something backwards"
}

PUT test/_doc/4
{
  "title":"to know something for a fact"
}

PUT test/_doc/5
{
  "title":"have sth to offer"
}
```

查询

```
GET test/_doc/_search
{
  "query":{
    "match_phrase_prefix":{
      "title":"to know som"
    } 
  } 
}
```

结果

```
{
  "took" : 45,
  "timed_out" : false,
  "_shards" : {
    "total" : 1,
    "successful" : 1,
    "skipped" : 0,
    "failed" : 0
  },
  "hits" : {
    "total" : {
      "value" : 2,
      "relation" : "eq"
    },
    "max_score" : 1.2984518,
    "hits" : [
      {
        "_index" : "test",
        "_type" : "_doc",
        "_id" : "3",
        "_score" : 1.2984518,
        "_source" : {
          "title" : "to know something backwards"
        }
      },
      {
        "_index" : "test",
        "_type" : "_doc",
        "_id" : "4",
        "_score" : 1.0882707,
        "_source" : {
          "title" : "to know something for a fact"
        }
      }
    ]
  }
}
```

##### 多字段查询(multi_match)

准备数据

```
PUT test/_doc/1
{
  "title":"python",
  "detail":"python是世界上最好的语言"
}

PUT test/_doc/2
{
  "title":"java是世界上最好的语言",
  "detail":"python真的很简单"
}

PUT test/_doc/3
{
  "title":"java",
  "detail":"java是世界上最好的语言"
}
```

查询

```
GET test/_doc/_search
{
  "query": {
    "multi_match": {key
      "query": "python",
      "fields": ["title", "detail"]   		#可用 tit* 正则来模糊匹配或者detail^2来提高权重(2为浮点数) 
    }
  }
}
```

结果

```
#! Deprecation: [types removal] Specifying types in search requests is deprecated.
{
  "took" : 0,
  "timed_out" : false,
  "_shards" : {
    "total" : 1,
    "successful" : 1,
    "skipped" : 0,
    "failed" : 0
  },
  "hits" : {
    "total" : {
      "value" : 2,
      "relation" : "eq"
    },
    "max_score" : 1.8096983,
    "hits" : [
      {
        "_index" : "test",
        "_type" : "_doc",
        "_id" : "1",
        "_score" : 1.8096983,
        "_source" : {
          "title" : "python",
          "detail" : "python是世界上最好的语言"
        }
      },
      {
        "_index" : "test",
        "_type" : "_doc",
        "_id" : "2",
        "_score" : 0.7457469,
        "_source" : {
          "title" : "java是世界上最好的语言",
          "detail" : "python真的很简单"
        }
      }
    ]
  }
}
```

multi_match也可用当成match_phrase短语查询或者match_phrase_prefix最左前缀查询使用，只需要指定type字段

```
GET test/_doc/_search  
{
  "query":{
    "multi_match":{
      "query":"pyth",
      "fields":["title","detail"],
      "type":"phrase_prefix"            
    }
  }
}

```

```
GET test/_doc/_search
{
  "query":{
    "multi_match":{
      "query":"世界",
      "fields":["title","detail"],
      "type":"phrase"
    }
  }
}
```

#### term系列查询

创建映射（使用term，那么字段类型应该设置成keyword，如果使用text，那么创建的倒排索引保存的都是小写，使用精确查询的是大写字符，但保存的是小写，就查询不到）

```
PUT test
{
  "mappings": {
    "properties": {
      "title":{
        "type": "keyword"
      }
    }
  }
}
```

写入数据

```
PUT test/_doc/1
{
  "title":"ABCD"
}
PUT test/_doc/2
{
  "title":"abcd"
}
PUT test/_doc/3
{
  "title":"ABcd"
}
```

查询

```
GET test/_doc/_search
{
  "query":{
    "term":{
      "title":"ABCD"
    }
  }
}
```

结果

```
#! Deprecation: [types removal] Specifying types in search requests is deprecated.
{
  "took" : 0,
  "timed_out" : false,
  "_shards" : {
    "total" : 1,
    "successful" : 1,
    "skipped" : 0,
    "failed" : 0
  },
  "hits" : {
    "total" : {
      "value" : 1,
      "relation" : "eq"
    },
    "max_score" : 0.9808291,
    "hits" : [
      {
        "_index" : "test",
        "_type" : "_doc",
        "_id" : "1",
        "_score" : 0.9808291,
        "_source" : {
          "title" : "ABCD"
        }
      }
    ]
  }
}

```

如果查询多个字段用terms

```
GET test/_doc/_search
{
  "query":{
    "terms":{
      "title":["ABCD","abcd"]
    }
  }
}
```

```
#! Deprecation: [types removal] Specifying types in search requests is deprecated.
{
  "took" : 1,
  "timed_out" : false,
  "_shards" : {
    "total" : 1,
    "successful" : 1,
    "skipped" : 0,
    "failed" : 0
  },
  "hits" : {
    "total" : {
      "value" : 2,
      "relation" : "eq"
    },
    "max_score" : 1.0,
    "hits" : [
      {
        "_index" : "test",
        "_type" : "_doc",
        "_id" : "1",
        "_score" : 1.0,
        "_source" : {
          "title" : "ABCD"
        }
      },
      {
        "_index" : "test",
        "_type" : "_doc",
        "_id" : "2",
        "_score" : 1.0,
        "_source" : {
          "title" : "abcd"
        }
      }
    ]
  }
}
```

#### 排序查询

##### 降序(dasc)

```
GET sort/doc/_search
{
  "query":{
    "match_all": {}
  },
  "sort":[
    {
      "age":{
        "order":"desc"
      }
    }  
  ]
}
```

```
{
  "took" : 49,
  "timed_out" : false,
  "_shards" : {
    "total" : 1,
    "successful" : 1,
    "skipped" : 0,
    "failed" : 0
  },
  "hits" : {
    "total" : {
      "value" : 4,
      "relation" : "eq"
    },
    "max_score" : null,
    "hits" : [
      {
        "_index" : "sort",
        "_type" : "doc",
        "_id" : "2",
        "_score" : null,
        "_source" : {
          "name" : "Bss",
          "age" : 25
        },
        "sort" : [
          25
        ]
      },
      {
        "_index" : "sort",
        "_type" : "doc",
        "_id" : "4",
        "_score" : null,
        "_source" : {
          "name" : "Dss",
          "age" : 22
        },
        "sort" : [
          22
        ]
      },
      {
        "_index" : "sort",
        "_type" : "doc",
        "_id" : "3",
        "_score" : null,
        "_source" : {
          "name" : "Css",
          "age" : 18
        },
        "sort" : [
          18
        ]
      },
      {
        "_index" : "sort",
        "_type" : "doc",
        "_id" : "1",
        "_score" : null,
        "_source" : {
          "name" : "Ass",
          "age" : 16
        },
        "sort" : [
          16
        ]
      }
    ]
  }
}
```

##### 升序(asc)

```
GET sort/doc/_search
{
  "query":{
    "match_all": {}
  },
  "sort":[
    {
      "age":{
        "order":"esc"
      }
    }  
  ]
}
```

#### 分页查询

```
GET page/doc/_search
{
  "query":{
    "match_all": {}
  },
  "sort":[
    {
      "heats":{
        "order":"desc"
      }
    }
  ],
  "from":0,
  "size":2  # 默认一次最多10000
}
```

```
{
  "took" : 636,
  "timed_out" : false,
  "_shards" : {
    "total" : 1,
    "successful" : 1,
    "skipped" : 0,
    "failed" : 0
  },
  "hits" : {
    "total" : {
      "value" : 10,
      "relation" : "eq"
    },
    "max_score" : null,
    "hits" : [
      {
        "_index" : "page",
        "_type" : "doc",
        "_id" : "8",
        "_score" : null,
        "_source" : {
          "title" : "舞蹈专业",
          "heats" : 17531
        },
        "sort" : [
          17531
        ]
      },
      {
        "_index" : "page",
        "_type" : "doc",
        "_id" : "2",
        "_score" : null,
        "_source" : {
          "title" : "计算机软件工程专业",
          "heats" : 17524
        },
        "sort" : [
          17524
        ]
      }
    ]
  }
}

```

#### 布尔查询

##### 且查询(must)

查询城市在长沙且age18的

```
GET bool/doc/_search   
{
  "query":{
    "bool": {
      "must": [
        {
          "match": {
            "city": "长沙"
          }
        },
        {
          "match": {
            "age": 18
          }
        }
      ]
    }
  }
}
```

```
{
  "took" : 1,
  "timed_out" : false,
  "_shards" : {
    "total" : 1,
    "successful" : 1,
    "skipped" : 0,
    "failed" : 0
  },
  "hits" : {
    "total" : {
      "value" : 1,
      "relation" : "eq"
    },
    "max_score" : 3.059239,
    "hits" : [
      {
        "_index" : "bool",
        "_type" : "doc",
        "_id" : "1",
        "_score" : 3.059239,
        "_source" : {
          "name" : "Ass",
          "city" : "长沙",
          "age" : 18
        }
      }
    ]
  }
}
```

##### 或查询(should)

查询city是长沙且age为15岁

```
GET bool/doc/_search
{
  "query":{
    "bool": {
      "should": [
        {
          "match": {
            "city": "长沙"
          }
        },
        {
          "match": {
            "age": "15"
          }
        }
      ]
    }
  }
}
```

```
{
  "took" : 1,
  "timed_out" : false,
  "_shards" : {
    "total" : 1,
    "successful" : 1,
    "skipped" : 0,
    "failed" : 0
  },
  "hits" : {
    "total" : {
      "value" : 3,
      "relation" : "eq"
    },
    "max_score" : 2.059239,
    "hits" : [
      {
        "_index" : "bool",
        "_type" : "doc",
        "_id" : "1",
        "_score" : 2.059239,
        "_source" : {
          "name" : "Ass",
          "city" : "长沙",
          "age" : 18
        }
      },
      {
        "_index" : "bool",
        "_type" : "doc",
        "_id" : "4",
        "_score" : 2.059239,
        "_source" : {
          "name" : "Dss",
          "city" : "长沙",
          "age" : 20
        }
      },
      {
        "_index" : "bool",
        "_type" : "doc",
        "_id" : "5",
        "_score" : 1.0,
        "_source" : {
          "name" : "Ess",
          "city" : "岳阳",
          "age" : 15
        }
      }
    ]
  }
}
```

##### 非查询(must_not)

查询age不是18或city不是长沙的

```
GET bool/doc/_search
{
  "query":{
    "bool": {
      "must_not": [
        {
          "match": {
            "city": "长沙"
          }
        },
        {
          "match": {
            "age": "18"
          }
        }
      ]
    }
  }
}
```

```
{
  "took" : 11,
  "timed_out" : false,
  "_shards" : {
    "total" : 1,
    "successful" : 1,
    "skipped" : 0,
    "failed" : 0
  },
  "hits" : {
    "total" : {
      "value" : 3,
      "relation" : "eq"
    },
    "max_score" : 0.0,
    "hits" : [
      {
        "_index" : "bool",
        "_type" : "doc",
        "_id" : "2",
        "_score" : 0.0,
        "_source" : {
          "name" : "Bss",
          "city" : "北京",
          "age" : 19
        }
      },
      {
        "_index" : "bool",
        "_type" : "doc",
        "_id" : "5",
        "_score" : 0.0,
        "_source" : {
          "name" : "Ess",
          "city" : "岳阳",
          "age" : 15
        }
      },
      {
        "_index" : "bool",
        "_type" : "doc",
        "_id" : "6",
        "_score" : 0.0,
        "_source" : {
          "name" : "Fss",
          "city" : "北京",
          "age" : 17
        }
      }
    ]
  }
}
```

##### 过滤查询(filter)

- `filter`：过滤条件。
- `range`：条件筛选范围。
- `gt`：大于，相当于关系型数据库中的`>`。
- `gte`：大于等于，相当于关系型数据库中的`>=`。
- `lt`：小于，相当于关系型数据库中的`<`。
- `lte`：小于等于，相当于关系型数据库中的`<=`。

查询city为长沙且age大于等于15，小于等于18

```
GET bool/doc/_search
{
  "query":{
    "bool": {
      "must": [
        {
          "match": {
            "city": "长沙"
          }
        }
      ],
      "filter": [
        {
          "range": {
            "age": {
              "gte": 15,
              "lte": 18
            }
          }
        }
      ]
    }
  }
}
```

```
{
  "took" : 0,
  "timed_out" : false,
  "_shards" : {
    "total" : 1,
    "successful" : 1,
    "skipped" : 0,
    "failed" : 0
  },
  "hits" : {
    "total" : {
      "value" : 1,
      "relation" : "eq"
    },
    "max_score" : 2.059239,
    "hits" : [
      {
        "_index" : "bool",
        "_type" : "doc",
        "_id" : "1",
        "_score" : 2.059239,
        "_source" : {
          "name" : "Ass",
          "city" : "长沙",
          "age" : 18
        }
      }
    ]
  }
}
```

当`filter`与`should`同时使用时，效果和想象的有出入，因为在查询过程中先使用的`filter`进行过滤，再或运算，所以长沙的被放出来了，这里本应该现查询city为北京和岳阳的再对其进行age过滤的

```
GET bool/doc/_search
{
  "query":{
    "bool": {
      "should": [
        {
          "match": {
            "city": "北京"
          }
        },
        {
          "match": {
            "city": "岳阳"
          }
        }
      ],
      "filter": [
        {
          "range": {
            "age": {
              "gte": 15,
              "lte": 18
            }
          }
        }
      ]
    }
  }
}
```

```
#! Deprecation: [types removal] Specifying types in search requests is deprecated.
{
  "took" : 0,
  "timed_out" : false,
  "_shards" : {
    "total" : 1,
    "successful" : 1,
    "skipped" : 0,
    "failed" : 0
  },
  "hits" : {
    "total" : {
      "value" : 4,
      "relation" : "eq"
    },
    "max_score" : 2.059239,
    "hits" : [
      {
        "_index" : "bool",
        "_type" : "doc",
        "_id" : "3",
        "_score" : 2.059239,
        "_source" : {
          "name" : "Css",
          "city" : "岳阳",
          "age" : 18
        }
      },
      {
        "_index" : "bool",
        "_type" : "doc",
        "_id" : "5",
        "_score" : 2.059239,
        "_source" : {
          "name" : "Ess",
          "city" : "岳阳",
          "age" : 15
        }
      },
      {
        "_index" : "bool",
        "_type" : "doc",
        "_id" : "6",
        "_score" : 2.059239,
        "_source" : {
          "name" : "Fss",
          "city" : "北京",
          "age" : 17
        }
      },
      {
        "_index" : "bool",
        "_type" : "doc",
        "_id" : "1",
        "_score" : 0.0,
        "_source" : {
          "name" : "Ass",
          "city" : "长沙",
          "age" : 18
        }
      }
    ]
  }
}
```

#### 结果过滤

只获取name、tel、email字段

```
GET res/doc/_search
{
  "query":{
    "match_all": {}
  },
  "_source":[
    "name",
    "tel",
    "email"
  ]
}
```

```
{
  "took" : 0,
  "timed_out" : false,
  "_shards" : {
    "total" : 1,
    "successful" : 1,
    "skipped" : 0,
    "failed" : 0
  },
  "hits" : {
    "total" : {
      "value" : 3,
      "relation" : "eq"
    },
    "max_score" : 1.0,
    "hits" : [
      {
        "_index" : "res",
        "_type" : "doc",
        "_id" : "1",
        "_score" : 1.0,
        "_source" : {
          "name" : "orz",
          "tel" : "123456",
          "email" : "xxx@163.com"
        }
      },
      {
        "_index" : "res",
        "_type" : "doc",
        "_id" : "2",
        "_score" : 1.0,
        "_source" : {
          "name" : "屁屁",
          "tel" : "654321",
          "email" : "xxx@qq.com"
        }
      },
      {
        "_index" : "res",
        "_type" : "doc",
        "_id" : "3",
        "_score" : 1.0,
        "_source" : {
          "name" : "Ass",
          "tel" : "666666",
          "email" : "xxx@aliyun.com"
        }
      }
    ]
  }
}

```

#### 高亮显示

##### 默认

```
GET high/doc/_search
{
  "query":{
    "match": {
      "title": "梦"
    }
  },
  "highlight":{
    "fields": {
      "title": {}
    }
  }
}
```

```
#! Deprecation: [types removal] Specifying types in search requests is deprecated.
{
  "took" : 326,
  "timed_out" : false,
  "_shards" : {
    "total" : 1,
    "successful" : 1,
    "skipped" : 0,
    "failed" : 0
  },
  "hits" : {
    "total" : {
      "value" : 3,
      "relation" : "eq"
    },
    "max_score" : 0.1447331,
    "hits" : [
      {
        "_index" : "high",
        "_type" : "doc",
        "_id" : "2",
        "_score" : 0.1447331,
        "_source" : {
          "title" : "晓梦随疏钟，飘然蹑云霞"
        },
        "highlight" : {
          "title" : [
            "晓<em>梦</em>随疏钟，飘然蹑云霞"
          ]
        }
      },
      {
        "_index" : "high",
        "_type" : "doc",
        "_id" : "3",
        "_score" : 0.13064247,
        "_source" : {
          "title" : "夜来幽梦忽还乡，小轩窗，正梳妆"
        },
        "highlight" : {
          "title" : [
            "夜来幽<em>梦</em>忽还乡，小轩窗，正梳妆"
          ]
        }
      },
      {
        "_index" : "high",
        "_type" : "doc",
        "_id" : "1",
        "_score" : 0.12653615,
        "_source" : {
          "title" : "庄生晓梦迷蝴蝶，望帝春心托杜鹃"
        },
        "highlight" : {
          "title" : [
            "庄生晓<em>梦</em>迷蝴蝶，望帝春心托杜鹃"
          ]
        }
      }
    ]
  }
}
```

##### 自定义

```
GET high/doc/_search
{
  "query":{
    "match": {
      "title": "梦"
    }
  },
  "highlight":{
    "pre_tags": "<b class='high' style='color:red'>",
    "post_tags": "</b>", 
    "fields": {
      "title": {}
    }
  }
}
```

```
#! Deprecation: [types removal] Specifying types in search requests is deprecated.
{
  "took" : 1,
  "timed_out" : false,
  "_shards" : {
    "total" : 1,
    "successful" : 1,
    "skipped" : 0,
    "failed" : 0
  },
  "hits" : {
    "total" : {
      "value" : 3,
      "relation" : "eq"
    },
    "max_score" : 0.1447331,
    "hits" : [
      {
        "_index" : "high",
        "_type" : "doc",
        "_id" : "2",
        "_score" : 0.1447331,
        "_source" : {
          "title" : "晓梦随疏钟，飘然蹑云霞"
        },
        "highlight" : {
          "title" : [
            "晓<b class='high' style='color:red'>梦</b>随疏钟，飘然蹑云霞"
          ]
        }
      },
      {
        "_index" : "high",
        "_type" : "doc",
        "_id" : "3",
        "_score" : 0.13064247,
        "_source" : {
          "title" : "夜来幽梦忽还乡，小轩窗，正梳妆"
        },
        "highlight" : {
          "title" : [
            "夜来幽<b class='high' style='color:red'>梦</b>忽还乡，小轩窗，正梳妆"
          ]
        }
      },
      {
        "_index" : "high",
        "_type" : "doc",
        "_id" : "1",
        "_score" : 0.12653615,
        "_source" : {
          "title" : "庄生晓梦迷蝴蝶，望帝春心托杜鹃"
        },
        "highlight" : {
          "title" : [
            "庄生晓<b class='high' style='color:red'>梦</b>迷蝴蝶，望帝春心托杜鹃"
          ]
        }
      }
    ]
  }
}

```

#### 聚合函数

##### 平均(avg)

```
GET agg/doc/_search
{
    "query":{
      "match_all": {}
    },
    "aggs":{
      "my_avg":{
        "avg": {
          "field": "age"
        }
      }
    },
    "_source":[
        "name",
        "age",
        "tel"
      ]
    
}
```

```
{
  "took" : 0,
  "timed_out" : false,
  "_shards" : {
    "total" : 1,
    "successful" : 1,
    "skipped" : 0,
    "failed" : 0
  },
  "hits" : {
    "total" : {
      "value" : 3,
      "relation" : "eq"
    },
    "max_score" : 1.0,
    "hits" : [
      {
        "_index" : "agg",
        "_type" : "doc",
        "_id" : "1",
        "_score" : 1.0,
        "_source" : {
          "name" : "orz",
          "tel" : "123456",
          "age" : 18
        }
      },
      {
        "_index" : "agg",
        "_type" : "doc",
        "_id" : "2",
        "_score" : 1.0,
        "_source" : {
          "name" : "屁屁",
          "tel" : "654321",
          "age" : 25
        }
      },
      {
        "_index" : "agg",
        "_type" : "doc",
        "_id" : "3",
        "_score" : 1.0,
        "_source" : {
          "name" : "Ass",
          "tel" : "666666",
          "age" : 17
        }
      }
    ]
  },
  "aggregations" : {
    "my_avg" : {
      "value" : 20.0
    }
  }
}
```

##### 最大(max)

```
GET agg/doc/_search
{
    "query":{
      "match_all": {}
    },
    "aggs":{
      "my_max":{
        "max": {
          "field": "age"
        }
      }
    },
    "_source":[
        "name",
        "age",
        "tel"
      ]
    
}
```

```
{
  "took" : 79,
  "timed_out" : false,
  "_shards" : {
    "total" : 1,
    "successful" : 1,
    "skipped" : 0,
    "failed" : 0
  },
  "hits" : {
    "total" : {
      "value" : 3,
      "relation" : "eq"
    },
    "max_score" : 1.0,
    "hits" : [
      {
        "_index" : "agg",
        "_type" : "doc",
        "_id" : "1",
        "_score" : 1.0,
        "_source" : {
          "name" : "orz",
          "tel" : "123456",
          "age" : 18
        }
      },
      {
        "_index" : "agg",
        "_type" : "doc",
        "_id" : "2",
        "_score" : 1.0,
        "_source" : {
          "name" : "屁屁",
          "tel" : "654321",
          "age" : 25
        }
      },
      {
        "_index" : "agg",
        "_type" : "doc",
        "_id" : "3",
        "_score" : 1.0,
        "_source" : {
          "name" : "Ass",
          "tel" : "666666",
          "age" : 17
        }
      }
    ]
  },
  "aggregations" : {
    "my_max" : {
      "value" : 25.0
    }
  }
}

```

##### 最小(min)

```
GET agg/doc/_search
{
    "query":{
      "match_all": {}
    },
    "aggs":{
      "my_min":{
        "min": {
          "field": "age"
        }
      }
    },
    "_source":[
        "name",
        "age",
        "tel"
      ] 
}
```

```
{
  "took" : 0,
  "timed_out" : false,
  "_shards" : {
    "total" : 1,
    "successful" : 1,
    "skipped" : 0,
    "failed" : 0
  },
  "hits" : {
    "total" : {
      "value" : 3,
      "relation" : "eq"
    },
    "max_score" : 1.0,
    "hits" : [
      {
        "_index" : "agg",
        "_type" : "doc",
        "_id" : "1",
        "_score" : 1.0,
        "_source" : {
          "name" : "orz",
          "tel" : "123456",
          "age" : 18
        }
      },
      {
        "_index" : "agg",
        "_type" : "doc",
        "_id" : "2",
        "_score" : 1.0,
        "_source" : {
          "name" : "屁屁",
          "tel" : "654321",
          "age" : 25
        }
      },
      {
        "_index" : "agg",
        "_type" : "doc",
        "_id" : "3",
        "_score" : 1.0,
        "_source" : {
          "name" : "Ass",
          "tel" : "666666",
          "age" : 17
        }
      }
    ]
  },
  "aggregations" : {
    "my_min" : {
      "value" : 17.0
    }
  }
}
```

##### 求和(sum)

```
GET agg/doc/_search
{
    "query":{
      "match_all": {}
    },
    "aggs":{
      "my_sum":{
        "sum": {
          "field": "age"
        }
      }
    },
    "_source":[
        "name",
        "age",
        "tel"
      ]
    
}
```

```
{
  "took" : 0,
  "timed_out" : false,
  "_shards" : {
    "total" : 1,
    "successful" : 1,
    "skipped" : 0,
    "failed" : 0
  },
  "hits" : {
    "total" : {
      "value" : 3,
      "relation" : "eq"
    },
    "max_score" : 1.0,
    "hits" : [
      {
        "_index" : "agg",
        "_type" : "doc",
        "_id" : "1",
        "_score" : 1.0,
        "_source" : {
          "name" : "orz",
          "tel" : "123456",
          "age" : 18
        }
      },
      {
        "_index" : "agg",
        "_type" : "doc",
        "_id" : "2",
        "_score" : 1.0,
        "_source" : {
          "name" : "屁屁",
          "tel" : "654321",
          "age" : 25
        }
      },
      {
        "_index" : "agg",
        "_type" : "doc",
        "_id" : "3",
        "_score" : 1.0,
        "_source" : {
          "name" : "Ass",
          "tel" : "666666",
          "age" : 17
        }
      }
    ]
  },
  "aggregations" : {
    "my_sum" : {
      "value" : 60.0
    }
  }
}

```

##### 分组查询

```
GET agg/doc/_search
{
  "query":{
    "match_all": {}
  },
  "aggs":{
    "agg_group":{
      "range": {
        "field": "age",
        "ranges": [
          {
            "from": 15,
            "to": 17
          },
           {
            "from": 19,
            "to": 30
          }
        ]
      },
      "aggs":{
        "my_max":{
          "max": {
            "field": "age"
          }
        }
      }
    }
    
  }
}
```

```
{
  "took" : 0,
  "timed_out" : false,
  "_shards" : {
    "total" : 1,
    "successful" : 1,
    "skipped" : 0,
    "failed" : 0
  },
  "hits" : {
    "total" : {
      "value" : 4,
      "relation" : "eq"
    },
    "max_score" : 1.0,
    "hits" : [
      {
        "_index" : "agg",
        "_type" : "doc",
        "_id" : "1",
        "_score" : 1.0,
        "_source" : {
          "name" : "orz",
          "age" : 18,
          "city" : "长沙",
          "email" : "xxx@163.com",
          "tel" : "123456"
        }
      },
      {
        "_index" : "agg",
        "_type" : "doc",
        "_id" : "2",
        "_score" : 1.0,
        "_source" : {
          "name" : "屁屁",
          "age" : 25,
          "city" : "北京",
          "email" : "xxx@qq.com",
          "tel" : "654321"
        }
      },
      {
        "_index" : "agg",
        "_type" : "doc",
        "_id" : "3",
        "_score" : 1.0,
        "_source" : {
          "name" : "Ass",
          "age" : 17,
          "city" : "岳阳",
          "email" : "xxx@aliyun.com",
          "tel" : "666666"
        }
      },
      {
        "_index" : "agg",
        "_type" : "doc",
        "_id" : "4",
        "_score" : 1.0,
        "_source" : {
          "name" : "Bss",
          "age" : 16,
          "city" : "深圳",
          "email" : "123@qq.com",
          "tel" : "888888"
        }
      }
    ]
  },
  "aggregations" : {
    "agg_group" : {
      "buckets" : [
        {
          "key" : "15.0-17.0",
          "from" : 15.0,
          "to" : 17.0,
          "doc_count" : 1,
          "my_max" : {
            "value" : 16.0
          }
        },
        {
          "key" : "19.0-30.0",
          "from" : 19.0,
          "to" : 30.0,
          "doc_count" : 1,
          "my_max" : {
            "value" : 25.0
          }
        }
      ]
    }
  }
}
```

## mapping映射

映射是用来定义一个文档及其包含的字段如何存储和索引的过程

### 映射操作

#### 基本创建

ES7默认不在支持指定索引类型，默认索引类型是_doc，(如果想像ES6一样设置类型，则配置`include_type_name: true `即可(用7.9版本试了一下，好像不行。建议不要这么做，因为ES8后就不在提供该字段)

- ES6版本

    ```
    PUT map
    {
      "mappings": {
        "doc":{
          "properties": {
            "name":{
              "type": "text"
            },
            "age":{
              "type": "text"
            }
          }
        }
      }
    }
    ```
    
- ES7版本

    ```
    PUT map
    {
      "mappings": {
        "properties": {
          "name":{
            "type": "text"
          },
          "age":{
            "type": "text"
          }
        }
      }
    }
    ```


#### 查看映射

如果不会写映射关系，可用直接插入数据，再查看映射照着写

```
GET map/_mapping
```

```
{
  "map" : {
    "mappings" : {
      "properties" : {
        "age" : {
          "type" : "long"
        },
        "name" : {
          "type" : "text"
        }
      }
    }
  }
}
```

### mapping字段参数

#### 字段的数据类型(type)

- 简单类型，如文本（`text`）、关键字（`keyword`）、日期（`date`）、整形（`long`）、双精度（`double`）、布尔（`boolean`）或`ip`。
- 可以是支持JSON的层次结构性质的类型，如对象或嵌套。
- 或者一种特殊类型，如`geo_point`、`geo_shape`或`completion`。

#### 创建索引(index)

```
PUT map
{
  "mappings": {
    "properties": {
      "name":{
        "type": "text"
      },
      "age":{
        "type": "text",
        "index": false       # 设置false后将不会创建索引，也不可以可以通过该字段来查询
      }
    }
  }
}
```

#### 复制字段(copy_to)

```
PUT mmp
{
  "mappings": {
    "properties": {
      "name":{
        "type": "text",
        "copy_to": "q"    # 多个用["q","y"]
      },
      "age":{
        "type": "long",
        "copy_to": "q"
      },
      "q":{
        "type": "text"  # 如果用keyword不会做分词
      }
    }
  }
}
```

将多个字段copy到q字段上，查询时可通过q字段对age和name进行查询，当创建字段时如下所示

```
PUT map/_doc/1
{
	"name":"orz",
	"age":18,
	"q":"aaa"	# 这个可写可不写
}
```

查询如下

```
GET map/_doc/_search
{
	"query":{
		"match":{
			"q":18    # 或者"q":"orz" "q":"aaa" 都可查询到该数据
		}
	}
}
```

#### 长度(ignore_above)

长于`ignore_above`设置的字符串将不会被索引或存储。对于字符串数组，`ignore_above`将分别应用于每个数组元素，且字符串元素的长度大于`ignore_above`将不会被索引或存储的字符串元素。

```
PUT len
{
  "mappings": {
    "properties": {
      "title": {
        "type":"keyword",   # 只能keyword，如果长度超过后会存储但不会建立索引
        "ignore_above": 10
      }
    }
  }
}
```



### 对象属性

前面讲的都是一层嵌套，如果是多层嵌套结构那该如何创建和查询呢?

```
PUT userinfo
{
  "mappings": {
    "properties": {
      "name":{
        "type": "text"
      },
      "age":{
        "type": "text"
      },
      "info":{
        "properties": {
          "nickname":{
            "type":"text"
          },
          "username":{
            "type":"text"
          },
          "password":{
            "type":"text",
            "index":false
          }
        }
      }
    }
  }
}
```

写入数据

```
PUT userinfo/_doc/1
{
	"name":"orz",
	"age":18,
	"info":{
		"nickname":"屁屁",
		"username":"m5xhsy",
		"password":"ass0876"
	}
}
```

查询数据

```
GET userinfo/_doc/_search
{
	"query":{
		"match":{
			"info.username":"m5xhsy"  # 用点的方式指定字段
		}
	}
}
```

### 映射三种状态

#### dynamic等于true

**这种模式创建后可用动态添加其他字段，和普通创建一样**

```
PUT map1
{
  "mappings": {
    "dynamic": true, 
    "properties": {
      "name":{
        "type": "text"
      },
      "age":{
        "type": "long"
      }
    }
  }
}
```

```
{
  "acknowledged" : true,
  "shards_acknowledged" : true,
  "index" : "map1"
}
```

#### dynamic等于false

**当映射关系创建后，如果再添加其他字段，可添加成功，但是不会进行分词，也不会添加索引，也就是说，如果通过后加入的字段进行查询，将查询不到**

```
PUT map2
{
  "mappings": {
    "dynamic":false,
    "properties": {
      "name":{
        "type": "text"
      },
      "age":{
        "type": "long"
      }
    }
  }
}
```

```
{
  "acknowledged" : true,
  "shards_acknowledged" : true,
  "index" : "map2"
}

```

#### dynamic等于strict

**比较严格的一种映射关系，创建后如果添加其他字段，就会报错，但是可以少写一个字段**

```
PUT map3
{
  "mappings": {
    "dynamic":"strict",
    "properties": {
      "name":{
        "type": "text"
      },
      "age":{
        "type": "long"
      }
    }
  }
}
```

```
{
  "acknowledged" : true,
  "shards_acknowledged" : true,
  "index" : "map3"
}
```

## settings设置

创建

```
PUT set
{
  "settings": {
    "number_of_shards": 1,   # 1个主分片
    "number_of_replicas": 0   # 0个复制分片
  }
}
```

查看

```
GET set 
```

```
{
  "set" : {
    "aliases" : { },   # 别名
    "mappings" : { },
    "settings" : {
      "index" : {    
        "creation_date" : "1604732236768",   # 创建时间
        "number_of_shards" : "1",          # 主分片
        "number_of_replicas" : "0",			# 复制分片
        "uuid" : "xfX9tAtjRR-buzQEcefbXQ",  # 
        "version" : {
          "created" : "7090399"
        },
        "provided_name" : "set"
      }
    }
  }
}
```

## 分析流程

1. 原始文本
2. 进入字符过滤器(比如将&转为and)
3. 进入标准分词器(将语句转换成一个一个的词)
4. 进入分词过滤器
   1. 全转小写
   2. 去除停用词
   3. 去除同义词
5. 建立倒排索引

## 分析器

### 标准分析器(standard analyzer)

标准分析器是Elasticsearch默认使用的分析器。它是分析各种语言文本最常用的选择。它根据 Unicode 联盟定义的 *单词边界* 划分文本。删除绝大部分标点。最后，将词条小写。

```
POST _analyze
{
  "analyzer": "standard",
  "text": "The 2 QUICK Brown-Foxes jumped over the lazy dog's bone."
}
```

输出结果：

```
[ the, 2, quick, brown, foxes, jumped, over, the, lazy, dog's, bone ]
```

```
{
  "tokens" : [
    {
      "token" : "the",
      "start_offset" : 0,
      "end_offset" : 3,
      "type" : "<ALPHANUM>",
      "position" : 0
    },
    {
      "token" : "2",
      "start_offset" : 4,
      "end_offset" : 5,
      "type" : "<NUM>",
      "position" : 1
    },
    {
      "token" : "quick",
      "start_offset" : 6,
      "end_offset" : 11,
      "type" : "<ALPHANUM>",
      "position" : 2
    },
    {
      "token" : "brown",
      "start_offset" : 12,
      "end_offset" : 17,
      "type" : "<ALPHANUM>",
      "position" : 3
    },
    {
      "token" : "foxes",
      "start_offset" : 18,
      "end_offset" : 23,
      "type" : "<ALPHANUM>",
      "position" : 4
    },
    {
      "token" : "jumped",
      "start_offset" : 24,
      "end_offset" : 30,
      "type" : "<ALPHANUM>",
      "position" : 5
    },
    {
      "token" : "over",
      "start_offset" : 31,
      "end_offset" : 35,
      "type" : "<ALPHANUM>",
      "position" : 6
    },
    {
      "token" : "the",
      "start_offset" : 36,
      "end_offset" : 39,
      "type" : "<ALPHANUM>",
      "position" : 7
    },
    {
      "token" : "lazy",
      "start_offset" : 40,
      "end_offset" : 44,
      "type" : "<ALPHANUM>",
      "position" : 8
    },
    {
      "token" : "dog's",
      "start_offset" : 45,
      "end_offset" : 50,
      "type" : "<ALPHANUM>",
      "position" : 9
    },
    {
      "token" : "bone",
      "start_offset" : 51,
      "end_offset" : 55,
      "type" : "<ALPHANUM>",
      "position" : 10
    }
  ]
}

```

### 简单分析器(simple analyzer)

该`simple`分析仪符文本在任何非字母字符标记，如数字，空格，连字符和撇号，丢弃非字母字符，并改变大写字母为小写。

```
POST _analyze
{
  "analyzer": "simple",
  "text": "The 2 QUICK Brown-Foxes jumped over the lazy dog's bone."
}
```

输出结果：

```text
[ the, quick, brown, foxes, jumped, over, the, lazy, dog, s, bone ]
```

```
{
  "tokens" : [
    {
      "token" : "the",
      "start_offset" : 0,
      "end_offset" : 3,
      "type" : "word",
      "position" : 0
    },
    {
      "token" : "quick",
      "start_offset" : 6,
      "end_offset" : 11,
      "type" : "word",
      "position" : 1
    },
    {
      "token" : "brown",
      "start_offset" : 12,
      "end_offset" : 17,
      "type" : "word",
      "position" : 2
    },
    {
      "token" : "foxes",
      "start_offset" : 18,
      "end_offset" : 23,
      "type" : "word",
      "position" : 3
    },
    {
      "token" : "jumped",
      "start_offset" : 24,
      "end_offset" : 30,
      "type" : "word",
      "position" : 4
    },
    {
      "token" : "over",
      "start_offset" : 31,
      "end_offset" : 35,
      "type" : "word",
      "position" : 5
    },
    {
      "token" : "the",
      "start_offset" : 36,
      "end_offset" : 39,
      "type" : "word",
      "position" : 6
    },
    {
      "token" : "lazy",
      "start_offset" : 40,
      "end_offset" : 44,
      "type" : "word",
      "position" : 7
    },
    {
      "token" : "dog",
      "start_offset" : 45,
      "end_offset" : 48,
      "type" : "word",
      "position" : 8
    },
    {
      "token" : "s",
      "start_offset" : 49,
      "end_offset" : 50,
      "type" : "word",
      "position" : 9
    },
    {
      "token" : "bone",
      "start_offset" : 51,
      "end_offset" : 55,
      "type" : "word",
      "position" : 10
    }
  ]
}

```

### 空白分析器(whitespace analyzer)

空格分析器在空格的地方划分文本

```
POST _analyze
{
  "analyzer": "whitespace",
  "text": "The 2 QUICK Brown-Foxes jumped over the lazy dog's bone."
}
```

```
[ The, 2, QUICK, Brown-Foxes, jumped, over, the, lazy, dog's, bone. ]
```

```
{
  "tokens" : [
    {
      "token" : "The",
      "start_offset" : 0,
      "end_offset" : 3,
      "type" : "word",
      "position" : 0
    },
    {
      "token" : "2",
      "start_offset" : 4,
      "end_offset" : 5,
      "type" : "word",
      "position" : 1
    },
    {
      "token" : "QUICK",
      "start_offset" : 6,
      "end_offset" : 11,
      "type" : "word",
      "position" : 2
    },
    {
      "token" : "Brown-Foxes",
      "start_offset" : 12,
      "end_offset" : 23,
      "type" : "word",
      "position" : 3
    },
    {
      "token" : "jumped",
      "start_offset" : 24,
      "end_offset" : 30,
      "type" : "word",
      "position" : 4
    },
    {
      "token" : "over",
      "start_offset" : 31,
      "end_offset" : 35,
      "type" : "word",
      "position" : 5
    },
    {
      "token" : "the",
      "start_offset" : 36,
      "end_offset" : 39,
      "type" : "word",
      "position" : 6
    },
    {
      "token" : "lazy",
      "start_offset" : 40,
      "end_offset" : 44,
      "type" : "word",
      "position" : 7
    },
    {
      "token" : "dog's",
      "start_offset" : 45,
      "end_offset" : 50,
      "type" : "word",
      "position" : 8
    },
    {
      "token" : "bone.",
      "start_offset" : 51,
      "end_offset" : 56,
      "type" : "word",
      "position" : 9
    }
  ]
}

```

### 停用词分析器(stop analyzer)

该停用词分析器和简单分析器是一样的，但增加了对移除停止字的支持。默认情况下使用 `_english_`停用词。

```
POST _analyze
{
  "analyzer": "stop",
  "text": "The 2 QUICK Brown-Foxes jumped over the lazy dog's bone."
}
```

```text
[ quick, brown, foxes, jumped, over, lazy, dog, s, bone ]
```

```
{
  "tokens" : [
    {
      "token" : "quick",
      "start_offset" : 6,
      "end_offset" : 11,
      "type" : "word",
      "position" : 1
    },
    {
      "token" : "brown",
      "start_offset" : 12,
      "end_offset" : 17,
      "type" : "word",
      "position" : 2
    },
    {
      "token" : "foxes",
      "start_offset" : 18,
      "end_offset" : 23,
      "type" : "word",
      "position" : 3
    },
    {
      "token" : "jumped",
      "start_offset" : 24,
      "end_offset" : 30,
      "type" : "word",
      "position" : 4
    },
    {
      "token" : "over",
      "start_offset" : 31,
      "end_offset" : 35,
      "type" : "word",
      "position" : 5
    },
    {
      "token" : "lazy",
      "start_offset" : 40,
      "end_offset" : 44,
      "type" : "word",
      "position" : 7
    },
    {
      "token" : "dog",
      "start_offset" : 45,
      "end_offset" : 48,
      "type" : "word",
      "position" : 8
    },
    {
      "token" : "s",
      "start_offset" : 49,
      "end_offset" : 50,
      "type" : "word",
      "position" : 9
    },
    {
      "token" : "bone",
      "start_offset" : 51,
      "end_offset" : 55,
      "type" : "word",
      "position" : 10
    }
  ]
}
```

### 关键词分析器(keyword analyzer)

该`keyword`分析器是一个“noop”分析器，它将整个输入字符串作为单个令牌返回。

```
POST _analyze
{
  "analyzer": "keyword",
  "text": "The 2 QUICK Brown-Foxes jumped over the lazy dog's bone."
}

```

```
[ The 2 QUICK Brown-Foxes jumped over the lazy dog's bone. ]
```

```
{
  "tokens" : [
    {
      "token" : "The 2 QUICK Brown-Foxes jumped over the lazy dog's bone.",
      "start_offset" : 0,
      "end_offset" : 56,
      "type" : "word",
      "position" : 0
    }
  ]
}

```

### 模式分析器(pattern analyzer)

所述`pattern`分析仪使用一个正则表达式的文本分成条款。正则表达式应与**令牌分隔符** 而不是令牌本身匹配。正则表达式默认为`\W+`（或所有非单词字符）

```console
POST _analyze
{
  "analyzer": "pattern",
  "text": "The 2 QUICK Brown-Foxes jumped over the lazy dog's bone."
}
```

```
[ the, 2, quick, brown, foxes, jumped, over, the, lazy, dog, s, bone ]
```

```
{
  "tokens" : [
    {
      "token" : "the",
      "start_offset" : 0,
      "end_offset" : 3,
      "type" : "word",
      "position" : 0
    },
    {
      "token" : "2",
      "start_offset" : 4,
      "end_offset" : 5,
      "type" : "word",
      "position" : 1
    },
    {
      "token" : "quick",
      "start_offset" : 6,
      "end_offset" : 11,
      "type" : "word",
      "position" : 2
    },
    {
      "token" : "brown",
      "start_offset" : 12,
      "end_offset" : 17,
      "type" : "word",
      "position" : 3
    },
    {
      "token" : "foxes",
      "start_offset" : 18,
      "end_offset" : 23,
      "type" : "word",
      "position" : 4
    },
    {
      "token" : "jumped",
      "start_offset" : 24,
      "end_offset" : 30,
      "type" : "word",
      "position" : 5
    },
    {
      "token" : "over",
      "start_offset" : 31,
      "end_offset" : 35,
      "type" : "word",
      "position" : 6
    },
    {
      "token" : "the",
      "start_offset" : 36,
      "end_offset" : 39,
      "type" : "word",
      "position" : 7
    },
    {
      "token" : "lazy",
      "start_offset" : 40,
      "end_offset" : 44,
      "type" : "word",
      "position" : 8
    },
    {
      "token" : "dog",
      "start_offset" : 45,
      "end_offset" : 48,
      "type" : "word",
      "position" : 9
    },
    {
      "token" : "s",
      "start_offset" : 49,
      "end_offset" : 50,
      "type" : "word",
      "position" : 10
    },
    {
      "token" : "bone",
      "start_offset" : 51,
      "end_offset" : 55,
      "type" : "word",
      "position" : 11
    }
  ]
}

```

也可以用来制定一个&符号分析器

```
PUT pattern
{
  "settings": {
    "analysis": {
      "analyzer": {
        "my_analyzer":{     # 这个字段可自定义  
          "tokenizer":"and_tokenizer"  #这个字段自定义，和下面那个字段应该一致   
        }
      },
      "tokenizer": {
        "and_tokenizer":{
          "type":"pattern",
          "pattern":"&"
        }
      }
    }
  }
}
POST pattern/_analyze
{
  "tokenizer": "and_tokenizer",
  "text":"Ass&Bss&Css"
}
```

结果如下

```
{
  "tokens" : [
    {
      "token" : "Ass",
      "start_offset" : 0,
      "end_offset" : 3,
      "type" : "word",
      "position" : 0
    },
    {
      "token" : "Bss",
      "start_offset" : 4,
      "end_offset" : 7,
      "type" : "word",
      "position" : 1
    },
    {
      "token" : "Css",
      "start_offset" : 8,
      "end_offset" : 11,
      "type" : "word",
      "position" : 2
    }
  ]
}

```

### 语言和多语言分析器(chinese)

```
POST _analyze
{
  "analyzer": "chinese",
  "text": "The 2 QUICK Brown-Foxes jumped over the lazy dog's bone.我的天哪"
}
```

```
{
  "tokens" : [
    {
      "token" : "2",
      "start_offset" : 4,
      "end_offset" : 5,
      "type" : "<NUM>",
      "position" : 1
    },
    {
      "token" : "quick",
      "start_offset" : 6,
      "end_offset" : 11,
      "type" : "<ALPHANUM>",
      "position" : 2
    },
    {
      "token" : "brown",
      "start_offset" : 12,
      "end_offset" : 17,
      "type" : "<ALPHANUM>",
      "position" : 3
    },
    {
      "token" : "foxes",
      "start_offset" : 18,
      "end_offset" : 23,
      "type" : "<ALPHANUM>",
      "position" : 4
    },
    {
      "token" : "jumped",
      "start_offset" : 24,
      "end_offset" : 30,
      "type" : "<ALPHANUM>",
      "position" : 5
    },
    {
      "token" : "over",
      "start_offset" : 31,
      "end_offset" : 35,
      "type" : "<ALPHANUM>",
      "position" : 6
    },
    {
      "token" : "lazy",
      "start_offset" : 40,
      "end_offset" : 44,
      "type" : "<ALPHANUM>",
      "position" : 8
    },
    {
      "token" : "dog's",
      "start_offset" : 45,
      "end_offset" : 50,
      "type" : "<ALPHANUM>",
      "position" : 9
    },
    {
      "token" : "bone",
      "start_offset" : 51,
      "end_offset" : 55,
      "type" : "<ALPHANUM>",
      "position" : 10
    },
    {
      "token" : "我",
      "start_offset" : 56,
      "end_offset" : 57,
      "type" : "<IDEOGRAPHIC>",
      "position" : 11
    },
    {
      "token" : "的",
      "start_offset" : 57,
      "end_offset" : 58,
      "type" : "<IDEOGRAPHIC>",
      "position" : 12
    },
    {
      "token" : "天",
      "start_offset" : 58,
      "end_offset" : 59,
      "type" : "<IDEOGRAPHIC>",
      "position" : 13
    },
    {
      "token" : "哪",
      "start_offset" : 59,
      "end_offset" : 60,
      "type" : "<IDEOGRAPHIC>",
      "position" : 14
    }
  ]
}
```

### 雪球分析器(snowball analyzer)

雪球分析器（snowball analyzer）除了使用标准的分词和分词过滤器（和标准分析器一样）也是用了小写分词过滤器和停用词过滤器，除此之外，它还是用了雪球词干器对文本进行词干提取。

```
POST _analyze
{
  "analyzer": "snowball",
  "text":"The 2 QUICK Brown-Foxes jumped over the lazy dog's bone."
}
```

```
{
  "tokens" : [
    {
      "token" : "2",
      "start_offset" : 4,
      "end_offset" : 5,
      "type" : "<NUM>",
      "position" : 1
    },
    {
      "token" : "quick",
      "start_offset" : 6,
      "end_offset" : 11,
      "type" : "<ALPHANUM>",
      "position" : 2
    },
    {
      "token" : "brown",
      "start_offset" : 12,
      "end_offset" : 17,
      "type" : "<ALPHANUM>",
      "position" : 3
    },
    {
      "token" : "fox",
      "start_offset" : 18,
      "end_offset" : 23,
      "type" : "<ALPHANUM>",
      "position" : 4
    },
    {
      "token" : "jump",
      "start_offset" : 24,
      "end_offset" : 30,
      "type" : "<ALPHANUM>",
      "position" : 5
    },
    {
      "token" : "over",
      "start_offset" : 31,
      "end_offset" : 35,
      "type" : "<ALPHANUM>",
      "position" : 6
    },
    {
      "token" : "lazi",
      "start_offset" : 40,
      "end_offset" : 44,
      "type" : "<ALPHANUM>",
      "position" : 8
    },
    {
      "token" : "dog",
      "start_offset" : 45,
      "end_offset" : 50,
      "type" : "<ALPHANUM>",
      "position" : 9
    },
    {
      "token" : "bone",
      "start_offset" : 51,
      "end_offset" : 55,
      "type" : "<ALPHANUM>",
      "position" : 10
    }
  ]
}

```

## 字符过滤器

### HTML过滤器

```
GET /_analyze
{
  "tokenizer": "keyword",
  "char_filter": [
    "html_strip"
  ],
  "text": "<p>I&apos;m so <b>happy</b>!</p>"
}
```

```
{
  "tokens" : [
    {
      "token" : """
I'm so happy!
""",
      "start_offset" : 0,
      "end_offset" : 32,
      "type" : "word",
      "position" : 0
    }
  ]
}
```

### 映射字符过滤器

映射字符过滤器接收键和值的映射。每当遇到与键相同的字符串时，它将用与该键关联的值替换它们

```
GET /_analyze
{
  "tokenizer": "keyword",
  "char_filter": [
    {
      "type": "mapping",
      "mappings": [
        "٠ => 0",
        "١ => 1",
        "٢ => 2",
        "٣ => 3",
        "٤ => 4",
        "٥ => 5",
        "٦ => 6",
        "٧ => 7",
        "٨ => 8",
        "٩ => 9"
      ]
    }
  ],
  "text": "My license plate is ٢٥٠١٥"
}
```

```
{
  "tokens" : [
    {
      "token" : "My license plate is 25015",
      "start_offset" : 0,
      "end_offset" : 25,
      "type" : "word",
      "position" : 0
    }
  ]
}
```

也可以这样定义

```
PUT map_filter
{
  "settings": {
    "analysis": {
      "analyzer": {
        "my_analyzer_filter":{
          "tokenizer":"keyword",
          "char_filter":["my_filter"]
        }
      },
      "char_filter":{
          "my_filter":{
            "type":"mapping",
            "mappings":["a => A","bbb => B"]
          }
        }
    }
  }
}

POST map_filter/_analyze
{
  "analyzer": "my_analyzer_filter",
  "text": "abCaDJFKbJSDab"
}
```

结果如下

```
{
  "tokens" : [
    {
      "token" : "AbCADJFKbJSDAb",
      "start_offset" : 0,
      "end_offset" : 14,
      "type" : "word",
      "position" : 0
    }
  ]
}

```

### 模式替换字符过滤器

模式替换字符过滤器使用一个正则表达式匹配应该与指定替换字符串替换字符。替换字符串可以引用正则表达式中的捕获组。

```
PUT my-index-00001
{
  "settings": {
    "analysis": {
      "analyzer": {
        "my_analyzer": {
          "tokenizer": "standard",
          "char_filter": [
            "my_char_filter"
          ]
        }
      },
      "char_filter": {
        "my_char_filter": {
          "type": "pattern_replace",
          "pattern": "(\\d+)-(?=\\d)",   # 正则表达式
          "replacement": "$1_" 	 		# 替换字符串
        }
      }
    }
  }
}

POST my-index-00001/_analyze
{
  "analyzer": "my_analyzer",
  "text": "My credit card is 123-456-789"
}
```

结果

```
[ My, credit, card, is, 123_456_789 ]
```

```
{
  "tokens" : [
    {
      "token" : "My",
      "start_offset" : 0,
      "end_offset" : 2,
      "type" : "<ALPHANUM>",
      "position" : 0
    },
    {
      "token" : "credit",
      "start_offset" : 3,
      "end_offset" : 9,
      "type" : "<ALPHANUM>",
      "position" : 1
    },
    {
      "token" : "card",
      "start_offset" : 10,
      "end_offset" : 14,
      "type" : "<ALPHANUM>",
      "position" : 2
    },
    {
      "token" : "is",
      "start_offset" : 15,
      "end_offset" : 17,
      "type" : "<ALPHANUM>",
      "position" : 3
    },
    {
      "token" : "123_456_789",
      "start_offset" : 18,
      "end_offset" : 29,
      "type" : "<NUM>",
      "position" : 4
    }
  ]
}

```

## 分词器

### 标准分词器(standard tokenizer)

标准分词器（standard tokenizer）是一个基于语法的分词器，对于大多数欧洲语言来说还是不错的，它同时还处理了Unicode文本的分词，但分词默认的最大长度是255字节，它也移除了逗号和句号这样的标点符号。

```console
POST _analyze
{
  "tokenizer": "whitespace",
  "text": "The 2 QUICK Brown-Foxes jumped over the lazy dog's bone."
}
```

```text
[ The, 2, QUICK, Brown-Foxes, jumped, over, the, lazy, dog's, bone. ]
```

```
{
  "tokens" : [
    {
      "token" : "The",
      "start_offset" : 0,
      "end_offset" : 3,
      "type" : "word",
      "position" : 0
    },
    {
      "token" : "2",
      "start_offset" : 4,
      "end_offset" : 5,
      "type" : "word",
      "position" : 1
    },
    {
      "token" : "QUICK",
      "start_offset" : 6,
      "end_offset" : 11,
      "type" : "word",
      "position" : 2
    },
    {
      "token" : "Brown-Foxes",
      "start_offset" : 12,
      "end_offset" : 23,
      "type" : "word",
      "position" : 3
    },
    {
      "token" : "jumped",
      "start_offset" : 24,
      "end_offset" : 30,
      "type" : "word",
      "position" : 4
    },
    {
      "token" : "over",
      "start_offset" : 31,
      "end_offset" : 35,
      "type" : "word",
      "position" : 5
    },
    {
      "token" : "the",
      "start_offset" : 36,
      "end_offset" : 39,
      "type" : "word",
      "position" : 6
    },
    {
      "token" : "lazy",
      "start_offset" : 40,
      "end_offset" : 44,
      "type" : "word",
      "position" : 7
    },
    {
      "token" : "dog's",
      "start_offset" : 45,
      "end_offset" : 50,
      "type" : "word",
      "position" : 8
    },
    {
      "token" : "bone.",
      "start_offset" : 51,
      "end_offset" : 56,
      "type" : "word",
      "position" : 9
    }
  ]
}

```

### 关键词分词器(keyword tokenizer)

关键词分词器（keyword tokenizer）是一种简单的分词器，将整个文本作为单个的分词，提供给分词过滤器，当你只想用分词过滤器，而不做分词操作时，它是不错的选择

```console
POST _analyze
{
  "tokenizer": "keyword",
  "text": "New York"
}
```

```text
[ New York ]
```

```
{
  "tokens" : [
    {
      "token" : "New York",
      "start_offset" : 0,
      "end_offset" : 8,
      "type" : "word",
      "position" : 0
    }
  ]
}
```

### 字母分词器(letter tokenizer)

该字母分词器根据非字母的符号，将文本切分成分词。对于大多数欧洲语言来说，它的工作是合理的，但是对于某些亚洲语言来说，这是很糟糕的，因为亚洲语言的单词之间没有空格。

```console
POST _analyze
{
  "tokenizer": "letter",
  "text": "The 2 QUICK Brown-Foxes jumped over the lazy dog's bone."
}
```

```text
[ The, QUICK, Brown, Foxes, jumped, over, the, lazy, dog, s, bone ]
```

```
{
  "tokens" : [
    {
      "token" : "The",
      "start_offset" : 0,
      "end_offset" : 3,
      "type" : "word",
      "position" : 0
    },
    {
      "token" : "QUICK",
      "start_offset" : 6,
      "end_offset" : 11,
      "type" : "word",
      "position" : 1
    },
    {
      "token" : "Brown",
      "start_offset" : 12,
      "end_offset" : 17,
      "type" : "word",
      "position" : 2
    },
    {
      "token" : "Foxes",
      "start_offset" : 18,
      "end_offset" : 23,
      "type" : "word",
      "position" : 3
    },
    {
      "token" : "jumped",
      "start_offset" : 24,
      "end_offset" : 30,
      "type" : "word",
      "position" : 4
    },
    {
      "token" : "over",
      "start_offset" : 31,
      "end_offset" : 35,
      "type" : "word",
      "position" : 5
    },
    {
      "token" : "the",
      "start_offset" : 36,
      "end_offset" : 39,
      "type" : "word",
      "position" : 6
    },
    {
      "token" : "lazy",
      "start_offset" : 40,
      "end_offset" : 44,
      "type" : "word",
      "position" : 7
    },
    {
      "token" : "dog",
      "start_offset" : 45,
      "end_offset" : 48,
      "type" : "word",
      "position" : 8
    },
    {
      "token" : "s",
      "start_offset" : 49,
      "end_offset" : 50,
      "type" : "word",
      "position" : 9
    },
    {
      "token" : "bone",
      "start_offset" : 51,
      "end_offset" : 55,
      "type" : "word",
      "position" : 10
    }
  ]
}
```

### 小写分词器(lowercase tokenizer)

小写分词器（lowercase tokenizer）结合了常规的字母分词器和小写分词过滤器（跟你想的一样，就是将所有的分词转化为小写）的行为。通过一个单独的分词器来实现的主要原因是，一次进行两项操作会获得更好的性能

```console
POST _analyze
{
  "tokenizer": "lowercase",
  "text": "The 2 QUICK Brown-Foxes jumped over the lazy dog's bone."
}
```

```text
[ the, quick, brown, foxes, jumped, over, the, lazy, dog, s, bone ]
```

```
{
  "tokens" : [
    {
      "token" : "the",
      "start_offset" : 0,
      "end_offset" : 3,
      "type" : "word",
      "position" : 0
    },
    {
      "token" : "quick",
      "start_offset" : 6,
      "end_offset" : 11,
      "type" : "word",
      "position" : 1
    },
    {
      "token" : "brown",
      "start_offset" : 12,
      "end_offset" : 17,
      "type" : "word",
      "position" : 2
    },
    {
      "token" : "foxes",
      "start_offset" : 18,
      "end_offset" : 23,
      "type" : "word",
      "position" : 3
    },
    {
      "token" : "jumped",
      "start_offset" : 24,
      "end_offset" : 30,
      "type" : "word",
      "position" : 4
    },
    {
      "token" : "over",
      "start_offset" : 31,
      "end_offset" : 35,
      "type" : "word",
      "position" : 5
    },
    {
      "token" : "the",
      "start_offset" : 36,
      "end_offset" : 39,
      "type" : "word",
      "position" : 6
    },
    {
      "token" : "lazy",
      "start_offset" : 40,
      "end_offset" : 44,
      "type" : "word",
      "position" : 7
    },
    {
      "token" : "dog",
      "start_offset" : 45,
      "end_offset" : 48,
      "type" : "word",
      "position" : 8
    },
    {
      "token" : "s",
      "start_offset" : 49,
      "end_offset" : 50,
      "type" : "word",
      "position" : 9
    },
    {
      "token" : "bone",
      "start_offset" : 51,
      "end_offset" : 55,
      "type" : "word",
      "position" : 10
    }
  ]
}

```

### 空白分词器(whitespace tokenizer)

空白分词器（whitespace tokenizer）通过空白来分隔不同的分词，空白包括空格、制表符、换行等。但是，我们需要注意的是，空白分词器不会删除任何标点符号。

```
POST _analyze
{
  "tokenizer": "whitespace",
  "text": "The 2 QUICK Brown-Foxes jumped over the lazy dog's bone."
}
```

```text
[ The, 2, QUICK, Brown-Foxes, jumped, over, the, lazy, dog's, bone. ]
```

```
{
  "tokens" : [
    {
      "token" : "The",
      "start_offset" : 0,
      "end_offset" : 3,
      "type" : "word",
      "position" : 0
    },
    {
      "token" : "2",
      "start_offset" : 4,
      "end_offset" : 5,
      "type" : "word",
      "position" : 1
    },
    {
      "token" : "QUICK",
      "start_offset" : 6,
      "end_offset" : 11,
      "type" : "word",
      "position" : 2
    },
    {
      "token" : "Brown-Foxes",
      "start_offset" : 12,
      "end_offset" : 23,
      "type" : "word",
      "position" : 3
    },
    {
      "token" : "jumped",
      "start_offset" : 24,
      "end_offset" : 30,
      "type" : "word",
      "position" : 4
    },
    {
      "token" : "over",
      "start_offset" : 31,
      "end_offset" : 35,
      "type" : "word",
      "position" : 5
    },
    {
      "token" : "the",
      "start_offset" : 36,
      "end_offset" : 39,
      "type" : "word",
      "position" : 6
    },
    {
      "token" : "lazy",
      "start_offset" : 40,
      "end_offset" : 44,
      "type" : "word",
      "position" : 7
    },
    {
      "token" : "dog's",
      "start_offset" : 45,
      "end_offset" : 50,
      "type" : "word",
      "position" : 8
    },
    {
      "token" : "bone.",
      "start_offset" : 51,
      "end_offset" : 56,
      "type" : "word",
      "position" : 9
    }
  ]
}

```

### 模式分词器(pattern tokenizer)

```console
POST _analyze
{
  "tokenizer": "pattern",
  "text": "The foo_bar_size's default is 5."
}
```

```text
[ The, foo_bar_size, s, default, is, 5 ]
```

```
{
  "tokens" : [
    {
      "token" : "The",
      "start_offset" : 0,
      "end_offset" : 3,
      "type" : "word",
      "position" : 0
    },
    {
      "token" : "foo_bar_size",
      "start_offset" : 4,
      "end_offset" : 16,
      "type" : "word",
      "position" : 1
    },
    {
      "token" : "s",
      "start_offset" : 17,
      "end_offset" : 18,
      "type" : "word",
      "position" : 2
    },
    {
      "token" : "default",
      "start_offset" : 19,
      "end_offset" : 26,
      "type" : "word",
      "position" : 3
    },
    {
      "token" : "is",
      "start_offset" : 27,
      "end_offset" : 29,
      "type" : "word",
      "position" : 4
    },
    {
      "token" : "5",
      "start_offset" : 30,
      "end_offset" : 31,
      "type" : "word",
      "position" : 5
    }
  ]
}

```

也可以这样写

```
PUT token
{
  "settings": {
    "analysis": {
      "analyzer": {
        "my_analyzer":{
          "tokenizer":"my_tokenizer"
        }
      },
      "tokenizer": {
        "my_tokenizer":{
          "type":"pattern",
          "pattern":"&"
        }
      }
    }
  }
}

POST token/_analyze
{
  "tokenizer": "my_tokenizer",
  "text":"Ass&Bss&Css"
}
```

```
{
  "tokens" : [
    {
      "token" : "Ass",
      "start_offset" : 0,
      "end_offset" : 3,
      "type" : "word",
      "position" : 0
    },
    {
      "token" : "Bss",
      "start_offset" : 4,
      "end_offset" : 7,
      "type" : "word",
      "position" : 1
    },
    {
      "token" : "Css",
      "start_offset" : 8,
      "end_offset" : 11,
      "type" : "word",
      "position" : 2
    }
  ]
}

```

### UAX URL电子邮件分词器(UAX RUL email tokenizer)

在处理单个的英文单词的情况下，标准分词器是个非常好的选择，但是现在很多的网站以网址或电子邮件作为结尾，比如我们现在有这样的一个文本：

```
POST _analyze
{
  "tokenizer": "uax_url_email",
  "text": "Email me at john.smith@global-international.com"
}
```

```text
[ Email, me, at, john.smith@global-international.com ]
```

```
{
  "tokens" : [
    {
      "token" : "Email",
      "start_offset" : 0,
      "end_offset" : 5,
      "type" : "<ALPHANUM>",
      "position" : 0
    },
    {
      "token" : "me",
      "start_offset" : 6,
      "end_offset" : 8,
      "type" : "<ALPHANUM>",
      "position" : 1
    },
    {
      "token" : "at",
      "start_offset" : 9,
      "end_offset" : 11,
      "type" : "<ALPHANUM>",
      "position" : 2
    },
    {
      "token" : "john.smith@global-international.com",
      "start_offset" : 12,
      "end_offset" : 47,
      "type" : "<EMAIL>",
      "position" : 3
    }
  ]
}

```

### 路径层次分词器(path hierarchy tokenizer)

允许以特定的方式索引文件系统的路径，这样在搜索时，共享同样路径的文件将被作为结果返回。

```console
POST _analyze
{
  "tokenizer": "path_hierarchy",
  "text": "/one/two/three"
}
```

```text
[ /one, /one/two, /one/two/three ]
```

```
{
  "tokens" : [
    {
      "token" : "/one",
      "start_offset" : 0,
      "end_offset" : 4,
      "type" : "word",
      "position" : 0
    },
    {
      "token" : "/one/two",
      "start_offset" : 0,
      "end_offset" : 8,
      "type" : "word",
      "position" : 0
    },
    {
      "token" : "/one/two/three",
      "start_offset" : 0,
      "end_offset" : 14,
      "type" : "word",
      "position" : 0
    }
  ]
}
```

## 分词过滤器

- [标准令牌过滤器](https://www.elastic.co/guide/en/elasticsearch/reference/6.5/analysis-standard-tokenfilter.html)
- [ASCII折叠令牌过滤器](https://www.elastic.co/guide/en/elasticsearch/reference/6.5/analysis-asciifolding-tokenfilter.html)
- [展平图令牌过滤器](https://www.elastic.co/guide/en/elasticsearch/reference/6.5/analysis-flatten-graph-tokenfilter.html)
- [长度令牌过滤器](https://www.elastic.co/guide/en/elasticsearch/reference/6.5/analysis-length-tokenfilter.html)
- [小写令牌过滤器](https://www.elastic.co/guide/en/elasticsearch/reference/6.5/analysis-lowercase-tokenfilter.html)
- [大写令牌过滤器](https://www.elastic.co/guide/en/elasticsearch/reference/6.5/analysis-uppercase-tokenfilter.html)
- [NGram令牌过滤器](https://www.elastic.co/guide/en/elasticsearch/reference/6.5/analysis-ngram-tokenfilter.html)
- [Edge NGram令牌过滤器](https://www.elastic.co/guide/en/elasticsearch/reference/6.5/analysis-edgengram-tokenfilter.html)
- [搬运工词干令牌过滤器](https://www.elastic.co/guide/en/elasticsearch/reference/6.5/analysis-porterstem-tokenfilter.html)
- [碎片令牌过滤器](https://www.elastic.co/guide/en/elasticsearch/reference/6.5/analysis-shingle-tokenfilter.html)
- [停止令牌过滤器](https://www.elastic.co/guide/en/elasticsearch/reference/6.5/analysis-stop-tokenfilter.html)
- [词定界符标记过滤器](https://www.elastic.co/guide/en/elasticsearch/reference/6.5/analysis-word-delimiter-tokenfilter.html)
- [词定界符图标记过滤器](https://www.elastic.co/guide/en/elasticsearch/reference/6.5/analysis-word-delimiter-graph-tokenfilter.html)
- [多路复用器令牌过滤器](https://www.elastic.co/guide/en/elasticsearch/reference/6.5/analysis-multiplexer-tokenfilter.html)
- [条件令牌过滤器](https://www.elastic.co/guide/en/elasticsearch/reference/6.5/analysis-condition-tokenfilter.html)
- [谓词令牌过滤器脚本](https://www.elastic.co/guide/en/elasticsearch/reference/6.5/analysis-predicatefilter-tokenfilter.html)
- [词干令牌过滤器](https://www.elastic.co/guide/en/elasticsearch/reference/6.5/analysis-stemmer-tokenfilter.html)
- [Stemmer Override令牌过滤器](https://www.elastic.co/guide/en/elasticsearch/reference/6.5/analysis-stemmer-override-tokenfilter.html)
- [关键字标记令牌过滤器](https://www.elastic.co/guide/en/elasticsearch/reference/6.5/analysis-keyword-marker-tokenfilter.html)
- [关键字重复标记过滤器](https://www.elastic.co/guide/en/elasticsearch/reference/6.5/analysis-keyword-repeat-tokenfilter.html)
- [KStem令牌过滤器](https://www.elastic.co/guide/en/elasticsearch/reference/6.5/analysis-kstem-tokenfilter.html)
- [雪球令牌过滤器](https://www.elastic.co/guide/en/elasticsearch/reference/6.5/analysis-snowball-tokenfilter.html)
- [语音令牌过滤器](https://www.elastic.co/guide/en/elasticsearch/reference/6.5/analysis-phonetic-tokenfilter.html)
- [同义词令牌过滤器](https://www.elastic.co/guide/en/elasticsearch/reference/6.5/analysis-synonym-tokenfilter.html)
- [同义词图令牌过滤器](https://www.elastic.co/guide/en/elasticsearch/reference/6.5/analysis-synonym-graph-tokenfilter.html)
- [复合词令牌过滤器](https://www.elastic.co/guide/en/elasticsearch/reference/6.5/analysis-compound-word-tokenfilter.html)
- [反向令牌过滤器](https://www.elastic.co/guide/en/elasticsearch/reference/6.5/analysis-reverse-tokenfilter.html)
- [省略令牌过滤器](https://www.elastic.co/guide/en/elasticsearch/reference/6.5/analysis-elision-tokenfilter.html)
- [截断令牌过滤器](https://www.elastic.co/guide/en/elasticsearch/reference/6.5/analysis-truncate-tokenfilter.html)
- [唯一令牌过滤器](https://www.elastic.co/guide/en/elasticsearch/reference/6.5/analysis-unique-tokenfilter.html)
- [模式捕获令牌过滤器](https://www.elastic.co/guide/en/elasticsearch/reference/6.5/analysis-pattern-capture-tokenfilter.html)
- [模式替换令牌过滤器](https://www.elastic.co/guide/en/elasticsearch/reference/6.5/analysis-pattern_replace-tokenfilter.html)
- [修剪令牌过滤器](https://www.elastic.co/guide/en/elasticsearch/reference/6.5/analysis-trim-tokenfilter.html)
- [限制令牌计数令牌过滤器](https://www.elastic.co/guide/en/elasticsearch/reference/6.5/analysis-limit-token-count-tokenfilter.html)
- [Hunspell令牌过滤器](https://www.elastic.co/guide/en/elasticsearch/reference/6.5/analysis-hunspell-tokenfilter.html)
- [通用克令牌过滤器](https://www.elastic.co/guide/en/elasticsearch/reference/6.5/analysis-common-grams-tokenfilter.html)
- [标准化令牌过滤器](https://www.elastic.co/guide/en/elasticsearch/reference/6.5/analysis-normalization-tokenfilter.html)
- [CJK宽度令牌过滤器](https://www.elastic.co/guide/en/elasticsearch/reference/6.5/analysis-cjk-width-tokenfilter.html)
- [CJK Bigram令牌过滤器](https://www.elastic.co/guide/en/elasticsearch/reference/6.5/analysis-cjk-bigram-tokenfilter.html)
- [分隔有效负载令牌过滤器](https://www.elastic.co/guide/en/elasticsearch/reference/6.5/analysis-delimited-payload-tokenfilter.html)
- [保持单词令牌过滤器](https://www.elastic.co/guide/en/elasticsearch/reference/6.5/analysis-keep-words-tokenfilter.html)
- [保留类型令牌过滤器](https://www.elastic.co/guide/en/elasticsearch/reference/6.5/analysis-keep-types-tokenfilter.html)
- [排除模式设置示例](https://www.elastic.co/guide/en/elasticsearch/reference/6.5/_exclude_mode_settings_example.html)
- [经典令牌过滤器](https://www.elastic.co/guide/en/elasticsearch/reference/6.5/analysis-classic-tokenfilter.html)
- [撇号令牌过滤器](https://www.elastic.co/guide/en/elasticsearch/reference/6.5/analysis-apostrophe-tokenfilter.html)
- [小数位数令牌过滤器](https://www.elastic.co/guide/en/elasticsearch/reference/6.5/analysis-decimal-digit-tokenfilter.html)
- [指纹令牌过滤器](https://www.elastic.co/guide/en/elasticsearch/reference/6.5/analysis-fingerprint-tokenfilter.html)
- [Minhash令牌过滤器](https://www.elastic.co/guide/en/elasticsearch/reference/6.5/analysis-minhash-tokenfilter.html)
- [删除重复令牌过滤器](https://www.elastic.co/guide/en/elasticsearch/reference/6.5/analysis-remove-duplicates-tokenfilter.html)

### 自定义长度分词过滤器

长度分词过滤器(限制长度2-5之间)

```
PUT filter
{
  "settings": {
    "analysis": {
      "filter": {
        "my_length_filter":{
          "type":"length",
          "max":5,
          "min":2
        }
      }
    }
  }
}

POST filter/_analyze
{
  "tokenizer": "standard",
  "filter": ["my_length_filter"],
  "text": "a abc abcde abcdefg"
  
}
```

```
{
  "tokens" : [
    {
      "token" : "abc",
      "start_offset" : 2,
      "end_offset" : 5,
      "type" : "<ALPHANUM>",
      "position" : 1
    },
    {
      "token" : "abcde",
      "start_offset" : 6,
      "end_offset" : 11,
      "type" : "<ALPHANUM>",
      "position" : 2
    }
  ]
}

```

### 自定义小写分词过滤器

```
PUT /lowercase_example
{
  "settings": {
    "analysis": {
      "analyzer": {
        "standard_lowercase_example": {
          "type": "custom",
          "tokenizer": "standard",
          "filter": ["lowercase"]
        },
        "greek_lowercase_example": {
          "type": "custom",
          "tokenizer": "standard",
          "filter": ["greek_lowercase"]
        }
      },
      "filter": {
        "greek_lowercase": {
          "type": "lowercase",
          "language": "greek"
        }
      }
    }
  }
}
POST lowercase_example/_analyze
{
  "tokenizer": "standard",
  "filter": ["greek_lowercase"],
  "text": "Παρακαλώ εισάγετε το περιεχόμενο κειμένου ή την διαδικτυακή διεύθυνση για μετάφραση"
}
```

```

{
  "tokens" : [
    {
      "token" : "παρακαλω",
      "start_offset" : 0,
      "end_offset" : 8,
      "type" : "<ALPHANUM>",
      "position" : 0
    },
    {
      "token" : "εισαγετε",
      "start_offset" : 9,
      "end_offset" : 17,
      "type" : "<ALPHANUM>",
      "position" : 1
    },
    {
      "token" : "το",
      "start_offset" : 18,
      "end_offset" : 20,
      "type" : "<ALPHANUM>",
      "position" : 2
    },
    {
      "token" : "περιεχομενο",
      "start_offset" : 21,
      "end_offset" : 32,
      "type" : "<ALPHANUM>",
      "position" : 3
    },
    {
      "token" : "κειμενου",
      "start_offset" : 33,
      "end_offset" : 41,
      "type" : "<ALPHANUM>",
      "position" : 4
    },
    {
      "token" : "η",
      "start_offset" : 42,
      "end_offset" : 43,
      "type" : "<ALPHANUM>",
      "position" : 5
    },
    {
      "token" : "την",
      "start_offset" : 44,
      "end_offset" : 47,
      "type" : "<ALPHANUM>",
      "position" : 6
    },
    {
      "token" : "διαδικτυακη",
      "start_offset" : 48,
      "end_offset" : 59,
      "type" : "<ALPHANUM>",
      "position" : 7
    },
    {
      "token" : "διευθυνση",
      "start_offset" : 60,
      "end_offset" : 69,
      "type" : "<ALPHANUM>",
      "position" : 8
    },
    {
      "token" : "για",
      "start_offset" : 70,
      "end_offset" : 73,
      "type" : "<ALPHANUM>",
      "position" : 9
    },
    {
      "token" : "μεταφραση",
      "start_offset" : 74,
      "end_offset" : 83,
      "type" : "<ALPHANUM>",
      "position" : 10
    }
  ]
}

```

### 多个分词过滤器

```
POST _analyze
{
  "tokenizer": "standard",
  "filter": ["lowercase","length"],
  "text": "a da ad fffffff dsda"
}

```

```
{
  "tokens" : [
    {
      "token" : "a",
      "start_offset" : 0,
      "end_offset" : 1,
      "type" : "<ALPHANUM>",
      "position" : 0
    },
    {
      "token" : "da",
      "start_offset" : 2,
      "end_offset" : 4,
      "type" : "<ALPHANUM>",
      "position" : 1
    },
    {
      "token" : "ad",
      "start_offset" : 5,
      "end_offset" : 7,
      "type" : "<ALPHANUM>",
      "position" : 2
    },
    {
      "token" : "fffffff",
      "start_offset" : 8,
      "end_offset" : 15,
      "type" : "<ALPHANUM>",
      "position" : 3
    },
    {
      "token" : "dsda",
      "start_offset" : 16,
      "end_offset" : 20,
      "type" : "<ALPHANUM>",
      "position" : 4
    }
  ]
}

```

## ik中文分词器

进入Elastic Search的bin目录下执行

```shell
$ elasticsearch-plugin install https://github.com/medcl/elasticsearch-analysis-ik/releases/download/v7.9.3/elasticsearch-analysis-ik-7.9.3.zip
```

### config目录介绍

- `IKAnalyzer.cfg.xml`,用来配置自定义的词库
- `main.dic`, ik原生内置的中文词库，大约有27万多条，只要是这些单词，都会被分在一起。

- `surname.dic`,中国的姓氏。
- `suffix.dic`,特殊（后缀）名词，例如`乡、江、所、省`等等。
- `preposition.dic`,中文介词，例如`不、也、了、仍`等等。
- `stopword.dic`,英文停用词库，例如`a、an、and、the`等。
- `quantifier.dic`,单位名词，如`厘米、件、倍、像素`等。

### 基本使用

#### ik_smart

```
GET _analyze
{
  "analyzer": "ik_smart",
  "text": "python是世界上最好的语言"
}
```

```
{
  "tokens" : [
    {
      "token" : "python",
      "start_offset" : 0,
      "end_offset" : 6,
      "type" : "ENGLISH",
      "position" : 0
    },
    {
      "token" : "是",
      "start_offset" : 6,
      "end_offset" : 7,
      "type" : "CN_CHAR",
      "position" : 1
    },
    {
      "token" : "世界上",
      "start_offset" : 7,
      "end_offset" : 10,
      "type" : "CN_WORD",
      "position" : 2
    },
    {
      "token" : "最好",
      "start_offset" : 10,
      "end_offset" : 12,
      "type" : "CN_WORD",
      "position" : 3
    },
    {
      "token" : "的",
      "start_offset" : 12,
      "end_offset" : 13,
      "type" : "CN_CHAR",
      "position" : 4
    },
    {
      "token" : "语言",
      "start_offset" : 13,
      "end_offset" : 15,
      "type" : "CN_WORD",
      "position" : 5
    }
  ]
}
```

#### ik_max_word

```
GET _analyze
{
  "analyzer": "ik_max_word",
  "text": "python是世界上最好的语言"
}

```

```
{
  "tokens" : [
    {
      "token" : "python",
      "start_offset" : 0,
      "end_offset" : 6,
      "type" : "ENGLISH",
      "position" : 0
    },
    {
      "token" : "是",
      "start_offset" : 6,
      "end_offset" : 7,
      "type" : "CN_CHAR",
      "position" : 1
    },
    {
      "token" : "世界上",
      "start_offset" : 7,
      "end_offset" : 10,
      "type" : "CN_WORD",
      "position" : 2
    },
    {
      "token" : "世界",
      "start_offset" : 7,
      "end_offset" : 9,
      "type" : "CN_WORD",
      "position" : 3
    },
    {
      "token" : "上",
      "start_offset" : 9,
      "end_offset" : 10,
      "type" : "CN_CHAR",
      "position" : 4
    },
    {
      "token" : "最好",
      "start_offset" : 10,
      "end_offset" : 12,
      "type" : "CN_WORD",
      "position" : 5
    },
    {
      "token" : "的",
      "start_offset" : 12,
      "end_offset" : 13,
      "type" : "CN_CHAR",
      "position" : 6
    },
    {
      "token" : "语言",
      "start_offset" : 13,
      "end_offset" : 15,
      "type" : "CN_WORD",
      "position" : 7
    }
  ]
}

```

#### 两种对比

对比

- ik_smart

  ```
  ["python", "是", "世界上", "最好", "的", "语言"]
  ```

- im_max_word 

  ```
  ["python", "是", "世界上", "世界", "上", "最好", "的", "语言"]
  ```

### 创建映射

如果使用默认分词器，查询 ”就是“，那么只要包含 ”就“ 字和 ”是“ 字的都会被查询出来，而使用ik分词器就不会

```
PUT iks
{
  "mappings": {
    "properties": {
      "name":{
        "type": "text"
      },
      "signature":{
        "type": "text",
        "analyzer": "ik_max_word"
      }
    }
  }
}

GET iks/_doc/_search
{
  "query":{
    "match":{
      "signature":"就是"    
    }
  }
}
```

```
#! Deprecation: [types removal] Specifying types in search requests is deprecated.
{
  "took" : 0,
  "timed_out" : false,
  "_shards" : {
    "total" : 1,
    "successful" : 1,
    "skipped" : 0,
    "failed" : 0
  },
  "hits" : {
    "total" : {
      "value" : 2,
      "relation" : "eq"
    },
    "max_score" : 0.7624619,
    "hits" : [
      {
        "_index" : "iks",
        "_type" : "_doc",
        "_id" : "3",
        "_score" : 0.7624619,
        "_source" : {
          "name" : "orz",
          "signature" : "沉默就是毁谤最好的答覆"
        }
      },
      {
        "_index" : "iks",
        "_type" : "_doc",
        "_id" : "1",
        "_score" : 0.6931471,
        "_source" : {
          "name" : "orz",
          "signature" : "对人恭敬，就是在庄严你自己"
        }
      }
    ]
  }
}
```

## 建议器

### 词条建议器（term suggester）

**对于给定文本的每个词条，该键议器从索引中抽取要建议的关键词，这对于短字段（如分类标签）很有效。**

准备数据

```
PUT test/_doc/1
{
  "title":"search"
}

PUT test/_doc/2
{
  "title":"searce"
}

PUT test/_doc/3
{
  "title":"scarce"
}

PUT test/_doc/4
{
  "title":"seance"
}

PUT test/_doc/5
{
  "title":"searat abc"
}

```

查询

```
GET test/_doc/_search
{
  "suggest":{
    "my_suggest":{
      "text":"searcc",
      "term":{
        "field":"title"
      }
    }
  }
}
```

结果

```
#! Deprecation: [types removal] Specifying types in search requests is deprecated.
{
  "took" : 790,
  "timed_out" : false,
  "_shards" : {
    "total" : 1,
    "successful" : 1,
    "skipped" : 0,
    "failed" : 0
  },
  "hits" : {
    "total" : {
      "value" : 0,
      "relation" : "eq"
    },
    "max_score" : null,
    "hits" : [ ]
  },
  "suggest" : {
    "my_suggest" : [
      {
        "text" : "searcc",
        "offset" : 0,
        "length" : 6,
        "options" : [
          {
            "text" : "searce",
            "score" : 0.8333333,
            "freq" : 1
          },
          {
            "text" : "search",
            "score" : 0.8333333,
            "freq" : 1
          },
          {
            "text" : "scarce",
            "score" : 0.6666666,
            "freq" : 1
          },
          {
            "text" : "seance",
            "score" : 0.6666666,
            "freq" : 1
          },
          {
            "text" : "searat",
            "score" : 0.6666666,
            "freq" : 1
          }
        ]
      }
    ]
  }
}

```

**字段**

- text：建议文本，建议文本是必需的选项，可以通过全局（多个建议器中查询相同的内容）或者按照单个建议器的格式来。
- field：从field字段中获取候选建议的字段。这是一个必需的选项，需要全局设置或根据建议设置。
- analyzer：用于分析建议文本的分析器。默认为建议字段的搜索分析器。
- size：个建议文本标记返回的最大条目。
- sort：定义如何根据建议文本术语对建议进行排序。它有两个可能的值。
  - score，先按分数排序，然后按文档频率排序，再按术语本身排序。
  - frequency，首先按文档频率排序，然后按相似性分数排序，然后按术语本身排序。也可以理解为按照流行度排序。
- suggest_mode：控制建议的模式，有3个模式可选择。
  - missing，仅为不在索引中的建议文本术语提供建议。这是默认值。
  - popular，仅建议在比原始建议文本术语更多的文档中出现的建议。也就是说提供比原有输入词频更高的词条
  - always，根据建议文本中的条款建议任何匹配的建议。说白了就是无论如何都会提供建议。
- lowercase_terms：在文本分析之后降低建议文本术语的大小写。
- min_word_length：建议文本术语必须具有的最小长度才能包含在内。默认为4.（旧名称`min_word_len`已弃用）。
- shard_size：设置从每个单独分片中检索的最大建议数。在减少阶段，仅根据size选项返回前N个建议。默认为该 size选项。将此值设置为高于该值的值size可能非常有用，以便以性能为代价获得更准确的拼写更正文档频率。由于术语在分片之间被划分，因此拼写校正频率的分片级文档可能不准确。增加这些将使这些文档频率更精确。
- max_inspections：用于乘以的因子， shards_size以便在碎片级别上检查更多候选拼写更正。可以以性能为代价提高准确性。默认为5。
- string_distance：用于比较类似建议术语的字符串距离实现。
  - internal，默认值基于damerau_levenshtein，但高度优化用于比较索引中术语的字符串距离。
  - damerau_levenshtein，基于Damerau-Levenshtein算法的字符串距离算法。
  - levenshtein，基于Levenshtein编辑距离算法的字符串距离算法。
  - jaro_winkler，基于Jaro-Winkler算法的字符串距离算法。
  - ngram，基于字符n-gram的字符串距离算法。

**选择哪些词条被建议**

了解了各字段的大致含义，我们来探讨一下，词条建议器是如何运作的。以便理解如何确定哪些建议将成为第一名。
词条建议器使用了Lucene的错拼检查器模块，该模块会根据给定词条的**编辑距离**（es使用了叫做Levenstein edit distance的算法，其核心思想就是一个词改动多少字符就可以和另外一个词一致），从索引中返回最大编辑距离不超过某个值的那些词条。比如说为了从`mik`得到`mick`，需要加入一个字母（也就是说需要至少要改动一次），所以这两个词的编辑距离就是1。我们可以通过配置一系列的选项，来均衡灵活和性能：

- max_edits：最大编辑距离候选建议可以具有以便被视为建议。只能是介于1和2之间的值。任何其他值都会导致抛出错误的请求错误。默认为2。
- prefix_length：必须匹配的最小前缀字符的数量才是候选建议。默认为1.增加此数字可提高拼写检查性能。通常拼写错误不会出现在术语的开头。（旧名`prefix_len`已弃用）。
- min_doc_freq：建议应出现的文档数量的最小阈值。可以指定为绝对数字或文档数量的相对百分比。这可以仅通过建议高频项来提高质量。默认为0f且未启用。如果指定的值大于1，则该数字不能是小数。分片级文档频率用于此选项。
- max_term_freq：建议文本令牌可以存在的文档数量的最大阈值，以便包括在内。可以是表示文档频率的相对百分比数（例如0.4）或绝对数。如果指定的值大于1，则不能指定小数。默认为0.01f。这可用于排除高频术语的拼写检查。高频术语通常拼写正确，这也提高了拼写检查的性能。分片级文档频率用于此选项。

小结，`term suggester`首先将输入文本经过分析器（所以，分析结果由于采用的分析器不同而有所不同）分析，处理为单个词条，然后根据单个词条去提供建议，并不会考虑多个词条之间的关系。然后将每个词条的建议结果（有或没有）封装到`options`列表中。最后由建议器统一返回。

### 词组建议器（phrase suggester）

**我们可以认为它是词条建议器的扩展，为整个文本（而不是单个词条）提供了替代方案，它考虑了各词条彼此临近出现的频率，使得该建议器更适合较长的字段，比如商品的描述。**

准备数据

```
PUT test/_doc/1
{
  "title":"to know full well"
}
```

查询

```
GET test/_doc/_search
{
  "suggest":{
    "my_suggest":{
      "text":"to know full walk",
      "phrase":{
        "field":"title"
      }
    }
  }
}
```

结果

```
#! Deprecation: [types removal] Specifying types in search requests is deprecated.
{
  "took" : 1,
  "timed_out" : false,
  "_shards" : {
    "total" : 1,
    "successful" : 1,
    "skipped" : 0,
    "failed" : 0
  },
  "hits" : {
    "total" : {
      "value" : 0,
      "relation" : "eq"
    },
    "max_score" : null,
    "hits" : [ ]
  },
  "suggest" : {
    "my_suggest" : [
      {
        "text" : "to know full walk",
        "offset" : 0,
        "length" : 17,
        "options" : [
          {
            "text" : "to know full well",
            "score" : 0.025013037
          }
        ]
      }
    ]
  }
}

```

也可以使用高亮提示拼错的单词

```
GET test/_doc/_search
{
  "suggest":{
    "my_suggest":{
      "text":"to know full walk",
      "phrase":{
        "field":"title",
        "highlight":{
          "pre_tag":"<b>",
          "post_tag":"</b>"
        }
      }
    }
  }
}
```

结果

```
#! Deprecation: [types removal] Specifying types in search requests is deprecated.
{
  "took" : 1,
  "timed_out" : false,
  "_shards" : {
    "total" : 1,
    "successful" : 1,
    "skipped" : 0,
    "failed" : 0
  },
  "hits" : {
    "total" : {
      "value" : 0,
      "relation" : "eq"
    },
    "max_score" : null,
    "hits" : [ ]
  },
  "suggest" : {
    "my_suggest" : [
      {
        "text" : "to know full walk",
        "offset" : 0,
        "length" : 17,
        "options" : [
          {
            "text" : "to know full well",
            "highlighted" : "to know full <b>well</b>",
            "score" : 0.025013037
          }
        ]
      }
    ]
  }
}

```

### 完成建议器（completion suggester）

**该建议器根据词条的前缀，提供自动完成的功能（智能提示，有点最左前缀查询的意思），为了实现这种实时的建议功能，它得到了优化，工作在内存中。所以，速度要比之前说的`match_phrase_prefix`快的多！**

创建映射,为了告诉elasticsearch我们准备将建议存储在自动完成的FST中，需要在映射中定义一个字段并将其`type`类型设置为`completion`

```
PUT test
{
  "mappings":{
    "properties": {
      "title": {
        "type": "completion",
        "analyzer": "standard"
      }
    }
  }
}
```

准备数据

```
PUT test/_doc/1
{
  "title":"to know full well"
}

PUT test/_doc/2
{
  "title":"to know no bounds"
}

PUT test/_doc/3
{
  "title":"to know something backwards"
}

PUT test/_doc/4
{
  "title":"to know something for a fact"
}
```

查询

```
GET test/_doc/_search
{
  "suggest":{
    "my_suggest":{
      "text":"to know something",
      "completion":{
        "field":"title",
        "analyzer": "standard"
      }
    }
  }
}
```

结果

```
#! Deprecation: [types removal] Specifying types in search requests is deprecated.
{
  "took" : 0,
  "timed_out" : false,
  "_shards" : {
    "total" : 1,
    "successful" : 1,
    "skipped" : 0,
    "failed" : 0
  },
  "hits" : {
    "total" : {
      "value" : 0,
      "relation" : "eq"
    },
    "max_score" : null,
    "hits" : [ ]
  },
  "suggest" : {
    "my_suggest" : [
      {
        "text" : "to know something",
        "offset" : 0,
        "length" : 17,
        "options" : [
          {
            "text" : "to know something backwards",
            "_index" : "test",
            "_type" : "_doc",
            "_id" : "3",
            "_score" : 1.0,
            "_source" : {
              "title" : "to know something backwards"
            }
          },
          {
            "text" : "to know something for a fact",
            "_index" : "test",
            "_type" : "_doc",
            "_id" : "4",
            "_score" : 1.0,
            "_source" : {
              "title" : "to know something for a fact"
            }
          }
        ]
      }
    ]
  }
}

```

上例的创建特殊映射中，支持以下参数：

- analyzer，要使用的索引分析器，默认为simple。
- search_analyzer，要使用的搜索分析器，默认值为analyzer。
- preserve_separators，保留分隔符，默认为true。 如果您禁用，您可以找到以Foo Fighters开头的字段，如果您建议使用foof。
- preserve_position_increments，启用位置增量，默认为true。如果禁用并使用停用词分析器The Beatles，如果您建议，可以从一个字段开始b。注意：您还可以通过索引两个输入来实现此目的，Beatles并且 The Beatles，如果您能够丰富数据，则无需更改简单的分析器。
- max_input_length，限制单个输入的长度，默认为50UTF-16代码点。此限制仅在索引时使用，以减少每个输入字符串的字符总数，以防止大量输入膨胀基础数据结构。大多数用例不受默认值的影响，因为前缀完成很少超过前缀长于少数几个字符。

#### 在索引阶段提升相关性

建议映射还可以定义在已存在索引字段的多字段

```
PUT test
{
  "mappings": {
    "properties": {
      "name":{
        "type": "text",
        "fields": {                   # 给name字段添加字段sug
          "sug":{
            "type":"completion"
          }
        }
      }
    }
  }
}

PUT test/_doc/1
{
  "name":"ABC"
}

PUT test/_doc/2
{
  "name":"abc"
}


GET test/_doc/_search
{
  "suggest":{
    "my_suggest":{
      "text":"A",
      "completion":{
        "field":"name.sug"
      }
    }
  }
}
```

结果

```
#! Deprecation: [types removal] Specifying types in search requests is deprecated.
{
  "took" : 0,
  "timed_out" : false,
  "_shards" : {
    "total" : 1,
    "successful" : 1,
    "skipped" : 0,
    "failed" : 0
  },
  "hits" : {
    "total" : {
      "value" : 0,
      "relation" : "eq"
    },
    "max_score" : null,
    "hits" : [ ]
  },
  "suggest" : {
    "my_suggest" : [
      {
        "text" : "A",
        "offset" : 0,
        "length" : 1,
        "options" : [
          {
            "text" : "ABC",
            "_index" : "test",
            "_type" : "_doc",
            "_id" : "1",
            "_score" : 1.0,
            "_source" : {
              "name" : "ABC"
            }
          },
          {
            "text" : "abc",
            "_index" : "test",
            "_type" : "_doc",
            "_id" : "2",
            "_score" : 1.0,
            "_source" : {
              "name" : "abc"
            }
          }
        ]
      }
    ]
  }
}

```

但是这也存在一个问题，我们查询的是A,但是把ABC和abc都建议出来了，所以我们需要在索引阶段提升相关性，可以通过`analyzer`和`search_analyzer`来进一步控制分析过程

```
PUT test
{
  "mappings": {
    "properties": {
      "name":{
        "type": "text",
        "fields": {
          "sug":{
            "type":"completion",
            "analyzer":"keyword",				# 控制name字段sug的索引分析器和搜索分析器为keyword,不进行分析
            "search_analyzer":"keyword"
          }
        }
      }
    }
  }
}

PUT test/_doc/1
{
  "name":"ABC"
}

PUT test/_doc/2
{
  "name":"abc"
}


GET test/_doc/_search
{
  "suggest":{
    "my_suggest":{
      "text":"A",
      "completion":{
        "field":"name.sug"
      }
    }
  }
}

```

结果

```
#! Deprecation: [types removal] Specifying types in search requests is deprecated.
{
  "took" : 1,
  "timed_out" : false,
  "_shards" : {
    "total" : 1,
    "successful" : 1,
    "skipped" : 0,
    "failed" : 0
  },
  "hits" : {
    "total" : {
      "value" : 0,
      "relation" : "eq"
    },
    "max_score" : null,
    "hits" : [ ]
  },
  "suggest" : {
    "my_suggest" : [
      {
        "text" : "A",
        "offset" : 0,
        "length" : 1,
        "options" : [
          {
            "text" : "ABC",
            "_index" : "test",
            "_type" : "_doc",
            "_id" : "1",
            "_score" : 1.0,
            "_source" : {
              "name" : "ABC"
            }
          }
        ]
      }
    ]
  }
}

```

除此之外，还可以使用`input`和可选的`weight`属性，`input`是建议查询匹配的预期文本，`weight`是建议评分方式（也就是权重）

```
PUT test
{
  "mappings": {
    "properties": {
      "name":{
        "type": "completion"
      }
    }
  }
}


PUT test/_doc/1
{
  "name":{
    "input":"apply",
    "weight":3
  }
}

PUT test/_doc/2
{
  "name":{
    "input":"apple",
    "weight":2
  }
}


PUT test/_doc/3
{
  "name":[
    {
      "input":"applocation",
      "weight":4
    },
    {
      "input":"applicable",
      "weight":2
    }]
}


PUT test/_doc/4
{
  "name":["appreciate","approach"],
  "weight":5
}


GET test/_doc/_search
{
  "suggest":{
    "my_suggest":{
      "text":"app",
      "completion":{
        "field":"name"
      }
    }
  }
}

```

结果

```
#! Deprecation: [types removal] Specifying types in search requests is deprecated.
{
  "took" : 0,
  "timed_out" : false,
  "_shards" : {
    "total" : 1,
    "successful" : 1,
    "skipped" : 0,
    "failed" : 0
  },
  "hits" : {
    "total" : {
      "value" : 0,
      "relation" : "eq"
    },
    "max_score" : null,
    "hits" : [ ]
  },
  "suggest" : {
    "my_suggest" : [
      {
        "text" : "app",
        "offset" : 0,
        "length" : 3,
        "options" : [
          {
            "text" : "applocation",
            "_index" : "test",
            "_type" : "_doc",
            "_id" : "3",
            "_score" : 4.0,
            "_source" : {
              "name" : [
                {
                  "input" : "applocation",
                  "weight" : 4
                },
                {
                  "input" : "applicable",
                  "weight" : 2
                }
              ]
            }
          },
          {
            "text" : "apply",
            "_index" : "test",
            "_type" : "_doc",
            "_id" : "1",
            "_score" : 3.0,
            "_source" : {
              "name" : {
                "input" : "apply",
                "weight" : 3
              }
            }
          },
          {
            "text" : "apple",
            "_index" : "test",
            "_type" : "_doc",
            "_id" : "2",
            "_score" : 2.0,
            "_source" : {
              "name" : {
                "input" : "apple",
                "weight" : 2
              }
            }
          },
          {
            "text" : "appreciate",
            "_index" : "test",
            "_type" : "_doc",
            "_id" : "4",
            "_score" : 1.0,
            "_source" : {
              "name" : [
                "appreciate",
                "approach"
              ],
              "weight" : 5
            }
          }
        ]
      }
    ]
  }
}
```

#### 在搜索阶段提升相关性

当在运行建议的请求时，可以决定出现哪些建议，就像其他建议器一样，`size`参数控制返回多少项建议（默认为5项）；还可以通过`fuzzy`参数设置模糊建议，以对拼写进行容错。当开启模糊建议之后，可以设置下列参数来完成建议：

- fuzziness，可以指定所允许的最大编辑距离。
- min_length，指定什么长度的输入文本可以开启模糊查询。
- prefix_length，假设若干开始的字符是正确的（比如block，如果输入blaw，该字段也认为之前输入的是对的），这样可以通过牺牲灵活性提升性能。

```
PUT test
{
  "mappings": {
    "properties": {
      "name":{
        "type": "completion"
      }
    }
  }
}

PUT test/_doc/1
{
  "name":{
    "input":"apply",
    "weight":3
  }
}

PUT test/_doc/2
{
  "name":{
    "input":"apple",
    "weight":2
  }
}

GET test/_doc/_search
{
  "suggest":{
    "my_search":{
      "text":"apply",
      "completion":{
        "field":"name",
        "size":2,
        "fuzzy":{
          "fuzziness":2,
          "min_length": 6,
          "prefix_length": 2
        }
      }
    }
  }
}

```

结果

```
#! Deprecation: [types removal] Specifying types in search requests is deprecated.
{
  "took" : 0,
  "timed_out" : false,
  "_shards" : {
    "total" : 1,
    "successful" : 1,
    "skipped" : 0,
    "failed" : 0
  },
  "hits" : {
    "total" : {
      "value" : 0,
      "relation" : "eq"
    },
    "max_score" : null,
    "hits" : [ ]
  },
  "suggest" : {
    "my_search" : [
      {
        "text" : "apply",
        "offset" : 0,
        "length" : 5,
        "options" : [
          {
            "text" : "apply",
            "_index" : "test",
            "_type" : "_doc",
            "_id" : "1",
            "_score" : 15.0,
            "_source" : {
              "name" : {
                "input" : "apply",
                "weight" : 3
              }
            }
          }
        ]
      }
    ]
  }
}

```

### 上下文建议器（context suggester）

**它是完成建议器的扩展，允许我们根据词条或分类亦或是地理位置对结果进行过滤。**

**[参考](https://www.cnblogs.com/Neeo/articles/10695031.html)**

## ES集群

### 搭建集群

- 在本地单独的目录中再复制一份ElasticSearch文件(如果复制使用过的集群要删除data目录下所有文件)

- 分别启动bin目录下的启动文件

- 在浏览器输入:

  ```
  http://127.0.0.1:9200/_cluster/health?pretty
  ```

  返回结果:

  ```
  {
    "cluster_name" : "elasticsearch",
    "status" : "green",
    "timed_out" : false,
    "number_of_nodes" : 2,
    "number_of_data_nodes" : 2,
    "active_primary_shards" : 0,
    "active_shards" : 0,
    "relocating_shards" : 0,
    "initializing_shards" : 0,
    "unassigned_shards" : 0,
    "delayed_unassigned_shards" : 0,
    "number_of_pending_tasks" : 0,
    "number_of_in_flight_fetch" : 0,
    "task_max_waiting_in_queue_millis" : 0,
    "active_shards_percent_as_number" : 100.0
  }
  ```

### 发现节点

#### 广播

当es启动时，发送广播到`224.2.2.4:54328`，而其他es使用同样的集群名响应了这个请求，一般集群名称就是`cluster_name`对应的`elasticsearch`，但是广播有一个缺点，过程不可控

#### 单播

只需要告诉集群及其他节点的IP及(可选的)端口及端口范围，在`elasticsearch.yml`配置文件中设置:

```
discovery.zen.ping.unicast.hosts: ["10.0.0.1", "10.0.0.3:9300", "10.0.0.6[9300-9400]"]
```

### 选取主节点

无论是广播发现还是到单播发现，一旦集群中的节点发生变化，它们就会协商谁将成为主节点，elasticsearch认为所有节点都有资格成为主节点。如果集群中只有一个节点，那么该节点首先会等一段时间，如果还是没有发现其他节点，就会任命自己为主节点。

```
discovery.zen.minimum_master_nodes: 3
```

一般规则是集群节点数除以二(向下取整)再加一，比如，比如3个节点集群要设置为2，防止脑裂(split brain)问题

### 什么是脑裂(split brain)

脑裂这个词描述的是这样的一个场景：（通常是在重负荷或网络存在问题时）elasticsearch集群中一个或者多个节点失去和主节点的通信，然后小老弟们（各节点）就开始选举新的主节点，继续处理请求。这个时候，可能有两个不同的集群在相互运行着，这就是脑裂一词的由来，因为单一集群被分成了两部分。

如果集群由于网络和负荷等原因，12345被分为12和345，因为`minimum_master_nodes`参数是3，所以345可以组成集群，而12不符合半数以上，一直处于寻找集群状态。

### 错误识别

当主节点被确定后，建立起内部的ping机制来确保每个节点在集群中保持活跃和健康，这就是错误识别。
主节点ping集群中的其他节点，而且每个节点也会ping主节点来确认主节点还活着，如果没有响应，则宣布该节点失联。

```
discovery.zen.fd.ping_interval: 1
discovery.zen.fd.ping_timeout: 30
discovery_zen.fd.ping_retries: 3
```

每个节点每隔`discovery.zen.fd.ping_interval`的时间（默认1秒）发送一个ping请求，等待`discovery.zen.fd.ping_timeout`的时间（默认30秒），并尝试最多`discovery.zen.fd.ping_retries`次（默认3次），无果的话，宣布节点失联，并且在需要的时候进行新的分片和主节点选举。