# **UBoot常用命令**

!> 进入Uboot后可以通过**help**或者**?**命令查看Uboot支持的所有命令，命令的详细信息可以在**help**或**?**后面加需要查看的命令查看。

## **(一)信息查询**

### bdinfo命令

```shell
$ bdinfo

# 输出信息
arch_number = 0x00000000
boot_params = 0x80000100
DRAM bank   = 0x00000000
-> start    = 0x80000000
-> size     = 0x20000000
eth0name    = FEC1
ethaddr     = (not set)
current eth = FEC1
ip_addr     = <NULL>
baudrate    = 115200 bps
TLB addr    = 0x9FFF0000
relocaddr   = 0x9FF51000
reloc off   = 0x18751000
irq_sp      = 0x9EF4EEA0
sp start    = 0x9EF4EE90
FB base     = 0x00000000
```

!>bdinfo主要用于查询开发板相关信息，例如DRAM的起始地址和大小、启动参数保存起始地址、波特率、sp堆栈指针的起始地址等信息。

### printenv命令


```shell
$ printenv

# 输出信息
baudrate=115200
board_name=EVK
board_rev=14X14
boot_fdt=try
bootcmd=run findfdt;mmc dev ${mmcdev};mmc dev ${mmcdev}; if mmc rescan; then if run loadbootscript; then run bootscript; else if run loadimage; then run mmcboot; else run netboot; fi; fi; else run netboot; fi
bootcmd_mfg=run mfgtool_args;bootz ${loadaddr} ${initrd_addr} ${fdt_addr};
bootdelay=1
bootscript=echo Running bootscript from mmc ...; source
console=ttymxc0
ethact=FEC1
ethprime=FEC
fdt_addr=0x83000000
fdt_file=imx6ull-14x14-emmc-7-1024x600-c.dtb
fdt_high=0xffffffff
findfdt=if test $fdt_file = undefined; then if test $board_name = EVK && test $board_rev = 9X9; then setenv fdt_file imx6ull-9x9-evk.dtb; fi; if test $board_name = EVK && test $board_rev = 14X14; then setenv fdt_file imx6ull-14x14-evk.dtb; fi; if test $fdt_file = undefined; then echo WARNING: Could not determine dtb to use; fi; fi;
image=zImage
initrd_addr=0x83800000
initrd_high=0xffffffff
ip_dyn=yes
loadaddr=0x80800000
loadbootscript=fatload mmc ${mmcdev}:${mmcpart} ${loadaddr} ${script};
loadfdt=fatload mmc ${mmcdev}:${mmcpart} ${fdt_addr} ${fdt_file}
loadimage=fatload mmc ${mmcdev}:${mmcpart} ${loadaddr} ${image}
logo_file=alientek.bmp
mfgtool_args=setenv bootargs console=${console},${baudrate} rdinit=/linuxrc g_mass_storage.stall=0 g_mass_storage.removable=1 g_mass_storage.file=/fat g_mass_storage.ro=1 g_mass_storage.idVendor=0x066F g_mass_storage.idProduct=0x37FF g_mass_storage.iSerialNumber="" clk_ignore_unused 
mmcargs=setenv bootargs console=${console},${baudrate} root=${mmcroot}
mmcautodetect=yes
mmcboot=echo Booting from mmc ...; run mmcargs; if test ${boot_fdt} = yes || test ${boot_fdt} = try; then if run loadfdt; then bootz ${loadaddr} - ${fdt_addr}; else if test ${boot_fdt} = try; then bootz; else echo WARN: Cannot load the DT; fi; fi; else bootz; fi;
mmcdev=1
mmcpart=1
mmcroot=/dev/mmcblk1p2 rootwait rw
netargs=setenv bootargs console=${console},${baudrate} root=/dev/nfs ip=dhcp nfsroot=${serverip}:${nfsroot},v3,tcp
netboot=echo Booting from net ...; run netargs; if test ${ip_dyn} = yes; then setenv get_cmd dhcp; else setenv get_cmd tftp; fi; ${get_cmd} ${image}; if test ${boot_fdt} = yes || test ${boot_fdt} = try; then if ${get_cmd} ${fdt_addr} ${fdt_file}; then bootz ${loadaddr} - ${fdt_addr}; else if test ${boot_fdt} = try; then bootz; else echo WARN: Cannot load the DT; fi; fi; else bootz; fi;
panel=ATK-LCD-7-1024x600
script=boot.scr
splashimage=0x88000000
splashpos=m,m

Environment size: 2534/8188 bytes
```

