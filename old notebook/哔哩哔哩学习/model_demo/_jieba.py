import jieba

sw = "自由的鱼，恬淡的纳西少女，围着旅客脚尖打转儿的小狗，一派祥和自然。"

res = jieba.cut(sw)     # 直接分
print(list(res))


jieba.add_word("自由的")       # 添加关键词
jieba.add_word("恬淡的")       #
jieba.add_word("儿的")         # 不副和分词规律，所以有关键词也不行
res = jieba.cut(sw)
print(list(res))


res = jieba.cut_for_search(sw)   # 搜索引擎
print(list(res))