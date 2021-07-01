"""
import pyautogui
import time


import six
import packaging
import packaging.version
import packaging.specifiers
import packaging.requirements
import os
class OpenQQ(object):
    def her(self):

        os.popen('D:\QQ\Bin\QQScLauncher.exe')
        time.sleep(5)
        pyautogui.click(944, 554)
        pyautogui.typewrite(message="1134344612", interval=0.1)
        pyautogui.press('tab')
        pyautogui.typewrite(message="Forever@620", interval=0.1)
        pyautogui.moveTo(985,665)
        pyautogui.click()







if __name__ == '__main__':
    obj = OpenQQ()
    obj.her()
"""

# import requests
# x = requests.get("https://www.bilibili.com/v/music/perform/?spm_id_from=333.5.b_7375626e6176.6#/372")
# print(x.text)
# with open("bilibili.html", mode="w", encoding="utf-8") as f:
#     f.write(x.text)

import os

print(os.environ.get("DJANGO_MYSQL_HOST"))



