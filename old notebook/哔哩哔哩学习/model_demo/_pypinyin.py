from pypinyin import lazy_pinyin, TONE, TONE2, TONE3

# res = lazy_pinyin("拼音",style=TONE)
# print(res)  # ['pīn', 'yīn']
# res = lazy_pinyin("拼音",style=TONE2)
# print(res)  # ['pi1n', 'yi1n']
# res = lazy_pinyin("拼音",style=TONE3)
# print(res)  # ['pin1', 'yin1']
ls = [
    '茕茕孑立', '沆瀣一气',
    '踽踽独行', '醍醐灌顶',
    '绵绵瓜瓞', '奉为圭臬',
    '龙行龘龘', '犄角旮旯',
    '娉婷袅娜', '涕泗滂沱',
    '呶呶不休', '不稂不莠',
    '咄嗟', '蹀躞', '耄耋', '饕餮',
    '囹圄', '蘡薁', '觊觎', '龃龉',
    '狖轭鼯轩', '怙恶不悛',
    '其靁虺虺', '腌臢孑孓',
    '陟罚臧否', '针砭时弊', '鳞次栉比', '一张一翕']
for item in ls:
    print(item,lazy_pinyin(item,style=TONE))
