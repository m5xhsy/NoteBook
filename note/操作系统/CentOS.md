# CentOS

## 用户登录

- root用户

  - 是一个特殊的管理账号，也可以成为超级管理员

  - root用户对系统有完全控制权限
  - 对系统的损害会无线大
  - 工作中没有必要的化，尽量不要使用root

- 普通用户

  - 权限有限
  - 对系统损害会小

## 用户

- 超级管理员用户 root 0
- 普通用户
  - 系统用户：用来启动系统的一些服务和进程的用户，不可以登录 1-999(centos7),1-499(centos6)
  - 可登录用户：能登录系统的用户 1000-65535(centos7),500-65535(centos6)

## 终端

分类

- 设备终端
- 物理终端
- 虚拟终端    
  - CTRL+ALT+[1~6]		
  - /dev/tty#

- 图形终端    
  - /dev/tt7
- 串行终端
- 伪终端    
  - 通过ssh远程连接

## 交互式接口

启动终端后，在终端设备上附加一个应用程序

- GUI

- CLI command line
  - cmd
  - PowerShell
  - sh
  - bash  (linux和mac默认程序)
  - zsh
  - csh
  - tcsh

## bash

bash是linux系统的用户界面，提供了用户和操作系统之间的交互，他接收用户的输入，让它送给操作系统执行

查看终端

```shell
$ tty
```

查看ip

```shell
$ ip addr
$ ip a
```

显示系统当前使用的shell

```shell
$ echo $SHELL
```

查看当前系统可以使用shell

```shell
$ cat /etc/shell
```

切换shell

```shell
$ chsh -s /bin/csh
```

快速终止当前连接

```
ctrl+z
```

修改ssh连接慢

```shell 
$ grep -i 'dns' /etc/ssh/sshd_config
$ echo "UseDNS no" >> /etc/ssh/sshd_config
$ systemctl restart sshd
```

显示命令提示符

```` 
[root@localhost ~]# echo $PS1
[\u@\h \W]\$

\u 代表当前登录用户
\h 和代表当前主机名
\w 完整的工作目录名称。家目录会以 ~代替 
\W 利用basename取得工作目录名称，所以只会列出最后一个目录 
````

修改命令提示符

```shell
$ PS1="\[\e[0;31m\][\u@\h \W]\\$\[\e[0m\]"
$ echo 'PS1="\[\e[0;31m\][\u@\h \W]\\$\[\e[0m\]"' >> /etc/profile
0表示默认字体
1表示加粗
4表示在字体加下划线
5闪烁
7代表突出显示
31-37以上表示字体颜色
40-47以上表示背景颜色
```

## DNS解析

> 解析时会先找本地/etc/hosts中查找
> 比如设置192.168.21.1 www.baidu.com
> 则在ping www.baidu.com时会有限使用本地的

## Lnux命令格式：

- unix格式: -h    -e
- BSD格式：a    x      u
- GNU长格式：--help

## 快捷键

- Ctrl + l    清屏
- Ctrl + o    执行当前命令并显示
- Ctrl + s    锁定屏幕
- Ctrl + q    解锁
- Ctrl + c    终止命令
- Ctrl + z    挂起，后台不执行
- Ctrl + a    关标移动到行首，相当于home键
- Ctrl + e    关标移动到行尾，相当于end键
- Ctrl + x   关标在开头和当前位置跳转
- ctrl + k    删除关标后的文字
- ctrl + u    删除关标前面的
- ctrl + r    搜索历史命令
- ctrl + g   取消搜索
- Alt  + r    删除整行
- tab
  - 命令补全
    - 内部命令
    - 外部命令
      1. 根据环境变量定义的路径，从前往后自动匹配第一个查找到的内容
      2. 如果用户给的命令只有唯一一个匹配，则自动补全
      3. 如果有多个匹配，则需要再按一次将所有匹配结果显示出来
  - 目录补全
    - 把用户指定的字符作为文件的开头匹配，多个文件则和命令补全一样匹配

## 软件安装

### rpm

- 得自己解决依赖关系，用的比较少

  ```shell
  $ rpm -q redis 					# 查询指定的包是否安装
  	-qa							# 查询安装的所有包
  	-qf /etc/ssh/ssd_config		# 查询文件由哪个包安装
  	-qc redis					# 查询这个包生成的配置文件
      -qd	redis					# 查询这个包生成了哪些文档
      -qi	redis					# 查询这个包详细信息
      -ql redis					# 查询指定包生成的文件	
      
  其他安装卸载方法查询百度
  ```

### yum

- 会自动解决依赖关系

- 配置文件存放在/etc/yum.repos.d

  ```shell
  $ yum repolist 		# 查看仓库
  ```

  ```shell
  #######/etc/yum.repos.d/CentOS-Base.repo
  [centosplus]  # 名称
  name=CentOS-$releasever - Plus - mirrors.aliyun.com	# 描述
  failovermethod=priority		# 使用顺序	顺序(priority)随机(roundrobin)
  baseurl=https://mirrors.aliyun.com/centos/$releasever/centosplus/$basearch/os/
          http://mirrors.aliyuncs.com/centos/$releasever/centosplus/$basearch/os/
          http://mirrors.cloud.aliyuncs.com/centos/$releasever/centosplus/$basearch/os/
  gpgcheck=1	# {0|1} 是否启用，1为启用，0为不启用
  enabled=0	# {0|1} 是否校验，1为校验，0为不校验
  gpgkey=https://mirrors.aliyun.com/centos/RPM-GPG-KEY-CentOS-Official	# 使用这个地址校验
  
  $releasever发行版本
  $basearch架构
  ```

- 命令

  ```shell
  $ yum repolist				# 查看仓库
  $ yum list					# 查看所有的包 已安装显示@anaconda 未安装显示base 可更新显示updates
  $ yum install redis			# 安装包
  $ yum reinstall redis		# 重新安装包
  $ yum update				# 更新所有可更新的包
  $ yum update redis			# 更新单个包
  $ yum downgrade redis		# 包降级(用的比较少)
  $ yum check-update			# 检查包是否可以更新(可以检查单个包，后面写包名)
  $ yum remove redis			# 卸载包
  $ yum info redis			# 显示包详细信息
  $ yum clean all				# 清除元数据信息 /var/cache/yum
  $ yum makecache				# 重新构建元数据信息
  $ yum search redis			# 搜索软件包名称和描述信息包含redis的
  $ yum provides redis		# 搜索redis命令由哪个包提供的
  
  -y				# 自动确认
  -q 				# 静默模式，不显示
  ```

- 软件包组

  ```shell
  $ yum grouplist							# 查看包组
  $ yum groupinstall "Development Tools"	# 安装包组(有空格加引号)
  $ yum groupinfo "Development Tools"		# 查看包组的组成信息
  $ yum groupupdate "Development Tools"	# 更新包组
  $ yum groupremove "Development Tools"	# 卸载包组
  ```

### 源码安装

```shell
设置环境变量
vim /etc/profile.d/python.sh
PATH=/opt/python36/bin:$PATH
source /etc/profile.d/python.sh


下载 wget
解压
切换目录
查看帮助文档  README INSTALL 文件
安装所需文件
编译
构建安装重新 make
安装程序 make install 
配置环境变量
```

### 包的命名规范

```shell
名字-版本(大版本.小版本.修订版)-打包版本-可用系统.架构,rpm
架构:x86_64、x86、i386、i486、ppc、以及noarch没有架构(通用)
```

## 环境变量

```shell
vim /etc/profile

PATH=$PATH:/opt/ruby/bin
source /etc/profile
```

## 命令

### 命令格式

command [options...] [args...]

- command 命令本身

- option 启动或者关闭命令里面的某些功能

  - 长选项  --help   --color

  - 短选项  -l    -a    可合并  -la

- args 命令作用体，一般情况下是目录文件或用户名等

注意：

- 短选项是可以合并的
- 空格隔开
- ctrl+c结束命令
- 在同一行执行多个目录用分号隔开
- 多行执行同一个命令用 \ 连接

### 帮助信息

- 内部命令

  ```shell
  $ type echo    	# 判断命令是内部命令还是外部命令
  $ man bash     	# 查看所有内部命令帮助信息
  $ help echo  	# 查看echo命令的帮助信息
  ```

- 外部命令

  ```shell
  $ python -h 	# 或者--help
  $ man python  	# 查看外部命令帮助信息,比较详细
  ```

### 别名

```shell
$ alias  										# 查看当前所有别名
$ alias cdetc='cd /etc'   						# 自定义别名
$ unalias cdetc									# 取消别名
$ echo "alias cdetc='cd /etc'" >> /etc/bashrc	# 对所有用户有效
$ echo "alias cdetc='cd /etc'" >> ~/.bashrc		# 对当前用户有效(修改完后source一下)
$ "ls"								    		# 或者\ls 执行原来的命令
```

### 查看which命令目录

```shell
$ which ls		# 查找命令在什么地方
```

### man帮助文章

