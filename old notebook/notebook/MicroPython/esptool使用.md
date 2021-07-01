## 一: esptool.py 简介

esptool.py 是乐鑫提供的开源库工具，用于乐鑫 ESP8285, ESP8266, ESP32, ESP32-S等系列芯片和 ROM Bootloader（即：一级 bootloader）通讯，从而实现：

固件烧录，flash 擦除，flash 读取，读 MAC 地址，读 flash id ，elf 文件转 bin 等常用功能；

flash 校验, 读取内存，载入 bin 到 RAM 执行，读内存，写内存，读 flash 状态，写 flash 状态，读 chip id，组装 bin等高级功能。

## 二: 安装方法

### [推荐] 安装方法一 (功能实时更新)

下载 esptool.py 源码

```shell
$ git clone https://github.com/espressif/esptool.git
```

目录导入到全局环境变量
以 ubuntu 为例:

将 export PATH=/home/chenwu/esp/esptool:$PATH 添加到 /etc/profile 文件结尾执行 source /etc/profile

```shell
$ esptool.py version 		# 查看版本
```

注意: esptool.py v3.0 版本后，才对 ESP32-S 系列支持。
如果使用新款芯片，可以通过 git pull 来更新 esptool.py 版本。

### 安装方法二：(安装简单)

如下 shell 命令任选其一，执行成功即可:

```shell
$ pip install esptool
$ python -m pip install esptool
$ pip2 install esptool
```



## 三: esptool.py 说明

- 当前支持命令: load_ram,dump_mem,read_mem,write_mem,write_flash,run,image_info,make_image,elf2image,read_mac,chip_id,flash_id,read_flash_status,write_flash_status,read_flash,verify_flash,erase_flash,erase_region,version,get_security_info
- 通过 esptool.py -h 查看所有命令和通用参数详细说明
- 通过 esptool.py <command> -h 查看每条命令对应的参数详细说明

### 通用参数说明 (命令前参数)

-  --help: 或 -h, 显示帮助文档
- --chip: 或 -c, 指定芯片，可选 auto,esp8266,esp32,esp32s2
- --port: 或 -p, 指定串口
- --baud: 或 -b, 指定波特率
- --before: 指定 esptool.py 命令执行前预做的，可选 default_reset,no_reset,no_reset_no_sync，具体参考文档
- --after: 或 -a, 指定 esptool.py 命令执行后将做的，可选 hard_reset,soft_reset,no_reset，具体参考文档
- --no-stub: 禁用 Boot Stub, 不让其管理 flash 操作，具体参考文档
- --trace: 或 -t, 打开 esptool.py 所有交互细节
- --override-vddsdio: VDDSDIO 内部电压调节
- --connect-attempts: 指定 esptool.py 尝试连接次数，默认 7

## 四: 常用命令

### 1.固件烧录 - write_flash

#### 命令参数说明:

- --erase-all: 或 -e, 在写固件时，擦除所有 flash 上所有 sector(默认只擦除要写区域的 sector)
- --flash_freq: 或 -ff， 可选 keep,40m,26m,20m,80m, 指定 SPI 速率
- --flash_mode：或 -fm, 可选 keep,qio,qout,dio,dout, 指定 SPI 模式
- --flash_size：或 -fs. 可选 1MB, 2MB, 4MB, 8MB, 16M + ESP8266 上特有的 256KB, 512KB, 2MB-c1, 4MB-c1。 指定 flash 大小
- --spi-connection：或 -sc, 指定 ESP32 SPI/HSPI 连接配置，具体参考文档
- --no-progress: 或 -p, 禁用进度条打印
- --verify: 在 flash 上验证刚刚写入的数据
- --encrypt: 写入数据时应用 flash 加密（需要正确的 efuse 设置）
- --ignore-flash-encryption-efuse-setting：忽略 flash 加密的 efuse 设置
- --compress: 传输中压缩数据（默认 --no-stub 未指定）
- --no-compress：传输中禁用压缩数据（默认 --no-stub 已指定）

#### 命令参考用法:

```shell
$ sudo esptool.py write_flash [-h][--erase-all][--flash_freq {keep,40m,26m,20m,80m}][--flash_mode {keep,qio,qout,dio,dout}][--flash_size FLASH_SIZE][--spi-connection SPI_CONNECTION] [--no-progress][--verify] [--encrypt][--ignore-flash-encryption-efuse-setting][--compress | --no-compress]<address> <filename> [<address> <filename> ...]
```

示例一：自动烧录

向 flash 的 0x0 地址烧录 factory.bin 文件

```shell
$ esptool.py write_flash 0x0 factory.bin
```

示例二：指定全参数烧录

指定芯片 ESP8266, 串口 USB0, flash DIO 模式, 80MHz, flash 为 2MB, 0x0 地址烧录 bootloader.bin, 0x10000 地址烧录 sntp.bin, 0x8000 地址烧录 partitions.bin

