# uwsgi

## 安装

```shell
$ yum groupinstall "Development tools"
$ yum install zlib-devel bzip2-devel pcre-devel openssl-devel ncurses-devel sqlite-devel readline-devel tk-devel
$ pip install uwsgi
```

## uwsgi启动django

```shell
$ uwsgi --ini /opt/TestProject/uwsgi.ini							# 配置文件命令运行
$ uwsgi --http 0.0.0.0:8000 --module TestProject.wsgi				# shell命令运行 

chdir=/opt/TestProject		# wsgi文件路径，在django项目底下
module=TestProject.wsgi 	# django项目下wsgi文件路径，也可以这样写 wsgi-file=TestProject/wsgi.py
home=/root/.Envs/venvLuffy  # 指定解释器目录
processes=5					# 开启进程数
socket=0.0.0.0:8000			# uwsgi启动一个socket连接(django+nginx时用)
# http=0.0.0.0:9000			# 启动一个http连接(不使用nginx时使用)
threads=2					# 线程数
master=True
pidfile=uwsgi.pid
daemonize=yes			# 后台运行
py-autireload=1			# 文件修改后uwsgi自动重启

# 其他配置查看官网
```