```shell
翻屏 空格
翻行 回车
推出 Q
$ whatis passwd		# 查看passwd命令在第几章节出现
$ man 5 passwd  	# 查看第五章节passwd命令
```

### scp命令

```shell
 $ scp 192.168.239.128:/etc/passwd /mnt/g/passwd   # 在192.168.239.128中复制/etc/passwd文件
 $ scp ./passwd.json 192.168.239.128:/home/orz/passwd.json # 本地文件上传到192.168.239.128的用户目录下
 # 传目录加-r
```

### 引号 变量引用

```shell
# 引号
$ name="m5xhsy"
$ echo "$name"
# 反引号  
$ echo "abc `tty`"			#打印结果 abc /dev/pts/2   相当于执行
$ echo "abc $(tty)"			#打印结果和上面一样
```

### 命令历史

- 可以使用箭头查找之前执行过的命令

1. 查看历史命令存放目录

   ```shell
   $ cat ~/.bash_history	# 当前窗口退出会保持进来
   ```

2. 查看历史命令

   ```shell
   $ history
   ```

3. 执行历史命令命令

   ```shell
   $ !!	# 执行上一条，相当于ctrl+p
   $ !-1	# 执行第-1条命令
   $ ! 102 # 执行第102条命令
   $ !echo # 执行最近匹配到的echo
   ```

4. 调用上一条命令的值：按esc + .

5. 搜索命令：ctrl + r  

6. 取消搜索：ctrl + g

7. 显示最后10条命令：history 10

### 命令展开

```shell
$ echo file{1,2,3}		# 打印file1到file3
$ echo file{0..20}		# 打印file0到file20
$ echo file{0..20..2}	# 打印file0到file20，步长为2
```

```shell
$ seq 1 10				# 竖着打印1到10
$ seq 1 2 10			# 竖着打印1到10，步长为2
```

```shell
$ touch file{1..10}		#创建文件file1到file10
```

### init命令

> init进程是所有Linux进程的父进程，他的进程号为1，是Linux内核引导运行的，是系统的第一个进程
>
> init命令是Linux下的进程初始化工具

```shell
$ init 0		# 停机（千万不能把initdefault 设置为0 ）
$ init 1		# 单用户模式
$ init 2 		# 多用户，没有 NFS 不联网
$ init 3  		# 就是切换到多用户-命令行模式
$ init 5  		# 就是切换到图形化界面
$ init 6  		# 就是重启（千万不要把initdefault 设置为6 ）
```



### echo 回显

```shell
$ echo -e "asd\nasd"			# 换行 \n
$ echo -e "\a"  				# 提示声音 \a
$ echo "xxx" >> /home/xxx.conf	# 将数据追加进文件
$ echo $?						# 判断上一条命令执行结果 0表示执行成功
```

### 查看用户登录信息

```shell
$ whoami		# 当前登录用户
$ who am i		# 详细信息
$ w				# 显示所有用户并显示用户执行的命令
```

### data 时间

```shell
$ date  								# 查看当前时间
$ date 111323102018  					# 2018年11月13号23点10分 修改时间
$ ntpdate time.windows.com				# 同步时间服务器
$ date +%m								# 查看月份，其他字段查看帮助文档
$ date +%Y/%m/%d						# 自定义显示
$ timedatectl							# 显示时区
$ timedatectl set-timezone Asia/Taipei 	# 设置时区
$ cal 									# 当月日历
$ cal -y								# 一年日历
$ cal 2018								# 2018年日历
```

### find 查找

find是Linux里面一个实时查找工具，通过定制路径完成文件查找

find [options]...[查找路径] [查找条件 ] [ 处理动作]

- 查找路径：查找的位置，默认是文件夹

- 查找条件：制定查找的标准，文件名、大小、类型、日期等等

  ```shell
  $ find -name a								# 按文件名查找
  $ find -maxdepth 2 -name a 					# 制定最大搜索层级，指定目录为第一层
  $ find -mindepth 3 -name a	 				# 制定最小搜索层级(包括3)
  $ find /etc -name *.conf 					# 搜索.conf结尾的文件
  $ find -regex "./a"							# 后面跟完整的路径，可以用来判断文件是否存在
  $ find -user m5xhsy							# 根据属主查询
  $ find -group root							# 根据属组查询
  $ find -uid 1000 							# 查找属主为id的文件
  $ find -gid 1001							# 查找属组为id的文件
  $ find /etc -nouser							# 查找没有属主的文件
  $ find /etc -nogroup						# 查找没有属组的文件
  $ find /etc -type d							# 查找类型为目录的文件
  $ find -empty								# 查找为空的文件和目录
  $ find -empty -type d						# 查找为空的目录
  $ find -name ab -o -type d					# 查找名字为ab的文件或者类型为目录的文件
  $ find -empty -not -type d 					# 查找为空并且不是目录的文件
  $ find -empty !-type d						# 同上
  $ find -empty -a -type d      		  		# 排除
  $ find !(-empty -a -type d)					# 非空文件或者类型不是目录(摩根定律)	
  $ find ./ -path a/b -prune -o -name "*.conf"# 查找排除a/b查找当前文件夹下的*.conf文件，-prune不打印
  $ find -size #M								# 搜索大小为(#-1,#]M的文件
  $ find -size -#M							# (0,#-1]
  $ find -size +#M							# (#,正无穷)
  $ find -atime #								# atime访问时间，表示[#,#+1)天之间，不包括#+1
  $ find -atime -#							# 表示(0,#)天之间
  $ find -atime +#							# 表示[#+1,正无穷)天之间
  $ find -mtime #								# mtime修改内容，用法同上
  $ find -ctime #								# ctime修改元数据，用法同上
  $ find -amin #								# 用法同上，单位为分钟。其他(mmin,cmin)
  ```

- 处理动作：对符合要求的文件做什么操作，默认是输出到屏幕上

  ```shell
  $ find /etc -name abc -print				# 显示屏幕上(默认)
  $ find /etc -name abc -ls					# 类似ls -l显示详细信息
  $ find /etc -name abc -delete				# 查找删除
  $ find /etc -name abc -fls test.txt			# 查找到的结果长格式保存在文件中
  $ find /etc -name abc -ok rm -rf {} \;		# 查找后执行命令,提醒
  $ find /etc -name abc -exec rm -rf {} \;	# 查找后执行命令，不提醒
  ```

### xargs

- 有的命令不支持管道

- 命令参数过长

  ```shell
  $ echo file{1..500000}|xargs touch			# 一条一条的执行
  ```

### grep文件过滤

- grep:Global search REgular expression and Print out the line

- 作用:文本搜索工具，根据用户指定的"模式"对目标文本逐行进行匹配检查并打印出匹配的行

- 模式:由正则表达式字符及文本字符所编写的过滤条件

- 格式: grep [options] pattern [file...]

- 其中PATTERN项需要使用"或者"，如果需要对模式进行转换，则需要使用""，如果不需要转换，则使用"或"都可以。模式还可以使用正则表达式来表示

- 命令

  ```shell
  $ grep --color=auto "root" passwd			# 对匹配的进行颜色显示
  $ grep -i "user" passwd 					# 忽略大小写
  $ grep -n "user" passwd 					# 匹配到的加行号
  $ grep -c "user" passwd						# 打印匹配到的行数
  $ grep -o "user" passwd 					# 只显示匹配到的内容
  $ grep -q "user" passwd						# 静默模式，不显示，配合 echo $? 使用，为0匹配成功
  $ grep -A # "user" passwd					# 匹配结果向下显示#行
  $ grep -B # "user" passwd					# 匹配结果向上显示#行
  $ grep -C # "user" passwd					# 匹配结果上下各显示#行
  $ grep -e "user" -e "root" passwd			# 匹配root或者user
  $ grep -F "user" passwd						# 不使用正则表达式		
  $ grep -r "user" passwd						# 递归匹配
  $ grep -w "user" passwd						# 匹配整个单词
  $ grep -E "u..r" passwd						# 使用正则表达式(部分),可与文件通配符一起使用，{}+|?需要转义
  $ grep "\(l..e\).*\1"						# \1表示第一个括号匹配后内容在\1处匹配(第二个括号用\2匹配)加-E不需要转义
  ```

### 压缩

- gz压缩文件

  ```shell
    $ gzip passwd						# 压缩,默认不保留源文件
    $ gzip -c passwd >> passwd.gz		# -c是将压缩结果打印，可以写入.gz文件中，就可以保存源文件
    $ gzip -1 -c passwd >> passwd.gz 	# 指定压缩比，压缩比是从1到9，默认为9
    $ gzip -d passwd.gz					# 解压
    $ gunzip passwd.gz					# 解压 
    $ zcat passwd.gz					# 不解压查看压缩包内容
  ```

- bz2压缩文件

  ```shell
  $ bzip2 passwd						# 压缩,默认不保留源文件
  $ bzip2 -k passwd 					# 压缩，保留源文件
  $ bzip2 -k -1 passwd				# 指定压缩比，压缩比是从1到9，默认为9 
  $ bzip2 -d passwd.bz2				# 解压
  $ bunzip2 passwd.bz2				# 解压
  $ bzcat	passwd.bz2					# 不解压查看压缩包内容
  ```

