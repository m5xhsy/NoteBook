'''
1、python --version  查看安装的Python版本，

　　pip --version  查看安装的pip版本，

　　升级pip命令： python -m pip install --upgrade pip

　　如果已经下载了安装文件就使用：pip install 文件名

　　如果没有下载就使用：python -m pip install --user 模块名，系统自动下载

2、如果没有安装pip，先安装pip。网址是：https://pypi.python.org/pypi/pip#downloads

　　

　　下载第二个就行，解压后，运行setup.py。

　　现在打开cmd，查看pip安装版本，现在pip已经安装完成了。

　　cmd中输入pip list ，你会看到使用pip安装的所有包。　

3、下载pygame：http://www.lfd.uci.edu/~gohlke/pythonlibs/#pygame

　　cp27代表python2.7版本，win32代表32位操作系统。我的是python3.7，系统是64位，所以我下载的是

　　pygame-1.9.4-cp37-cp37m-win_amd64.whl

　　下载的文件名后缀是whl，因此下一步就是安装能够运行whl文件的程序。

4、安装wheel ，进入cmd，输入命令：pip install wheel

5、在cmd中进入.whl文件的目录，我的文件放在（E:\Python\pygame），

　　进入方法如下：在cmd中输入指令E:（先进入E盘），然后输入cd E:\Python\pygame，最后输入pip install pygame-1.9.4-cp37-cp37m-win_amd64.whl



6、查看安装是否成功，cmd中输入Python，然后输入import pygame



7、编辑器pycharm，此时在编辑器中还不能使用pygame，需要在设置中安装一下，

　　打开settings-project interpreter,发现在project Interpreter中没有pygame，点右边的+,搜索pagame,点击左下角的安装，以后安装其他模块，也是如此。


#############################################################


更换pip国内源

pip国内的一些镜像
  阿里云 https://mirrors.aliyun.com/pypi/simple/
  中国科技大学 https://pypi.mirrors.ustc.edu.cn/simple/
  豆瓣(douban) http://pypi.douban.com/simple/
  清华大学 https://pypi.tuna.tsinghua.edu.cn/simple/
  中国科学技术大学 http://pypi.mirrors.ustc.edu.cn/simple/
修改源方法：
临时使用：
可以在使用pip的时候在后面加上-i参数，指定pip源
eg: pip install scrapy -i https://pypi.tuna.tsinghua.edu.cn/simple
永久修改：
网上很多人说windows下pip的配置文件需要在

~/pip/pip.ini
中修改. 但是这个根本不生效. 太多人进行转载, 复制, 抄袭别人的内容, 导致全都不生效.

需要修改或者添加的文件应该是

~/AppData/Romaing/pip/pip.ini
这个文件的确定事通过设置pip全局选项的命令得到的.

pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
注: linux下的路径为下面所示, 与大多数blog中描述的也是不一样的.

~/.pip/pip.conf
————————————————
版权声明：本文为CSDN博主「宝_Di」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/u011627161/java/article/details/92766340

'''

#安装指定文件夹
#pip3 install 模块 --target=C:\Users\m5xhsy\PycharmProjects\untitled\venv\Lib\site-packages -i https://pypi.tuna.tsinghua.edu.cn/simple/