!>printenv命令用于输出环境变量信息。在UBoot中有许多环境变量，例如系统启动时进入UBoot的倒计时就是由bootdelay这个环境变量控制的，如果将其修改成5，进入系统时就会等待5秒。除了bootdelay外，还有很多环境变量，比如baudrate、board_name、board_rec、boot_fdt、bootcmd等等。

### version命令

```shell
$ version

# 输出信息
U-Boot 2016.03-ge468cdc (Mar 29 2021 - 15:59:40 +0800)
arm-poky-linux-gnueabi-gcc (GCC) 5.3.0
GNU ld (GNU Binutils) 2.26.0.20160214
```

!> version命令用于查看UBoot的版本信息，如上，该UBoot版本为20016.03版本，编译器是NXP提供的arm-poky-linux-gnueabi-gcc编译器，编译时间为2021年3月29日。

## **(二)环境变量**

### setenv命令

```shell
$ setenv bootdelay 5						# 设置进入系统等待时间
$ setenv '/dev/mmcblk1p2 rootwait rw'		# 设置带空格的字符串
$ setenv auther	m5xhsy						# 设置自定义环境变量
$ setenv auther								# 删除环境变量
$ setenv -f bootdelay						# 强制设置环境变量
$ setenv -f auther							# 强制删除环境变量
```

!>setenv用于设置或修改环境变量的值，也可以设置自定义环境变量，当设置环境变量的值为空时，就是删除环境变量。该命令需要使用saveenv保存，否则重启会失效。

### saveenv命令

```shell
$ saveenv 

# 输出信息
Saving Environment to MMC...
Writing to MMC(1)... done
```

!>一般环境变量是存放在外部flash中的，uboot启动时会将其读取到DRAM中，所以setenv修改的是DRAM中的值，修改以后要使用saveenv命令将修改后的环境变量保存在flash中。如上，使用该命令保存后会提示将数据写到EMMC(1)中，也即是EMMC设备。

## **(三)内存操作**

### md命令

```shell
$ md.b 0x80000000 0x10		# 查看0x80000000开始往后的0x10个byte长度，也就是16个字节
$ md.w 0x80000000 0x10		# 查看0x80000000开始往后的0x10个word长度，也就是32个字节
$ md.l 0x80000000 0x10		# 查看0x80000000开始往后的0x10个long长度，也就是64个字节
```

!>md命令用于显示内存值。如上b、w和l分别对应byte、word和long，也就是分别以1字节、2字节和4字节来显示；0x80000000表示查看的内存起始地址，0x10表示查看的数据长度，单位是md后面的b、w或l。这里无论是内存地址还是数据长度均已十六进制表示(可以不带0x，但是带上看起来更加直观)。

### nm命令

```shell
$ nm.b 0x80000000			# 修改0x80000000地址1byte的内存值
$ nm.w 0x80000000			# 修改0x80000000地址1word的内存值
$ nm.l 0x80000000			# 修改0x80000000地址1long的内存值

# 示例输出
80000000: 000081a4 ? 00000000
80000000: 00000000 ? q
```

!>nm命令用于修改某一个内存地址的数据值。如上示例输出，冒号前面表示当前修改的内存地址，问号前面表示修改当前内存地址的数据值，问号后面表示输入要改的的数据值，输入确认后还可以重复修改当前地址的内存值，输入q退出修改。

### mm命令

```shell
$ mm.b 0x80000000			# 修改0x80000000地址1byte的内存值
$ mm.w 0x80000000			# 修改0x80000000地址1word的内存值
$ mm.l 0x80000000			# 修改0x80000000地址1long的内存值

# 示例输出
80000000: 000081a4 ? 00001111
80000004: 00000eb1 ? 00002222
80000008: 5d540236 ? 00003333
8000000c: 5d540236 ? q
```