- xz压缩文件

  ```shell
  $ xz passwd						# 压缩,默认不保留源文件
  $ xz -k passwd 					# 压缩，保留源文件
  $ xz -k -1 passwd				# 指定压缩比，压缩比是从1到9，默认为9 
  $ xz -d passwd.xz				# 解压
  $ xz passwd.xz					# 解压
  $ xzcat	passwd.xz				# 不解压查看压缩包内容
  ```

- zip压缩文件

  ```shell
  $ zip -r Test.zip ./Test		# 遍历压缩Test目录
  $ unzip Test.zip				# 解压
  ```

- tar归档

  ```shell
  $ tar -cpvf etc.tar ./Test		# 归档，不压缩
  	-c			创建
  	-p			把原来属性带过来
  	-v			显示过程
  	-f			要操作的文件名
  	-r			增加文件再最后
  	-C			指定解压路径
  	-z			压缩tar.gz 
  	-xz			解压tar.gz
  	-j			压缩tar.bz2
  	-jz			解压tar.bz2
  	-J			压缩tar.xz
  	-Jz			解压tar.xz
  	--exclude 	排除目录
  $ tar xf etc.tar.gz 			# 解压
  $ tar cvf test a b				# a和b文件压缩
  $ tar -rf etc.tar ./passwd		# 追加passwd文件到etc.tar中
  $ tar -tf etc.tar
  ```

### split切割

```\shell
$ split -b 2M etc.tar.gz etc				# -b指定每个文件大小	前一个路径为压缩包，后一个加后缀为切割后的文件名
$ split -b 2M -d etc.tar.gz etc				# -d指定后缀数字
$ split -b 2M -d -a 3 etc.tar.gz etc		# -a指定数字大小，默认为2位
$ cat etc.tar.gz0[0-9] > etc.tar.gz			# 合并切割后的文件
```



### 关机重启

```shell
$ shutdown 			# 一分钟后关机
$ shutdown -c		# 取消
$ shutdown -r		# --reboot 一分钟后重启
$ shutdown now		# 立即关机
$ shutdown +2		# 2分钟后关机
$ shutdown 18:00	# 18:00关机
$ poweroff			# 关机
$ halt  			# 关机
$ init 0			# 关机
```

```shell
$ reboot 			# 重启
$ init 6			# 重启
$ reboot -f			# 强制重启
$ reboot -p 		# 关机
```

### useradd用户添加

添加用户时系统id是递减的，用户id是递增的,用户创建的id从最大的开始

```shell
$ useradd -d /home/m5xhsy m5xhsy			# -d指定家目录
$ useradd -g m5xhsy ass						# 创建用户ass和m5xhsy一个组
$ useradd -G m5xhsy,root bss				# 创建bss添加到m5xhsy和root的2个组里面
$ useradd -k /etc -m css					# 创建css用户并将/etc下的文件复制过来， -m为创建家目录
$ useradd -c "xxx" dss						# 创建用户dss并在/etc/passwd中该用户行添加描述信息
$ useradd -N ess							# 创建用户ess，且组与自己不同名，为users
$ useradd -r pdd							# 创建系统用户pdd
$ useradd -s /usr/bin/bash kss				# 创建用户kss，并指定shell，查看shell:$ cat /etc/shells
$ useradd -u 2000 gcc						# 创建用户id为2000的用户
$ useradd -D [options]						# 显示系统默认配置，也可以修改
```

- 相关文件

  ```shell
  /etc/default/useradd					# 创建用户的默认信息
  /etc/skel/* 							# 默认复制的文件
  ```

### usermod用户修改

```shell
$ usermod -c "xxx" m5xhsy					# 修改描述信息
$ usermod -d /home/xxx m5xhsy				# 修改家目录，默认不会创建新目录
$ usermod -d -m /home/xxx m5xhsy			# 移动家目录
$ usermod -G root,m5xhsy orz				# 修改orz的家目录(替换)
$ usermod -a -G root.m5xhsy orz				# 修改家目录(追加)	-G后面必须为组
$ usermod -l pp orz							# 修改orz的名字为pp
$ usermod -L m5xhsy							# 锁定用户，拒绝登录，修改密码则默认解锁
$ usermod -U m5xhsy							# 解锁用户，允许登录
$ usermod -s /usr.bin/bash m5xhsy			# 修改用户登录后的shell
$ usermod -u 1200 m5xhsy					# 修改用户uid
$ usermod -e 2020-08-07 m5xhsy				# 设置用户过期日期
```

### userdel用户删除

默认删除用户不删除家目录，用户登录不能删除

```shell
$ userdel -r m5xhsy							# 删除用户以及家目录
$ userdel -r -f m5xhsy						# 强制删除登录的用户
```

### passwd密码设置

密码复杂性策略

- 密码包含数字、大小写、特殊符号
- 密码必须12位以上
- 不能为弱口令
- 必须为随机密码
- 3个月或者半年修改一次

```shell
$ passwd m5xhy								# 设置密码
$ passwd -d m5xhsy							# 删除密码，不能登录
$ passwd -l m5xhsy							# 锁定用户
$ passwd -u m5xhsy							# 解锁用户
$ passwd -e m5xhsy							# 下次登录以后强制用户修改密码
$ passwd -f m5xhsy							# 强制操作
$ passwd -x 20 m5xhsy 						# 设置密码最大有效时间20天
$ passwd -n 20 m5xhsy						# 密码最短使用时间，20天内不能修改
$ passwd -w 1 m5xhsy						# 密码过期前1天提醒
$ passwd -i 1 m5xhsy						# 密码过期多长时间禁用
$ echo "123"|passwd --stdin	m5xhsy			# 标准输入读取密码
```

配置文件:

- /etc/shadow

  ```shell
  root:$6$OZ9RBcSIzQ1Hn5Kn$H2Hn7K907nKxA0rV/chcpCLDCvBwIynSkmg7vAcL/2sOPbVDrP9PdIavADDaU2TNt9QPw4oI3KzCf5WK7DzFK1::0:99999:7:::
  
  用户名:$加密方式(默认sha512)$加盐后的字符串:unix元年到最近一次修改密码天数:密码使用的最小时间(0表示可以随时修改):密码可以使用的最大时间(99999表示永不过期):多长时间过期提醒(默认7天):密码过期多长时间锁定:unix元年开始算多长时间失效
  ```

- /etc/passwd

  ```shell
  orz:x:1000:1000:orz:/home/orz:/bin/bash
  
  用户名:密码:uid:gid:描述:家目录:登录后使用的shell
  ```

### chage修改用户密码策略

```shell
$ chage m5xhsy					# 交互式修改密码策略
选项：
  -d, --lastday 最近日期        将最近一次密码设置时间设为“最近日期”
  -E, --expiredate 过期日期     将帐户过期时间设为“过期日期”
  -h, --help                    显示此帮助信息并推出
  -I, --inactive INACITVE       过期 INACTIVE 天数后，设定密码为失效状态
  -l, --list                    显示帐户年龄信息
  -m, --mindays 最小天数        将两次改变密码之间相距的最小天数设为“最小天数”
  -M, --maxdays MAX_DAYS        set maximum number of days before password
                                change to MAX_DAYS
  -R, --root CHROOT_DIR         chroot 到的目录
  -W, --warndays 警告天数       将过期警告天数设为“警告天数”

```

### chfn修改用户信息

```shell
$ chfn m5xhsy				# 交互式修改
选项：
  -d, --lastday 最近日期        将最近一次密码设置时间设为“最近日期”
  -E, --expiredate 过期日期     将帐户过期时间设为“过期日期”
  -h, --help                    显示此帮助信息并推出
  -I, --inactive INACITVE       过期 INACTIVE 天数后，设定密码为失效状态
  -l, --list                    显示帐户年龄信息
  -m, --mindays 最小天数        将两次改变密码之间相距的最小天数设为“最小天数”
  -M, --maxdays MAX_DAYS        set maximum number of days before password
                                change to MAX_DAYS
  -R, --root CHROOT_DIR         chroot 到的目录
  -W, --warndays 警告天数       将过期警告天数设为“警告天数”

```

### groupadd 用户组

- 超级用户组 root 0
- 普通用户组
  - 系统用户组 1-999
  - 可登录用户组 1000-65535

```shell
$ groupadd m5xhsy				# 添加用户组m5xhsy
选项:
  -f, --force		如果组已经存在则成功退出
			并且如果 GID 已经存在则取消 
  -g, --gid GID                 为新组使用 GID
  -h, --help                    显示此帮助信息并推出
  -K, --key KEY=VALUE           不使用 /etc/login.defs 中的默认值
  -o, --non-unique              允许创建有重复 GID 的组
  -p, --password PASSWORD       为新组使用此加密过的密码
  -r, --system                  创建一个系统账户

$ tail -1 /etc/group 			#查看最后一行(只适用新建的组)

配置文件
/etc/group		组名:密码占位:gid:组成员
/etc/gshadow	组名:密码占位:组管理员密码:组成员
```