```shell
$ esptool.py --chip esp8266 --port /dev/ttyUSB0 --baud 115200 --before default_reset --after hard_reset write_flash -z --flash_mode dout --flash_freq 80m --flash_size 2MB 0x0 build/bootloader/bootloader.bin 0x10000 build/sntp.bin 0x8000 build/partitions.bin
```

### 2.flash 读取 - read_flash

#### 命令参数说明:

- --spi-connection：或 -sc, 指定 ESP32 SPI/HSPI 连接配置，具体参考文档

- --no-progress: 或 -p, 禁用进度条打印
  命令参考用法：

  ```shell
  - esptool.py read_flash [-h] [--spi-connection SPI_CONNECTION][--no-progress] address size filename
  ```

#### 示例一：自动读取

读取从 0x0 地址开始的 4KB 内容，保存到 dump.bin 文件

```shell
esptool.py read_flash 0x0 0x1000 dump.bin
```

示例二: 指定参数读取

指定串口 USB1, 波特率 460800, 从 0x10000 地址读取 1MB 内容到 dump.bin 文件

```shell
esptool.py -p /dev/ttyUSB1 -b 460800 read_flash 0x10000 0x100000 dump.bin
```

### 3.flash 擦除 - erase_flash & erase region

#### 命令参数说明:

- --spi-connection：或 -sc, 指定 ESP32 SPI/HSPI 连接配置，具体参考文档

#### 命令参考用法：

```shell
	esptool erase_flash [-h] [--spi-connection SPI_CONNECTION]
	esptool erase_region [-h] [--spi-connection SPI_CONNECTION] address size
```

示例一：自动擦除

擦除 flash 上所有内容，即所有数据将是 0xFF

```shell
esptool.py erase_flash
```

示例二: 擦除指定区域

擦除从 0x20000 地址开始的 16KB 空间

```shell
esptool.py erase_region 0x20000 0x4000
```



### 4.读 MAC 地址 - read_mac

无命令参数

#### 命令参考用法：

```shell
esptool.py read_mac
```

通常设备有多个 MAC 地址，例如做 station 的 MAC 地址，做 softAP 时的 MAC 地址，etc
这里读取的是 MAC 地址是 station 地址

### 5.读 flash id - flash_id

#### 命令参数说明:

- --spi-connection：或 -sc, 指定 ESP32 SPI/HSPI 连接配置，具体参考文档

#### 命令参考用法：

```shell
esptool.py flash_id [-h] [--spi-connection SPI_CONNECTION]
```

示例：读取 flash id

```shell
esptool.py flash_id
```

结果将有如下厂商信息和设备信息:

...
Manufacturer: c8
Device: 4016
...

### 6.elf 文件转 bin - elf2image

#### 命令参数说明:

- --output: 或 -o, 输出文件名前缀（image version=1）或文件名（image version=2）
- --version: 或 -e, 可选 1,2, 输出的 image version
- --min-rev: 或 -r, 可选 0,1,2,3, 最小芯片修正
- --secure-pad: 填充 image，因为一旦签名，它将以 64KB 的边界结束。(适用于安全引导v1映像)
- --secure-pad-v2: 将 image 填充到 64KB，因为一旦签名，其签名扇区将在下一个 64K block开始。（适用于安全引导v2映像）
- --elf-sha256-offset：如果已设置，请在二进制文件的指定偏移量处插入输入ELF文件的 SHA256 哈希（32字节）
- --flash_freq: 或 -ff， 可选 keep,40m,26m,20m,80m, 指定 SPI 速率
- --flash_mode：或 -fm, 可选 keep,qio,qout,dio,dout, 指定 SPI 模式
- --flash_size：或 -fs. 可选 1MB, 2MB, 4MB, 8MB, 16M + ESP8266 上特有的 256KB, 512KB, 2MB-c1, 4MB-c1。 指定 flash 大小
- --spi-connection：或 -sc, 指定 ESP32 SPI/HSPI 连接配置，具体参考文档

#### 命令参考用法：

```shell
esptool elf2image [-h] [--output OUTPUT] [--version {1,2}][--min-rev {0,1,2,3}] [--secure-pad][--secure-pad-v2][--elf-sha256-offset ELF_SHA256_OFFSET][--flash_freq {40m,26m,20m,80m}][--flash_mode {qio,qout,dio,dout}][--flash_size FLASH_SIZE][--spi-connection SPI_CONNECTION] input
```

示例一：

ESP8266 上将 elf 文件转为可执行的 bin 文件

```shell
esptool.py --chip esp8266 elf2image my_app.elf
```

示例二：

ESP8266 上将 elf 文件转为可执行的 bin 文件，指定 image version 为 2

```shell
esptool.py --chip esp8266 elf2image --version=2 -o my_app-ota.bin my_app.elf
```

示例三：

ESP32 上将 elf 文件转为可执行的 bin 文件

```shell
esptool.py --chip esp32 elf2image my_esp32_app.elf
```



### 7.输出 bin 信息 - image_info

#### 无命令参数

#### 命令参考用法：

```
esptool image_info [-h] filename
```

示例一：