!>mm命令也是用于修改某一个内存地址的数据值，和nm不同的是，修改完某一内存地址的数据后，冒号前面的内存地址会增加一个单位长度，所以可以连续修改一段内存地址。

### mw命令

```shell
$ mw.b 0x80000000 0xff 0x10			# 0x80000000内存地址开始往后填充16个0xff
$ mw.w 0x80000000 0xffff 0x10		# 0x80000000内存地址开始往后填充16个0xffff
$ mw.l 0x80000000 0xffffffff 0x10	# 0x80000000内存地址开始往后填充16个0xffffffff

# 示例输出
# 修改前
80000000: 000081a4 00000eb1 5d540236 5d540236    ........6.T]6.T]
80000010: 5d540236 00000000 00010000 00000008    6.T]............
80000020: 00080000 00000001 0001f30a 00000004    ................
80000030: 00000000 00000000 00000001 00009d34    ............4...
#修改后
80000000: ffffffff ffffffff ffffffff ffffffff    ................
80000010: ffffffff ffffffff ffffffff ffffffff    ................
80000020: ffffffff ffffffff ffffffff ffffffff    ................
80000030: ffffffff ffffffff ffffffff ffffffff    ................
```

!>mw命令用于使用一个指定的数来填充一段内存地址.

### cp命令

```shell
$ cp.l 0x80000010 0x80000000 0x10
$ cp.l 0x80000010 0x80000000 0x10
$ cp.l 0x80000010 0x80000000 0x10

# 示例输出
# 修改前
80000000: 000081a4 00000eb1 5d540236 5d540236    ........6.T]6.T]
80000010: 5d540236 00000000 00010000 00000008    6.T]............
80000020: 00080000 00000001 0001f30a 00000004    ................
80000030: 00000000 00000000 00000001 00009d34    ............4...
#修改后
80000000: 5d540236 00000000 00010000 00000008    6.T]............
80000010: 00080000 00000001 0001f30a 00000004    ................
80000020: 00000000 00000000 00000001 00009d34    ............4...
80000030: 00000000 00000000 00000000 00000000    ................
```

!>cp命令是数据拷贝命令，用于将DRAM中的数据从一段内存拷贝到另外一段内存中，或者把NorFalsh中的数据拷贝到DRAM中。

### cmp命令

```shell
$ cmp.b 0x80000000 0x80000100 0x10		# 比较0x80000000地址开始0x10个byte的内存
$ cmp.w 0x80000000 0x80000100 0x10		# 比较0x80000000地址开始0x10个word的内存
$ cmp.l 0x80000000 0x80000100 0x10		# 比较0x80000000地址开始0x10个long的内存

#输出示例
# 2个地址数据不同时：
word at 0x80000004 (0xeb1) != word at 0x80000104 (0xf48)
Total of 1 word(s) were the same

# 2个地址数据相同时：
Total of 1 word(s) were the same
```

!>cmp命令用于比较两段内存的数据是否相等。如上输出示例，两个内存地址数据不相等时会输出不相等的数据段和值。

## **(四)网络操作**

**在进行网络相关命令操作时，需要对部分环境变量进行设置，如下：**

```shell
$ setenv ipaddr 192.168.1.3
$ setenv ethaddr 6c:ef:c0:12:34:56
$ setenv gatewayip 192.168.1.1
$ setenv netmask 255.255.255.0
$ setenv serverip 192.168.1.7
$ saveenv
```

### ping命令

```shell
$ ping 192.168.1.6

#输出信息
#ping成功
Using FEC1 device
host 192.168.1.6 is alive
#ping失败
Using FEC1 device
ARP Retry count exceeded; starting again
ping failed; host 192.168.1.7 is not alive
```

!>ping命令用于检测网络是否可用，这个命令使用必须设置ipaddr和ethaddr。

### dhcp命令

```shell
$ dhcp										# 自动获取ip并根据上次配置从tftp服务器上获取文件写入内存中
$ dhcp 0x80800000 zImage					# 自动获取ip并根据配置serverip的ftp服务器上获取文件写入内存中
$ dhcp 0x80800000 192.168.1.6:zImage		# 自动获取ip并从tftp服务器上获取文件写入指定地址
```

