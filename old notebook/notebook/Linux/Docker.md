# Docker

- 一处编译，多处运行
- 对系统消耗小
- 可快速启动
- 维护简单
- 拓展容易

## 底层实现原理

- namespace


- cgroup


## 下载安装

```shell
# 安装
$ cd /etc/yum.repos.d
$ wget https://mirrors.aliyun.com/docker-ce/linux/centos/docker-ce.repo
$ yum install docker-ce

# 配置加速
$ systemctl start docker
$ vim /etc/docker/daemon.json
{
    "registry-mirrors":[
        "https://1nj0zren.mirror.aliyuncs.com",
        "https://vx4zvv7x.mirror.aliyuncs.com",
        "http://f1361db2.m.daocloud.io",
        "https://registry.docker-cn.com",
        "https://docker.mirrors.ustc.edu.cn"
    ]   
}

$ systemctl daemon-reload
$ systemctl restart docker
```

## 组成

- 镜像
- 容器
- 仓库

## 命令

```python
$ docker run hello-world
# 先查看本地是否有镜像，如果没有就去下载再启动
```

- 搜索镜像

  ```shell
  $ docker search mysql
  名字						描述信息			点赞数				  Docker官方提供		
  NAME                     DESCRIPTION        STARS               OFFICIAL            AUTOMATED
  mysql                    MySQL is a…   		10129               [OK]                
  mariadb                  MariaDB is …   	3724                [OK]                
  mysql/mysql-server       Optimized My…   	740                                     [OK]
  percona                  Percona S…   		511                 [OK]                
  ```

- 下载镜像

  ```shell
  $ docker pull centos
  $ docker pull mariadb:10.4.16    
  # 采用分层技术，如果下载的包底层采用了相同技术，就不重复下载
  ```

- 查看本地镜像

  ```shell
  $ docker images
  $ docker image ls			# 和上面一样
  $ docker images -q 			# 只显示镜像ID
  $ docker images mariadb		# 只显示mariadb
  ```

- 删除

  ```shell
  $ docker rmi mariadb:10.4.16 			# 根据名字删除
  $ docker rmi 14b488eb2d72				# 根据id删除
  $ docker rmi -f  `docker images -q`  	# 删除所有
  ```

- 创建容器

  ```shell
  $ docker run centos
  $ docker run centos echo "xxx"  # 容器执行命令 加-d就后台输出，可通过docker logs 加返回id前3位查看
  $ docker run -ti centos /bin/bash 		# 进入容器 -t创建虚拟终端 -i将容器的标准输入保持
  $ docker run -ti --name mylinux centos /bin/bash	# 设置名字，删除的时候就可以通过名字删除(docker rm mylinux)
  $ docker run -d nginx							# -d 后台运行
  $ docker run --name nginx -dP nginx				# -P将容器端口暴露在宿主上
  $ docker run --name nginx -d -p 80:80 nginx     # -p 宿主机端口:容器端口  将容器的80端口映射到宿主机上，
  $ docker run --name nginx -d -p 80:80 -v ./index.html:/usr/share/nginx/html/index.html nginx #-v 宿主机指定目录文件挂载到到容器中 
  ```

- 启动容器

  ```shell
  $ docker start nginx
  $ docker start -i centos 	# -i将容器的标准输入保持
  ```

- 关闭容器

  ```shell
  $ docker stop nginx
  ```

- 进入容器

  ```shell
  $ docker exec -ti centos \bin\bash
  ```

- 查看容器运行状态

  ```shell
  $ docker stats nginx
  ```

- 退出容器

  ```shell
  $ exit		# 或者CTRL+D
  ```

- 查看容器

  ```shell
  $ docker ps -a		# 查看所有
  $ docker ps -aq 	# 只查看容器
  ```

- 提交容器

  ```shell
  # 进入容器后,在另一个终端docker ps -a获取容器执行的id(也就是下面的id)，mycentos为名字，latest为tag，不写就是None
  # commit命令返回值为字符串
  $ docker commit -m "新建xxx目录" ae78fa1c78e7 mycentos:latest
  ```

- 保存镜像

  ```shell
  $ docker save -o mycentos.tar.gz mycentos
  $ docker save mycentos > mycentos.tar.gz
  ```