### groupmod 修改组信息

```shell
$ groupmod -g 1234 1000		# 修改组id，1234为新的组id
-g 			修改组id
-n			改名
-o			允许重复gid
-p			修改组密码
```

### groupdel删除组

```shell
$ groupdel m5xhsy
```

### id查看用户信息

```shell
$ id m5xhsy									# 查看用户id
$ id -g m5xhsy								# 只显示id
$ id -G m5xhsy								# 只显示附加组id
$ id -u m5xhsy								# 只显示用户id
$ id -n m5xhsy								# 只显示名称，需要和guG配合使用
```

### su 切换用户

root用户切换不需要密码

```shell
$ su 										# 进入root
$ su m5xhsy									# 不完整切换，环境变量不改变
$ su - m5xhsy								# 完整切换，环境变量改变
$ su - m5xhsy -c "ls ~/"					# 切换到m5xhsy用户执行命令再切回来				
$ exit 
```

### sudo临时root权限

配置信息位置：/etc/sudoers

- 用户sudo

  ```shell
  ## Allow root to run any commands anywhere
  root	ALL=(ALL)			ALL
  ```

  下面添加:

  ```shell
  mxhsy	ALL=(ALL)			ALL
  ```

  如果该用户使用sudo不需要输入密码则添加:

  ```shell
  m5xhsy	ALL=(ALL)			NOPASSWD:ALL
  ```

- 组sudo

  ```shell
  ## Allows people in group wheel to run all commands
  %wheel	ALL=(ALL)	ALL
  ```

  下面添加

  ```shell
  %m5xhsy	ALL=(ALL)	ALL
  ```

### ip 网络配置

0.0.0.0表示当前主机上所有ip地址

```shell
# 不保存到配置文件
$ ip a add 192.168.21.23/24 dev ens33					# 将24位网段的IP地址添加到ens33网卡
$ ip a del 192.168.21.23/24 dev ens33					# 删除ip地址
$ ip a add 192.168.21.23/24 dev ens33 label ens33:name	# 增加IP地址和别名
```

- 配置文件  /etc/config/network-scripts/ifcfg-ens33	(ens33为网卡名称)

  ```shell
  TYPE="Ethernet"								# 网卡接口类型
  PROXY_METHOD="none"							
  BROWSER_ONLY="no"
  BOOTPROTO="dhcp"							# 获取IP地址方式dhcp，static,none
  DEFROUTE="yes"								
  IPV4_FAILURE_FATAL="no"
  IPV6INIT="yes"
  IPV6_AUTOCONF="yes"
  IPV6_DEFROUTE="yes"
  IPV6_FAILURE_FATAL="no"
  IPV6_ADDR_GEN_MODE="stable-privacy"
  NAME="ens33"								# 网卡名称
  UUID="f3624411-90f9-4d45-8afc-c55d00370493"	# 唯一标识码
  DEVICE="ens33"								# 设备用到的文件
  ONBOOT="yes"								# k开机是否启动
  # HWADDR=""									# 写mac地址
  # IPADDR=192.168.21.100						# IP地址
  # NETMASK=255.255.255.0						# 子网掩码
  # GETEWAY=196.168.21.2						# 网关
  ```

- 重启网卡服务

  ```shell
  $ systemctl restart network
  如果出现 Failed to restart network.service: Unit network.service not found.
  可以尝试使用以下命令：
  $ service network-manager restart
  如果是 Kali Linux（Debian），则需要用以下命令：
  $ service networking restart
  如果是Centos 8，则需要用以下命令：
  $ nmcli c reload
  ```

- 配置DNS  /etc/resolv.conf

  ```shell
  # Generated by NetworkManager
  search localdomain
  nameserver 8.8.8.8			# 谷歌
  nameserver 119.29.29.2		# Public DNS
  nameserver 182.254.116.116	# Public DNS备用
  nameserver 114.114.114.114	# 114 DNS
  nameserver 114.114.114.115	# 114 DNS 备用
  nameserver 223.5.5.5		# 阿里 DNS
  nameserver 223.6.6.6		# 阿里 NDS备用
  ```

### hostnamectl 主机名配置

```shell
$ hostnamectl						# 获取主机详细信息
$ hostnamectl orz					# 设置主机名(不保存到配置文件)
$ hostnamectl set-hostname orz 		# 写入/etc/hostname中，也可以直接修改hostname
```

### ss 网络状态

ss目录用来打印linux系统中的网络状态，可以让管理员更好的了解网络情况

```shell
-a 			# 所有
-l 			# 监听中的
-t 			# tcp
-u			# udp
-x			# unix socket文件
-p			# 相关程序
-n			# 不显示服务名字，显示端口号
常用组合 -anlp -tnlp -unlp
$ ss -anlp|grep 22		# 查看端口

0.0.0.0	# ipv4,表示当前主机上所有ip地址
::		# ipv6
*	  	# 表示当前主机上所有ip地址
```

### netstat 网络状态

```shell
$ netstat -t 							# TCP
$ netstat -u 							# UDP
$ netstat -raw 							# RAW类型
$ netstat --unix 						# UNIX域类型
$ netstat -i							# 显示网卡列表
$ netstat -g							# 显示组播组的关系
$ netstat -s							# 显示网络统计
$ netstat -r							# 显示路由信息 也可以用$ route -n
$ netstat -lntup						# l:listening  n:num  t:tcp u:udp p:process
$ netstat -pt							# 在 netstat 输出中显示 TCP连接信息
$ netstat -ap | grep ssh				# 找出程序运行的端口 
```

### wget 下载

```shell
-q				# 静默模式 
-c				# 断点续传
-O filename		# 另存为
-P /home/orz	# 保存到指定目录
-r				# 递归下载
-p				# 下载所有html文件
```

### curl 

```shell
$ curl -i https://www.baidu.com			# 查看网页响应头相关信息
```

### systemctl 服务

```shell
centos6中没有systemctl，只有service和chkconfig
systemctl start name		# 启动服务
systemctl stop name			# 关闭服务
systemctl reload name		# 重读配置文件(平滑处理)
systemctl restart name		# 重启服务
systemctl status name		# 查看状态
systemctl enable name		# 开机自启动
systemctl disabled name		# 关闭开机自启动
systemctl list-unit-files 	# 查看服务
```

### ping

ping走的是ICMP协议

ICMP（Internet Control Message Protocol）Internet控制报文协议。它是TCP/IP协议簇的一个子协议，用于在IP主机、路由器之间传递控制消息。控制消息是指网络通不通、主机是否可达、路由是否可用等网络本身的消息。这些控制消息虽然并不传输用户数据，但是对于用户数据的传递起着重要的作用。

```shell
$ ping -c 5 www.baidu.com	# 设置5次
```



## 目录结构

> 文件和目录被组织成一颗倒置的树状结构
>
> 文件系统从根开始 “ / ” 
>
> 文件名字严格区分大小写
>
> 隐藏文件以" . "开头
>
> 文件路径分割符为 “ / ”

### 文件命名规范

- 文件字符最长为255个字符
- 包括路径在内文件名最初为4095个
- 颜色表示
  - 蓝色 >> 文件夹
  - 绿色 >> 可执行文件
  - 红色 >> 压缩文件
  - 蓝绿色 >> 连接文件
  - 灰色 >> 其他文件
  - 白色 >> 文件

- 除了斜杠和null其他字符都可以用

### 文件目录

```shell
/boot									# 引导文件存放位置，内核文件，引导加载器
/bin 									# 所有用户都可以使用的命令
/sbin									# 管理类命令	
/lib									# 存放系统动态链接共享库，几乎所有的应用程序都会用到该目录下的共享库
/lib64									# 专门放64位系统上的库文件
/etc									# 存放配置文件的目录
/home/user								# 普通用户的家目录
/root									# 管理员的家目录
/media									# 便携式移动设备的挂载点
/mnt 									# 临时文件挂载点
/dev 									# 设备文件和特殊文件存放位置
/opt 									# 第三方应用的安装位置
/tmp									# 一般用户或正在执行的程序临时存放文件的目录，会自动清空，不能存重要文件
/usr									# 存放安装程序
/var									# 存放经常变化的文件，比如日志
/proc									# 存放内核进程启动和进程相关的虚拟文件
/sys									# 输出当前系统上硬件相关的文件
/srv									# 存放系统允许的服务用到的数据
```

二进制文件

- /bin
- /sbin
- /usr/bin
- /usr/sbin
- /usr/local/bin
- /usr/local/sbin

库文件

- /lib
- /lib64
- /usr/lib
- /usr/lib64
- /usr/local/lib
- /usr/local/lib64

配置文件

- /etc

