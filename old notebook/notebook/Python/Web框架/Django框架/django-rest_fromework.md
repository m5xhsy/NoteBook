#    DRF安装使用

其他资料查询restframework官网API

```shell
$ pip3 install django
$ pip3 install djangorestframework
```

```python
# 安装后将'rest_framework'添加到Django项目中setting中的app配置中			***
```

## 1.django restframework

### 		1.1 	APIView*

#### 使用方法

```python
from rest_framework.views import APIView
class Ass(APIView):
    def get(self,request)
    	return render(request,'xxx.html')
```

### 		1.2	解析器组件*

#### 1.2.1 使用方法

```html
<!-- html -->
$.ajax({
	url:'',
	type:'post',
	contentType:'application/json',			<!-- json数据，框架只认application/json -->
	headers:{
		'X-CSRFToken':$.cookie('csrftoken')
	},
    data:JSON.stringify({
        username:$('#id_username').val(),
        password:$('#id_password').val(),
    }),
    success:function (data) {
        alert(data)
    },
})
```

```python
# view.py
from rest_framework.parsers import JSONParser, FormParser
from rest_framework.views import APIView
from django.shortcuts import HttpResponse
class Ass(APIView):
    parser_class = [JSONParser, FormParser]	# 本次请求只解析json和urlencode数据
    def post(self,request)
    	print(request.data)
    	return HttpResponse('ok')
```

#### 1.2.2 源码分析

```python
1. view.LoginView.as_view()
2. LOginView中没有as_view()方法,到父类APIView中去找
3.执行View里面的as_view()方法，返回view函数
	def view(request, *args, **kwargs):
		self = cls(**initkwargs)
		if hasattr(self, 'get') and not hasattr(self, 'head'):
			self.head = self.get
		self.request = request
		self.args = args
		self.kwargs = kwargs
		return self.dispatch(request, *args, **kwargs)
4.url和视图函数之间的绑定关系建立完毕{"login":view},等待用户请求
5.接收到用户的请求: login, 到建立好的绑定关系中去执行对于的视图函数:view(request)
6.视图函数的执行结果是什么就返回给用户什么: self.dispatch()
7.此时的self代表的是LoginView的实例化对象
8.开始查找dispatch方法，self里面没有，LoginView中也没有，在APIView中找到
9.执行APIView中的dispatch
10.最后找到http的方法(GET,POST,PUT,DELETE),根据请求类型查找request.method.lower()
11.开始执行找到的方法(GET)，self.get(),self此时代表LoginView的实例化
	11.1.如果接收到的是POST请求，执行request.data
	11.2.所有的解析工作都在request.data中实现，且data是一个方法(被装饰后的)
	11.3.开始执行data
        @property
        def data(self):
            if not _hasattr(self, '_full_data'):
                self._load_data_and_files()
            return self.full_data
    11.4.执行self._load_data_and_files()
    11.5.执行self._data, self._file = self.parse()
    11.6.parser = self.negotiator.select_parser(self, self.parsers)
    11.7.点进self.parsers发现self.parsers = parsers or ()是request实例化过来的
    11.8.进dispatch()查看实例化reques的部分并点进request = self.initialize_request(request, *args, **kwargs)
    11.9.get_parsers(self)返回的为[parser() for parser in self.parser_classes]，而self表示的是调用dispatch的类，也就是视图类
    11.10.如果视图类设置了parser_classes则第11.7中的self为设置的解析器，否则在APIView中找
    11.11.在APIView中parser_classes = api_settings.DEFAULT_PARSER_CLASSES
    11.12.点击进入api_settings发现api_settings是APISettings(None, DEFAULTS, IMPORT_STRINGS)的实例，进去找DEFAULT_PARSER_CLASSES属性，没有这个属性执行__getattr__(self, attr)
    11.13.self.defaults是实例化传进来的，attr在self.defaults里面
    11.14.执行self.user_settings,由于实例化时user_settings传进来为None，所以self._user_settings = getattr(settings, 'REST_FRAMEWORK', {})去settings中找'REST_FRAMEWORK'，如果没找到取空字典，并返回
    11.15.返回的self.user_settings如果是空字典，则self.user_settings[attr]会报一个KeyError的错误并被捕获
    11.16.捕获后在self.defaults[attr]找到并return出去
12.在LoginView里面找到对应的方法，执行该方法，最后返回给用户
```



