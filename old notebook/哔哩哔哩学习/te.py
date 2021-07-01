from machine import Pin, Timer, PWM
import time
import network, time
from umqtt.simple import MQTTClient


class Ass(object):
    def __init__(self):
        self.S1 = PWM(Pin(18),freq=50,duty=0)

    @classmethod
    def wifi(self):
        wlan = network.WLAN(network.STA_IF)  # STA 模式
        wlan.active(True)  # 激活接口
        start_time = time.time()  # 记录时间做超时判断
        if not wlan.isconnected():
            print('wifi连接中...')
            wlan.connect('m5xhsy', 'Ass078678')  # 输入 WIFI 账号密码

            while not wlan.isconnected():
                # 超时判断,15 秒没连接成功判定为超时
                if time.time() - start_time > 15:
                    # led闪
                    break
            return False
        else:
            pass
            # led亮
            return True
    def Servo(self, angle):
        self.S1.duty(int((((angle + 90) * 2 / 180 + 0.5) / 20) * 1023))

    def MQTT_callback(self, topic, msg):
        her = int(msg)
        if her>-3 and her < 3:
            self.Servo(her*45)

        elif her == -3:
            s = (((self.S1.duty()/1023)*20-0.5)*180/2-90-45)/45
            if s <-3:
                pass
            else:
                self.Servo(s)
        elif her == 3:
            s = (((self.S1.duty()/1023)*20-0.5)*180/2-90+45)/45
            if s >3:
                pass
            else:
                self.Servo(s)


    def MQTT_rev(self):
        self.client.check_msg()

    @classmethod
    def mqtt(self):
        SERVER = 'nncoitfr.xiaomy.net'
        HOST = 45076
        CLIENT_ID = '2366078678'
        TOPIC = 'test'
        self.client = MQTTClient(CLIENT_ID, SERVER, HOST)
        self.client.set_callback(self.MQTT_callback)
        self.client.connect()
        self.client.subscribe(TOPIC)
        tim = Timer(-1)
        tim.init(period=300, mode=Timer.PERIODIC, callback=self.MQTT_rev)




s = Pin(27, Pin.OUT)
s.on()
if s.value() == 1:
    # WIFI 连接
    while not Ass.wifi():
        pass
    # led点亮
    Ass.mqtt()
    # 连接服务器


else:
    pass