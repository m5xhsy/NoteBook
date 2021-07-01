# Nginx

## 安装

1. 安装依赖

   ```shell
   $ yum -y install make zlib zlib-devel gcc-c++ libtool  openssl openssl-devel
   ```

2. 安装PCRE(PCRE 作用是让 Nginx 支持 Rewrite 功能)

   - 下载PCRE安装包

     ```shell
     $ wget https://udomain.dl.sourceforge.net/project/pcre/pcre/8.44/pcre-8.44.tar.gz
     ```

   - 解压

     ```shell
     $ tar -zxf pcre-8.44.tar.gz
     ```

   - 进入文件夹编译安装

     ```shell
     $ cd pcre-8.44 && ./configure
     $ make && make install
     ```

   - 查看pcre版本

     ```shell
     $ pcre-config --version
     ```

3. 安装Nginx

   - 下载Nginx

     ```shell
     $ wget https://nginx.org/download/nginx-1.9.9.tar.gz
     ```

   - 解压

     ```shell
     $ ter -zxf nginx-1.9.9.tar.gz
     ```

   - 进入文件夹编译安装

     ```shell
     $ cd nginx-1.9.9 && ./configure --prefix=/opt/nginx
     $ make && make install
     ```

   - 查看版本

     ```shell
     $ /opt/nginx/sbin/nginx -v				# 可添加环境变量
     ```

4. 安装过程错误解决

   - 错误一: 警告被当成错误

     ```shell
     src/core/ngx_murmurhash.c: 在函数‘ngx_murmur_hash2’中:
     src/core/ngx_murmurhash.c:37:11: 错误：this statement may fall through [-Werror=implicit-fallthrough=]
              h ^= data[2] << 16;
              ~~^~~~~~~~~~~~~~~~
     src/core/ngx_murmurhash.c:38:5: 附注：here
          case 2:
          ^~~~
     src/core/ngx_murmurhash.c:39:11: 错误：this statement may fall through [-Werror=implicit-fallthrough=]
              h ^= data[1] << 8;
              ~~^~~~~~~~~~~~~~~
     src/core/ngx_murmurhash.c:40:5: 附注：here
          case 1:
          ^~~~
     cc1：所有的警告都被当作是错误
     ```

     解决方法：

     ```shell
     $ vim /opt/nginx/objs/Makefile
     将 CFLAGS =  -pipe  -O -W -Wall -Wpointer-arith -Wno-unused-parameter -Werror -g　中的 -Werror去掉
     -Werror 指gcc将所有的警告当成错误进行处理
     ```

   - 错误二

     ```shell
     src/os/unix/ngx_user.c: 在函数‘ngx_libc_crypt’中:
     src/os/unix/ngx_user.c:36:7: 错误：‘struct crypt_data’没有名为‘current_salt’的成员
          cd.current_salt[0] = ~salt[0];
            ^
     make[1]: *** [objs/Makefile:732：objs/src/os/unix/ngx_user.o] 错误 1
     make[1]: 离开目录“/root/nginx-1.9.8”
     make: *** [Makefile:8：build] 错误 2
     ```

     解决方法：

     ```shell
     $ vim /opt/nginx/src/os/unix/ngx_user.c
     将文件中 cd.current_salt[0] = ~salt[0]; 注释掉
     再将错误一解决办法操作一遍
     ```

## 命令

```
./nginx #启动
./nginx -s stop #关闭
./nginx -s reload 
```

## Nginx目录

1. html 网页根目录

   > 网页存放目录，可以改名，需要在nginx中配置

2. conf 配置

   > 存放配置文件

3. logs 日志

   > 存放日志文件

4. sbin 启动

   > 存放启动文件nginx，可用将此目录添加环境变量

## Nginx配置

```shell
########### 每个指令必须有分号结束。#################
#user administrator administrators;  #配置用户或者组，默认为nobody nobody。
#worker_processes 2;  #允许生成的进程数，默认为1
#pid /nginx/pid/nginx.pid;   #指定nginx进程运行文件存放地址
error_log log/error.log debug;  #制定日志路径，级别。这个设置可以放入全局块，http块，server块，级别以此为：debug|info|notice|warn|error|crit|alert|emerg
events {
    accept_mutex on;   #设置网路连接序列化，防止惊群现象发生，默认为on
    multi_accept on;  #设置一个进程是否同时接受多个网络连接，默认为off
    #use epoll;      #事件驱动模型，select|poll|kqueue|epoll|resig|/dev/poll|eventport
    worker_connections  1024;    #最大连接数，默认为512
}
http {
    include       mime.types;   #文件扩展名与文件类型映射表
    default_type  application/octet-stream; #默认文件类型，默认为text/plain
    #access_log off; #取消服务日志    
    log_format myFormat '$remote_addr–$remote_user [$time_local] $request $status $body_bytes_sent $http_referer $http_user_agent $http_x_forwarded_for'; #自定义格式
    access_log log/access.log myFormat;  #combined为日志格式的默认值
    sendfile on;   #允许sendfile方式传输文件，默认为off，可以在http块，server块，location块。
    sendfile_max_chunk 100k;  #每个进程每次调用传输数量不能大于设定的值，默认为0，即不设上限。
    keepalive_timeout 65;  #连接超时时间，默认为75s，可以在http，server，location块。

    upstream mysvr {   
      server 127.0.0.1:7878;
      server 192.168.10.121:3333 backup;  #热备
    }
    error_page 404 https://www.baidu.com; #错误页
    server {
        keepalive_requests 120; #单连接请求上限次数。
        listen       4545;   #监听端口
        server_name  127.0.0.1;   #监听地址       
        location  ~*^.+$ {       #请求的url过滤，正则匹配，~为区分大小写，~*为不区分大小写。
           #root path;  #根目录
           #index vv.txt;  #设置默认页
           proxy_pass  http://mysvr;  #请求转向mysvr 定义的服务器列表
           deny 127.0.0.1;  #拒绝的ip
           allow 172.18.5.54; #允许的ip           
        } 
    }
}


```

