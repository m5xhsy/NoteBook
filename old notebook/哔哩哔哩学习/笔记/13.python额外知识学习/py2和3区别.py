'''
- 打印
    py2:print '123'
    py3:print('123')
- 继承
    py2:经典类/新式类
    pr3:新式类
- 字符串
    py2:
        str/bytes---v='abc'            #是字节存储，str和bytes都一样
        unicode  ---v=u'abc'           #用unicode存储
    py3:
        str      ---v='abc'            #用unicode存储
        bytes    ---v=b'abc'           #用字节存储
-  编码
    py2:默认使用ascii码                #文件头写#-*- encoding：utf-8 -*-
    py3:默认使用utf-8
- 输入
    py2:x=raw_input()
    py3:x=input
- 范围
    py2:range/xrange                    # py2中range是列表
    py3:range                           # 相当于py2里面的xrange
- 除法
    py2:3/2=1
    py3:3/2=1.5