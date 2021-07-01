import os,time
os.chdir('d:')
os.chdir('D:\platform-tools_r30.0.2-windows\platform-tools')
def transcribe():
    cont = 0
    while cont < 200:
        cont += 1
        x = os.popen('adb devices').readlines()
        if len(x) == 3:
            f = x[1].split('\t')[0]  # 设备号
            print('\r正在查找第%s次,设备号: %s' % (cont, f))
            x = os.popen('adb shell getevent -c 2000').read()
            with open(__file__.split('.')[0] + '.txt', mode='w+', encoding='gbk') as f1:
                with open(__file__.split('.')[0] + '1.txt', mode='w', encoding='gbk') as f2:
                    f1.write(x)
                    f1.seek(0)
                    data = f1.readlines()
                    for item in data:
                        if 'add' in item or 'name' in item:
                            pass
                        else:
                            headler_list = item.split(' ')
                            headler_str = 'adb shell sendevent ' + headler_list[0].split(':')[0] + " " + str(
                                int(headler_list[1], 16)) + " " + str(int(headler_list[2], 16)) + " " + str(
                                int(headler_list[3].split('\n')[0], 16))
                            f2.write(headler_str + '\n')
            os.rename(__file__.split('.')[0] + '.txt', __file__.split('.')[0])
            os.rename(__file__.split('.')[0] + '1.txt', __file__.split('.')[0] + '.txt')
            os.remove(__file__.split('.')[0])
            break
        else:
            time.sleep(1)
            print('\r正在查找第%s次,ERROR: 未找到设备....' % cont, end='')

def ttt():
    time.sleep(0.5)
    os.system('adb shell input tap 236 729')
    time.sleep(0.5)
    os.system('adb shell input tap 431 617')
    time.sleep(0.5)
    os.system('adb shell input tap 558 624')
    time.sleep(0.5)
    os.system('adb shell input tap 702 674')
    time.sleep(0.5)
    os.system('adb shell input tap 721 685')
    time.sleep(0.5)
    os.system('adb shell input tap 858 756')
    time.sleep(0.5)
    os.system('adb shell input tap 335 758')
    time.sleep(0.5)
    os.system('adb shell input tap 505 627')
    time.sleep(0.5)
    os.system('adb shell input tap 472 465')
    time.sleep(0.5)
# transcribe()
def xxx():
    cont = 0
    while cont < 200:
        cont += 1
        x = os.popen('adb devices').readlines()
        if len(x) == 3:
            f = x[1].split('\t')[0]  # 设备号
            print('\r正在查找第%s次,设备号: %s' % (cont, f))
            os.system('adb shell input keyevent 224')
            os.system('adb shell input swipe 500 1200 500 200')
            os.system('adb shell input tap 536 1450')
            os.system('adb shell input tap 536 1650')
            os.system('adb shell input tap 536 1850')
            os.system('adb shell input tap 536 2050')
            os.system('adb shell input tap 850 1980')
            os.system('adb shell input swipe 500 2279 500 2000 50')
            time.sleep(1)
            os.system('adb shell input swipe 500 1800 500 20')
            os.system('adb shell input tap 500 180')
            os.system('adb shell input text zfb')
            time.sleep(0.5)
            os.system('adb shell input tap 980 2134')
            os.system('adb shell input tap 153 440')
            time.sleep(1)
            os.system('adb shell input tap 956 761')
            time.sleep(0.5)
            os.system('adb shell input swipe 500 200 500 966 400')
            os.system('adb shell input swipe 500 1883 500 966 200')
            time.sleep(0.5)
            os.system('adb shell input tap 701 1050')
            time.sleep(4)
            '''
            ttt()
            '''
            os.system('adb shell input swipe 500 1700 500 500 1000')
            time.sleep(1)
            i = 0
            while i <11:
                os.system('adb shell input tap 715 1900')
                time.sleep(0.5)
                ttt()
                os.system('adb shell input tap 68 126')
                time.sleep(1)
                os.system('adb shell input swipe 500 2138 500 1940')
            os.system('adb shell input swipe 500 2279 500 1580 1500')
            time.sleep(1)
            os.system('adb shell input tap 540 1939')
            os.system('adb shell input keyevent 26')
            break
        else:
            time.sleep(1)
            print('\r正在查找第%s次,ERROR: 未找到设备....' % cont, end='')
xxx()
