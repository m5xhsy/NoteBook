
'''模板语法'''
# 1.渲染变量
'''
在 Django 模板中遍历复杂数据结构的关键是句点字符, 语法：{{var_name}}
    列表  lis=['aaa','bbb','ccc']
    字典  dic={'aaa':111,'bbb':222,'ccc':333}
    日期  dat=datetime.date(1999,5,2)
    对象  class
'''
# 2.过滤器
'''{{名称|过滤器:参数}}
data                {{ value|data:'Y-m-d' }}            如果 value=datetime.datetime.now()

default             {{ value|default:"nothing" }}       如果为空则显示默认值

length              {{ value|length }}                  返回值的长度。它对字符串和列表都起作用

filesizeformat      {{ value|filesizeformat }}          将值格式化为一个 “人类可读的” 文件尺寸，如果 value 是 123456789，输出将会是 117.7 MB。　

slice               {{ value|slice:"2:-1" }}            如果 value="hello world"，切片相当于values[2:-1]

truncatechars       {{ value|truncatechars:9 }}         参数为要截断的字符数，如果字符串字符多于指定的字符数量，那么会被截断。截断的字符串将以可翻译的省略号序列（“...”）结尾。

truncatewords       {{ value|truncatechars:9 }}         截断单词数

safe                value="<a href="">点击</a>"          Django的模板中会对HTML标签和JS等语法标签进行自动转义，原因显而易见，这样是为了安全。
                    {{ value|safe }}                    但是有的时候我们可能不希望这些HTML元素被转义，比如我们做一个内容管理系统，
     mark_safe()#在python中用这个                         后台添加的文章中是经过修饰的，这些修饰可能是通过一个类似于FCKeditor编辑加注了HTML修饰符的文本，
                                                        如果自动转义的话显示的就是保护HTML标签的源文件。为了在Django中关闭HTML的自动转义有两种方式，
                                                        如果是一个单独的变量我们可以通过过滤器“|safe”的方式告诉Django这段代码是安全的不必转义                  
'''
# 3.渲染标签
'''
for循环
{% for item in list %}
    <p>{{ forloop.counter }}{{ item }}</p>    
{% empty %}         #可选的{% empty %} 从句，以便在给出的组是空的或者没有被找到时，可以有所操作。
    <p>no</p>          
{% endfor %}
forloop:
    forloop.counter            1开始循环 (1-indexed)
    forloop.counter0           0开始循环 (0-indexed)
    forloop.revcounter         倒序循环到1 (1-indexed)
    forloop.revcounter0        倒叙循环到0 (0-indexed)
    forloop.first              第一个则true，其他为false
    forloop.last               最后一个则true，其他为false

if语句
{% if num > 100 or num < 0 %}
...
{% elif num > 80 and num < 100 %}
...
{% else %}
...
{% endif %}  

with语句          使用一个简单地名字缓存一个复杂的变量，当你需要使用一个“昂贵的”方法（比如访问数据库）很多次的时候是非常有用的
{% with total=business.employees.count %}
{{ total }} employee{{ total|pluralize }}
{% endwith %}

csrf_token
在form表单中加{% csrf_token %}
这个标签用于跨站请求伪造保护
'''
# 4.自定义标签和过滤器
'''

1.检查settings中有没有添加app
2.app下创建templatetags
3.添加脚本
###########过滤器###############
脚本中:    #前三步为固定格式
    from django.template import Library
    register = Library() 
    @register.filter            ##标签则是register.simple_tag
    def mul(x,y):
        return x * y
html:
    {% load 脚本文件名 %}          #标签{% num x y %}
    {{ 12|mul:24 }}
###########标签###############    
脚本中:    #前三步为固定格式
    from django.template import Library
    register = Library() 
    @register.simple_tag
    def mul(x,y,z):
        return x * y
html:
    {% load 脚本文件名 %}
    {% num x y z %}
###########补充#################
脚本中:    #前三步为固定格式
    from django.template import Library
    register = Library() 
    @register.inclusion_tag("menu.html")
    def mul(request):
        menu_list = [1,2,3]
        return {'menu_list':menu_list,'request':request}        #参数传到“menu.html”中渲染，最后返回模板
html:
    {% load 脚本文件名 %}
    {% num request %}
'''
# 5.模板继承 (extend)
'''
{% include 'xxx.html' %}    #将xxx.html中的内容拿过来放在指定位置

母版.html
{% block 名字 %}
{% endblock %}
子版.html
{% extends '母版.html' %}
{% block 名字 %}
{{ block.super }}       #保留母版中的，并追加后面的内容
{% endblock %}

这里是使用继承的一些提示：
如果你在模版中使用 {% extends %} 标签，它必须是模版中的第一个标签。其他的任何情况下，模版继承都将无法工作。
在base模版中设置越多的 {% block %} 标签越好。请记住，子模版不必定义全部父模版中的blocks，所以，你可以在大多数blocks中填充合理的默认内容，然后，只定义你需要的那一个。多一点钩子总比少一点好。
如果你发现你自己在大量的模版中复制内容，那可能意味着你应该把内容移动到父模版中的一个 {% block %} 中。
If you need to get the content of the block from the parent template, the {{ block.super }} variable will do the trick. This is useful if you want to add to the contents of a parent block instead of completely overriding it. Data inserted using {{ block.super }} will not be automatically escaped (see the next section), since it was already escaped, if necessary, in the parent template.
为了更好的可读性，你也可以给你的 {% endblock %} 标签一个 名字 。例如：
{% block content %}
...
{% endblock content %}　　
在大型模版中，这个方法帮你清楚的看到哪一个　 {% block %} 标签被关闭了。     


'''