### nginx启动uwsgi连接配置

```shell
方式一: 
uwsgi.ini 里面指定为http = 127.0.0.1:8000
nginx的配置文件里面需要写
proxy_pass http://127.0.0.1:8000;
方式二:
uwsgi.ini里面指定为socket = 127.0.0.1:8000
nginx的配置文件需要写 
include /etc/nginx/uwsgi.conf;
uwsgi_pass 127.0.0.0:8000;
方式三:
uwsgi.ini里面指定为socket = /data/mysite/mysite.socket
nginx的配置文件需要写 
include /etc/nginx/uwsgi.conf;
uwsgi_pass unix:/data/mysite/mysite.socket;
```



## Nginx代理

> **正向代理的对象——> 客户端**
>
> 客户端  <——>  代理  ——>  服务端
>
> **反向代理的对象——> 服务器**
>
> 客户端  ——>  代理  <——>  服务端

### 配置

1. 准备2个服务器,一个过web服务器，一个做代理服务器

2. 开开启web服务器

3. 代理服务器配置

   ```shell
   $ vim /opt/nginx/conf/nginx.conf
   server {
   	listen 80;
       server_name localhost;
       location / {
       	proxy_pass http://192.168.13.79;	# web服务器地址
       }
   }
   ```

4. 访问代理服务器地址测试

## Nginx负载均衡

> Nginx要实现负载均衡需要用到proxy_pass代理模块配置
>
> Nginx负载均衡与Nginx代理不同地方在于Nginx代理仅代理一台服务器，而Nginx负载均衡则是将客户端请求代理转发至一组upstream虚拟服务池，Nginx可以配置代理多台服务器，当一台服务器宕机之后，仍能保持系统可用。

### 配置

1. 3台nginx服务器，台作为web服务器，一台作为负载均衡器

2. 负载均衡器配置
   
   ```shell
   html {
   	upstream m5xhsy {
           server 192.168.239.131;
           server 192.168.239.132;
       }
       server {
       	location / {
       		proxy_pass http://m5xhsy;
       	}
       }
   }
   ```
   
3. 启动三台服务器

4. 测试

### 分配模式

- 轮询

  轮询即Round Robin，根据Nginx配置文件中的顺序，依次把客户端的Web请求分发到不同的后端服务器。

  ```shell
  upstream m5xhsy {
  	server 192.168.239.131;
  	server 192.168.239.132;
  }
  ```

- 最少连接

  Web请求会被转发到连接数最少的服务器上。

  ```shell
  upstream m5xhsy {
  	least_conn; 
  	server 192.168.239.131;
  	server 192.168.239.132;
  }
  ```

- IP地址哈希

  前述的两种负载均衡方案中，同一客户端连续的Web请求可能会被分发到不同的后端服务器进行处理，因此如果涉及到会话Session，那么会话会比较复杂。常见的是基于数据库的会话持久化。要克服上面的难题，可以使用基于IP地址哈希的负载均衡方案。这样的话，同一客户端连续的Web请求都会被分发到同一服务器进行处理。

  ```shell
  upstream m5xhsy {
  	ip_hash;
  	server 192.168.239.131;
  	server 192.168.239.132;
  }
  ```

- 基于权重的负载均衡

  基于权重的负载均衡即Weighted Load Balancing，这种方式下，我们可以配置Nginx把请求更多地分发到高配置的后端服务器上，把相对较少的请求分发到低配服务器。

  ```shell
  upstream m5xhsy {
  		ip_hash;
          server 192.168.239.131 weight=10;
  		server 192.168.239.132 weight=1;
  }
  # 基于权重的负载均衡和基于IP地址哈希的负载均衡可以组合在一起使用
  ```

- backup

  在非backup机器繁忙或者宕机时，请求backup机器，因此机器默认压力最小

  ```shell
  upstream django {
         server 192.168.239.131 weight=5;
         server 192.168.239.132;
         server 192.168.239.133 backup;
  }
  ```

  

## 补充

1. vue直接访问子路由404解决

   ```shell
   location / {
               root   /opt/vue/dist;
               index  index.html;
               try_files $uri $uri/ /index.html;			# 添加这句
   }
   ```

2. uwsgi启动django以及静态文件处理

   ```shell
   server {
           listen       8000;
           server_name  192.168.239.128;
           location / {
               include /opt/nginx/conf/uwsgi_params;	# 导入uwsgi配置文件
               uwsgi_pass 192.168.239.128:9000;		# uwsgi启动的端口
   
           }
           location /static/ {
               alias /opt/vue/dist/static/;		# 将所有static请求定位到static文件夹
           }
       }
   ```

   ​				

