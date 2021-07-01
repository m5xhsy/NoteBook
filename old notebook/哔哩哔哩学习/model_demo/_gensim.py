import jieba
import gensim
from gensim import corpora
from gensim import models
from gensim import similarities

issue_list = ["你今年几岁了","你的名字是什么","今天天气怎么样","你有多高"]

issue = "你今年多大了"

issue_participle = [word for word in jieba.cut_for_search(issue)]
print(issue_participle)
"""
['你', '今年', '多大', '了']
"""

issue_participle_list = []
for item in issue_list:
    item_list = [word for word in jieba.cut_for_search(item)]
    issue_participle_list.append(item_list)
print(issue_participle_list)
"""
[
    ['你', '的', '名字', '是', '什么'], 
    ['你', '今年', '几岁', '了'], 
    ['今天', '天天', '天气', '今天天气', '怎么', '怎么样'], 
    ['你', '有', '多', '高']
]
 """
# 制作词袋
"""
将很多的词，进行排序，形成一个词(key)与标准位(value)的字典
"""

dictionary = corpora.Dictionary(issue_participle_list)

print(dictionary.token2id)
# {'什么': 0, '你': 1, '名字': 2, '是': 3, '的': 4, '了': 5, '今年': 6, '几岁': 7, '今天': 8, '今天天气': 9, '天天': 10, '天气': 11, '怎么': 12, '怎么样': 13, '多': 14, '有': 15, '高': 16}
print(dictionary,type(dictionary))
# Dictionary(17 unique tokens: ['什么', '你', '名字', '是', '的']...) <class 'gensim.corpora.dictionary.Dictionary'>



# 词料库, 将列表中每一个词与dictionary中的key进行匹配
''' 元组(词,出现次数)
[[(0, 1), (1, 1), (2, 1), (3, 1), (4, 1)], 
[(1, 1), (5, 1), (6, 1), (7, 1)], 
[(8, 1), (9, 1), (10, 1), (11, 1), (12, 1), (13, 1)], 
[(1, 1), (14, 1), (15, 1), (16, 1)]]
'''
corpus = [dictionary.doc2bow(doc) for doc in issue_participle_list] # 语料库
print(corpus)


issue_corpus = dictionary.doc2bow(issue_participle) # 测试问题
print(issue_corpus)


lsi = models.LsiModel(corpus)  # 训练模型。做成向量
print("lsi>>",lsi, type(lsi))
print("lsi[corpus]>>>",lsi[corpus]) # 训练结果
print("lsi[issue_corpus]>>>",lsi[issue_corpus]) # 获取语料库issue_corpus在语料库corpus中的训练结果，用向量表示


# 文本相似度
# 稀疏矩阵相似度 ,将主语料库corpus的训练结果，作为初始值
index = similarities.SparseMatrixSimilarity(lsi[corpus], num_features=len(dictionary.keys()))
print("index>>>", index, type(index))


sim = index[lsi[issue_corpus]]
print("sim>>",sim,type(sim))

cc = sorted(enumerate(sim), key=lambda  item: -item[1])
print(cc)

print(issue,issue_list[cc[0][0]])