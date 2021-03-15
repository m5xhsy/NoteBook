# Flask

## 1.Response

```python
from flask import Flask, redirect, render_template, jsonify,send_file

app = Flask(__name__)


@app.route("/")
def index():
    return redirect("/login")		 		# 重定向


@app.route("/login")
def login():
 	data = {
        'name':'m5xhsy',
        'age':21
    }
    return render_template("login.html",data=data)	    # 取参数用data取
	# return render_template("login.html",**data)		# 取参数时用data中的key取

@app.route('/json')
def jsons():
    return jsonify({"state": "ok"})			# 返回json字符串


@app.route('/file')
def file():
    return send_file("4.mp4")				# 返回文件可自动识别音频视频图片文件


app.run(debug=True)	
```

## 2.Request

```python
from flask import request
request.method			# 请求方式
request.args			# get中的参数(可用to_dict()转换成字典)
request.from			# post中的数据(可用to_dict()转换成字典)
request.values			# get和post的数据(可用to_dict()转换成字典，如果args和from同时有参数且key相同会覆盖)
request.path			# 路由地址(/index)
request.host			# 主机地址(127.0.0.1:5000)
request.url				# 主机地址+路由(127.0.0.1:5000/index)
request.json			# contentype为json的数据
request.data			# contentype无法识别的原始数据,相当于django中的request.body
request.files			# 文件数据 用get取,取出来的file_obj用file_obj.save(file_obj.filename)保存
request.cookies			# 获取cookies
request.environ			# 原始request数据
```

## 3.Session

```python
from flask import Flask
from flask import session
app = Flask(__name__)
app.secret_key = "asdjajfkja[oasoaf"	# 相当于算法加盐加密session数据

设置 session['user'] = 'user'
获取 user = session.get('user')
```

## 4.Flask与jinja2语法

!>与django模板语法不同地方

**（1）渲染变量中字典value获取**

```python
{ { dict.key	} }
{ { dict['key'] } }
{ { dict.get('key') } }
```

**（2）字典循环**

```python
{ % key,value foo in dict.ietms() % }		# 也可以循环dict.keys()或者item.values() 
	{{ key }}:{{ value }}
{ % endfor % }
```

**（3）safe渲染标签**

```python
a = <input type="text">
方法一：前端使用safe
{ { a|safe } }
方法二：后端Markup
from flask import Markup
a=Markup(a)
{ { a } }
```

**（4）函数,相当于django自定义标签**

```python
from flask import Flask
app = Flask(__name__)

@app.template_global()
def add(a,b):
    return a+b

@app.roter('/')
def index():
    return render_template('index.html',add=add)

{ { add(1,2) } } 
```

**（5）偏函数，相当于django自定义过滤器**

```python
from flask import Flask
app = Flask(__name__)

@app.template_filter()
def add(a,b,c):
    return a+b+c
    
@app.roter('/')
def index():
    return render_template('index.html',add=add)

{ { 2|add(1,3) } }				# 相当于add(2,1,3),2的位置可执行一个函数
```

## 5.flask与装饰器

### **5.1 before_request**

```python
@app.before_request
def before():
	return None		# return的值为真则直接跳过视图函数
					# 不写return或者return不带参数以及return None就可用跳过这个装饰器
```

### **5.2 after_request**

```python
@app.after_request
def after(res):
	print(res)		# 视图函数返回的值
	return res
```

### **5.3 errorhandler**

```python
@app.errorhandler(404)	# 捕捉404错误
def error(res):
    print(res)			# 错误提示
    return render_template('404.html')
```

### **5.4 自定义装饰器**

!>**装饰器出现问题及解决方法：**AssertionError: View function mapping is overwriting an existing endpoint function: session_wai

```python
方法一:python自带解决方法
import functools
def wai(func, *args, **kwargs):
    @functools.wraps(func)      # 保留原始属性
    def session_wai():
        if not request.cookies:
            return redirect('/login')
        return func()
    return session_wai
	
方法二:flask提供方法
@app.route('/',endpoint=index)	# endpoint=index  
def index():
	return render_template('index.html')
```

## 6.flask配置

### **6.1 flask的路由配置**

**（1）反向生成url地址**

```python
from flask import url_for
@app.route('/',endpoint=“index”)
def home():
    print(url_for('index'))				# index将其反向解析成 ' / '
    return 'ok'
```

