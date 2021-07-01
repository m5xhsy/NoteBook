import socketserver
class Ass(socketserver.BaseRequestHandler):
    def handle(self):
        pass
    """
    代码
    self.request相当于conn
    self.client_address相当于addr
    """

server=socketserver.ThreadingTCPServer(('192.168.121.1',8898),Ass)          #TCP线程并发
server.serve_forever()

server=socketserver.ThreadingUDPServer(('192.168.121.1',8898),Ass)          #UDP线程并发
server.serve_forever()

server=socketserver.ForkingTCPServer(('192.168.121.1',8898),Ass)    #TCP进程并发
server.serve_forever()

server=socketserver.ForkingUDPServer(('192.168.121.1',8898),Ass)    #UDP进程并发
server.serve_forever()