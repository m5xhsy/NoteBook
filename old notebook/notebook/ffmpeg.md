## 安装

### 安装流程

```shell
$ git clone https://git.ffmpeg.org/ffmpeg.git ffmpeg
$ cd ffmpeg     # 也可用用--prefix=/opt/ffmpeg 指定目录，最后添加环境变量（不建议这么做）
$ ./configure
$ make&&make install
```

### 安装常见错误

1. #### 错误一：执行./configure 的时候出现以下错误

   ```shell
   nasm/yasm not found or too old. Use --disable-x86asm for a crippled build.
   
   If you think configure made a mistake, make sure you are using the latest
   version from Git.  If the latest version fails, report the problem to the
   ffmpeg-user@ffmpeg.org mailing list or IRC #ffmpeg on irc.freenode.net.
   Include the log file "ffbuild/config.log" produced by configure as this will help
   solve the problem.
   ```

   ```shell
   错误的意思是 yasm/nasm 包不存在或者很旧,yasm是一款汇编器，并且是完全重写了nasm的汇编环境，接收nasm和gas语法，支持x86和amd64指令集，
   # 解决方法
   方法一:  --disable-yasm表示禁用yasm。
   方法二:  更新yasm
   $ wget http://www.tortall.net/projects/yasm/releases/yasm-1.3.0.tar.gz
   $ tar -xf yasm-1.3.0.tar.gz
   $ cd yasm-1.3.0
   $ ./configure
   $ make && make install
   ```

2. #### 错误二：执行ffmpeg出现ffmpeg: error while loading shared libraries: libavdevice.so.58: ......

   ```shell
   # 解决方法
   1.找到指令位置
   $ ldd /opt/ffmpeg/bin/ffmpeg		# 查看依赖
   2.发现下面许多not found
   	linux-vdso.so.1 (0x00007ffd4cd7e000)
   	libavdevice.so.58 => not found
   	libavfilter.so.7 => not found
   	libavformat.so.58 => not found
   	libavcodec.so.58 => not found
   	libswresample.so.3 => not found
   	libswscale.so.5 => not found
   	libavutil.so.56 => not found
   	libm.so.6 => /lib64/libm.so.6 (0x00007f05e27a1000)
   	libpthread.so.0 => /lib64/libpthread.so.0 (0x00007f05e2581000)
   	libc.so.6 => /lib64/libc.so.6 (0x00007f05e21bf000)
   	/lib64/ld-linux-x86-64.so.2 (0x00007f05e2b23000)
   3.将上面not found的用find命令查找
   $ find / -name "libavdevice.so.58"
   	/root/ffmpeg/libavdevice/libavdevice.so.58
   4.将环境写入开机启动文件/etc/profile中
   $ vim /etc/profile
   ####
   export LD_LIBRARY_PATH=/root/ffmpeg/libavformat/:/root/ffmpeg/libavfilter/:/root/ffmpeg/libavdevice/:/root/ffmpeg/libavcodec/:/root/ffmpeg/libswresample/:/root/ffmpeg/libswscale/:/root/ffmpeg/libavutil/
   ```









- 























ffmpeg -hwaccel cuvid -c:v h264_cuvid -i G:/test/video/op.flv -c:v h264_nvenc  -r 60 -b 10000k -y G:/test/video/op_xx1.mp4

https://blog.csdn.net/COCO56/article/details/89517157

https://blog.csdn.net/a2657222/article/details/7894839

https://www.cnblogs.com/xcjit/p/10831096.html

```
configuration: 
--prefix=/ffbuild/prefix 
--pkg-config-flags=--static 
--pkg-config=pkg-config 
--cross-prefix=x86_64-w64-mingw32- 
--arch=x86_64 
--target-os=mingw32 
--enable-gpl 
--enable-version3 
--disable-debug 
--disable-w32threads 
--enable-pthreads 
--enable-iconv 
--enable-zlib 
--enable-libxml2 
--enable-libfreetype 
--enable-libfribidi 
--enable-gmp 
--enable-lzma 
--enable-fontconfig 
--enable-opencl 
--enable-libvmaf 
--disable-vulkan 
--enable-libvorbis 
--enable-amf 
--enable-libaom 
--enable-avisynth 
--enable-libdav1d 
--enable-libdavs2 
--enable-ffnvcodec 
--enable-cuda-llvm 
--disable-libglslang 
--enable-libass 
--enable-libbluray 
--enable-libmp3lame 
--enable-libopus 
--enable-libtheora 
--enable-libvpx 
--enable-libwebp 
--enable-libmfx 
--enable-libopencore-amrnb 
--enable-libopencore-amrwb 
--enable-libopenjpeg 
--enable-librav1e 
--enable-librubberband 
--enable-schannel 
--enable-sdl2 
--enable-libsoxr 
--enable-libsrt 
--enable-libsvtav1 
--enable-libtwolame 
--enable-libuavs3d 
--enable-libvidstab 
--enable-libx264 
--enable-libx265 
--enable-libxavs2 
--enable-libxvid 
--enable-libzimg 
--extra-cflags=-DLIBTWOLAME_STATIC 
--extra-cxxflags= 
--extra-ldflags=-pthread 
--extra-libs=-lgomp
```