- /etc/***
- /usr/local/etc/

帮助文件

- /usr/share/man
- /usr/share/doc
- /usr/local/share/man
- /usr/local/share/doc

### 绝对路径和相对路径

- 绝对路径
  - 以根开始
  - 完整的文件位置
  - 可以指定任何一个文件
- 相对路径
  - 不以根开始
  - 相对当前文件夹来决定
  - 可以简短的表示一个文件或者文件夹
  - ./ 表示当前目录
  - ../  表示父级目录

### 目录类型

- -表示文件
- d表示目录
- b表示设备
- c表示字符设备
- l表示符号链接文件
- s表示socket套接字
- f表示普通文件
- p管道文件

### 文件通配符

- *表示所有
- ?表示单个字符
- ~表示用户家目录
- [^123]表示取反
- [123]表示其中一个
- [0-9]表示数字之间一个
- [abc]表示abc之间一个
- [a-z] 有坑缺少Z
- [A-Z]有坑确实a
- [[:lower:]] 表示小写字母中的一个
- [[:upper:]] 表示大写字母中的一个
- [[:alpha:]] 表示a-z和A-Z中的一个
- [[:alnum:]] 表示数字和字母中的一个
- [[:digit:]]表示数字中的一个
- [[:black:]]匹配空白
- [[:punct:]]匹配标点符号

### 目录命令

#### cd 切换目录

```shell
$ cd 							# 切换到家目录
$ cd -							# 切换到上一次的目录
$ pwd 							# 显示当前工作目录
$ pwd -p						# 查看当前目录链接的真正目录
$ chdir=/opt/redis ./configure	# cd 到/opt/redis目录下执行./configure命令
```

#### ls 目录展示

```shell
$ ls			# 显示当前目录文件，不包括隐藏文件
$ ls -a			# 显示隐藏文件
$ ls -l			# 显示详细信息，或者ll
$ ls -R			# 递归显示目录
$ ls -d 		# 显示目录本身
$ ls -1			# 文件竖排显示(数字1)
$ ls -S			# 按照文件大小排序
$ ls -Sr		# 安照文件大小倒序显示
$ ls -lh		# 文件大小按易读的方式排序
$ ls -t			# 安装时间排序
$ ls -d	*/		# 显示当前目录下的文件夹
$ l.			# 只显示隐藏文件 
$ ls file[^012] # 显示策略file0，file1，file2以外的
```

#### stst 文件状态

```shell
$ stat xxx.conf   #查看文件状态
# atime 访问时间Access	查看文件
# mtime	修改时间Modify	改变内容
# ctime 改动时间Change	元数据变化
```

#### touch 创建文件

```shell
$ touch a.conf		# 创建文件，如果文件存在则刷新数据，不存在则创建
$ touch -a a.conf	# 修改atime和ctime
$ touch -m a.conf	# 只修改atime和mtime
$ touch a{a..z}		# 命令展开
```

#### mkdir 创建目录

```shell
$ mkdir a	      	# 创建a目录
$ mkdir -p a/b/c/d	# 递归创建
$ mkdir -pv a/b/c/d # 显示详细过程
$ mkdir -p a/{a,b}	# a下面创建a文件和b文件
```

#### tree显示目录树

```shell
$ yum install -y tree   # 安装
$ tree ./				# 显示目录树
$ tree -d				# 只显示目录
$ tree -L 3 ./			# 只显示3层
```

#### rmdir 删除空目录

```shell
$ rmdir a					# 删除空目录
$ rmdir -p a/b/c/d			# 递归删除b目录以及b目录下面的空目录
$ rmdir -pv a/b/c/d			# 显示删除详细过程
```

#### cp 复制文件目录

```shell
$ cp f1 f0   				# 相当于cp -i命令 复制f1为f0，文件存在则显示提示信息
$ \cp f1 f0					# 原命令，直接覆盖	
$ cp -n f1 f0				# 不覆盖
$ cp -a f1 f0 				# 归档
$ cp -d	f1 f2				# 只复制符号链接文件,不复制源文件			
$ cp -s	f1 f0				# 创建快捷方式
$ cp -r f1 f0				# 递归复制	-R一样
$ cp -f f1 f0				# 不是强制覆盖
$ cp -b	f1 f0				# 复制之前备份要覆盖的文件
$ cp --backup=number f1 f0	# 覆盖的备份文件名字加数字
$ cp -p f1 f0 				# 复制保留原来的属性
$ cp f1 f2 f0				# 把f1 f2 复制到目录f0中
$ cp -r f1 f2				# 递归复制f1目录
```

- 如果源文件是文件的话
  - 目标文件是文件
    - 目标文件存在，本来命令是直接覆盖，建议用-i来提示用户
    - 目标文件不存在，则直接创建目标文件，并把内容写到目标文件中
  - 目标是文件夹
    - 在文件夹中新建一个同名文件，并把内容写到新文件中去
- 如果源文件为多个文件夹
  - 目标必须是文件夹，文件夹必须存在，否则报错
- 如果源文件是文件夹
  - 目标文件不能是文件
  - 目标文件必须是文件夹，且必须使用-r选项
  - 如果目标文件不存在，则直接创建目标文件夹，并且把源文件夹的数据都复制到目标文件夹
  - 如果目标文件夹存在
    - 如果是文件则报错
    - 如果是文件夹，则在目标文件夹中创建同名文件，并且把所有数据都复制到新文件夹中去

#### mv  移动文件目录

```shell
$ mv -i a /home/			# 提示
$ mv -f a /home/			# 强制
$ mv -b a /home/			# 备份
$ mv -v a /home/			# 显示过程
$ mv --backup=number f1 f0	# 备份加数字
```

#### rm 删除文件目录

```shell
$ rm -rf /*			# 递归强制删除根目录下
$ rm -rf *			# 递归强制删除当前目录下
$ rm -i aa			# 提示
$ rm -r	aa			# 递归删除
$ rm -f aa			# 强制删除
```

#### file 判断文件目录类型

```shell
$ file aaa 
aaa: empty										# 空
aaa: ASCII text									# 文本
aaa: directory									# 目录
aaa: aymbolic link to `/etc`					# 符号链接
aaa:Zip archive data,at least v2.0 to extract 	# 压缩包
aaa:socket										# socket套接字
```

### 链接

#### 软链接

```shell
$ ln -s f1 f2			# 给f1创建软链接f2
```

- 相当于快捷方式
- 可以对目录做软链接
- 可以指向一个目录或者文件的路径，大小是路径的长度的字符串
- 对磁盘的引用次数没有影响
- 可以跨分区

#### 硬链接

```shell
$ ln f1 f3				# 给f1创建硬链接f3
```

- 磁盘引用次数会发生变化			
- 指向的是磁盘上的同一块区域
- 磁盘引用数会随着硬盘链接次数增加
- 不能对目录做硬链接
- 不能跨分区

## 输入输出

- 标准输入 默认是来自键盘的输入stdin 0
- 标准输出 默认是输出到终端窗口  stdout 1
- 标准错误输出 默认输出到终端窗口 stderr 2 

### I/O重定向

- 覆盖

```shell
$ echo "ass" > a				# 将标准输出重定向到文件中
$ ls ass  2> a              	# 将错误输出重定向到文件中
$ echo "ass" &> a             	# 将所有输出重定向到文件里面去  
```

- 禁止允许覆盖

```shell
set -C  						# 禁止覆盖
set +C							# 运行覆盖
```

- 追加

```shell
$ echo "ass" >> a				# 将标准输出追加到文件中
$ ls ass  2>> a              	# 将错误输出追加到文件中
$ echo "ass" &>> a             	# 将所有输出追加到文件里面去  
```

- 其他用法

```shell
$ ls ass > file 2>&1			# 合并输出
$ ls ass >> file 2>&1			# 合并输出
$ (ls ass;ls bss) > a			# 合并多个文件输出
$ (ls ass;ls bss) &> /dev/null	# 所有数据都可以输出，类似于黑洞，与之相反的是/dev/zero
```

### 从文件导入stdout

```shell
aaabbbcccsca
$ tr ab 123 < a			# 输出：111222cccsc1
$ tr abc 123 < a		# 输出：111222333s31
$ tr abc 12 < a			# 输出：111222222s21
$ tr -t abc 12 < a 		# 输出：111222cccsc1	截断
$ tr -d	a < a			# 输出：bbbcccsc		删除
$ tr -s a < a			# 输出：abbbcccsca		a去重
$ tr -sc a < a			# 输出：aaabcsca		除了a去重	
$ tr -dc "a\n" < a		# 输出：aaaa			除了a和换行都删除 输入模式如果删除了换行，卡住用ctrl+d退出 
$ tr -d a < a > a1		# 处理完成写回新文件，不能写回原文件
```

### 多行发送给stdout

```shell
$ cat > f1			# 将即将输入的多行数据写入f1中，按ctrl+c退出
$ cat > f2 <<EOF	# 将即将输入的多行数据写入f2中，输入EOF退出。EOF可以可以随便写，建议EOF
```

### 管道

- 管道用 | 表示

- 命令一|命令二|命令三 ，命令一的输入结果当成命令二的输入结果，命令二的输入结果当成命令三的输入结果

- 正常情况下，管道只能传送标准输出
- 如果想要把错误输出也传递，需要在接收错误输出的命令前面加&符号
- 一般用来组合多个命令
- 有一些命令是不接受管道的

## 文本相关

### cat显示文本

```shell
$ cat -E a.txt			# 显示结尾的$符
$ cat -n a.txt			# 对显示的每一行编号
$ cat -b a.txt			# 对非空行编号
$ cat -s a.txt			# 对连续空行压缩成一行
```

### tac 倒序显示

### less 分屏显示文本

```shell
$ less a.txt		# less是man命令的默认分页器
空格 		向下翻一屏是
回车 		向下翻一行是
q		 退出
/文本		搜索文本
n		 搜索内容向下找
N		 搜索内容向上找
```

### more 分页显示文本

```shell
$ more a.txt		# 默认显示百分比，按q退出
$ more -d a.txt		# 显示翻屏和退出提示
```

### head 显示文件前10行

```shell
$ head a.txt 			# 默认显示前10行
$ head -n 2 a.txt		# 显示前2行，或者-2
$ head -c 9 a.txt		# 显示前9个字符
```

### tail 显示文件后10行

```shell
$ tail a.txt 			# 默认显示后10行
$ tail -n 2 a.txt		# 显示后2行，或者-2
$ tail -c 9 a.txt		# 显示后9个字符(包括换行符)
```

### cut 切割

```shell
$ cut -d: -f2-4,7	a.txt	#
-d 		# 指定切割符，默认tab
-c  	# 按照字符切割
-f1-5 	# 切割1到5
-f1,2,5	# 切割1，2，5
-f1-5,7	# 组合切割
```

### paste 合并

```shell
$ paste a.txt b.txt			# 相同行合并，默认tab健
$ paste -d: a.txt b.txt		# 指定间隔符为冒号
$ paste -s a.txt b.txt		# 将所有的行安装列来显示
```

### wc 文本分析

```shell
$ wc a.txt	# 输出: "行数 单词数 字节数 文本名"
-l 			# 只显示行
-w 			# 只显示单词数
-c 			# 只显示字节数
-m			# 只显示字符数
-L  		# 显示文件中最长行的长度
```

### sort 排序

```shell
$ sort a.txt		# 默认按照字母排序
-r 					# 倒序
-R					# 随机排序
-n					# 按照数字排序
-f 					# 忽略大小写
-nt: -k3			# 指定分隔符按第三个字段数字排序
```

### uniq 合并相邻相同行

```shell
$ uniq a.txt		# 合并相同相邻的行
-c					# 显示相同的次数
-d 					# 只显示重复的行
-u					# 只显示没有重复过的行
```

### diff 文件对比

```shell
$ diff a.txt b.txt	# 输出行数对比的数据，以及每个文件不同的内容
```

## 权限

### chown 修改所以者和组

chgrp 修改文件属主和属组和chown一样

```shell
$ chown m5xhsy test				# 修改属主
$ chown :m5xhsy test			# 修改属组
$ chown m5xhsy:m5xhsy test		# 修改属主和属组
$ chowm root:root test			# 修改属主和属组
$ chown -R m5xhsy test			# 递归修改
$ chowm --reference=a test		# 按照c文件模板修改
```

### chmod 修改权限

- 权限定义	rwx r-x r--
  - rwx    属主    u 
  - r - x    属组    g 
  - r - -     其他    o

- r表示可读，w表示可写，x表示可执行
- 对由于文件来说
  - r	可以使用文本工具查看
  - w   可以修改文本内容
  - x   ./fike可以直接执行
- 对于目录来说
  - r	可以使用ls命令查看
  - w   可以创建文件删除文件
  - x    可以cd进去
- 数字表示
  - 1	--x	001
  - 2    -w-   010
  - 3    -wx  011
  - 4    r--    100
  - 5    r-x    101
  - 6    rw-   110
  - 7    rwx   111

```shell
$ chmod u+r	test			# 属主增加读权限
$ chmod g-w test			# 属组删除写权限
$ chmod o=r test			# 其他只有读权限
$ chmod a+x	test			# 全部加上可执行权限
$ chmod 751 test 			# rwx r-x --x  
$ chmod --reference=a test	# 按照a文件权限直接赋值
```

### chattr 特殊权限修改

```shell
$ chattr +i test	# 不能删除，不能修改，不能变更,取消则-i
$ chattr +a test 	# 只能a追加，取消-a
$ lsattr			# 查看特殊权限
```

## vim使用

### 图片示例

![2](./vim.png)

### 打开vim

```shell
$ vim test				# 打开test文件
$ vim +2 test			# 打开文件关标在第二行
$ vim +/abc test		# 打开文件后直接定位到第一个匹配到abc的地方
$ vim -b test			# 以二进制方法打开文件
$ vim -d test test1		# 对比的打开test和test1文件
$ vim -m test			# 以只读的方式打开
$ vim test test1 test3	# 同时打开多个文件
$ vim -o test test2		# 多窗口水平分割打开多个文件	按ctrl+w松开后点箭头 多个文件切换
$ vim -O test test2		# 多窗口垂直分割打开多个文件
```

### 模式切换

- 底行 > 命令    Esc
- 插入 > 命令    Esc
- 命令 > 底行    :
- 命令 > 插入    i、I、a、A、o、O

### vim工作特性

配置全局

- 全局有效：/etc/vimrc
- 当前用户有效：~/.vimrc
- 设置行号：
  - 设置 set nu   	
  - 取消 set nonu
- 忽略大小写(搜索)
  - 设置  set ic
  - 取消 set noic
- 自动缩进
  - 设置 set ai
  - 取消 set noai

- 高亮显示(搜索内容)
  - 设置 set hls
  - 取消 set nohls
- 语法高亮
  - 设置 syntax on
  - 取消 syntax off
- 文件格式
  - win文件    set fileformat=dos   简写：set ff=dos
  - unix文件   set fileformat=unix
- 标识线
  - 设置 set cul
  - 取消 set nocul
- 设置TAB
  - 制表符宽度设置 set tabstop=8  	
  - tab键宽度设置 set softtabstop=8 
- 获取帮助
  - set all

### 插入模式

| 命令 | 说明                                 |
| ---- | ------------------------------------ |
| i    | 光标所在处插入                       |
| I    | 在当前光标所在行的行首插入           |
| a    | 光标所在位置的后面插入               |
| A    | 光标所在位置的行尾插入               |
| o    | 在当前光标所在的行的下一行(新开)插入 |
| O    | 在当前光标所在的行的上一行(新开)插入 |

### 底行模式 

|              | 命令                | 说明                                                        |
| ------------ | ------------------- | ----------------------------------------------------------- |
| 退出操作     | :x                  | 保存并退出                                                  |
|              | :w                  | 保存                                                        |
|              | :q                  | 退出                                                        |
|              | :wq                 | 保持并退出                                                  |
|              | :q!                 | 强制退出                                                    |
|              | :wq!                | 强制保持并退出                                              |
|              | :r file             | 读入文件                                                    |
|              | :w file             | 另存为                                                      |
|              | :!command           | 直接执行命令                                                |
| 地址定界     | :start,end          | 表示start行到end行                                          |
|              | :#                  | 表示#行                                                     |
|              | :#,+n               | 表示#到第#+n行                                              |
|              | :.                  | 表示关标所在的行                                            |
|              | :$-1                | 表示倒数第二行                                              |
|              | :%                  | 表示全文                                                    |
|              | :/abc/,/123/        | 匹配到的第一个123到匹配到的第一个456                        |
|              | :/abc/,$            | 匹配到的abc到结尾                                           |
| 查找替换     | :s/find/replace/    | 光标行匹配到的find替换成replace                             |
|              | :%s/find/replace/   | 全文匹配到的find替换成replace                               |
|              | :%s/\\(f.*\\)/#\\1/ | 匹配到f开头的替换成#号，括号表示分组，要转义，\\1表示第一组 |
|              | :%s/abc/abb/i       | 装饰器，i表示忽略大小写                                     |
|              | :%s/abc/abb/g       | g表示全部替换                                               |
|              | :%s/abc/abb/gc      | gc表示每一次提醒                                            |
|              | :%s#/a#s#           | /a替换成s，分割符号可以用#或者@符号替换                     |
|              | :%s/g.m/#&/         | &符号表示前面匹配到的内容，加#号                            |
| 打开多个文件 | :next               | 跳转下一个文件                                              |
|              | :prev               | 跳转上一个文件                                              |
|              | :last               | 跳转最后一个文件                                            |
|              | :first              | 跳转第一个文件                                              |
|              | :qall               | 退出全部                                                    |
|              | :wall               | 保存全部                                                    |
|              | :xall               | 保存退出全部                                                |
|              | :wqall              | 保存退出全部                                                |

### 命令模式

|              | 命令           | 说明                                                         |
| ------------ | -------------- | ------------------------------------------------------------ |
| 退出         | ZZ             | 保存退出(大写按2下)                                          |
|              | ZQ             | 不保存退出                                                   |
| 字符跳转     | l              | 光标右移一个字符                                             |
|              | h              | 光标左移一个字符                                             |
|              | j              | 光标下移一行                                                 |
|              | k              | 光标上移一行                                                 |
| 单词跳转     | w              | 光标移到下一个单词词首                                       |
|              | e              | 光标移到当前单词词尾或者下一个单词词尾                       |
|              | b              | 光标移到当前单词词首或者上一个单词词首                       |
|              | #(除了0)       | 光标移动#个单词(#表示数字)                                   |
| 页面跳转     | H              | 光标跳转到页首                                               |
|              | L              | 光标跳转到也尾                                               |
|              | M              | 光标跳转到页中                                               |
|              | zt             | 将光标所在行移动到屏幕顶端                                   |
|              | zb             | 将光标所在行移动到屏幕底端                                   |
|              | zz             | 将光标所在行移动到屏幕中间                                   |
| 行首尾跳转   | ^              | 光标跳转到所在行的第一个非空字符                             |
|              | 0              | 光标跳转到所在行的行首                                       |
|              | $              | 光标跳转到所在行的行尾                                       |
| 行间移动     | #G(除了0)      | 光标跳转到#行(#表示数字)                                     |
|              | G              | 跳转到最后一行行首                                           |
|              | gg             | 跳转到第一行的行首(1G也表示跳转到第一行)                     |
| 段落跳转     | {              | 上一段(空行表示一段)                                         |
|              | }              | 下一段                                                       |
| 翻屏         | CTRL+F         | 向下翻屏                                                     |
|              | CTRL+B         | 向上翻屏                                                     |
|              | CTRL+D         | 向下翻半屏                                                   |
|              | CTRL+U         | 向上翻半屏                                                   |
| 字符编辑操作 | x              | 删除光标所在处的字符(可以当作剪切)                           |
|              | #x             | 删除光标所在处及后面的#个字符(#表示数字)                     |
|              | xp             | 将光标所在处的字符互换(先剪切后粘贴到光标后面)               |
|              | ~              | 将光标所在位置大小写互换                                     |
|              | #~             | 将光标所在位置开始#个字符大小写互换                          |
|              | r#             | 将光标所在位置替换成#(#可为任意字符)                         |
|              | R              | 进入REPLACE模式(取代，相当于覆盖)                            |
| 删除         | d$             | 删除到行尾，包括当前位置                                     |
|              | d0             | 删除到行首，不包括当前位置                                   |
|              | d^             | 删除到非空字符                                               |
|              | dw             | 删除一个单词                                                 |
|              | de             | 向后删除一个单词                                             |
|              | db             | 向前删除一个单词                                             |
|              | dd             | 删除整行                                                     |
|              | #dd            | 删除#行                                                      |
|              | dG             | 删除到结尾                                                   |
|              | dgg            | 删除到开头                                                   |
|              | D              | 相当于d$                                                     |
| 复制         | y$             | 复制到行尾                                                   |
|              | y0             | 复制到行首                                                   |
|              | y^             | 复制到非空字符                                               |
|              | yw             | 复制一个单词                                                 |
|              | ye             | 向后复制一个单词                                             |
|              | yb             | 向前复制一个单词                                             |
|              | yy             | 复制整行                                                     |
|              | #yy            | 复制#行                                                      |
|              | yG             | 复制到结尾                                                   |
|              | ygg            | 复制到开头                                                   |
|              | Y              | 复制整行                                                     |
| 粘贴         | p              | 复制一行，粘贴到当前光标所在行的下一行.如果是字符，则粘贴到光标后面 |
|              | P              | 复制一行，粘贴到当前光标所在行的上一行.如果是字符，则粘贴到光标前面 |
| 改变         | cc             | 删除整行并将模式切换成插入模式(可与其他组合，参照：删除)     |
|              | C              | 相当于cc                                                     |
|              | cgg            | 删除到行首并插入                                             |
| 其他         | 10+i+"123"+Esc | 相当于生成10个123                                            |
| 搜索         | /name          | 光标开始向下搜索N和n切换                                     |
|              | ?name          | 光标开始向上搜索                                             |
|              | n              | 跳转下一个匹配到的字符                                       |
|              | N              | 跳转上一个匹配到的字符                                       |
| 撤销         | u              | 撤销多次修改                                                 |
|              | #u             | 撤销最近的#次修改                                            |
|              | U              | 撤销最近的修改                                               |
|              | CTRL+R         | 撤销之前的撤销                                               |
|              | .              | 重做上一次操作                                               |
|              | #.             | 重做#次上一次的操作                                          |
| 文件切割     | CTRL+W,S       | 水平切割                                                     |
|              | CTRL+W,V       | 垂直切割                                                     |
|              | CTRL+W,Q       | 取消相邻窗口                                                 |
|              | CTRL+W,O       | 取消全部窗口                                                 |
|              | CTRL+W,箭头    | 切换窗口                                                     |
| 可视化       | v              | 可视化                                                       |
|              | V              | 面向行                                                       |
|              | CTRL+V         | 面向块                                                       |

### 帮助

```shell
$ vimtutor	# 命令获取
:help		# 底行模式获取帮助
```

## ssh连接

- 直接连接

  ```shell
  $ ssh root@192.168.239.128			# 输入密码直接登录
  ```

- 免密登录

  ```shell
  $ ssh-keygen    					# 直接回车
  $ ssh-copy-id root@192.168.239.128	# 回车后输入yes再输入密码
  $ ssh root@192.168.239.128			# 以后登录就不需要输入密码了
  ```


## 磁盘管理

### df 查看磁盘占有率

```shell
$ df			# 查看磁盘占用率 
$ df -h			# 易读方式查看
linux下磁盘命名格式 /dev/sd[a-z]
```

### du查看目录的占用空间

```shell
$ du -sh /*		# 查看所有目录磁盘占用空间
-s  # 查看目录
-h	# 易读的方式
```

### dd 测试速度

```shell
$ dd if=/dev/zero of=file bs=100M count=10
if 		# 表示从inputfile中读取内容
of		# 表示将读出数据写入到什么地方去
bs 		# byte 可以是 K,M,G,T
cuont	# 读取次数

清除文件$ cat/dev/null > file
```

## 计划任务

### 使用

- /var/spool/cron/ 目录下存放的是每个用户包括root的crontab任务，每个任务以创建者的名字命名

- /etc/crontab 这个文件负责调度各种管理和维护任务。

  ```shell
  $ vim /etc/crontab
  ```

  ```shell
  SHELL=/bin/bash
  PATH=/sbin:/bin:/usr/sbin:/usr/bin
  MAILTO=root
  
  # For details see man 4 crontabs
  
  # Example of job definition:
  # .---------------- minute (0 - 59)
  # |  .------------- hour (0 - 23)
  # |  |  .---------- day of month (1 - 31)
  # |  |  |  .------- month (1 - 12) OR jan,feb,mar,apr ...
  # |  |  |  |  .---- day of week (0 - 6) (Sunday=0 or 7) OR a.txtsun,mon,tue,wed,thu,fri,sat
  # |  |  |  |  |
  # *  *  *  *  * user-name  command to be executed
  
  2  		*  		*  		*  		*  		root touch a.txt	# 每天每小时的第二分钟root用户创建文件a,txt
  2  		12,24 	* 		* 		*  		root touch a.txt	# 每天第12点和24点的第二分钟root用户创建a.txt
  2		12-19  	* 		*		*		root touch a.txt	# 每天12-19点的第二分钟root用户创建a.txt
  3		15-20/5	*		*		*		root touch a.txt	# 每天12-20点每隔5小时的第二分钟root用户创建a.txt
  */7		*		*		*		*		root touch a.txt	# 每隔7分钟root用户创建创建a.txt（到整点会更新）
  * 		12		12,13	*		4		root touch a.txt	# 每月周4和12，13号的12点root用户创建a.txt		
  *		*		*		*		* 		root echo $(data) >>/home/orz/a.txt		#每分钟写数据到a.txt中去
  ```

- /var/log/cron 查看计划任务是否执行成功的日志文件

- /etc/cron.d/ 这个目录用来存放任何要执行的crontab文件或脚本。

- 我们还可以把脚本放在/etc/cron.hourly、/etc/cron.daily、/etc/cron.weekly、/etc/cron.monthly目录中，让它每小时/天/星期、月执行一次。

- 命令

  ```shell
  $ crontab -e		# 编辑当前用户定时任务
  $ crontab -u		# 指定用户(需要权限)
  $ crontab -l		# 列处当前用户的计划任务
  $ crontab -r		# 删除当前用户的计划任务
  ```

### 作业管理

- 前台作业：一直占用终端的作业

- 后台作业：不占用当前终端

- 让作业运行于后台

  - ctrl+z对于启动中
  - 命令后面加& 也会输出到终端

- 脱离终端

  - nohup + 命令 + & > /dev/null

  - screen

    ```shell
    $ screen 			# 开启可用脱离终端的窗口
    $ screen -list 		# 查看脱离终端的进程及id
    $ screen -r id		# 进入脱离终端的进程
    ```

### 作用

- 定时删除
- 定时备份
- 同步时间

## 安全

### 防火墙

- 绿盟
- 深信副
- 启明星辰
- 飞塔
- 思科
- 华为
- 华三

### 防火墙相关命令

```shell
$ iptables -L								# 查看防火墙策略
$ iptables -F								# 清空防火墙策略
$ systemctl disable firewalld				# 开机不启动
$ systemctl stop firewalld.service 			# 关闭防火墙
```

### selinux

美国国家安全局开发(一般会关闭)

```shell
$ vim /etc/selinux/config  	# 编辑 SELINUX=disabled，系统重启后生效
$ setenforce 0				# 临时设置
$ getenforce				# 查看
```



## 进程

### ps命令

```shell
$ ps			# 当前用户会话打开的进程
$ ps -ef		# 查看系统上的每个进程
$ ps -e			# 显示系统内的所有进程信息。与ax选项功能相同。
$ ps -f			# 使用完整的(full)格式显示进程信息。还会打印命令参数相当于u
$ ps -F			# 在-f选项基础上显示额外的完整格式的进程信息。包含SZ、RSS和PSR这三个字段
$ ps a			# 所有终端
$ ps ax			# 显示当前终端下的所有信息(包括不连接终端的)
$ ps axu		# 详细信息
$ ps aux k-pid	# 排序显示 k接小写的属性，负号表示递减
$ ps opid,cmd 	# o表示显示指定的属性
$ ps -L			# 显示线程
$ ps -p 1165	# 根据pid查找
$ ps -U	orz		# 获取指定用户信息 


