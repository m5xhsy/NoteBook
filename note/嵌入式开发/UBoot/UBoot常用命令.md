# UBoot常用命令

!> 进入Uboot后可以通过**help**或者**?**命令查看Uboot支持的所有命令，命令的详细信息可以在**help**或**?**后面加需要查看的命令查看。

## 信息查询

### bdinfo命令

```shell
$ bdinfo

# 命令输出信息：
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

!>**bdinfo主要用于查询开发板相关信息，例如DRAM的起始地址和大小、启动参数保存起始地址、波特率、sp堆栈指针的起始地址等信息。**

### printenv命令


```shell
$ printenv

# 命令输出
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

!>**printenv命令用于输出环境变量信息。在UBoot中有许多环境变量，例如系统启动时进入UBoot的倒计时就是由bootdelay这个环境变量控制的，如果将其修改成5，进入系统时就会等待5秒。除了bootdelay外，还有很多环境变量，比如baudrate、board_name、board_rec、boot_fdt、bootcmd等等。**

### version命令

```shell
$ version

# 命令输出
U-Boot 2016.03-ge468cdc (Mar 29 2021 - 15:59:40 +0800)
arm-poky-linux-gnueabi-gcc (GCC) 5.3.0
GNU ld (GNU Binutils) 2.26.0.20160214
```

!> **version命令用于查看UBoot的版本信息，如上，该UBoot版本为20016.03版本，编译器是NXP提供的arm-poky-linux-gnueabi-gcc编译器，编译时间为2021年3月29日。**

## 环境变量

### setenv命令

```shell
$ setenv bootdelay 5						# 设置进入系统等待时间
$ setenv '/dev/mmcblk1p2 rootwait rw'		# 设置带空格的字符串
$ setenv auther	m5xhsy						# 设置自定义环境变量
$ setenv auther								# 删除环境变量
```

!>**setenv用于设置或修改环境变量的值，也可以设置自定义环境变量，当设置环境变量的值为空时，就是删除环境变量。该命令需要使用saveenv保存，否则重启会失效。**

### saveenv命令

```shell
$ saveenv 

# 命令输出
Saving Environment to MMC...
Writing to MMC(1)... done
```

!>**一般环境变量是存放在外部flash中的，uboot启动时会将其读取到DRAM中，所以setenv修改的是DRAM中的值，修改以后要使用saveenv命令将修改后的环境变量保存在flash中。如上，使用该命令保存后会提示将数据写到EMMC(1)中，也即是EMMC设备。**

## 内存操作

### md命令

### nm命令

### mm命令

### mw命令

### cp命令

### cmp命令
