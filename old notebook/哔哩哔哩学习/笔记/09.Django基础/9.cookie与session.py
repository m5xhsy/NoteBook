


创建Cookie'''
    obj = render(request,'index.http')
    obj.set_cookie('is__login',True)
    obj.set_cookie('user',user)
    return obj


class HttpResponseBase:
        def set_cookie(self, key,                 键
        　　　　　　　　　　　　 value='',            值
        　　　　　　　　　　　　 max_age=None,        超长时间 
　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　cookie需要延续的时间（以秒为单位）
　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　如果参数是\ None`` ，这个cookie会延续到浏览器关闭为止。

        　　　　　　　　　　　　 expires=None,        超长时间
       　　　　　　　　　　　　　　　　　　　　　　　　　　expires默认None ,cookie失效的实际日期/时间。 
    　　　　　　　　　　　　　　　　　　　　　　　　　　　　

        　　　　　　　　　　　　 path='/',           Cookie生效的路径，
                                                 浏览器只会把cookie回传给带有该路径的页面，这样可以避免将
                                                 cookie传给站点中的其他的应用。
                                                 / 表示根路径，特殊的：根路径的cookie可以被任何url的页面访问
        　　　　　　　　　　　　 
                             domain=None,         Cookie生效的域名

                                                  你可用这个参数来构造一个跨站cookie。
                                                  如， domain=".example.com"
                                                  所构造的cookie对下面这些站点都是可读的：
                                                  www.example.com 、 www2.example.com 
        　　　　　　　　　　　　　　　　　　　　　　　　　和an.other.sub.domain.example.com 。
                                                  如果该参数设置为 None ，cookie只能由设置它的站点读取。

        　　　　　　　　　　　　 secure=False,        如果设置为 True ，浏览器将通过HTTPS来回传cookie。
        　　　　　　　　　　　　 httponly=False       只能http协议传输，无法被JavaScript获取
                                                 （不是绝对，底层抓包可以获取到也可以被覆盖）
        　　　　　　　　　　): pass

'''
获取Cookie'''
    is_login = request.COOKIES.get('is_login')
'''
删除Cookie'''
    obj = delete_cookie("cookie_key",path="/",domain=name)
'''
jquery操作Cookie'''
Cookies定义:让网站服务器把最少量的数据储存到客户端的硬盘或者内存。从客户端的硬盘读取数据的一种技术;
引用jQuery.cookie.js      <script src="jquery.cookie.js"></script>

1.添加一个"会话Cookie"
    $.cookie('cookie_key','cookie_value');
        这里没有设置cookie有效时间，所创建的cookie有效默认期默认到用户关闭浏览器为止，所以被称为"会话cookie(session cookie)"

2.创建一个cookie并设置有效期为7天
    $.cookie('cookie_key','cookie_value',{ expires:7 });
        这里指明了cookie的有效时间，所创建的cookie被称为"持久cookie(persistent cookie)"。注意单位为:天;

3.创建一个cookie并设置cookie的有效路径
    $.cookie('cookie_key', 'cookie_value', { expires: 7, path: '/' });
        在默认情况下，只有设置 cookie的网页才能读取该 cookie。如果想让一个页面读取另一个页面设置的cookie，
        必须设置cookie的路径。cookie的路径用于设置能够读取 cookie的顶级目录。将这个路径设置为网站的根目录，
        可以让所有网页都能互相读取 cookie （一般不要这样设置，防止出现冲突）

4.读取cookie
    $.cookie('cookie_key');

5.删除cookie
    $.cookie('cookie_key', null);   //通过传递null作为cookie的值即可

6.可选参数
    $.cookie('the_cookie','the_value',{
        expires:7,                          expires：（Number|Date）有效期；设置一个整数时，单位是天；也可以设置一个日期对象作为Cookie的过期日期；
        path:'/',                           path：（String）创建该Cookie的页面路径
        domain:'jquery.com',                domain：（String）创建该Cookie的页面域名；
        secure:true                         secure：（Booblean）如果设为true，那么此Cookie的传输会要求一个安全协议，例如：HTTPS；
    })　
'''