**（2）请求方式**

```python
methods=['GET']
```

**（3）默认参数**

```python
@app.route('/index', defaults={'name':'m5xhsy'})		# 后面字典类型（一般不用）加装饰器容易出错
def index(name):
    print(name)
    return 'ok'
```

**（4）严格遵循斜杠**

```python
strict_slashes=True 
```

**（5）永久重定向**

```python
redirect_to="/index"		# 301访问视图前重定向 
```

**（6）动态路由**

```python
@app.route('/index/<int:page>')		# <page>这样写默认为str类型(可接收所有参数)
def index(page):
	print(page,type(page))
	return 'ok'
```

### **6.2 flask实例化配置**

```python
static_folder = 'static',  			# *静态文件目录的路径 默认当前项目中的static目录
static_url_path = None,  			# *静态文件目录的url路径 默认不写是与static_folder同名,远程静态文件时复用
template_folder = 'templates'  		# *template模板目录, 默认当前项目中的 templates 目录
                                    
host_matching = False,  			# 如果不是特别需要的话,慎用,否则所有的route 都需要host=""的参数
subdomain_matching = False, 		# 理论上来说是用来限制SERVER_NAME子域名的,但是目前还没有感觉出来区别在哪里
									# host_matching是否开启host主机位匹配,是要与static_host一起使用,如果配置了static_host, 则必须赋值为True
                                    # 这里要说明一下,@app.route("/",host="localhost:5000") 就必须要这样写
                                    # host="localhost:5000" 如果主机头不是 localhost:5000 则无法通过当前的路由
static_host = None,  				# 远程静态文件所用的Host地址,默认为空
instance_path = None,  				# 指向另一个Flask实例的路径
instance_relative_config = False  	# 是否加载另一个实例的配置
root_path = None  					# 主模块所在的目录的绝对路径,默认项目目录
```

### **6.3 flask的对象配置**

#### **配置说明**

```python
使用app.config['DEBUG'] = True
{
    'DEBUG': False,  # 是否开启Debug模式
    'TESTING': False,  # 是否开启测试模式
    'SECRET_KEY': None,  # 相当于app.secret_key
    'PERMANENT_SESSION_LIFETIME': 31,  # days , Session的生命周期(天)默认31天
    'SESSION_COOKIE_NAME': 'session',  # 在cookies中存放session加密字符串的名字(设置在浏览器cookie中的键)
    
    # 下面的知道就行
    'PROPAGATE_EXCEPTIONS': None,  # 异常传播(是否在控制台打印LOG) 当Debug或者testing开启后,自动为True
    'PRESERVE_CONTEXT_ON_EXCEPTION': None,  # 一般不用它
    'USE_X_SENDFILE': False,  # 是否弃用 x_sendfile
    'LOGGER_NAME': None,  # 日志记录器的名称
    'LOGGER_HANDLER_POLICY': 'always',
    'SERVER_NAME': None,  # 服务访问域名（一般web服务器会来配置，除非裸跑flask）
    'APPLICATION_ROOT': None,  # 项目的完整路径
    'SESSION_COOKIE_DOMAIN': None,  # 在哪个域名下会产生session记录在cookies中(需要开启SERVER_NAME)
    'SESSION_COOKIE_PATH': None,  # cookies的路径
    'SESSION_COOKIE_HTTPONLY': True,  # 控制 cookie 是否应被设置 httponly 的标志，
    'SESSION_COOKIE_SECURE': False,  # 控制 cookie 是否应被设置安全标志
    'SESSION_REFRESH_EACH_REQUEST': True,  # 这个标志控制永久会话如何刷新
    'MAX_CONTENT_LENGTH': None,  # 如果设置为字节数， Flask 会拒绝内容长度大于此值的请求进入，并返回一个 413 状态码
    'SEND_FILE_MAX_AGE_DEFAULT': 12,  # hours 默认缓存控制的最大期限
    'TRAP_BAD_REQUEST_ERRORS': False,
    # 如果这个值被设置为 True ，Flask不会执行 HTTP 异常的错误处理，而是像对待其它异常一样，
    # 通过异常栈让它冒泡地抛出。这对于需要找出 HTTP 异常源头的可怕调试情形是有用的。
    'TRAP_HTTP_EXCEPTIONS': False,
    # Werkzeug 处理请求中的特定数据的内部数据结构会抛出同样也是“错误的请求”异常的特殊的 key errors 。
    # 同样地，为了保持一致，许多操作可以显式地抛出 BadRequest 异常。
    # 因为在调试中，你希望准确地找出异常的原因，这个设置用于在这些情形下调试。
    # 如果这个值被设置为 True ，你只会得到常规的回溯。
    'EXPLAIN_TEMPLATE_LOADING': False,
    'PREFERRED_URL_SCHEME': 'http',  # 生成URL的时候如果没有可用的 URL 模式话将使用这个值
    'JSON_AS_ASCII': True,
    # 默认情况下 Flask 使用 ascii 编码来序列化对象。如果这个值被设置为 False ，
    # Flask不会将其编码为 ASCII，并且按原样输出，返回它的 unicode 字符串。
    # 比如 jsonfiy 会自动地采用 utf-8 来编码它然后才进行传输。
    'JSON_SORT_KEYS': True,
    #默认情况下 Flask 按照 JSON 对象的键的顺序来序来序列化它。
    # 这样做是为了确保键的顺序不会受到字典的哈希种子的影响，从而返回的值每次都是一致的，不会造成无用的额外 HTTP 缓存。
    # 你可以通过修改这个配置的值来覆盖默认的操作。但这是不被推荐的做法因为这个默认的行为可能会给你在性能的代价上带来改善。
    'JSONIFY_PRETTYPRINT_REGULAR': True,
    'JSONIFY_MIMETYPE': 'application/json',
    'TEMPLATES_AUTO_RELOAD': None,
}
```

