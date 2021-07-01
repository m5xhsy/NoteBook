- 浏览器

- wsgi.py
    1.封装socket
    2.按http协议解包:request

- 中间件

- url控制器

- 视图函数



from django.utils.deprecation import MiddlewareMixin
class SecurityMiddleware(MiddlewareMixin):
    def process_request(self, request):

        return None         #跳过中间件

    def process_response(self, request, response):

        return response

    def process_view(self, request, callback, callback_args, callback_kwargs):      #很少用
        print("md2 process_view...")
        #提前执行视图函数
        ret = cllback(request,callback_args)
        return ret

    def process_exception(self,request,exception):      #捕获错误

        print("md1 process_exception...")

流程'''
url请求
中间件 process_request
路由控制
中间件 process_view
视图函数
中间件 process_exception
中间件 process_response
'''

中间件应用'''
1、做IP访问频率限制
    某些IP访问服务器的频率过高，进行拦截，比如限制每分钟不能超过20次。

2、URL访问过滤
    如果用户访问的是login视图（放过） 
    if request.path in ['/login/']
        return None
    如果访问其他视图，需要检测是不是有session认证，已经有了放行，没有返回login，这样就省得在多个视图函数上写装饰器了！
'''