### 		1.3	序列化组件*

#### 1.3.1接口设计

##### 1.3.1.1 Serializer

```python
# app_serializer.py
from rest_framework import serializers  # 导入模块
class BookSerializer(serializers.Serializer):	#创建一个类
    title = serializers.CharField(max_length=32)	
    price =serializers.IntegerField()
    publish = serializers.CharField(max_length=32)		# ForeignKey字段值取决于__str__(self)
    publish_city = serializers.CharField(read_only=True,max_length=32, source="publish.city") # 只读字段
    publish_name = serializers.CharField(read_only=True,max_length=32, source="publish.name") # 只读字段
    auther_list = serializers.SerializerMethodField()  #多对多，默认只读

    def get_auther_list(self, book_obj):	#设计多对多
        auther_list = []
        print(book_obj.auther.all())
        for auther in book_obj.auther.all():
            auther_list.append(auther.name)
        return auther_list

    def create(self, validated_data):
        print('validated_data>>>',validated_data)
        publish = Publish.objects.filter(id=validated_data.get('publish')).first()
        book_obj = Book.objects.create(title=validated_data.get('title'),price=validated_data.get('price'),publish=publish)
        return book_obj
    
    
# views.py    
from App.models import Book
from App.app_serializer import BookSerializer
from rest_framework.view import APIview
class Books(APIView):
    def get(self, request):
        origin_data = Book.objects.all()
        data = BookSerializer(origin_data, many=True)    # many=True表示传多个数据
        return Response(data.data)

    def post(self, request):
        print(request.data)
        serializers_data = BookSerializer(data=request.data)
        if serializers_data.is_valid():
            book_obj = serializers_data.save()      #会走create()方法,
            book_obj.auther.add(*request.data.get('auther'))        #接收create方法中返回的book对象
            return Response(serializers_data.data)
        else:
            return Response(serializers_data.errors)

```

##### 1.3.1.2 ModelSerializer

```python
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book            # 指定模型
        # fields = "__all__"        # 全部字段
        fields = ("title", "price", "publish", "auther", "publish_name", "publish_city", "auther_list") # 指定部分字段
        extra_kwargs = {            # 指定只写字段
            "publish": {'write_only': True},
            "auther": {'write_only': True}
        }

    publish_name = serializers.CharField(max_length=32,source='publish.name',read_only=True)
    publish_city = serializers.CharField(max_length=32,source='publish.city',read_only=True)
    auther_list = serializers.SerializerMethodField()

    def get_auther_list(self,book_obj):     #多对多字段获取
        # 拿到queryset开始循环
        authers = list()
        for auther in book_obj.auther.all():
            authers.append(auther.name)
        return authers

    def create(self, validated_data):       # create方法
        print('validated_data>>>', validated_data)
        book_obj = Book.objects.create(
            title=validated_data.get('title'), 
            price=validated_data.get('price'),
            publish=validated_data.get('publish')
        )
        book_obj.auther.add(*[item.id for item in validated_data.get('auther')])
        return book_obj

    def update(self, instance, validated_data):
        print(validated_data)
        instance.title  = validated_data.get('title')
        instance.price = validated_data.get('price')
        instance.publish = validated_data.get('publish')
        auther_list = [item.id for item in validated_data.get('auther')]
        instance.auther.set(auther_list)
        instance.save()
        return instance

class Books(APIView):
    def get(self, request):
        origin_data = Book.objects.all()
        data = BookSerializer(origin_data, many=True)    # many=True表示传多个数据
        return Response(data.data)

    def post(self, request):
        print(request.data)
        serializers_data = BookSerializer(data=request.data)
        if serializers_data.is_valid():
            book_obj = serializers_data.save()  # 会走create()方法,
            return Response(serializers_data.data)
        else:
            return Response(serializers_data.errors)

        
class BooksId(APIView):
    def get(self, request, id):
        book_obj = Book.objects.filter(pk=id)
        serialized_data = BookSerializer(book_obj, many=False)  # queryset列表则是True,单个数据False
        return Response(serialized_data.data)

    def put(self, request, id):
        book_obj = Book.objects.filter(pk=id).first()
        serializerd_data = BookSerializer(data=request.data, instance=book_obj, many=False)
        if serializerd_data.is_valid():
            bookObj = serializerd_data.save()
            return Response(serializerd_data.data)
        else:
            return Response(serializerd_data.errors)

    def delete(self, request, id):
        book_obj = Book.objects.filter(pk=id).delete()
        return Response(id)

```

