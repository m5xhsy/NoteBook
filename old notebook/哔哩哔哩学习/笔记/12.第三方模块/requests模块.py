import requests

r1=requests.get('https://www.bilibili.com/')
# print(r1.content)
print(r1.text)