### Django原生序列化组件使用

#### 使用

```python
from django.core.serializers import serialize  # 1.导入模块
def user(request):
    user_obj = UserInfo.objects.all()		  # 2.获取queryset
    user_data = serialize("json", user_obj)    # 3.对queryset进行序列化
    return HttpRespones(user_data)			  # 4.响应给客户端
```

#### 打印结果

```json
[
    {
        "model": "Ass.userinfo", 
     	"pk": 1, 
     	"fields": {
         			"username": "admin", 
        			"password": "password"
     			}
    },
    {	
        "model": "Ass.userinfo", 
        "pk": 2, 
        "fields":{
            		"username": "m5xhsy", 
            		"password": "password"
        		}
    }
]
```

### JsonResponse的使用

```python
from django.http import JsonResponse        #JsonResponse(list(xxx),safe=False) 序列化非字典结构时加safe=False
                                            #ajax解的时候就自动反序列化
    
def book(request):
    data = {
        title:'python入门'，
        price:56,
        publish:'人民出版社'
    }
    return JsonResponse(data)   #如果data是数组，加上safe = False
    
```

