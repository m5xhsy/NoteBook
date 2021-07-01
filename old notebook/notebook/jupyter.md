**1.背景主题、字体大小设置**

安装Jupyter主题：

```
pip install jupyterthemes
```

然后，更新Jupyter主题：

```
pip install --upgrade jupyterthemes
```

查看可用主题：　　

```
jt -l
```

我个人喜欢暗一点的背景主题，于是选择了monokai，它还支持语法高亮。下面是我的背景主题设置：　　

```
jt -t monokai -f fira -fs 13 -cellw 90% -ofs 11 -dfs 11 -T -N
```

　　-f(字体) -fs(字体大小) -cellw(占屏比或宽度) -ofs(输出段的字号) -T(显示工具栏) -N(显示自己主机名)![img](https://img2018.cnblogs.com/blog/1286166/201903/1286166-20190328094037442-943078025.png)

 

 也有人这样设置的：

```
jt -t oceans16 -f fira -fs 13 -cellw 90% -ofs 11 -dfs 11 -T -N
```

![img](https://img2018.cnblogs.com/blog/1286166/201903/1286166-20190328094232875-212094135.png)

 白色主题：

 

```
jt -t grade3 -f fira -fs 13 -cellw 90% -ofs 11 -dfs 11 -T -N
```

 

　　

 

**2.代码自动补全**

首先安装 **nbextensions：**

```
pip install jupyter_contrib_nbextensions
```

 

```
jupyter contrib nbextension install --user
```

然后安装 **nbextensions_configurator：**

```
pip install jupyter_nbextensions_configurator
```

　　

```
jupyter nbextensions_configurator enable --user
```

如果提示缺少依赖，就使用pip安装对应依赖即可。

最后重启jupyter，在弹出的Home面里，能看到增加了一个Nbextensions标签页，在这个页面里，勾选Hinterland即启用了代码自动补全，如图所示：![img](https://img2018.cnblogs.com/blog/1286166/201903/1286166-20190328094902912-2074345235.png)

这时可以打开一个jupyter notebook文件进行书写了：![img](https://img2018.cnblogs.com/blog/1286166/201903/1286166-20190328095052014-1939801085.png)