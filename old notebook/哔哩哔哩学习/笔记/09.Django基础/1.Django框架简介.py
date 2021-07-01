1.下载Django            pip3 install django==2.1.1            (版本号,可写可不写)
2.将下载的Django目录添加环境变量
3.创建Django项目        diango-admin startproject 项目名称
4.进入文件夹            cd 应用名
5.创建应用              python manage.py startapp 应用名   djange-admin startapp 应用名
6.启动项目              python manage.py runserver IP:PORT      PORT默认8000


Django项目
    --manage.py
    --项目名称
        --asgi.py
        --settings.py       配置文件信息
        --urls.py           路径与视图函数的映射
        --wsgi.py           封装的socket
    --应用1
        --models            存放与该app相关的表结构
        --view              存放该app相关的视图函数