#### **导入配置**

```python
# app.py
import settings
app = Flask(__name__)
app.config.from_object(settings.FlaskDebugSetting)

# settings.py
class FlaskDebugSetting(object):
    DEBUG = True
    SECRET_KEY = "m5xhsy"
    PERMANENT_SESSION_LIFETIME = 7
    SESSION_COOKIE_NAME = "debug_session"

class FlaskTestSetting(object):
    DEBUG = True
    SECRET_KEY = "m5xhsy"
    PERMANENT_SESSION_LIFETIME = 15
    SESSION_COOKIE_NAME = "debug_session"
```

## 7.flask的flash

```python
from flask import flash,get_flashed_messages
# 直接获取
flash('as')				# 设置
get_flashed_messages() 	# 获取
# 过滤
flash('as','tar')
flash('bs','tar1')
get_flashed_messages(category_filter=['tar'])			# 过滤tar对应的值
get_flashed_messages(category_filter=['tar1'])			# 过滤tar对应的值
get_flashed_messages(category_filter=['tar1','tar'])	# 过滤tar与tar1对应的值
get_flashed_messages(category_filter='tar1')			# 不要这样写,tar1字符串包含tar,会把tar一起取出来
# 模板中使用
{ % with list in get_flashed_messages(category_filter=['tar1']) % }
	{ % for foo in list % }
    	{ { foo } }
    { % endfor % }
{ % endwith % }
```

## 8.flask蓝图

### **8.1 目录结构**

>.
>├── App
>│   ├── __init__.py
>│   ├── static
>│   ├── templates
>│   └── views
>│       ├── apiView.py
>│       └── userView.py
>├── manager.py
>└── venv

```python
# manager.py
import App

if __name__ == '__main__':
    app = App.create_app()
    app.run()
```

```python
# __init__.py
from flask import Flask

from .views.apiView import api
from .views.userView import user

app = Flask(__name__)

def create_app():
    app.register_blueprint(api)
	app.register_blueprint(user)
    return app
```

```python
# apiView.py
from flask import Blueprint

api = Blueprint("api",__name__,url_prefix="/api")

@api.route('/')
def index():
    return "Api蓝图"
```

```python
# userView.py
from flask import Blueprint

user = Blueprint("user",__name__,url_prefix="/user")

@user.route("/")
def index():
    return "User蓝图"
```

### **8.2 使用方法**

```python
# app.py
from flask import Flask
from Api import apiView

app = Flask(__name__)
app.register_blueprint(apiView.apiApp)

@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()

```

