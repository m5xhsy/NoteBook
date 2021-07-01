'''
#*****文件操作*****
    newline=''                                      #写在open()中,读取真正的换行符号，windows回车为\r\n
    f.open()                                        #打开文件
    f.close()                                       #关闭文件
    f.closed                                        #判断文件是否关闭
    f.encoding                                      #判断文件打开的编码
    f.flush()                                       #(终端可用)立刻将文件内容从内存刷到硬盘
    f.tell()                                        #光标当前所在位置
    f.name                                          #文件名
    f.seek(a,b)                                     #最好b模式运行  移动光标（字节操作）从0开始
                                                    #b=0,开始移动a个字节
                                                    #b=1,相对位置移动a个字节
                                                    #b=2,从结尾开始移动a个字节
    f.truncate(10)                                  #截取10个字节，其余删除
    f.
    读:f.read()
        模式 r rb r+ r+b
            (1).print(f.read())                       #全部读取
            (2).print(f.read(n))                      #指定读取字符，包括换行符，rb模式下代表字节
            (3).print(f.readline())                   #按行读取
            (4).print(f.readlines())                  #按行读取，返回列表
            (5).for line in f:                        #for循环,f为可迭代对象
    写:f.write(con)
        模式 w wb w+ w+b
            (1)write(con)
    追加:f.write(con)
        a
        ab
        a+
        a+b


'''
with open(en)