- 删除容器

  ```shell
  $ docker rm  b82 657 854 e30
  $ docker rm -f b82  # 删除正在运行的容器(b82为docker ps -a命令的id前三位)
  ```

- 导入镜像

  ```shell
  $ docker load -i mycentos.tar.gz
  ```

- 查看端口映射关系

  ```
  $ docker port nginx				# port加容器id或者容器名
  ```

- 查看日志

  ```shell
  $ docker logs as5			# 查看日志
  $ docker logs -f as5		# 实时输出
  ```

- 移除所有stop的容器

  ```shell
  $ docker container prune
  ```

- 远程仓库

  ```shell
  $ docker login    						# 登录
  $ docker tag ng:v1 m5xhsy/nginx:v1		# 改名
  $ docker push m5xhsy/nginx:v1			# 上传
  $ docker pull m5xhsy/nginx:v1			# 下载
  $ docker logout							# 退出登录
  ```

- 本地仓库

  ```shell
  $ docker run -p 5000:5000 -d -v /opt/data/registry:/var/lib/registry registry		# 开启本地仓库
  $ docker tag ng:v1 127.0.0.1:5000/nginx:v1 	# 改名
  $ docker push 127.0.0.1:5000/nginx:v1	# 上传
  $ curl 127.0.0.1:5000/v2/_catalog     # 校验{"repositories":["nginx"]}
  $ docker pull 127.0.0.1:5000/nginx   # 重新下载下来
  
  # 如果其他机器要访问，需要该地址(本地是https协议,需要配置)
  $ vim /etc/docker/daemon.json
  {
  	"insecure-registries":[
  		"192.168.239.128:5000"
  	]
  }
  $ systemctl daemon-reload
  $ systemctl restart docker
  ```

  Docker CE  社区版本

  Docker EE  商业版本

## dockerfile

```
FROM mycentos  								# 指定基础镜像
COPY epel.repo /etc/yum.repos.d/			# 复制文件
Add  epel.repo /etc/yum.repos.d/			# 复制文件（如果是压缩包就解压）
RUN yum install -y nginx 					# 运行命令
RUN mkdir -p /data/html				
VOLUME # 指定容器目录
RUN touch /data/html/index.html
RUN echo "mynginx" >> /data/html/index.html
COPY nginx.conf /etc/nginx/nginx.conf
ENV username=m5xhsy							# 设置变量
ENV password=Ass078678				
WORKDIR /data/html							# 设置工作目录(exec进入后直接进入这个目录)
EXPOSE 80									# 设置端口
CMD /bin/bash -c systemctl start nginx		# CMD只能有一个(如果多个按最后一个计算)，RUN可以有多个
LABEL # 描述信息
USER	# 执行RUN和CMD的用户

$ docker build -t mycentos:v1 -f centos .
$ docker run mycentos:v1
```

## dockers-compose

**docker编排工具**

### 安装

```shell
$ pip3 install docker-compose -i https://mirrors.aliyun.com/pypi/simple
$ curl -L https://raw.githubusercontent.com/docker/compose/1.8.0/cintrib/completion/bash/docker-compose > /etc/bash_completion.d/docker-compose
```

```shell
$ docker-compose up    # 默认文件docker-compose.yml
$ docker-compose up -d	# 
$ docker-compose build
$ docker-compose -f xxx.yml build
```

Dockerfile

```
FROM python:3.8.6-alpine
RUN mkdir /data
COPY app.py /data
WORKDIR /data
RUN pip3 install flask redis -i https://mirrors.aliyun.com/pypi/simple
CMD ["python","app.py"]
```

app.py

```
from flask import Flask,request,jsonify,send_file
from redis import Redis

app = Flask(__name__)
redis = Redis(host="redis",port=6379)		# 这里host的redis是yml文件中redis服务名称

@app.route("/")
def index():
    count = redis.incr("count")
    return f"当前页面被访问了{count}次"
    

@app.route("/home")
def home():
    return "这是home页面"

@app.route("/iu")
def iu():
    return send_file("./iu.jpg")

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=4000)
```

docker-compose.yml

```
version: "3"
services:
  web:
    build: .
    ports:
    - "4000:4000"
  redis:
    image: redis:alpine
```

[参考官网](https://docs.docker.com/compose/reference/build/)