```python
# 蓝图
from flask import Blueprint, render_template
apiApp = Blueprint('Api',__name__,template_folder='apiTemp', static_folder='apiStatic', url_prefix='/api')
# 第一个参数是对蓝图区分的名称
@apiApp.route('/index')
def index():
    return render_template('index.html')
```

## 9.第三方组件

### **9.1 Flask-session组件**

```python
from flask import Flask, session
from flask_session import Session
from redis import Redis

app = Flask(__name__)
app.config['SESSION_TYPE'] = 'redis'
app.config['SESSION_REDIS'] = Redis(host="127.0.0.1", port=6379, db=6)
Session(app)

@app.route('/')
def index():
    session['user'] = 'm5xhsy'
    return 'index'

@app.route('/home')
def home():
    print(session.get('user'))
    return 'home'
    
if __name__ == "__main__":
    app.run()
```

### **9.2 WTForms组件**

```python
#### py文件
from flask import Flask, render_template, request
from wtforms.fields import simple, core
from wtforms import Form, widgets
from wtforms import validators

app = Flask(__name__)


class LoginForm(Form):

    username = simple.StringField(
        label="用户名: ",  	# label标签
        validators=[			# 验证
            validators.DataRequired(message="用户名不能为空"),
            validators.Length(max=11, min=6, message="用户名长度错误"),
            validators.Length(max=11, min=6, message="用户名长度错误")
        ],
        description="user",  # 描述
        id="user_name",  # 标签id
        default=None,  # 默认值
        widget=widgets.TextInput(),  # 默认组件(type="text")
        render_kw={"class": "username"}  # {"class":"username"}
    )
    password = simple.PasswordField(
        label="密  码: ",  # 标记
        validators=[
            validators.DataRequired(message='用户名不能为空'),
            validators.Length(max=10, min=6, message="密码长度错误")
        ],  #
        description="pswd",  # 描述
        id="pass_word",  # 标签id
        default=None,  # 默认值
        widget=widgets.PasswordInput(),  # 默认组件(type="text")
        render_kw={"class": "password"}		# 标签属性
    )
    repassword = simple.PasswordField(
        label="确认密码: ",  # 标记
        validators=[
            validators.EqualTo('password', message="密码不一致")		# 将这个标签指向password标签
        ],  #
        description="repswd",  # 描述
        id="repass_word",  # 标签id
        default=None,  # 默认值
        widget=widgets.PasswordInput(),  # 默认组件(type="text")
        render_kw={"class": "repassword"}
    )
    email = simple.StringField(
        label='邮箱:',
        validators=[
            validators.DataRequired(message="邮箱不能为空"),
            validators.Email(message="请输入正确的邮箱"),		# 邮箱验证，需要pip3 install email_validator
        ],
        description="email",
        id="email",
        default=None,
        widget=widgets.TextInput(),
        render_kw={"class": "email"}
    )
    gender = core.RadioField(		# 单选
        label="性别",
        validators=None,
        coerce=int,
        choices=(
            (1, '女'),
            (2, '男')
        ),
        default=1,
        validate_choice=True,
    )
    hobby = core.SelectMultipleField(		# 多选
        label="爱好",
        coerce=int,
        validators=[validators.Length(min=2, max=4, message="只能选择2-4个")],
        choices=(		# 选项
            (1, '女'),
            (2, '男')
        ),
        default=(1,),  # 默认选1
        validate_choice=True,
    )


@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "POST":
        new_fm = LoginForm(request.form)
        if new_fm.validate():		# 验证
            return new_fm.data
        else:
            return render_template('index.html', fm=new_fm)
    input_form = LoginForm()
    return render_template('index.html', fm=input_form)


if __name__ == '__main__':
    app.run()

```

```html
#html文件
<form action="" method="post" novalidate>
    { % for field in fm % }
        <div style="width: 150px">{ { field.label } }</div>{ { field } }{ { field.errors.0 } }<br>
    { % endfor % }
    <input type="submit" value="提交">
</form>
```

### **9.3 Flask-SQLAlchemy**

#### **目录结构**

**参照蓝图目录结构**