!>dhcp命令用于从路由器上获取ip地址，需要开发板链接到路由器上。这个命令不仅可以获取ip地址，还会通过TFTP下载镜像，功能和tftpboot命令一样，还可以自动获取IP。

### nfs命令

```shell
$ nfs 0x80800000 192.168.1.6:/home/orz/nfs/zImage	#  从服务器获取文件写入指定内存中

#输出信息
Using FEC1 device
File transfer via NFS from server 192.168.1.6; our IP address is 192.168.1.3
Filename '/home/orz/share/nfs/zImage'.
Load address: 0x80800000
Loading: #################################################################
         #################################################################
         #################################################################
         #################################################################
         #################################################################
         #################################################################
         #################################################################
         #################################################################
         #################################################################
         #################################################################
         #################################################################
         #################################################################
         #################################################################
         #################################################################
         #################################################################
         #################################################################
         #################################################################
         #################################################################
         #################################################################
         #################################################################
         ##########################
done
Bytes transferred = 6785480 (6789c8 hex)
```

!> nfs命令用于通过网络将镜像写进开发板的DRAM中。由于开发板的nfs和ubuntu的版本可能不同，需要在Linux系统中做如下所示的配置。

```shell
# 向etc/hosts文件添加以下内容，其中IP地址为开发板的IP，文件路径为nfs的路径
192.168.1.3 /home/orz/share/nfs/

# 修改/etc/default/nfs-kernel-server文件中如下项
RPCNFSDCOUNT="-V 2 8"
RPCMOUNTDOPTS="-V 2 --manage-gids"
RPCNFSDOPTS="--nfs-version 2,3,4 --debug --syslog"

# 最后重启NFS服务 
$ systemctl restart nfs-kernel-server.service
```

### tftpboot命令

```shell
$ tftp 0x80800000 192.168.1.6:zImage		# 从192.168.1.6服务器上获取zImage写入0x80800000地址中
$ tftpboot 0x80800000 zImage				# 如果设置了环境变量serverip可以省略服务器地址

# 输出信息
Using FEC1 device
TFTP from server 192.168.1.6; our IP address is 192.168.1.3
Filename 'zImage'.
Load address: 0x80800000
Loading: #################################################################
         #################################################################
         #################################################################
         #################################################################
         #################################################################
         #################################################################
         #################################################################
         ########
         2.4 MiB/s
done
Bytes transferred = 6785480 (6789c8 hex)
```

!> tftp命令作用和nfs一样，都是用于通过网络下载文件到DRAM中，只不过tftp是使用TFTP协议

## **(五)MMC操作**

| 命令            | 描述                                         |
| --------------- | -------------------------------------------- |
| mmc info        | 输出MMC 设备信息。                           |
| mmc read        | 读取MMC 中的数据。                           |
| mmc wirte       | 向MMC 设备写入数据。                         |
| mmc rescan      | 扫描MMC 设备。                               |
| mmc part        | 列出MMC 设备的分区。                         |
| mmc dev         | 切换MMC 设备。                               |
| mmc list        | 列出当前有效的所有MMC 设备。                 |
| mmc hwpartition | 设置MMC 设备的分区。                         |
| mmc bootbus……   | 设置指定MMC 设备的 BOOT_BUS_WIDTH 域的值。   |
| mmc bootpart……  | 设置指定MMC 设备的 boot 和 RPMB 分区的大小。 |
| mmc partconf……  | 设置指定MMC 设备的 PARTITION_CONFG 域的值。  |
| mmc rst         | 复位MMC 设备                                 |
| mmc setdsr      | 设置DSR 寄存器的值。                         |

### info命令

```shell
$ mmc info

# 输出信息
Device: FSL_SDHC
Manufacturer ID: 15
OEM: 100
Name: 8GTF4 
Tran Speed: 52000000
Rd Block Len: 512
MMC version 4.0
High Capacity: Yes
Capacity: 7.3 GiB
Bus Width: 8-bit
Erase Group Size: 512 KiB
```

!> info命令主要查看MMC设备的信息，如上设备容量大小为7.3GiB(8G)，8位宽总线。

### rescan命令

```shell
$ mmc rescan
```

