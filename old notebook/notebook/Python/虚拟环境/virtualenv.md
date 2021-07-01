# virtualenv

基于物理环境下单python解释器

```shell
$ virtualenv venv			# 创建虚拟环境
$ source /bin/activate		# 进入虚拟环境
$ deactivate				# 退出虚拟环境
```

# virtualenvwrapper

1. 安装

   ```SHELL
   $ pip3 install virtualenvwrapper -i https://mirrors.aliyun.com/pypi/simple
   ```

2. 配置开机启动文件~/.bashrc

   ```
   export WORKON_HOME=$HOME/.Envs    # 配置统一管理目录
   export PROJECT_HOME=$HOME/Devel    # 该变量PROJECT_HOME告诉virtualenvwrapper将项目工作目录放在何处。
   export VIRTUALENVWRAPPER_PYTHON=/usr/bin/python3.6    # 配置python解释器模板
   export VIRTUALENVWRAPPER_SCRIPT=/usr/local/bin/virtualenvwrapper.sh    # 如果不在环境中则用这个指向他
   # export VIRTUALENVWRAPPER_VIRTUALENV_ARGS='--no-site-packages'    # 从版本20开始，默认就是这个，需要删除
   source /usr/local/bin/virtualenvwrapper_lazy.sh    # virtualenvwrapper_lazy.sh提供了一个替代的初始化脚本，而不是直接使用
   ```

3. 重新加载~/.bashrc

   ```shell
   $ source ~/.bashrc
   ```

4. 创建虚拟环境

   ```shell
   $ mkvirtualenv venv
   ```

5. 查看所有虚拟环境

   ```shell
   $ lsvirtualenv
   ```

6. 进入虚拟环境

   ```shell
   $ workon venv
   ```

7. 删除虚拟环境

   ```shell
   $ rmvirtualenv venv
   ```

8. 进入虚拟环境的文件夹

   ```shell
   $ cdvirtualenv venv
   ```