```python
# models.py		# 参照蓝图目录结构，在App下也就是__init__.py同级目录下创建

from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()		# 这个如果写在__init__.py中,会出现循环导入错误

class UserInfo(db.Model):	# 创建表
    __tablename__ = "userinfo"
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(32),index=True)
    age = db.Column(db.Integer)


# db.create_all(app=app)
if __name__ == '__main__':			# 离线脚本，创建表时用到
    from App import create_app		# 导入创建app的函数,这个写在main中,写上面会有循环导入的错误
    app = create_app()				# 创建app
    db.drop_all(app=app)    		# 先清除继承db.Model的表
    db.create_all(app=app)  		# 再创建
```

```python
# __init__.py 配置 

from flask import Flask


from App.views.apiView import api
from App.views.userView import user	# 
from App.models import db		# 导入models中的db

app = Flask(__name__)


def create_app():
    app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:Ass078678@192.168.239.128:3306/m5xhsy?charset=utf8"	# 创建连接
    app.config["SQLALCHEMY_POOL_SIZE"] = 5      # SQLALCHEMY_POOL_SIZE 配置 SQLAlchemy 的连接池大小
    app.config["SQLALCHEMY_POOL_TIMEOUT"] = 15  # SQLALCHEMY_POOL_TIMEOUT 配置 SQLAlchemy 的连接超时时间
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False	# 这个默认不写会等于None,只有设置False才不会出现警告
    db.init_app(app)    # 先配置config再创建init_app才有效
    app.register_blueprint(api)
    app.register_blueprint(user)
    return app
```

#### 增删改查

```python
from flask import Blueprint,jsonify
from App.models import UserInfo,db

user = Blueprint("user",__name__,url_prefix="/user")

@user.route("/create_userinfo")	# 增
def create_userInfo():		
    db.session.add(UserInfo(name="m5xhsy",age=18))
    db.session.add(UserInfo(name="Ass", age=18))
    db.session.commit()
    return "create ok!"

@user.route("/find_userinfo")	# 查
def find_userinfo():
    user_list = UserInfo.query.all()	# 查找用query不加括号
    return jsonify({"data":[(item.name,item.age) for item in user_list]})

@user.route("/update_userinfo")	# 改
def update_userinfo():
    UserInfo.query.filter_by(age=18).update({"age":19})
    db.session.commit()
    return "update ok!"

@user.route("/delete_userinfo")	# 删
def delete_userinfo():
    UserInfo.query.filter_by(name="Ass").delete()
    db.session.commit()
    return "delete ok!"
```

### **9.4 Flask-Script**

#### **终端中启动**

```python
# python manager.py runserver -h 0.0.0.0 -p 9527
import App
from flask_script import Manager

app = App.create_app()
manager = Manager(app)

if __name__ == '__main__':
    manager.run()
```

#### **自定义终端启动**

```python
import App
from flask_script import Manager

app = App.create_app()
manager = Manager(app)

# python manager.py runflask -p 0.0.0.0 -h 9527	# 自定义
@manager.option("-h","--name",dest="host")   # -h为简写，--host为全称，以host传到runflask中
@manager.option("-p","--port",dest="port")
def runflask(host,port):
    app.run(debug=True,host=host,port=int(port))
    return "ok"		# 这里返回的值会打印到终端上

# python manager.py run # 直接运行
@manager.command	
def run():		# 这里可用传参数
    app.run(debug=True)

if __name__ == '__main__':
     manager.run()
```

**9.5 Flask-Migrate**

```python
# 要使用Flask-Script才可使用Flask-Migrate
import App
from flask_script import Manager
from flask_migrate import Migrate,MigrateCommand	
from App.models import db

app = App.create_app()
manager = Manager(app)	

manager.add_command("db",MigrateCommand)		# 当你的命令中出现 db 指令,则去MigrateCommand指令集中寻找对应关系
Migrate(app=app,db=db)	# 告诉它支持的app以及操作的数据库

if __name__ == '__main__':
     manager.run()
        
# 指令集
$ python manager.py db init
$ python manager.py db migrate		# 相当于Django中的 makemigration
$ python manager.py db upgrade		# 相当于Django中的 migrate
```

## 10.CBV

```python
from flask.views import MethodView
class Login(MethodView):
    methods = ['GET']		# 允许的请求方法
    decorators = [timer]	# 执行的装饰器
    def get(self):
        return 'get'

    def post(self):
        return 'post'
        
app.add_url_rule("/login",view_func=Login.as_view("login"))
```

