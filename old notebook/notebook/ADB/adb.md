```shell
./adb devices                                  确保你的手机可以调试。
./adb shell input keyevent 224                 让手机屏幕点亮。
./adb shell input keyevent 26                  让手机屏幕点亮。(相当于按电源键)
./adb shell input swipe 300 1000 300 300       如果锁屏没有密码，是通过滑动手势解锁，那么可以通过 input swipe 来解锁。
./adb install  **<package名>**                 通过电脑向手机安装一个 .apk 的文件/应用 
./adb shell pm list packages                   查看手机里面的应用列表。我接下来要打开应用com.haie.demo.phone  所以找到这个已安装应用。
./adb shell dumpsys package com.haie.demo.phone    查看应用com.haie.demo.phone 详细信息。在Activity Resolver Table中找到com.haie.demo.phone/com.haie.demo.ui.MainActivity
./adb shell am start -n com.haie.demo.phone/com.haie.demo.ui.MainActivity       调起应用com.haie.demo.phone的Activity，也就是打开应用com.haie.demo.phone，进入应用主界面。

```

adb可以同时连接多台设备，想要查看当前adb连接的设备有哪些可以使用👇这个命令ao

> $ adb devices

以下示例向您展示了 devices 命令及其输出：

![img](https:////upload-images.jianshu.io/upload_images/9099771-292cf71ab150e901.png?imageMogr2/auto-orient/strip|imageView2/2/w/956/format/webp)

adb当前连接了3台设备

**那么问题来了，在同时连接到多台设备的情况下，怎么将命令发送至特定设备呢？**

上图中的emulator-5554、emulator-5556、emulator-5558被称为序列号，是用来区分设备用的。如果多个模拟器/设备实例正在运行，在发出 adb 命令时必须指定一个目标实例。为此，请在命令中使用 **-s** 选项。

比如：在 emulator-5556 设备上安装微信

> adb **-s** emulator-5556 install weixin703android1400.apk

**注：**weixin703android1400.apk 为电脑本地apk路径

**安装应用**

在上面的实例中我们通过adb执行了安装微信的命令，所以adb是支持安装应用到设备的，下面我们介绍一下安装应用的命令，其中path_to_apk是电脑本地的apk路径。

> adb install -r **path_to_apk** 

**注：** -r 表示替换掉原来的apk；如果没有-r，会提示apk已经存在

**卸载应用**

既然上面说到可以安装应用，那么我们能不能卸载应用呢，答案是肯定的，只不过卸载应用之前需要知道应用的安装包名。

> adb uninstall com.tencent.mm // com.tencent.mm 就是微信的安装包名

那怎么才能知道应用的安装包名呢？这个之后讲解

**截图和录屏**

adb是支持截图和录屏的，方便记录我们的操作。我们看一下具体的命令：

>  adb shell screencap /sdcard/screen.png
>
> adb shell  在设备运行脚本命令
>
> screencap  截屏命令
>
> /sdcard/screen.png 截图保存路径

> adb shell screenrecord --size 1920x480 --time-limit 100 /sdcard/demo.mp4
>
> adb shell  在设备运行脚本命令
>
> screenrecord  录制视频命令
>
> --size **1920x480**  widthxheight 设置视频大小
>
> --time-limit **100**   设置最大录制时长（以秒为单位）。默认值和最大值均为 180（3 分钟）。
>
> 按 Control + C 停止屏幕录制

screenrecord 选项说明

--help显示命令语法和选项

--size widthxheight设置视频大小：1280x720。默认值是设备的原生显示分辨率（如果支持），如果不支持，则使用 1280x720。为实现最佳结果，请使用设备的 Advanced Video Coding (AVC) 编码器支持的大小。

--bit-rate rate设置视频的视频比特率（以兆比特每秒为单位）。默认值为 4Mbps。您可以增加比特率以提升视频质量，但这么做会导致影片文件变得更大。以下示例将录制比特率设为 6Mbps：screenrecord --bit-rate 6000000 /sdcard/demo.mp4

--time-limit time设置最大录制时长（以秒为单位）。默认值和最大值均为 180（3 分钟）。

--rotate将输出旋转 90 度。此功能是实验性的。

--verbose显示命令行屏幕上的日志信息。如果您不设置此选项，则运行时此实用程序不会显示任何信息。

**将文件复制到设备/从设备复制文件**

上面我们既然已经截图和录制了视频，那怎么把他们发送到自己的电脑上呢，用蓝牙？用微信？其实，adb就可以轻松搞定。

1、要*从*模拟器或设备复制文件或目录

> adb pull remote local

2、要将文件文件或目录（及其子目录）复制*到*模拟器或设备

> adb push local remote

**注**：local 和 remote 指的是开发计算机（本地）和模拟器/设备实例（远程）上目标文件/目录的路径

举个🌰，把刚才截屏的图片发送到我的电脑桌面

> adb pull /sdcard/screen.png ~/Desktop



作者：无敌老夫子
链接：https://www.jianshu.com/p/88dcc48d2760
来源：简书
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。