### 1.4 视图组件

视图组件是用来优化接口逻辑的

#### 1.4.1 接口优化（一）

序列化类参考ModelSerializer

##### 1.4.1.1 Mixin的使用

```python
# url设计*
path('mixinbooks/', views.MixinBooks.as_view()),
re_path('mixinbooks/(?P<pk>\d+)/', views.MixinBooksId.as_view())
```

```python
# view.py

from rest_framework.generics import GenericAPIView
from rest_framework.mixins import (
    ListModelMixin,     # 查
    CreateModelMixin,   # 增
    DestroyModelMixin,  # 删
    UpdateModelMixin,   # 改
    RetrieveModelMixin, # 查
)

class MixinBooks(ListModelMixin, CreateModelMixin, GenericAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer		#序列化类
    
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
 
class MixinBooksId(UpdateModelMixin, RetrieveModelMixin, DestroyModelMixin, GenericAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
```

#### 1.4.2 接口优化（二）

##### 1.4.2.1genericviews的使用

```python
# url设计
path('mixinbooks/', views.MixinBooks.as_view()),
re_path('mixinbooks/(?P<pk>\d+)/', views.MixinBooksId.as_view())
```

```python
from rest_framework import generics
class MixinBooks(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class MixinBooksId(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
```



#### 1.4.3 接口优化（三）

##### 1.4.3.1 viewset使用

```python
# url设计*
path('mixinbooks/', views.MixinBooks.as_view({
	'get':'list',
    'post':'create'
})),
re_path('mixinbooks/(?P<pk>\d+)/', views.MixinBooks.as_view({
	'get':'retrieve',
    'put':'update',
    'delete':'destroy'
}))
```

```python
# view.py
from rest_framework.viewsets import ModelViewSet
class MixinBooks(ModelViewSet):
    queryset = Book.objects.all()
    serializer = BookSerializer
```

##### 1.4.3.2 viewset源码解析

```python
## create方法
1.Django程序启动，开始序列化，读取urls.py、sttings和视图类
2.执行as_views()，MixinBooks没有，去父类(ModelViewSet)中找
3.ModelViewSet继承了mixins中的几个GenericViewSet和ModelMinxin的几个个类,ModelMixin中没有，去GenericViewSet中找
4.GenericViewSet中继承(ViewSetMixin, generics.GenericAPIView)两个类
5.在ViewSetMixin中找到as_view()，在重新封装的view函数中有一个self.action_map = actions
6.这个actions就是as_view()传递的参数
7.绑定url和视图函数(actions)的映射关系
8.等待用户请求
9.接收到用户请求后，根据url找到视图函数
10.执行视图函数的dispath()方法,因为视图函数的返回值是self.dispath()
11.dispath分发请求，查到视图类中五个方法的某个
12.开始执行，比如post请求，返回self.create(),视图类本身没有则去父类找
13.最后在CreateModelMixin中找到，执行create方法，queryset和serialuzer_class,返回数据
```

```python
## retrieve方法
1.Django程序启动，开始初始化，获取配置信息，获取视图类并加载到内存中，获取url及视图类的对应关系
2.开始绑定视图类和url的对应关系，执行as_view()方法
3.as_view()方法被执行的时候传递了参数，为字典形式：{ “get”: “retrieve”, “delete”: “destroy”, “put”: “update” }
4.上一步中执行as_view()方法传递参数的目的是为了完成优化，将delete请求方式重新命名为不同的函数
5.ViewSetMixin类重写了as_view()方法，也就是在这个地方将几个函数重新绑定，它并没有重写dispatch方法
6.该方法返回视图函数view，注意在这个函数中有一个行 self = cls(**initkwargs), cls是视图类，执行视图函数时self就指向视图函数的实例对象
7.等待客户端请求
8.请求到来，开始执行视图函数，注意，调用视图函数时的方式是view(request)，而如果url带有参数，调用方式为view(request, xxx=id)的形式
9.显然，我们有命名参数(?P\d+)，所以此时的调用方式为view(request, pk=id)
10.视图函数中有一行self.kwargs = kwargs，所以pk已经被视图函数找到了
11.视图函数返回self.dispatch()，开始执行dispatch方法，注意self是视图类的实例化对象（每个请求都被封装为一个对象）
12.dispatch开始执行get方法，注意此时的get方法会执行retrieve，以为已经被重定向了
13.开始执行retrieve，有一行instance = self.get_object(), 该方法在GenericAPIView中
14.至关重要的是拿到self.kwargs中的pk关键字，然后从queryset中拿到想要的数据
15.返回结果
```