!> 该命令用于扫描当前开发板上所有的MMC设备，包括EMMC和SD卡。

### list命令

```shell
$ mmc list

# 输出信息
FSL_SDHC: 0 (SD)
FSL_SDHC: 1 (eMMC)
```

!>list命令用于查看开发版有几块MMC设备。

### dev命令

```shell
$ mmc dev 1				# 切换到第一个mmc设备的分区0
$ mmc dev 1 1			# 切换到第一个mmc设备的分区1

# 输出信息
switch to partitions #0, OK
mmc1(part 0) is current device
```

!> dev命令用于切换MMC设备，dev后第一个参数为设备号，第二个参数为分区号，分区号不设置的话默认为分区0。

### part命令

```shell
$ mmc part

# 输出信息

Partition Map for MMC device 1  --   Partition Type: DOS

Part    Start Sector    Num Sectors     UUID            Type
  1     2048            65536           768150a1-01     0c Boot
  2     67584           15202304        768150a1-02     83
```

!> part命令用于查看MMC设备的分区信息，如上所示，第一个分区起始扇区为2048，长度为65536个扇区；第二个分区起始地址为67584，长度为15202304个扇区。如果MMC设备中烧写Linux系统的话，是有三个分区的，第0个分区存放uboot，第1个分区存放Linux镜像和设备树，第2个分区存放根文件系统。

### read命令

```shell
$ mmc read 0x80800000 0x600 0x10  # 读取从MMC设备0x600个块开始，读取0x10个块到DRAM中的0x80800000地址(这里一个块512字节)
```

!> read命令用于读取mmc设备的数据，read后第一个参数是需要读到DRAM中的地址，第二个是要读取的块起始地址(十六进制)，最后一个参数是尧都区的块数据量(十六进制)。这里可以通过md命令查看读取前后的数据进行验证。

### wirte命令

```shell
# tftp更新uboot
$ mmc list                                       # 查看所有MMC设备
$ mmc dev 1                                      # 切换到EMMC设备
$ mmc info                                       # 查看当前MMC设备信息
$ tftp 0x80800000 192.168.1.6:u-boot.imx         # tptp下载uboot镜像到DRAM中0x80800000位置，显示镜像大小429056比特
$ mmc write 0x80800000 2 346                     # 从DRAM中0x80800000后到0x346个块(429056/512=838=0x346)写入第二个分区(不要写入0和1分区，里面保存分区表)
$ mmc partconf 1 1 0 0                           # 分区配置
```

!> wirte命令可以用来在uboot中更新uboot。注意更新不能写到前2个分区，里面放着分区表信息。

### erase命令

```shell
$ mmc erase 0 1520    

# 输出信息
MMC erase: dev # 1, block # 0, count 5408 ... 

Caution! Your devices Erase group is 0x400
The erase range would be change to 0x0~0x17ff

5408 blocks erased: OK
```

!> erase命令用于擦除MMC设备。erase后第一个参数为要擦除的起始地址，第二个参数为要擦除的大小。建议没事不要用erase擦除MMC设备。

## **(六)FAT文件操作**

### fatinfo命令

```shell
$ fatinfo <interface> [<dev[:part]>]	
$ fatinfo mmc 1:1		# 查看mmc设备1的第1个分区信息

#输出信息
Interface:  MMC
  Device 1: Vendor: Man 000015 Snr 82dc4278 Rev: 0.6 Prod: 8GTF4R
            Type: Removable Hard Disk
            Capacity: 7456.0 MB = 7.2 GB (15269888 x 512)
Filesystem: FAT32 "NO NAME    "
```

!> fatinfo命令用于查看指定mmc设备分区的文件系统信息，interface表示接口，dev表示查询的设备号，part表示查询的分区。如上EMMC分区1的文件系统未FAT32格式的。

### fatls命令