USER 	# 用户
PID		# 进程号
PSR		# 运行哪一核的cpu上
VSZ		# 虚拟内存
RSS		# 实际内存
STAT	# 状态
%CPU	# cpu占用率
%MEM	# 内存占用率
LWP		# 线程
```

### pidof命令

```shell
$ pidof python			# 根据名称查询
```



### kill命令

```shell
$ kill 9234				# 杀死进程9234
$ kill -l				# 查询可用信号
信号
	 1)sighub			# 不需要关闭程序重新加载配置文件
     2)sigint			# 终止进程 相当于ctrl+c
     9)sigkill			# 强制杀死
	15)sigterm			# 终止正在运行的进程
    18)sigcont			# 拉起进程
    19)sigstop			# 停止进程(后台休眠)
$ killall -9 sshd		# 没装桌面可能用不了，杀死所有sshd进程(sshd链接也会被杀死，需要重启sshd服务)
$ pkill -n

```

## 系统工具

### uptime 系统启动数据

```shell
18:18:40 up  1:56,  		2 users,  	load average: 0.00, 0.00, 0.00
当前时间	   服务器运行时长	 当前登录用户	  cpu平均负载	 1分钟  10分钟	15分钟
cpu平均负载：特定时间内cpu运行的平均进程数(不超过cpu的核数的2倍表示负载良好)
```

### top 监控linux的系统状况

```shell
$ top -d 1			# 刷新频率为，并打开
$ top -b			# 显示所有信息
$ top -n 3			
#######
top - 18:24:09 up  2:01,        2 users,     load average: 0.01, 0.00, 0.00	
	  当前时间	    服务器运行时长	 当前登录用户	  cpu平均负载	  1分钟  10分钟	15分钟
