客户端 CS架构    client  ->server
服务器 BS架构    browser ->setver

服务器
import socket
while 1:
    sk = socket.socket()
    sk.bind(('192.168.121.1',8898))  #把地址绑定到套接字
    sk.listen(5)          #监听链接
    conn,addr = sk.accept() #阻塞，只有客户端来连接，才继续往下走
    ret = conn.recv(1024)  #阻塞，接收客户端信息：1024表示服务器获取数据时，一次性最多拿1024个字节
    print(ret)       #打印客户端信息
    conn.send(b'hi')        #向客户端发送信息
    conn.close()       #关闭客户端套接字
    sk.close()        #关闭服务器套接字(可选)

客户端
import socket
sk = socket.socket()           # 创建客户套接字
sk.connect(('192.168.121.1',8898))    #阻塞，尝试连接服务器，连接成功才走下去
sk.send(b'hello!')                      #连接后向服务器发送消息
ret = sk.recv(1024)         # 阻塞，对话(发送/接收)等待服务器回消息
print(ret)                  #打印消息
sk.close()            # 关闭客户套接字



#客户端没断开连接直接退出，服务端报错
#windows用try解决
#linux会接受一个空，用len()==0解决