Plex Media Server是一个客户端-服务器媒体播放器系统和软件套件，可在Windows，macOS，Linux，FreeBSD或NAS上运行。Plex整理了计算机个人媒体库中的所有视频，音乐和照片，并让您流式传输到设备。

Plex转码器使用FFmpeg来处理媒体并将其转换为客户端设备支持的格式。

## 如何将FFmpeg / libav与NVIDIA GPU一起使用

#### 将单个H.264解码为YUV

要将单个H.264编码的基本比特流文件解码为YUV，请使用以下命令：

```
FFMPEG: ffmpeg -vsync 0 -c:v h264_cuvid -i <input.mp4> -f rawvideo <output.yuv>LIBAV: avconv -vsync 0 -c:v h264_cuvid -i <input.mp4> -f rawvideo <output.yuv>
```

示例应用程序：

- 视频分析，视频推理
- 视频后期处理
- 视频回放

#### 将单个YUV文件编码为比特流

要将单个YUV文件编码为H.264 / HEVC比特流，请使用以下命令：

##### H.264

```
FFMPEG: ffmpeg -f rawvideo -s:v 1920x1080 -r 30 -pix_fmt yuv420p -i <input.yuv> -c:v h264_nvenc -preset slow -cq 10 -bf 2 -g 150 <output.mp4>LIBAV: avconv -f rawvideo -s:v 1920x1080 -r 30 -pix_fmt yuv420p -i <input.yuv> -c:v h264_nvenc -preset slow -cq 10 -bf 2 -g 150 <output.mp4>
```

##### HEVC（无B帧）

```
FFMPEG: ffmpeg -f rawvideo -s:v 1920x1080 -r 30 -pix_fmt yuv420p -i <input.yuv> -vcodec hevc_nvenc -preset slow -cq 10 -g 150 <output.mp4>LIBAV: avconv -f rawvideo -s:v 1920x1080 -r 30 -pix_fmt yuv420p -i <input.yuv> -vcodec hevc_nvenc -preset slow -cq 10 -g 150 <output.mp4>
```

示例应用程序：

- 监视
- 归档远程摄像机的镜头
- 从单个摄像机存档原始捕获的视频

#### 转码单个视频文件

要执行1：1转码，请使用以下命令：

```
FFMPEG: ffmpeg -hwaccel cuvid -c:v h264_cuvid -i <input.mp4> -vf scale_npp=1280:720 -c:v h264_nvenc <output.mp4>LIBAV: avconv -hwaccel cuvid -c:v h264_cuvid -i <input.mp4> -vf scale_npp=1280:720 -c:v h264_nvenc <output.mp4>
```

示例应用程序：

- 消费视频加速转码

#### 将单个视频文件转码为N个流

要执行1：N转码，请使用以下命令：

```
FFMPEG: ffmpeg -hwaccel cuvid -c:v h264_cuvid -i <input.mp4> -vf scale_npp=1280:720 -vcodec h264_nvenc <output0.mp4> -vf scale_npp 640:480 -vcodec h264_nvenc <output1.mp4>LIBAV: avconv -hwaccel cuvid -c:v h264_cuvid -i <input.mp4> -vf scale_npp=1280:720 -vcodec h264_nvenc <output0.mp4> -vf scale_npp 640:480 -vcodec h264_nvenc <output1.mp4>
```

示例应用程序：

- 商业（数据中心）视频转码

























CUVID现在也被Nvidia称为nvdec，可以在Windows和Linux上进行解码。结合nvenc，它提供了完整的硬件转码。

CUVID offers decoders for H264, HEVC, MJPEG, mpeg1/2/4, vp8/9, vc1. Codec support varies by hardware. The full set of codecs 仅在Pascal硬件上可用，它增加了VP9和10位支持。



虽然支持解码10位视频，但目前还不能进行完整的硬件转码(参见下面的部分硬件示例)。



使用CUVID解码器，本例中CUVID解码器将帧复制到系统内存中:

```
ffmpeg -c:v h264_cuvid -i input output.mkv
```

- 全硬件转码与CUVID和NVENC:

```
ffmpeg -hwaccel cuvid -c:v h264_cuvid -i input -c:v h264_nvenc -preset slow output.mkv
```

部分硬件转码，帧通过系统内存(这是必要的转码10位内容):

```
ffmpeg -c:v h264_cuvid -i input -c:v h264_nvenc -preset slow output.mkv
```

如果编译ffmpeg时支持libnpp，可以使用它在链中插入一个基于GPU的scaler:

```
ffmpeg -hwaccel_device 0 -hwaccel cuvid -c:v h264_cuvid -i input -vf scale_npp=-1:720 -c:v h264_nvenc -preset slow output.mkv
```

 `-hwaccel_device` 选项可以用来指定ffmpeg中的cuvid hwaccel要使用的GPU。