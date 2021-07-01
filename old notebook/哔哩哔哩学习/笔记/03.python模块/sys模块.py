import sys
sys.argv           # 命令行参数List，第一个元素是程序本身路径
                        # 可以直接输入，避免交互
                        # username=sys.argv[1]
                        # password=sys.argv[2]
                        # 在解释器运行的py文件后面直接写，以空格结束
                        # 你的命令>>>python py文件路径 参数1 参数2 参数3
                        # sys.argv=['py文件路径'，参数1 参数2 参数3]
sys.exit(n)        #退出程序，正常退出时exit(0),错误退出sys.exit(1)
sys.version        #获取Python解释程序的版本信息
sys.path           # 返回模块的搜索路径，初始化时使用PYTHONPATH环境变量的值
                        # 一个模块能被导入，是因为这个模块所在的文件夹在path列表中
                        # 内置模块和第三方模块不需要操作path,直接用就可以了
                        # 如果一个模块导入不进来，就把模块的文件夹添加进sys.path中
sys.platform       # 返回操作系统平台名称
sys.modules        # 导入内存的模块的名字：内存地址
                        # print(sys.modules['re'].findall('\d','abc1123'))相当于re.findall('\d','abc1123')
                        # 被导入模块的内存地址存在modules中