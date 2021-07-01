http协议:应用层协议
    1.基于TCP协议
    2.基于请求响应
    3.短链接
    4.无状态保存(所有引入cookie和session技术)



1.基于请求响应
2.基于TCP/IP
    http协议是基于TCP/IP协议之上的应用层协议。
3.请求协议格式
    - 请求首行
        请求方式         GET POST
        URI            URL的路径之后的内容         URL:  协议://域名(IP)+端口(80)/路径?参数(a=1&b=2)
        协议/版本号      HTTP/1.1
    - 请求头   key: value
        Host:hackr.jp
        Connection:keep-alive
        Conntent-Type:application/x-www-from-urlencoded
        Content-Length:16
        userAgent:win Chorome=
    - 请求体
        name-ueno&age=37
4.响应协议格式
    - 响应首行
        协议/版本号
        状态码
        状态码译文
    - 响应头
        Comtent-Type:text/html
    - 响应体
        <h1>xxx</h1>


响应状态码
    1开头: 请求中
    200:    请求成功
    3开头:    重定向
    4开头:    文件路径找不到
    5开头:    服务器错误(语法错误或者服务器部署错误)



MVC:
    M   mdoel       数据库相关
    C   controller  控制器(url的分发与视图函数的逻辑处理)
    V   View        视图(html文件)

MTV
    M   mdoel       数据库
    T   templates   存放HTML模板文件
    V   View        视图函数(逻辑处理)


http_method_names = ['get', 'post', 'put', 'patch', 'delete', 'head', 'options', 'trace']
'''
form表单中的enctype:
    application/x-www-form-urlencoded   使用&符号连接多个键值对,键值对使用等号拼接
    multipart/form-data                 上传文件图片使用该方式
    text/plain                          空格转换为+号
'''

'''
Accept:可接受响应内容类型
Accept-Encoding:对请求数据进行编码的类型
Accept-Language:语言
Cache-Control:
Connection:请求连接方式
Content-Length:内容长度(字节)
Content-Type:请求数据编码协议，只有POST，DELETE等请求方式有该部分内容()重点记忆
Cookie:服务端设置的cookies
Host: 127.0.0.1:8000
Origin: http://127.0.0.1:8000
Referer: http://127.0.0.1:8000/app/login/
Sec-Fetch-Dest:
Sec-Fetch-Mode:
Sec-Fetch-Site:
Sec-Fetch-User: 
Upgrade-Insecure-Requests: 1
User-Agent:客户端信息