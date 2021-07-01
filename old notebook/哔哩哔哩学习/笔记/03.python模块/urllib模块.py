from urllib.parse import parse_qs       #user=111&pswd=222转换成字典
x=parse_qs("user=111&pswd=222")
print(x)
# {'user': ['111'], 'pswd': ['222']}








from  urllib.request import urlretrieve
url = ""
filename = ""
urlretrieve(url=url, filename=filename)

# 爬取url后保存到filename路径