```shell
$ fatls <interface> [<dev[:part]>] [directory]
$ fatls mmc 1:1 				# 查看mmc设备1分区1的所有文件和目录
#输出信息
  6785480   zimage 
    39327   imx6ull-14x14-emmc-4.3-480x272-c.dtb 
    39327   imx6ull-14x14-emmc-4.3-800x480-c.dtb 
    39327   imx6ull-14x14-emmc-7-800x480-c.dtb 
    39327   imx6ull-14x14-emmc-7-1024x600-c.dtb 
    39327   imx6ull-14x14-emmc-10.1-1280x800-c.dtb 
    40159   imx6ull-14x14-emmc-hdmi.dtb 
    40067   imx6ull-14x14-emmc-vga.dtb 

8 file(s), 0 dir(s)
```

!> fatls命令用于查询FAT格式设备的目录和文件信息，interface表示接口，dev表示查询的设备号，part表示查询的分区。directory为目录名称，没有目录可以不写。

### fstype命令

```shell
$ fstype <interface> <dev>:<part>
$ fstype mmc 1:0		# 输出mmc设备1的第0个分区类型	未知
$ fstype mmc 1:1		# 输出mmc设备1的第0个分区类型	fat
$ fstype mmc 1:2		# 输出mmc设备1的第0个分区类型	ext4
```

!> fstype命令用于查看设备某个分区的格式,interface表示接口，dev表示查询的设备号，part表示查询的分区。如上分区0存放uboot并且没有格式化，类型是未知的；分区1格式为fat，用来存放设备树和系统镜像；分区2用来存放文件系统，格式为ext4。

### fatload命令

```shell
$ fatload <interface> [<dev[:part]> [<addr> [<filename> [bytes [pos]]]]]
$ fatload mmc 1:1 0x80800000 zImage		# 将mmc设备1的分区1中zImage读取到DRAM中

# 输出信息
reading zimage
6785480 bytes read in 222 ms (29.1 MiB/s)
```

!> fatload命令用于将文件读取到DRAM中，insterfac为接口，dev是设备号，part是分区，addr表示保存在DRAM中的地址，filename是要读取文件的名字，bytes表示要读取的文件字节数，pos表示要读取文件相对于文件首地址的偏移。如上所示，将zImage读取到DRAM中的0x80800000地址处。

### fatwrite命令

该命令在uboot中默认没有开启的需要修改开发板配置文件，例如mx6ullevk.h\mx6ull_alientek_emmc.h文件，在其配置文件中添加**#define CONFIG_FAT_WRITE**来开启此命令。

```shell
$ fatwrite <interface> <dev[:part]> <addr> <filename> <bytes>
$ fatwrite mmc 1:1 0x80800000 zImage 0x6788f8

# 输出信息
writing test
6785272 bytes written
```

!> fatwrite命令用于将DRAM中的数据写到MMC设备中，insterfac为接口，dev是设备号，part是分区，addr表示读取DRAM中的起始地址，filename是要写的文件的名字，bytes表示要写的文件字节数。如上，将DRAM中0x80800000处开始读取0x6788f8个字节写到MMC设备zImage中。

## **(七)EXT文件操作**

### ext4ls/ext2ls命令

```shell
$ ext4ls <interface> <dev[:part]> [directory]
$ ext4ls mmc 1:2 	# 查看MMC设备分区2的文件

# 输出信息
<DIR>       4096 .
<DIR>       4096 ..
<DIR>      16384 lost+found
<DIR>       4096 bin
<DIR>       4096 boot
<DIR>       4096 dev
<DIR>       4096 etc
<DIR>       4096 home
<DIR>       4096 lib
<DIR>       4096 media
<DIR>       4096 mnt
<DIR>       4096 opt
<DIR>       4096 proc
<DIR>       4096 run
<DIR>       4096 sbin
<DIR>       4096 sys
<SYM>          8 tmp
<DIR>       4096 usr
<DIR>       4096 var
```

!> ext4ls/ext2ls命令用于查看ext文件系统的文件。interface表示接口，dev表示查询的设备号，part表示查询的分区。directory为目录名称，没有目录可以不写。

### ext4load/ext2load命令

```shell
$ ext4load <interface> [<dev[:part]> [addr [filename [bytes [pos]]]]]
$ ext4load mmc 1:2 0x80800000 /etc/passwd 

# 输出信息
ext4load mmc 1:2 0x80800000 /etc/passwd 
1061 bytes read in 570 ms (1000 Bytes/s)
```

