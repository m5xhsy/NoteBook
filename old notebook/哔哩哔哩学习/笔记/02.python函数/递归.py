#递归深度：自己可以调用自己的次数，python最大深度为1000，1000以前就会报错，，比较消耗内存
# count=1
# def func():递归函数
#     global count
#     print('abc',count)
#     count+=1
#     func()
# func()   #查看当前电脑pyth深度


########递归函数应用#遍历文件夹
import os
def fun(filspath,k):
    a=0
    files=os.listdir(filspath)                  #获取文件名称
    for file in files:
        file_p=os.path.join(filspath,file)      #获取路径
        if os.path.isdir(file_p):  # 判断是不是路径
            a=fun(file_p,k)
        else:
            if file == k:
                os.remove(os.path.join(filspath, file))
                print('删除成功')
                return 1
    return a
while 1:
    s=input('请输入你要删除文件的路径:')
    d=input('请输入你要删除文件的名称:')
    if os.path.isdir(s):
        break
    else:
        continue
b=fun(s,d)
print(b)
if b!=1:
    print("文件未找到")


########递归函数应用#求阶乘

def func(n):
    if n == 1:
        return 1
    else:
        f = n - 1
        c = func(f)
        return n * c
x = input('请输入要计算阶乘的数：')
p = func(int(x))
print(p)


########递归函数应用#求裴波那契数列
l=[1,1]
def func(a,b,n):
    n=n-1
    c=a+b
    l.append(c)
    if n==0:
        return 1
    func(b,c,n)
k=input('请输入要打印的位数：')       #请输入要打印的位数：9
func(l[0],l[1],int(k)-2)            #[1, 1, 2, 3, 5, 8, 13, 21, 34]
print(l)