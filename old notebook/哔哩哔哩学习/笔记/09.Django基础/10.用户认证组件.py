from django.contrib import auth
from django.contrib.auth.models import User,AbstractUser
from django.contrib.
登录验证'''
from django.contrib.auth.decorators import login_required

@login_required     #当未登录时自动跳转到登录页面  登录页面在settings中配置   LOGIN_URL = '/App/login/'
def index(request):
    retuen HttpResponse('index')
    
url会显示从哪个页面跳转过来的，登录后则跳转回去
当发Ajax请求时       http:127.0.0.1:8000/login/?next=xxx
if(location.search.slice(6)){
    location.href = location.location.search.slice(6)      #其他页面跳转过来则切片
}else{
    location.href = "/"     #否则跳转到登录后要进的页面
}

'''

继承django.user表'''
from django.contrib.auth.models import AbstractUser
class UserInfo(AbstractUser):
    tel = models.CharField(max_length = 32)
    gander = models.IntegerField(choices=((1,'男'),(2,'女')),default=1)



    obj = UserInfo.filter(pk = 1)
    obj.gander          #取出来值为1
    obj.get_gander_display()    #取出来的值为对应的值
AUTH_USER_MODEL = "app01.UserInfo"         #写再setting.py中
'''

auth模块'''
user_obj = auth.authenticate(username = user,password = pswd)
    提供了用户认证，即验证用户名以及密码是否正确,一般需要username  password两个关键字参数
    如果认证信息有效，会返回一个  User  对象。authenticate()会在User 对象上设置一个属性标识那种认证后端认证了该用户，
    且该信息在后面的登录过程中是需要的。当我们试图登陆一个从数据库中直接取出来不经过authenticate()的User对象会报错的！！

auth.login(request,user_obj)
    该函数接受一个HttpRequest对象，以及一个认证了的User对象
    此函数使用django的session框架给某个已认证的用户附加上session id等信息。

auth.logout(request)
    该函数接受一个HttpRequest对象，无返回值。当调用该函数时，当前请求的session信息会全部清除。
    该用户即使没有登录，使用该函数也不会报错。
'''
user对象'''
request.user.is_authenticated()
    如果是真正的 User 对象，返回值恒为 True 。 用于检查用户是否已经通过了认证。
    通过认证并不意味着用户拥有任何权限，甚至也不检查该用户是否处于激活状态，这只是表明用户成功的通过了认证。 
    这个方法很重要, 在后台用request.user.is_authenticated()判断用户是否已经登录，如果true则可以向前台展示request.user.username
要求：
    1  用户登陆后才能访问某些页面，
    2  如果用户没有登录就访问该页面的话直接跳到登录页面
    3  用户在跳转的登陆界面中完成登陆后，自动访问跳转到之前访问的地址
    方法1:
        def my_view(request):
            if not request.user.is_authenticated():
            return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
    方法2:
        django已经为我们设计好了一个用于此种情况的装饰器：login_requierd()
        from django.contrib.auth.decorators import login_required     
        @login_required
        def my_view(request):
          ...
    若用户没有登录，则会跳转到django默认的 登录URL '/accounts/login/ ' (这个值可以在settings文件中通过LOGIN_URL进行修改)。并传递  当前访问url的绝对路径 (登陆成功后，会重定向到该路径)。

request.user.username

request.user.__dir__()

'''

用户操作'''
创建用户
    from django.contrib.auth.models import User
    user = User.objects.create_user(username=user, password=pswd, email=email)

验证用户密码
    request.user.check_password(passwd)
    用户需要修改密码的时候 首先要让他输入原来的密码 ，如果给定的字符串通过了密码检查，返回 True

修改密码set_password()
    user = User.objects.get(username='')
    user.set_password(password='')
    user.save()
'''

注册示例'''
def sign_up(request):
    state = None
    if request.method == 'POST':

        password = request.POST.get('password', '')
        repeat_password = request.POST.get('repeat_password', '')
        email = request.POST.get('email', '')
        username = request.POST.get('username', '')
        if User.objects.filter(username=username):
            state = 'user_exist'
        else:
            new_user = User.objects.create_user(username=username, password=password, email=email)
            new_user.save()

            return redirect('/book/')
    content = {
        'state': state,
        'user': None,
    }
    return render(request, 'sign_up.html', content)　　
'''
修改密码'''
@login_required
def set_password(request):
    user = request.user
    state = None
    if request.method == 'POST':
        old_password = request.POST.get('old_password', '')
        new_password = request.POST.get('new_password', '')
        repeat_password = request.POST.get('repeat_password', '')
        if user.check_password(old_password):
            if not new_password:
                state = 'empty'
            elif new_password != repeat_password:
                state = 'repeat_error'
            else:
                user.set_password(new_password)
                user.save()
                return redirect("/log_in/")
        else:
            state = 'password_error'
    content = {
        'user': user,
        'state': state,
    }
    return render(request, 'set_password.html', content)
'''


def auth_login(request):
    session_user = request.user.username
    if session_user:
        if request.method == "GET":
            return render(request,'auth_login.html',{'flag':session_user})
        else:
            user = request.POST.get('user')
            pswd = request.POST.get('pswd')
            if user == session_user:
                return render(request,'auth_login.html',{'flag':session_user})
            else:
                user_obj = auth.authenticate(username = user, password =pswd)
                if user_obj:
                    auth.login(request, user_obj)
                    return render(request,'auth_login.html',{'flag':user})
                else:
                    return HttpResponse('登录失败')
    else:
        if request.method == "GET":     #GET请求
            return render(request,'auth_login.html',{'flag':'登录'})
        user = request.POST.get('user') #POST请求
        pswd = request.POST.get('pswd')
        user_obj = auth.authenticate(username=user, password=pswd)
        if user_obj:
            auth.login(request, user_obj)
            return render(request, 'auth_login.html', {'flag': user})
        else:
            return HttpResponse('登录失败')
def auth_logout(requset):
    auth.logout(requset)
    return redirect('/App/auth_login/')