!> ext4load/ext2load命令用于将文件读取到DRAM中，insterfac为接口，dev是设备号，part是分区，addr表示保存在DRAM中的地址，filename是要读取文件的名字，bytes表示要读取的文件字节数，pos表示要读取文件相对于文件首地址的偏移。如上所示，将/etc/passwd文件读取到DRAM中的0x80800000地址处。

### ext4write命令

```shell
$ ext4write <interface> <dev[:part]> <addr> <absolute filename path> [sizebytes] [file offset]
$ ext4write mmc 1:2 0x80800000 /var/passwd 0x425

# 输出信息
File System is consistent
update journal finished
1061 bytes written in 1106 ms (0 Bytes/s)
```

!> ext4write命令用于将DRAM中的数据写到MMC设备中，insterfac为接口，dev是设备号，part是分区，addr表示读取DRAM中的起始地址，absolute filename path是要写的文件的路径，bytes表示要写的文件字节数，file offset表示文件偏移地址。如上，将DRAM中0x80800000处开始读取0x425个字节写到MMC设备分区2的/var/passwd中。

## **(八)BOOT命令**

### bootz命令

```shell
$ bootz [addr [initrd[:size]] [fdt]]

$ tftp 0x80800000 192.168.1.6:zImage
$ tftp 0x83000000 192.168.1.6:imx6ull-14x14-emmc-7-1024x600-c.dtb
$ bootz 0x80800000 - 0x83000000

# 输出信息
=> bootz 0x80800000 - 0x83000000
Kernel image @ 0x80800000 [ 0x000000 - 0x6789c8 ]
## Flattened Device Tree blob at 83000000
   Booting using the fdt blob at 0x83000000
   Using Device Tree in place at 83000000, end 8300c99e
Starting kernel ...
```

!> bootz命令用于启动DRAM中的zImage镜像，addr表示linux镜像在DRAM中的位置，initrd是initrd文件在DRAM中的地址，如果不使用initrd的话使用“-”代替即可，fdt是设备树文件在DRAM中的地址。如上将内核镜像下载到0x80800000地址，设备树下载到0x83000000地址，通过bootz启动内核。

### bootm命令

```shell
$ bootm [addr [arg ...]]
$ bootm 0x80800000
```

!> bootm命令和bootz命令功能相似，如果不使用设备树,addr就是uImage镜像文件在DRAM中的首地址，使用设备树的话命令格式和bootz一样。(uImage是U-boot专用镜像文件，它是在zImage前面加上一个0x40长度的TAG)。

### boot命令

```shell
$ setenv bootcmd 'tftp 0x80800000 zImage;tftp 0x83000000 imx6ull-14x14-emmc-7-1024x600-c.dtb;bootz 0x80800000 - 0x83000000'
$ saveenv
$ boot
```

!> boot命令也是用于启动Linux系统的，只是boot会读取环境变量中的bootcmd来启动linux系统。在linux系统启动倒计时后，就是通过bootcmd环境变量来启动内核的。



## **(九)其他命令**

### reset命令

```shell
$ reset
```

!> reset命令用于复位重启设备。

### go命令

```shell
$ go addr [arg ...]

$ tftp 0x87800000 192.168.1.6:led.bin
$ go 0x87800000
```

!> go命令用于跳转到指定地址执行应用，addr表示应用在DRAM中的首地址。例如，将led的bin文件下载到指定地址，然后通过go命令来执行。

### run命令

```shell
$ run var [...]
$ rub bootcmd
```

!> run命令用于运行环境变量中定义的命令，比如通过如上命令来运行bootcmd变量。与boot命令不同的是，run命令可以运行我们自定义的环境变量，例如在系统调试过程中通常要通过网络启动和EMMC/NAND启动之间切换，而boot只能保存一种启动方式，就会比较麻烦。

### mtest命令

```shell
$ mtest [start [end [pattern [iterations]]]]
$ mtest 0x80000000 0x80001000 					
```

!> mtest用于内存测试，可以用来测试开发板上的DDR，start表示要测试的起始地址，end表示要测试的结束地址，pattern表示要写入的数据，iterations表示需要测试的次数。不写pattern和iterations默认写入0xFFFFFFFF，一直测试，结束使用"CTRL+C"组合键。
