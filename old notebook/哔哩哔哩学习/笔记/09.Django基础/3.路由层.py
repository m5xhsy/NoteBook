"""

Django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))

Django URL配置
“urlpatterns”列表将url路由到视图。详情请参阅:
https://docs.djangoproject.com/en/3.0/topics/http/urls/
例子:
功能视图
    1. 添加导入:   from my_app import views
    2. 将URL添加到urlpatterns: path('', views.home, name='home')
基于类的观点
    1. 添加导入: from other_app.views import Home
    2. 将URL添加到urlpatterns: path("， home .as_view()， name='home')
包括另一个URLconf
    1. 导入include()函数: from django.urls import include, path
    2. 向urlpatterns添加一个URL:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path,re_path,include,reverse
from django.conf.urls import url        #相当于re_path
from app import views
urlpatterns = [
    path('admin/', admin.site.urls),
    re_path('articles/(\d{4})/',views.special),  #正则表达式用()分组，视图函数special(request,year)则传2个值
    re_path('timer/(?P<year>\d{4})/(?P<month>\d{2})/',timer),  #有名分组，视图函数timer(request,year,month)传3个值，关键字要保持一致
    re_path('^$',views.home)                #首页
    path('App/',views.app_home)             #app首页
    #分发
    # path('App/',include('App.urls'))
    # path('app01/',include('app01.urls'))
    #http://127.0.0.1:8000/app/index/

    # from django.contrib import admin
    # from django.urls import path,re_path,include
    # from app01 import views
    # urlpatterns = [
    #    re_path(r'^admin/', admin.site.urls),    #在app中添加一个urls.py
    #    re_path(r'^blog/', include(('blog.urls',app_name='blog')),namespace="blog"),     #名称空间django2必须声明app_name
    #    #反向解析  reverse("blog:index")     #index为app中路径的别名
    # ]

    #反向解析
    # 视图函数中重定向加反向解析
        # from django.shortcuts import redirect,reverse
        # url = reverse('别名')
        # return redirect(url)

    #reverse('xxx/',args(1,))   反向解析带参数的别名


    # 模版中反向解析
        #path('login/',views.login,name='xxx')      <form action="{% url 'xxx' %}" method="post"></form>
        #login/无论怎么变，form传过来只找别名
        # <a href="{% url 'news-year-archive' 2012 %}">2012 Archive</a>
        # <ul>
        # {% for yearvar in year_list %}
        # <li><a href="{% url 'news-year-archive' yearvar %}">{{ yearvar }} Archive</a></li>
        # {% endfor %}
        # </ul>


  ]


'''
请求的url的路径部分与url方法的正则表达式进行匹配，一旦匹配成功，则执行对应的视图函数
#伪代码
http://127.0.0.1:8000/articles/2003
path = "articles/2003/"
for item in urlpatterns:
    ret = re.search(items.regex,path)
    if ret:
        item.function(request)

'''