Tasks: 305 total,   1 running, 303 sleeping,   1 stopped,   0 zombie
		进程总数	  运行		睡眠数			  停止数		 孤儿进程
%Cpu(s):  0.1 us,  0.1 sy,  0.0 ni, 99.7 id,  0.0 wa,  0.1 hi,  0.1 si,  0.0 st	
CPU信息	用户空间   系统空间	  nice值	 空闲		  等待	  硬中断	 软中断	虚拟机偷走时间  
MiB Mem :   1800.6 total,    128.2 free,   1181.0 used,    491.4 buff/cache

MiB Swap:   2088.0 total,   1764.2 free,    323.8 used.    447.6 avail Mem 

   2548 root      20   0  414664  28476   7864 S   0.3   1.5   0:11.93 sssd_kcm
   2715 orz       20   0  741880  27408  20488 S   0.3   1.5   0:06.84 vmtoolsd                       
      1 root      20   0  245376  10052   6420 S   0.0   0.5   0:02.84 systemd                       
      2 root      20   0       0      0      0 S   0.0   0.0   0:00.01 kthreadd                    
      3 root       0 -20       0      0      0 I   0.0   0.0   0:00.00 rcu_gp                         
      4 root       0 -20       0      0      0 I   0.0   0.0   0:00.00 rcu_par_gp                 
      6 root       0 -20       0      0      0 I   0.0   0.0   0:00.00 kworker/0:0H-kblockd    
      8 root       0 -20       0      0      0 I   0.0   0.0   0:00.00 mm_percpu_wq                       
      9 root      20   0       0      0      0 S   0.0   0.0   0:00.02 ksoftirqd/0 
     10 root      20   0       0      0      0 I   0.0   0.0   0:00.88 rcu_sched                      
     11 root      rt   0       0      0      0 S   0.0   0.0   0:00.00 migration/0            
     12 root      rt   0       0      0      0 S   0.0   0.0   0:00.00 watchdog/0     
     
     
     
