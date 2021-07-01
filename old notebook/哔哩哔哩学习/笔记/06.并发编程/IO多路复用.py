#检测多个socket是否发生变化(是否可读可写)

#操作系统检测socket变化有三种模式
    select:         最多检查1024个socket，内部循环检测
    poll：          不再限制检测socket个数，内部循环检测(水平触发)
    epoll:          不再限制检查socket个数，回调方式(边缘触发)           #windows没有


#########异步非阻塞
    - 非阻塞：不等待
        比如创建socket对某个地址进行connect、获取接收数据recv时默认都会等待(连接成功或者收到数据)，才继续操作，
        如果设置setblocking(False),以上两个过程都会不在等待，但是会报BlockingIOError的错误，只要捕获即可
    - 异步：执行完成后自动执行回调函数或者自动执行某些操作(通知)
        比如做爬虫时候向某个地址发送请求，当请求执行完成后自动执行回调函数。
#########同步阻塞
    - 阻塞：等待
    - 同步：按照顺序同步执行








#########基于IO多路复用实现单线程
import socket
import select
client1=socket.socket()
client1.setblocking(False)
try:
    client1.connect(('www.baidu.com',80))
except BlockingIOError:
    pass

client2=socket.socket()
client2.setblocking(False)
try:
    client2.connect(('www.sogou.com',80))
except BlockingIOError:
    pass

client3=socket.socket()
client3.setblocking(False)
try:
    client3.connect(('www.bilibili.com',80))            #https://search.bilibili.com/all?keyword=123
except BlockingIOError:
    pass

socket_list=[client1,client2,client3]
conn_list=[client1,client2,client3]

while True:
    read_list,write_list,error_list=select.select(socket_list,conn_list,[],0.005)
    for items in write_list:
        if items==client1:
            client1.sendall(b'GET /s?wd=123 HTTP/1.0\r\nhost:www.baidu.com\r\n\r\n')
        elif items==client2:
            client2.sendall(b'GET /tx?query=123 HTTP/1.0\r\nhost:www.baidu.com\r\n\r\n')
        elif items==client3:
            client3.sendall(b'GET /all?keyword=123 HTTP/1.0\r\nhost:www.bilibili.com\r\n\r\n')
        conn_list.remove(items)
    for itdate in read_list:
        client_list=[]
        while True:
            try:
                chunk=itdate.recv(8096)
                client_list.append(chunk)
                if not chunk:
                    break
            except BlockingIOError as e:
                break

        print('```````````````````````',client_list[0].decode('utf-8'))
        itdate.close()
        socket_list.remove(itdate)

    if not socket_list:
        break