ESP8266 上输出 image 信息

```
esptool.py image_info build/sntp.bin
```

示例二：

ESP32 上输出 image 信息

```shell
esptool.py --chip esp32 image_info build/sntp.bin
```

## 五: 高级命令

### 1.flash 校验 - verify_flash

#### 命令参数说明:

- --diff: 或 -d, 可选 yes,no, 显示不同
- --flash_freq: 或 -ff， 可选 keep,40m,26m,20m,80m, 指定 SPI 速率
- --flash_mode：或 -fm, 可选 keep,qio,qout,dio,dout, 指定 SPI 模式
- --flash_size：或 -fs. 可选 1MB, 2MB, 4MB, 8MB, 16M + ESP8266 上特有的 256KB, 512KB, 2MB-c1, 4MB-c1。 指定 flash 大小
- --spi-connection：或 -sc, 指定 ESP32 SPI/HSPI 连接配置，具体参考文档

#### 命令参考用法：

esptool verify_flash [-h] [--diff {no,yes}][--flash_freq {keep,40m,26m,20m,80m}][--flash_mode {keep,qio,qout,dio,dout}][--flash_size FLASH_SIZE][--spi-connection SPI_CONNECTION] addr_filename [addr_filename ...]

示例：
对比 flash 上 0x10000 位置的 bin 和 build/sntp.bin 是否相等

```shell
esptool.py verify_flash --diff yes 0x10000 build/sntp.bin
```

### 2.读取内存 - dump_mem

#### 无命令参数

#### 命令参考用法：

```shell
esptool.py dump_mem [-h] address size filename
```

示例：
读取 ESP8266 上 0x40000000 内存地址开始的 4KB 内容，保存到 iram0.bin

```shell
esptool.py dump_mem 0x40000000 4096 iram0.bin
```

### 3.载入 bin 到 RAM 执行 - load_ram

#### 无命令参数

#### 命令参考用法：

```shell
esptool load_ram [-h] filename
```

示例：
将 ESP8266 可执行的 image 加载到 ram 中，然后立即执行其中包含的程序

```shell
esptool.py --no-stub load_ram ./test/images/helloworld-esp8266.bin
```

### 4.读内存 - read_mem

#### 无命令参数

#### 命令参考用法：

```shell
esptool.py read_mem [-h] address
```

示例：
读取 ESP8266 上内存地址为 0x400C0000 中的值 (4字节)

```shell
esptool.py read_mem 0x400C0000
```

### 5.写内存 - write_mem

#### 无命令参数

#### 命令参考用法：

```shell
esptool write_mem [-h] address value mask
```

示例：
向 0x400C0000 地址写入 0xabad1dea

```shell
esptool.py write_mem 0x400C0000 0xabad1dea 0xFFFFFFFF
```

### 6.读 flash 状态 - read_flash_status

#### 命令参数说明:

- --bytes: 可选 1,2,3, 要读的字节数

- --spi-connection：或 -sc, 指定 ESP32 SPI/HSPI 连接配置，具体参考文档

#### 命令参考用法：

```shell
esptool read_flash_status [-h] [--spi-connection SPI_CONNECTION][--bytes {1,2,3}]
```

示例：

```shell
esptool.py read_flash_status --bytes 2
```

### 7.写 flash 状态 - write_flash_status

#### 命令参数说明:

- --bytes: 可选 1,2,3, 要读的字节数
- --spi-connection：或 -sc, 指定 ESP32 SPI/HSPI 连接配置，具体参考文档
- --non-volatile: 写入非易失位

#### 命令参考用法：

```shell
esptool write_flash_status [-h] [--spi-connection SPI_CONNECTION][--non-volatile] [--bytes {1,2,3}] value
```

示例：

```shell
esptool.py write_flash_status --bytes 2 --non-volatile 0
```

### 8.读 chip id - chip_id

#### 无命令参数

#### 命令参考用法：

```shell
esptool chip_id [-h]
```

示例：

```shell
esptool.py chip_id
```

### 9.组装 bin - make_image

#### 命令参数说明:

- --segfile: 或 -f, 输入的 segment 文件
- --segaddr: 或 -a, segment 基地址
- --entrypoint: 或 -e, 入口地址

#### 命令参考用法：

```shell
esptool make_image [-h] [--segfile SEGFILE] [--segaddr SEGADDR][--entrypoint ENTRYPOINT] output
```



示例：

```shell
esptool.py --chip esp8266 make_image -f app.text.bin -a 0x40100000 -f app.data.bin -a 0x3ffe8000 -f app.rodata.bin -a 0x3ffe8c00 app.flash.bin
```

### 10.退出 boot, 执行 app - run

#### 无命令参数

#### 命令参考用法：

```shell
esptool run [-h]
```

示例：

```shell
esptool.py run
```

...
我就是这条街这条街最靓的仔
走起路一定要大摇大摆
墨镜要戴 发型要甩
一出门 低调不下来
...

原文链接：https://blog.csdn.net/espressif/article/details/105028809