t	cpu切换显示模式(进度条和数字显示)
l	top行显示隐藏
1	cpu展开显示
m	内存信息切换显示模式(进度条和数字显示)
s 	修改刷新频率(按数字切换，默认)
k	杀死进程(默认第一个)
w	保存到/home/orz/.config/procps
排序
    P	cpu占用率(默认cpu)
    M	内存占用率
    T	cpu占用时间
退出
	q	退出
```

### htop 系统进程状况

```shell
# 阿里镜像安装epel源 
$ yum install -y https://mirrors.aliyun.com/epel/epel-release-latest-8.noarch.rpm
# 安装htop
$ yum -y install htop
```

### free 系统内存的使用情况

```shell
$ free -k		# KB
$ free -m		# MB
$ free -g		# GB
$ free -h		# 易读方式
$ free -c		# 刷新次数
```

### vmstat cpu速度

```shell
$ vmstat 
$ vmstat 1			# 一秒刷新一次
$ vmstat 1 3		# 一秒刷新一次，刷新三次

procs -----------memory---------- ---swap-- -----io---- -system-- ------cpu-----
 r  b   swpd   free   buff  cache   si   so    bi    bo   in   cs us sy id wa st
 1  0 310016 558764   1180 514820    1    9    52    22   53   76  0  0 99  0  0
procs
	r:正在运行的进程个数
	b:阻塞队列成都
memory
	swpd:虚拟内容大小
	free:空闲物理内存大小
	buff:用于buff缓存大小
	cache:用于cache的大小
swap
	si:从磁盘交换到内存的数据速率(kb/s)
	so:从内存交换到磁盘的数据数率(kb/s)
	io:从系统写入到磁盘的速率(kb/s)
	bi:从硬盘读取到系统的速率(kb/s)
system
	in:中断频率
	cs:进程间切换的频率
cpu
	us:用户空间
	sy:系统空间
	id:空闲
	wa:等待
	st:虚拟机偷走时间
```

### iostat	磁盘读写速度

```shell
$ iostat 
$ iostat 1 3	# 1秒刷新一次，刷新三次

##########
Linux 4.18.0-193.el8.x86_64 (localhost.localdomain) 	2020年09月19日 	_x86_64_	(4 CPU)
avg-cpu:  %user   %nice %system %iowait  %steal   %idle
           0.25    0.04    0.38    0.19    0.00   99.13
Device             tps    kB_read/s    kB_wrtn/s    kB_read    kB_wrtn
sda               5.61       190.68        89.88    2332336    1099428
scd0              0.00         0.09         0.00       1064          0
dm-0              4.32       183.07        49.66    2239226     607435
dm-1              8.95         2.96        32.99      36180     403568
dm-2              0.73         1.42         7.22      17429      88265
```

### dstat cpu内存

可用代替vmstat和iostat

```shell
$ yum -y install dstat	# 安装
$ dstat -c				# cpu
$ dstat -d				# 硬盘
$ dstat -n				# 网络
$ dstat -m				# 内存
$ dstat -p				# 进程
$ dstat -r 				# io请求
$ dstat -s				# swap空间
$ dstat --top-cpu		# 显示占用cpu最多的进程
$ dstat --top-men		# 显示占用内存最多的进程
$ dstat --tcp			# tcp
$ dstat --udp			# udp
```

### iftop 网卡流量

```shell
$ iftop				
```











压测工具

ab   apache	# 只对页面不包括静态文件

siege				# 包括静态文件

