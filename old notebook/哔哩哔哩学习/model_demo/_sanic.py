from sanic import Sanic
from sanic.websocket import WebSocketProtocol
from sanic import request,response
from sanic_jinja2 import SanicJinja2

app = Sanic(__name__)
jj = SanicJinja2(app)
ws_list = []

@app.websocket("/feed")
async def feed(request,ws):
    ws_list.append(ws)
    while True:
        data =await ws.recv()
        print(data)
        print('ws_list',ws_list)
        for item in ws_list:
            try:
                await item.send(data)
            except :
                pass
@app.route("/")
@jj.template("index.html")
def index(request):
    return {"data":["as","ad","ab"]}
if __name__ == '__main__':
    app.run(host="127.0.0.1",port=5000,debug=True,protocol=WebSocketProtocol)