from django.contrib.sessions.models import Session
Django默认支持Session，并且默认是将Session数据存储在数据库中，即：django_session表中。
设置Session'''
    request.session['user'] = user
    request.session['is_login'] = Trut
    上面这两句语法其实相当于做了以下几件事:

           if request.COOKIES.get("sessionid"):
               random_str=request.COOKIE.get("sessionid")
               在django_seesion表中过滤session_key=random_str的记录将session_data进行update,session_key保持不变
                
           else:
                            
               1 生成一个随机字符串   23423hkjsf890234sd
               2 向django_session表中插入记录
                   session-key         session-data
                  23423hkjsf890234sd   {"susername":"egon","slogin":True}
            
               3 响应set_cookie :   {"sessionid":23423hkjsf890234sd}

以上说明了一个浏览器客户端在服务器的django_session中只会保留一条用户认证信息记录,当有新的用户用此浏览器登陆时,会对之前的session_data里面的信息进行更改.

'''
获取Session'''
    user = request.session['user']              #没有值则报错
    is_login = request.session.get('is_login')  #没有值返回None
        request.session
            1.session = request.COOKIE.get('sessionid')
            2.在django-session表中过滤session-key = session的记录
            3.取过滤记录的反序列化字典
'''
删除Session'''
    del request.session['user']
    del request.session['is_login']
'''
flush()'''
上面这条语法相当于做了以下几件事:
1 request.COOKIE.get("sessionid")   :23423hkjsf890234sd
2 在django-session表过滤session-key=23423hkjsf890234sd的记录删除
3 response.delete_cookie("sessionid")

'''
session相关方法'''
1、设置Sessions值
          request.session['session_name'] ="admin"
2、获取Sessions值
          session_name = request.session["session_name"]
3、删除Sessions值
          del request.session["session_name"]
4、flush()
     删除当前的会话数据并删除会话的Cookie。
     这用于确保前面的会话数据不可以再次被用户的浏览器访问
5、get(key, default=None)
    fav_color = request.session.get('fav_color', 'red')

6、pop(key)

    fav_color = request.session.pop('fav_color')

7、keys()

8、items()

9、setdefault()

10、用户session的随机字符串
request.session.session_key

    # 将所有Session失效日期小于当前日期的数据删除
    request.session.clear_expired()

    # 检查 用户session的随机字符串 在数据库中是否
    request.session.exists("session_key")

    # 删除当前用户的所有Session数据
    request.session.delete("session_key")

request.session.set_expiry(value)
    *如果value是个整数，session会在些秒数后失效。
    *如果value是个datatime或timedelta，session就会在这个时间后失效。
    *如果value是0, 用户关闭浏览器session就会失效。
    *如果value是None, session会依赖全局session失效策略。
'''
相关配置'''
1. 数据库Session
SESSION_ENGINE = 'django.contrib.sessions.backends.db'   # 引擎（默认）

2. 缓存Session
SESSION_ENGINE = 'django.contrib.sessions.backends.cache'  # 引擎
SESSION_CACHE_ALIAS = 'default'                            # 使用的缓存别名（默认内存缓存，也可以是memcache），此处别名依赖缓存的设置

3. 文件Session
SESSION_ENGINE = 'django.contrib.sessions.backends.file'    # 引擎
SESSION_FILE_PATH = None                                    # 缓存文件路径，如果为None，则使用tempfile模块获取一个临时地址tempfile.gettempdir() 

4. 缓存+数据库
SESSION_ENGINE = 'django.contrib.sessions.backends.cached_db'        # 引擎

5. 加密Cookie Session
SESSION_ENGINE = 'django.contrib.sessions.backends.signed_cookies'   # 引擎

其他公用设置项：
SESSION_COOKIE_NAME ＝ "sessionid"                       # Session的cookie保存在浏览器上时的key，即：sessionid＝随机字符串（默认）
SESSION_COOKIE_PATH ＝ "/"                               # Session的cookie保存的路径（默认）
SESSION_COOKIE_DOMAIN = None                             # Session的cookie保存的域名（默认）
SESSION_COOKIE_SECURE = False                            # 是否Https传输cookie（默认）
SESSION_COOKIE_HTTPONLY = True                           # 是否Session的cookie只支持http传输（默认）
SESSION_COOKIE_AGE = 1209600                             # Session的cookie失效日期（2周）（默认）
SESSION_EXPIRE_AT_BROWSER_CLOSE = False                  # 是否关闭浏览器使得Session过期（默认）
SESSION_SAVE_EVERY_REQUEST = False                       # 是否每次请求都保存Session，默认修改之后才保存（默认）
'''