### 		1.5	认证组件*

#### 1.5.1 使用方法

```python
# 第一步:定义认证类
from rest_framework.viewsets import ModelViewSet
from rest_framework.exceptions import APIException
from rest_framework.authentication import BaseAuthentication
from Apps.Ass.models import UserToken
from rest_framework.exceptions import AuthenticationFailed

class UserAuth(BaseAuthentication):  # 继承BaseAuthentication可以不写authenticate_header方法
    def authenticate(self, request):
        user_token = request.query_params.get("token")
        username = request.query_params.get("username")
        try:
            token = UserToken.objects.filter(token=user_token,user__username=username).first()
            return username, token.token  # 这里返回的值分别在reuqest.user和request.auth中取,多个认证类则在最后一个中return
        except Exception:
            raise AuthenticationFailed({"code":"1003","error":"认证失败"})

            
class UserView(APIView):		#登录生成Token
    def post(self, request):
        fields = {'username', 'password'}
        user_info = dict()
        response = dict()

        if fields.issubset(set(request.data)):
            for key in fields:
                user_info[key] = request.data.get(key)
        user_instance = User.objects.filter(**user_info).first()

        if user_instance is not None:
            access_token = ''.join(str(uuid.uuid4()).split('-'))    # 导入uuid模块生成随机字符串
            UserToken.objects.update_or_create(user=user_instance, defaults={
                'token': access_token
            })
            response['status_code'] = 200
            response['status_message'] = '登录成功'
            response['access_token'] = access_token
        else:
            response['status_code'] = 201
            response['status_message'] = '登录失败'
        return Response(response)


class MixinBooks(ModelViewSet):
    authentication_classes = [UserAuth]   # 这个优先级比全局高
    queryset = Book.objects.all()
    serializer_class = BookSerializer
```

#### 1.5.2 全局设置

**注意**：视图类中authentication_classes的优先级比全局的高，如果视图类不需要验证，则直接写authentication_classes = []  

```python
# APIView中authentication_classes = api_settings.DEFAULT_AUTHENTICATION_CLASSES会先在setting中找
# 写在settings中
REST_FRAMEWORK = {
    # 认证组件
    'DEFAULT_AUTHENTICATION_CLASSES': [
        "Apps.Ass.Aus.LoginAuth"	# 验证类
    ]
}
```

#### 1.5.3 源码分析

```python
1.APIView中找到dispatch()方法
2.dispatch执行request = self.initialize_request(request, *args, **kwargs)将self.get_authenticators()返回的[auth() for auth in self.authentication_classes]认证类列表实例化后封装在了request.authenticators中
3.dispatch继续执行到self.initial(request, *args, **kwargs)中的self.perform_authentication(request)返回执行了request.user
4.在request.user中执行self._authenticate()
5.循环request.authenticators认证类列表
6.调用认证类中所写的authenticate方法进行认证，认证成功将返回的2个值赋值给reque.user和request.auth
7.认证失败则抛出APIException并捕获
```

### 		1.6	权限组件*

#### 1.6.1权限组件

```python
class UserPerms():
    message = "你没有权限访问该数据"

    def has_permission(self, request, view):
        """
        去数据库中查询权限，
        有权限return True
        无权限return False
        """


class MixinBooks(ModelViewSet):
    permission_classes = [UserPerms]
    queryset = Book.objects.all()
    serializer_class = BookSerializer
```

#### 1.6.2源码分析

```python
1.APIView中找到dispatch()方法
2.在dispatch()中找到self.initial(request, *args, **kwargs)方法
3.initial()中执行self.check_permissions(request)检查权限
4.循环self.get_permissions()返回的权限认证类的实例化列表
5.执行实例化类中的has_permission()方法，如果有权限返回True，无权限返回None或者False并抛出没有权限的错误
```

### 		1.7 	频率组件

#### 1.7.1普通用法

```python
class VisitThrottle():
    def allow_request(self, request, view):
        """
        	访问频率判断
        """
        return True # 通过返回True，限制返回False

    def wait(self):
        return 1		# 返回剩下秒数

class MixinBooks(ModelViewSet):
    throttle_classes = [VisitThrottle]
    queryset = Book.objects.all()
    serializer_class = BookSerializer
```

