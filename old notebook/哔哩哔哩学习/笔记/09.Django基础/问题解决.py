Forbidden (403)         #post请求问题，注释掉settings中的'django.middleware.csrf.CsrfViewMiddleware',

Django3 中遇到django.core.exceptions.ImproperlyConfigured mysqlclient 1.3.13 or newer is required; you have 0.9.3.异常的解决方案
'''
安装Django3后不想折腾mysqlclient那堆库文件，直接装了pymysql替代mysqlclient。还是老办法，__init__.py 中patch一下:
    import pymysql
    pymysql.install_as_MySQLdb()

启动项目出现以下异常:
    raise ImproperlyConfigured('mysqlclient 1.3.13 or newer is required; you have %s.' % Database.__version__)
    django.core.exceptions.ImproperlyConfigured: mysqlclient 1.3.13 or newer is required; you have 0.9.3.

看来是Django3对mysqlclient的要求提高了: 1.3.13. 但pymysql的版本没有跟上。
看了下tracelog指向的异常抛出处的代码, 发现如下代码片段:
    if version < (1, 3, 13):
        raise ImproperlyConfigured('mysqlclient 1.3.13 or newer is required; you have %s.' % Database.__version__)
果然是有个版本判断并raise了异常，而且校验的是Database库的version_info属性。
那pymysql中的version_onfo属性是怎么返回的呢？找到pymysql源码，发现如下片段:
    version_info = (1, 3, 13, "final", 0)
实际上pymysql版本号是 0.9.3，却明目张胆篡改version_info欺骗Django。
这样一来就简单了，patch一下这个属性就行了嘛， 修改settings.py同级目录下的__init__.py，多插入一行代码:
    import pymysql
    pymysql.version_info = (1, 3, 13, "final", 0)
    pymysql.install_as_MySQLdb()
保存后启动项目成功。
该方案只是个兼容方案，不确定Django3是否依赖mysqlclient的新特性，因此生产环境还是建议部署mysqlclient，而非pymysql。
- mysqlclient与pymysql区别是什么？
    - mysqlclient是mysql官方提供的Python SDK，安装时依赖mysql-dev与python-dev相关的库函数完成当前系统平台的编译，因为使用大量C库，
      性能会比pymysql优秀得多。SDK更新和维护也有官方保障。
    - pymysql是第三方在MySQL通信协议上实现的SDK，所有与数据库的交互都是通过MySQL独有的通信协议完成，性能上会比mysqlclient有劣势。
      且版本更新可能滞后，且维护不一定到位。但好处就是pip install安装很容易，不像mysqlclient先要把编译依赖的C库装好，在一些建档任务和开发环境快速搭建上有优势。


'''
Pycharm连接数据库出现：RuntimeError: cryptography is required for sha256_password or caching_sha2_password
'''
安装cryptography

pip install cryptography
'''