#### 1.7.2频率组件用法

##### 1.7.2.1局部用法

```python
# - 导入模块
from rest_framework.throttling import SimpleRateThrottle

# - 定义并继承SimpleRateThrottle
class RateRhtottle(SimpleRateThrottle):
    rate = "5/m"  # 指定访问频率 m为分钟

    def get_cache_key(self, request, view):
        print("self.get_ident",self.get_ident(request)) #获取IP地址方法一
        print("request.META.get('EMOTE_ADDR')",request.META.get("REMOTE_ADDR")) #获取IP地址方法二
        return self.get_ident(request)	#返回控制频率的IP地址或者用户名


# - 指定频率类
class MixinBooks(ModelViewSet):
    throttle_classes = [RateRhtottle]
    queryset = Book.objects.all()
    serializer_class = BookSerializer

```

##### 1.7.2.2全局用法

```python
# - 导入模块
from rest_framework.throttling import SimpleRateThrottle

# - 定义并继承SimpleRateThrottle
class RateRhtottle(SimpleRateThrottle):
    scope = "visit_rate"
    
    def get_cache_key(self, request, view):
        return self.get_ident(request)	#返回控制频率的IP地址或者用户名

# 另外，我们需要在全局settings中配置频率控制参数
REST_FRAMEWORK = {
    "DEFAULT_THROTTLE_CLASSES": ('throttler.utils.throttles.RateThrottle',),
    "DEFAULT_THROTTLE_RATES": {
        "visit_rate": "5/m"
    }
}
```

##### 1.7.2.3源码分析

```python
1.APIView中的dispatch(self, request, *args, **kwargs)
2.self.initial(request, *args, **kwargs)
3.self.check_throttles(request)
4.循环self.get_throttles()获取到的频率认证类列表并实例化
5.执行实例化类中自己写的allow_request(request, self)方法
6.如果没通过将实例化类中wait()的剩余的秒值返回并添加进列表
7.获取多个实例化类wait()方法返回的最大值
8.self.throttled(request, duration)
9.抛出异常Throttled(APIException) 
说明：自定义抛出异常可继承此异常重写
```

### 		1.8	URL注册器组件

#### 1.8.1 URL注册器组件的使用

浏览器访问http://127.0.0.1:8000/ass/mixinboks.json可返回json数据

```python
# - 导入模块
from rest_framework import routers

# - 生成一个注册器实例对象
router = routers.DefaultRouter()

# 将需要自动生成的url的接口注册
router.register("mixinbooks", views.MixinBooks)

# 开始自动生成URL

# 方法一
urlpatterns = {
    re_path(r'^', include(router.urls))
}
# 方法二
urlpatterns = [
    path('testlogin/', views.TestLogin.as_view()),
]
urlpatterns += router.urls


```

路由进行其他操作见rest_framework官网https://www.django-rest-framework.org/

### 		1.9	分页器组件

#### 1.9.1 APIView用法

```python
class PageBookView(APIView):
    def get(self, request, *args, **kwargs):
        book_obj = Book.objects.all()
        renderers_obj = Page()
        page_book = renderers_obj.paginate_queryset(book_obj, request)
        serializers_book = BookSerializer(page_book, many=True)
        return Response(serializers_book.data)
```

需要在settings中配置每次分页数

```python
REST_FRAMEWORK = {
    "PAGE_SIZE": 2
}
```

#### 1.9.2 继承ListModelMixin的用法

```python
# 例如 ModelViewSet
from rest_framework.pagination import PageNumberPagination
class Page(PageNumberPagination):
    page_size = 2
    page_query_param = 'p'
    page_size_query_param = 'size'
    max_page_size = 5


class MixinBooks(ModelViewSet):
    pagination_class = Page
    queryset = Book.objects.all()
    serializer_class = BookSerializer
```

### 		1.10	响应器组件

#### 1.10.1使用方法

```python
from rest_framework.renderers import JSONRenderer,BrowsableAPIRenderer

class MixinBooks(ModelViewSet):
    renderer_classes = [JSONRenderer,BrowsableAPIRenderer]
    queryset = Book.objects.all()
    serializer_class = BookSerializer
# JSONRenderer只响应json格式，BrowsableAPIRenderer为浏览器渲染
```



