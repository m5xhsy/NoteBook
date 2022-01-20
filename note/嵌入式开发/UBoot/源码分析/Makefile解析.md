# Makefile解析

## 1.版本号

顶层Makefile文件一开始就是版本号,`VERSION`是主版本号，`PATCHLEVEL`是补丁版本号，`SYUBLEVEL`是次版本号，这三个版本号一起构成uboot的版本号，比如下图所示版本号为2016.03。`EXTRAVERSION`是附加的版本信息，NAME和名字有关，一般不使用这2个。

```makefile
VERSION = 2016
PATCHLEVEL = 03
SUBLEVEL =
EXTRAVERSION =
NAME =
```

## 2.特殊变量

Makefile中有2个特殊变量`SHELL`和`MAKEFLAGS`，这2个变量除非使用`unexport`声明，否则在整个make的执行过程中，他们的值都会始终传给子Makefile。

```makefile
# o Do not use make's built-in rules and variables
#   (this increases performance and avoids hard-to-debug behaviour);
# o Look for make include files relative to root of kernel src
MAKEFLAGS += -rR --include-dir=$(CURDIR)
```

如上所示代码，`MAKEFLAGS`变量追加了一些值，其中`-rR`表示禁用内置的隐含规则和变量定义，`--include-dir`指明搜索路径为`$(CURDIR)`，也就是当前的目录。

## 3.语言环境

```makefile
# Avoid funny character set dependencies
unexport LC_ALL
LC_COLLATE=C
LC_NUMERIC=C
export LC_COLLATE LC_NUMERIC
```

`LC_ALL`这个变量如果设置了，则会覆盖所有的`LC_*`的设置值，这里的`unexport`相对于清除了这个全局选项，`LC_COLLATE=C`则定义了排序和比较规则以C的方式进行，`LC_NUMERIC`表示非货币的数字显示格式以C的方式进行。

## 4.grep高亮

```makefile
# Avoid interference with shell env settings
unexport GREP_OPTIONS
```

这个grep变量取消后可避免当前shell环境变量对编译的影响，去除grep命令的配置选项。例如有些版本运行环境中有定义此变量，但是grep命令对该变量不支持，就会报错`grep: warning: GREP_OPTIONS is deprecated; please use an alias or script`，如果不取消的话将会导致编译失败。

## 5.编译输出控制

```makefile
# A simple variant is to prefix commands with $(Q) - that's useful
# for commands that shall be hidden in non-verbose mode.
#
#	$(Q)ln $@ :<
#
# If KBUILD_VERBOSE equals 0 then the above command will be hidden.
# If KBUILD_VERBOSE equals 1 then the above command is displayed.
#
# To put more focus on warnings, be less verbose as default
# Use 'make V=1' to see the full commands

ifeq ("$(origin V)", "command line")
  KBUILD_VERBOSE = $(V)
endif
ifndef KBUILD_VERBOSE
  KBUILD_VERBOSE = 0
endif

ifeq ($(KBUILD_VERBOSE),1)
  quiet =
  Q =
else
  quiet=quiet_
  Q = @
endif
```

通过`make V=1` 可以对输出进行控制，上述代码中使用`ifeq`来判断`$(origin V)`和`command line`是否相等，即判断`V`这个变量的值是不是来源于命令行的输入，来源于命令行的话则将`V`赋值给`KBUILD_VERBOSE`，如果没有赋值的话就赋值为0，最后对`KBUILD_VERBOSE`这个变量进行判断，如果为1的话，`quiet`和`Q`都为空；如果为0的话`quiet`等于`quiet_`，`Q`为`@`符号。例如`$(Q)$(MAKE) $(build)=tools`,将其展开后就是`@make $(build)=tools`，Makefile中如果在命令前面加个`@`就不会在终端输出命令了，所以该命令也不会输出到屏幕上。有些命令有2个版本，如`quiet_cmd_sym?=SYM  $@`和`cmd_sym?=$(OBJDUMP) -t $< > $@`，这2个命令执行的结果都是一样的，但是`quiet_cmd_xxx`命令输出的信息比较少，也就是短命令。总结一下就是`quiet`为空则全部输出，为`quiet_`的话仅输出短命令，为`silent_`整个命令都不会输出。

## 6.静默输出

```makefile
# If the user is running make -s (silent mode), suppress echoing of
# commands

ifneq ($(filter 4.%,$(MAKE_VERSION)),)	# make-4
ifneq ($(filter %s ,$(firstword x$(MAKEFLAGS))),)
  quiet=silent_
endif
else					# make-3.8x
ifneq ($(filter s% -s%,$(MAKEFLAGS)),)
  quiet=silent_
endif
endif

export quiet Q KBUILD_VERBOSE
```

在编译uboot的时候如果不需要输出的话可以用`make -s`来使用静默输出功能，其实现如上所示代码，首先先过滤`MAKE_VERSION`变量中版本号，也就是make工具的版本号是不是匹配`4.%`，其中`%`为通配符，`ifneq($(filter 4.%, $(MAKE_VERSION)),)`这一行表示过滤出来的值不等于空则成立，也就是版本号为4.x，否则的话则是版本3.8x；命令行加入-s选项编译后会将`s`拼接进`MAKEFLASGS`变量，如果版本号为4.x则多加了一个`firstword`函数获取第一个单词，然后用`filter`函数过滤，不等于空则将`silent_`赋值给`quiet`，最后用`export`导出`quiet`、`Q`和`KBUILD_VERSION`。

## 7.输出目录

```makefile
# kbuild supports saving output files in a separate directory.
# To locate output files in a separate directory two syntaxes are supported.
# In both cases the working directory must be the root of the kernel src.
# 1) O=
# Use "make O=dir/to/store/output/files/"
#
# 2) Set KBUILD_OUTPUT
# Set the environment variable KBUILD_OUTPUT to point to the directory
# where the output files shall be placed.
# export KBUILD_OUTPUT=dir/to/store/output/files/
# make
#
# The O= assignment takes precedence over the KBUILD_OUTPUT environment
# variable.

# KBUILD_SRC is set on invocation of make in OBJ directory
# KBUILD_SRC is not intended to be used by the regular user (for now)
ifeq ($(KBUILD_SRC),)

# OK, Make called in directory where kernel src resides
# Do we want to locate output files in a separate directory?
ifeq ("$(origin O)", "command line")
  KBUILD_OUTPUT := $(O)
endif

# That's our default target when none is given on the command line
PHONY := _all
_all:

# Cancel implicit rules on top Makefile
$(CURDIR)/Makefile Makefile: ;

ifneq ($(KBUILD_OUTPUT),)
# Invoke a second make in the output directory, passing relevant variables
# check that the output directory actually exists
saved-output := $(KBUILD_OUTPUT)
KBUILD_OUTPUT := $(shell mkdir -p $(KBUILD_OUTPUT) && cd $(KBUILD_OUTPUT) \
								&& /bin/pwd)
$(if $(KBUILD_OUTPUT),, \
     $(error failed to create output directory "$(saved-output)"))

# Look for make include files relative to root of kernel src
#
# This does not become effective immediately because MAKEFLAGS is re-parsed
# once after the Makefile is read.  It is OK since we are going to invoke
# 'sub-make' below.
MAKEFLAGS += --include-dir=$(CURDIR)

PHONY += $(MAKECMDGOALS) sub-make

$(filter-out _all sub-make $(CURDIR)/Makefile, $(MAKECMDGOALS)) _all: sub-make
	@:

sub-make: FORCE
	$(Q)$(MAKE) -C $(KBUILD_OUTPUT) KBUILD_SRC=$(CURDIR) \
	-f $(CURDIR)/Makefile $(filter-out _all sub-make,$(MAKECMDGOALS))

# Leave processing to above invocation of make
skip-makefile := 1
endif # ifneq ($(KBUILD_OUTPUT),)
endif # ifeq ($(KBUILD_SRC),)
```

uboot可以将编译出来的文件输出到单独的目录中，在make时使用`O`来指定输出目录，例如`make O=out`，就是将目标文件输出到out目录中去，这样可以将源文件和目标文件分开，如果不指定的话源文件和编译产生的文件都在同一个目录下。在编译过程中首先会判断变量`O`是否来源于命令行，如果是命令行的话将输出目录赋值给`KBUILD_OUTPUT`,然后对该变量进行检查是否为空。接着又把`KBUILD_OUTPUT`赋值给`saved-output`，最后使用`mkdir`创建目录，并进入该文件夹，执行`/bin/pwd`命令将该文件夹的绝对路径赋值给`KBUILD_OUTPUT`。至此，通过`O`指定的输出目录就存在了。

## 8.代码检查

```makefile
# Call a source code checker (by default, "sparse") as part of the
# C compilation.
#
# Use 'make C=1' to enable checking of only re-compiled files.
# Use 'make C=2' to enable checking of *all* source files, regardless
# of whether they are re-compiled or not.
#
# See the file "Documentation/sparse.txt" for more details, including
# where to get the "sparse" utility.

ifeq ("$(origin C)", "command line")
  KBUILD_CHECKSRC = $(C)
endif
ifndef KBUILD_CHECKSRC
  KBUILD_CHECKSRC = 0
endif
```

uboot编译时使用`make C=1`可以使能代码检查，检查需要重新编译的文件，`make C=2`可以检查所有的源码文件，代码如上所示，先判断`C`是否源于命令行，来自命令行的话就将`C`赋值给变量`KBUILD_CHECKSRC`，如果命令行没有`C`的话变量`KBUILD_CHECKSRC`就为0。

## 9.模块编译

```makefile
# Use make M=dir to specify directory of external module to build
# Old syntax make ... SUBDIRS=$PWD is still supported
# Setting the environment variable KBUILD_EXTMOD take precedence
ifdef SUBDIRS
  KBUILD_EXTMOD ?= $(SUBDIRS)
endif

ifeq ("$(origin M)", "command line")
  KBUILD_EXTMOD := $(M)
endif

# If building an external module we do not care about the all: rule
# but instead _all depend on modules
PHONY += all
ifeq ($(KBUILD_EXTMOD),)
_all: all
else
_all: modules
endif
```

uboot可以单独编译某个模块，使用命令`make M=dir`，以前也可以使用旧版语法`make SUBDIRS=dir`。代码如上所示，首先原来判断是否定义了`SUBDIRS`，这里是为了支持老语法。接着判断变量`M`是否源于命令行，如果有定义则将`$(M)`赋值给`KBUILD_EXTMOD`。如果`KBUILD_EXTMOD`为空的话目标`_all`依赖`all`，否则的话默认目标`_all`依赖`modules`，要先编译模块。

## 10.主机架构

```makefile
HOSTARCH := $(shell uname -m | \
	sed -e s/i.86/x86/ \
	    -e s/sun4u/sparc64/ \
	    -e s/arm.*/arm/ \
	    -e s/sa110/arm/ \
	    -e s/ppc64/powerpc/ \
	    -e s/ppc/powerpc/ \
	    -e s/macppc/powerpc/\
	    -e s/sh.*/sh/)

HOSTOS := $(shell uname -s | tr '[:upper:]' '[:lower:]' | \
	    sed -e 's/\(cygwin\).*/cygwin/')

export	HOSTARCH HOSTOS
```

`HOSTARCH`用于保存主机架构，这里调用了shell命令`uname -m`获取架构名称，例如`x86_64`系统获取后通过管道传到`sed`命令进行替换；`HOSTOS`表示主机的系统，如`Linux`系统获取系统名称后通过管道将传到`tr`将大写字母换成小写，最后使用`sed`将`(cygwin).*`替换成`cygwin`，再将2个变量导出。

## 11.编译工具

```makefile
# set default to nothing for native builds
ifeq ($(HOSTARCH),$(ARCH))
CROSS_COMPILE ?=
endif

ARCH = arm
CROSS_COMPILE = arm-linux-gnueabihf-
```

在编译uboot的时候需要设置目标板架构和交叉编译器，`make ARCH=arm CROSS_COMPILE=arm-linux-gnueabihf-`就是在命令行设置的，在Makefile中也可以对其设置，如果`HOSTARCH`和`ARCH`是相等的，`CROSS_COMPILE`则不会被设置，所以可以在下面加一行`CROSS_COMPILE`和`ARCH`的定义，就不用每次编译时输入了，下面代码是对编译工具具体变量的设置。

```makefile
# Make variables (CC, etc...)

AS		= $(CROSS_COMPILE)as
# Always use GNU ld
ifneq ($(shell $(CROSS_COMPILE)ld.bfd -v 2> /dev/null),)
LD		= $(CROSS_COMPILE)ld.bfd
else
LD		= $(CROSS_COMPILE)ld
endif
CC		= $(CROSS_COMPILE)gcc
CPP		= $(CC) -E
AR		= $(CROSS_COMPILE)ar
NM		= $(CROSS_COMPILE)nm
LDR		= $(CROSS_COMPILE)ldr
STRIP		= $(CROSS_COMPILE)strip
OBJCOPY		= $(CROSS_COMPILE)objcopy
OBJDUMP		= $(CROSS_COMPILE)objdump
```

## 12.导出变量

在顶层Makefile中会导出很多变量，如下所示：

```makefile
export VERSION PATCHLEVEL SUBLEVEL UBOOTRELEASE UBOOTVERSION
export ARCH CPU BOARD VENDOR SOC CPUDIR BOARDDIR
export CONFIG_SHELL HOSTCC HOSTCFLAGS HOSTLDFLAGS CROSS_COMPILE AS LD CC
export CPP AR NM LDR STRIP OBJCOPY OBJDUMP
export MAKE AWK PERL PYTHON
export HOSTCXX HOSTCXXFLAGS DTC CHECK CHECKFLAGS

export KBUILD_CPPFLAGS NOSTDINC_FLAGS UBOOTINCLUDE OBJCOPYFLAGS LDFLAGS
export KBUILD_CFLAGS KBUILD_AFLAGS
```

其中有几个变量在前面Makefile中找不到，是由其他文件中导出来的，例如`ARCH`、`CPU`、`BOARD`、`VENDOR`、`SOC`、`CPUDIR`、`BOARDDIR`将这几个变量打印出来后如下所示：

```makefile
ARCH=arm
CPU=armv7
BOARD=mx6ullevk
VENDOR=freescale
SOC=mx6
CPUDIR=arch/arm/cpu/armv7
BOARDDIR=freescale/mx6ullevk
```

这几个变量是定义在Makefile同级目录下的`config.mk`文件中，内容如下:

```makefile
#
# (C) Copyright 2000-2013
# Wolfgang Denk, DENX Software Engineering, wd@denx.de.
#
# SPDX-License-Identifier:	GPL-2.0+
#
#########################################################################

# This file is included from ./Makefile and spl/Makefile.
# Clean the state to avoid the same flags added twice.
#
# (Tegra needs different flags for SPL.
#  That's the reason why this file must be included from spl/Makefile too.
#  If we did not have Tegra SoCs, build system would be much simpler...)
PLATFORM_RELFLAGS :=
PLATFORM_CPPFLAGS :=
PLATFORM_LDFLAGS :=
LDFLAGS :=
LDFLAGS_FINAL :=
OBJCOPYFLAGS :=
# clear VENDOR for tcsh
VENDOR :=
#########################################################################

ARCH := $(CONFIG_SYS_ARCH:"%"=%)
CPU := $(CONFIG_SYS_CPU:"%"=%)
ifdef CONFIG_SPL_BUILD
ifdef CONFIG_TEGRA
CPU := arm720t
endif
endif
BOARD := $(CONFIG_SYS_BOARD:"%"=%)
ifneq ($(CONFIG_SYS_VENDOR),)
VENDOR := $(CONFIG_SYS_VENDOR:"%"=%)
endif
ifneq ($(CONFIG_SYS_SOC),)
SOC := $(CONFIG_SYS_SOC:"%"=%)
endif

# Some architecture config.mk files need to know what CPUDIR is set to,
# so calculate CPUDIR before including ARCH/SOC/CPU config.mk files.
# Check if arch/$ARCH/cpu/$CPU exists, otherwise assume arch/$ARCH/cpu contains
# CPU-specific code.
CPUDIR=arch/$(ARCH)/cpu$(if $(CPU),/$(CPU),)

sinclude $(srctree)/arch/$(ARCH)/config.mk	# include architecture dependend rules
sinclude $(srctree)/$(CPUDIR)/config.mk		# include  CPU	specific rules

ifdef	SOC
sinclude $(srctree)/$(CPUDIR)/$(SOC)/config.mk	# include  SoC	specific rules
endif
ifneq ($(BOARD),)
ifdef	VENDOR
BOARDDIR = $(VENDOR)/$(BOARD)
else
BOARDDIR = $(BOARD)
endif
endif
ifdef	BOARD
sinclude $(srctree)/board/$(BOARDDIR)/config.mk	# include board specific rules
endif

ifdef FTRACE
PLATFORM_CPPFLAGS += -finstrument-functions -DFTRACE
endif

# Allow use of stdint.h if available
ifneq ($(USE_STDINT),)
PLATFORM_CPPFLAGS += -DCONFIG_USE_STDINT
endif

#########################################################################

RELFLAGS := $(PLATFORM_RELFLAGS)

PLATFORM_CPPFLAGS += $(RELFLAGS)
PLATFORM_CPPFLAGS += -pipe

LDFLAGS += $(PLATFORM_LDFLAGS)
LDFLAGS_FINAL += -Bstatic

export PLATFORM_CPPFLAGS
export RELFLAGS
export LDFLAGS_FINAL
export CONFIG_STANDALONE_LOAD_ADDR
```

`ARCH`变量由`ARCH := $(CONFIG_SYS_ARCH:"%"=%)`提取出来，表示`ARCH`等于双引号中匹配的字符串，其他变量也是。`sinclude $(srctree)/arch/$(ARCH)/config.mk`表示读取指定文件中的内容，和`include`不同的是读取不到也不会报错。文件中`CONFIG_SYS_ARCH`这些变量的值在根目录下的`.config`文件中有定义。在`config.mk`文件中还导入了其他文件，如下：

```makefile
arch/arm/config.mk 
arch/arm/cpu/armv7/config.mk 
arch/arm/cpu/armv7/mx6/config.mk (此文件不存在) 
board/freescale/mx6ullevk/config.mk (此文件不存在)
```

## 13.defconfig预配置

在编译`uboot`前要使用`make xxx_defconfig`来配置uboot，具体代码如下：

```makefile
# To make sure we do not include .config for any of the *config targets
# catch them early, and hand them over to scripts/kconfig/Makefile
# It is allowed to specify more targets when calling make, including
# mixing *config targets and build targets.
# For example 'make oldconfig all'.
# Detect when mixed targets is specified, and make a second invocation
# of make so .config is not included in this case either (for *config).

version_h := include/generated/version_autogenerated.h
timestamp_h := include/generated/timestamp_autogenerated.h

no-dot-config-targets := clean clobber mrproper distclean \
			 help %docs check% coccicheck \
			 ubootversion backup

config-targets := 0
mixed-targets  := 0
dot-config     := 1

ifneq ($(filter $(no-dot-config-targets), $(MAKECMDGOALS)),)
	ifeq ($(filter-out $(no-dot-config-targets), $(MAKECMDGOALS)),)
		dot-config := 0
	endif
endif

ifeq ($(KBUILD_EXTMOD),)
        ifneq ($(filter config %config,$(MAKECMDGOALS)),)
                config-targets := 1
                ifneq ($(words $(MAKECMDGOALS)),1)
                        mixed-targets := 1
                endif
        endif
endif

ifeq ($(mixed-targets),1)
# ===========================================================================
# We're called with mixed targets (*config and build targets).
# Handle them one by one.

PHONY += $(MAKECMDGOALS) __build_one_by_one

$(filter-out __build_one_by_one, $(MAKECMDGOALS)): __build_one_by_one
	@:

__build_one_by_one:
	$(Q)set -e; \
	for i in $(MAKECMDGOALS); do \
		$(MAKE) -f $(srctree)/Makefile $$i; \
	done

else
ifeq ($(config-targets),1)
# ===========================================================================
# *config targets only - make sure prerequisites are updated, and descend
# in scripts/kconfig to make the *config target

KBUILD_DEFCONFIG := sandbox_defconfig
export KBUILD_DEFCONFIG KBUILD_KCONFIG

config: scripts_basic outputmakefile FORCE
	$(Q)$(MAKE) $(build)=scripts/kconfig $@

%config: scripts_basic outputmakefile FORCE
	$(Q)$(MAKE) $(build)=scripts/kconfig $@

else
# ===========================================================================
# Build targets only - this includes vmlinux, arch specific targets, clean
# targets and others. In general all targets except *config targets.

ifeq ($(dot-config),1)
# Read in config
-include include/config/auto.conf
......
```

首先定义了`version_h`来保存版本号文件的路径`include/generated/version_autogenerated.h`，这个文件是自动生成的，内容如下所示：

```c
#define PLAIN_VERSION "2016.03"
#define U_BOOT_VERSION "U-Boot " PLAIN_VERSION
#define CC_VERSION_STRING "arm-linux-gnueabihf-gcc (Linaro GCC 7.5-2019.12) 7.5.0"
#define LD_VERSION_STRING "GNU ld (Linaro_Binutils-2019.12) 2.28.2.20170706"
```

然后定义了`timestamp_h`变量来保存时间戳文件路径`include/generated/timestamp_autogenerated.h`，这个文件也是自动生成，内容如下所示：

```c
#define U_BOOT_DATE "Dec 20 2021"
#define U_BOOT_TIME "23:25:25"
#define U_BOOT_TZ "+0800"
#define U_BOOT_DMI_DATE "12/20/2021"
```

然后定义`no-dot-config-targets`保存`clean clobber mrproper distclean help %docs check% coccicheck ubootversion backup`这些不需要依赖`.config`文件即可构建的目标。`config-targets`变量用来记录当前是否需要重新构建`.config`文件，如果编译时指定了`%config`作为目标，就会设置这个变量。`mixed-targets`变量表示make中是否指定了多种类型的目标，如果存在就会设置这个变量开启混合模式。`dot-config`变量表示当前编译是否要引入`.config`中的配置项变量，例如`make help`就不需要引入`.config`。

```makef
ifneq ($(filter $(no-dot-config-targets), $(MAKECMDGOALS)),)
	ifeq ($(filter-out $(no-dot-config-targets), $(MAKECMDGOALS)),)
		dot-config := 0
	endif
endif
```

如上代码`MAKECMDGOALS`变量是用来保存命令行中传入的值，如果指定了`no-dot-config-targets`中的一个或多个变量，且没有指定该变量外的目标则设置`dot-config:=0`，表示后续不需要在`Makefile`中包含`.config`文件中的CONFIG宏定义变量。

```makefile
ifeq ($(KBUILD_EXTMOD),)
        ifneq ($(filter config %config,$(MAKECMDGOALS)),)
                config-targets := 1
                ifneq ($(words $(MAKECMDGOALS)),1)
                        mixed-targets := 1
                endif
        endif
endif
```

如果没有指定`M=`且指定了`%config`则设置`config-targets:=1`表示要重建`.config`文件，如果在指定了`%config`的情况下如果命令行输入数大于1，则设置`mixed-targets`

```makefile
ifeq ($(mixed-targets),1)
# ===========================================================================
# We're called with mixed targets (*config and build targets).
# Handle them one by one.

PHONY += $(MAKECMDGOALS) __build_one_by_one

$(filter-out __build_one_by_one, $(MAKECMDGOALS)): __build_one_by_one
	@:

__build_one_by_one:
	$(Q)set -e; \
	for i in $(MAKECMDGOALS); do \
		$(MAKE) -f $(srctree)/Makefile $$i; \
	done
```

如果设置了`mixed-targets`则会将所有目标和`__build_one_by_one`设置成伪目标，然后将所有目标置空，后只执行`__build_one_by_one`这一个伪目标，`$(Q)set -e;`表示命令以非0的状态退出时则退出shell，然后遍历`MAKECMDGOALS`中的目标，对每一个目标都做一个make的单独目标，也就是说如果是混合目标，就会一个一个的去执行submake编译。

```makefile
ifeq ($(config-targets),1)
# ===========================================================================
# *config targets only - make sure prerequisites are updated, and descend
# in scripts/kconfig to make the *config target

KBUILD_DEFCONFIG := sandbox_defconfig
export KBUILD_DEFCONFIG KBUILD_KCONFIG

config: scripts_basic outputmakefile FORCE
	$(Q)$(MAKE) $(build)=scripts/kconfig $@

%config: scripts_basic outputmakefile FORCE
	$(Q)$(MAKE) $(build)=scripts/kconfig $@
```

当编译时`%config`目标会依赖`scripts_basic`、`outputmakefile`和`FORCE`，`FORCE`是一个空目标，在前面有定义，每次执行都会重新生成`FORCE`，因此依赖所在的规则总是被执行。而`scripts_basic`、`outputmakefile`在顶层定义如下：

```makefile
# Basic helpers built in scripts/
PHONY += scripts_basic
scripts_basic:
	$(Q)$(MAKE) $(build)=scripts/basic
	$(Q)rm -f .tmp_quiet_recordmcount

# To avoid any implicit rule to kick in, define an empty command.
scripts/basic/%: scripts_basic ;

PHONY += outputmakefile
# outputmakefile generates a Makefile in the output directory, if using a
# separate output directory. This allows convenient use of make in the
# output directory.
outputmakefile:
ifneq ($(KBUILD_SRC),)
	$(Q)ln -fsn $(srctree) source
	$(Q)$(CONFIG_SHELL) $(srctree)/scripts/mkmakefile \
	    $(srctree) $(objtree) $(VERSION) $(PATCHLEVEL)
endif
```

`scripts_basic`目标中用到了`build`变量，这个变量值为`build=-f ./scripts/Makefile.build obj`，该命令展开就是`@make -f ./scripts/Makefile.build obj=scripts/basic`，而`outputmakefile`目标先会判断`KBUILD_SRC`是否为空，只要不为空时`outputmakefile`变量才有用。最后`%config`这个目标执行的就是`@make -f ./scripts/Makefile.build obj=scripts/kconfig xxx_defconfig`这条命令。

## 14.Makefile.build

在`make xxx_defconfig`的时候会执行如下两行命令：

```shell
make -f ./scripts/Makefile.build obj=scripts/basic
make -f ./scripts/Makefile.build obj=scripts/kconfig xxx_defconfig
```

这里先以`obj=scripts/basic`为例，代码如下：

```makefile
# Modified for U-Boot
prefix := tpl
src := $(patsubst $(prefix)/%,%,$(obj))
ifeq ($(obj),$(src))
prefix := spl
src := $(patsubst $(prefix)/%,%,$(obj))
ifeq ($(obj),$(src))
prefix := .
endif
endif
```

首先将`prefix`赋值为`tpl`，然后执行替换函数，用`tpl/%`去匹配`$(obj)`，如果匹配上了就将其替换为`%`，也就是`$(obj)`中有`tpl`的话就去掉。再判断`$(obj)`和`$(src)`是否相等，如果相等也就是没对`$(obj)`进行处理，然后再去掉`$(obj)`中的`spl`，如果也没有那就将`prefix`赋值为`.`。

```makefile
# The filename Kbuild has precedence over Makefile
kbuild-dir := $(if $(filter /%,$(src)),$(src),$(srctree)/$(src))
kbuild-file := $(if $(wildcard $(kbuild-dir)/Kbuild),$(kbuild-dir)/Kbuild,$(kbuild-dir)/Makefile)
include $(kbuild-file)
```

因为`src`不是以`/`开头，所以`$(filter /%, $(src))`为空，`kbuild-dir`等于`./scripts/basic`。下一行代码中因为`./scripts/build`文件夹中没有`Kbuild`中文件,所以`kbuild-file`这个变量的值为`./scripts/basic/Makefile`，所以第三行代码导入的文件就是这个文件。

```makefile
__build: $(if $(KBUILD_BUILTIN),$(builtin-target) $(lib-target) $(extra-y)) \
	 $(if $(KBUILD_MODULES),$(obj-m) $(modorder-target)) \
	 $(subdir-ym) $(always)
	@:
```

如上代码`__build`是默认目标，在顶层Makefile中`KBUILD_BUILTIN`的值为1，`KBUILD_MODULES`的值为0，所以展开后`__build`为`$(builtin-target) $(lib-target) $(extra-y) $(subdir-ym) $(always)`，经过`make xxx_defconfig`将这几个值打印出来，发现只有`$(always)`是`scripts/basic/fixdep`，其他的都为空，所以`__build`这个目标也就是开头第一个命令，是为了编译出`fixdep`这个软件。

```
src=scripts/kconfig
kbuild-dir=./scripts/kconfig
kbuild-file=./scripts/kcoonfig/Makefile
include ./scripts/kconfig/Makefile
```

接着以第二个命令`obj=scripts/kconfig xxx_defconfig`，这条命令执行后，变量如上所示。

```make
%_defconfig: $(obj)/conf
	$(Q)$< $(silent) --defconfig=arch/$(SRCARCH)/configs/$@ $(Kconfig)

# Added for U-Boot (backward compatibility)
%_config: %_defconfig
	@:
```

如上所示，`include`导入的`./scripts/kconfig/Makefile`中有如下内容，目标`%_defconfig`刚好和输入的`xxx_defconfig`对应，依赖为`$(obj)/conf`，这是一个用于处理配置的二进制文件，由`conf.c`和`zconf.tab.c`编译。接着会执行`(Q)$< $(silent) --defconfig=arch/$(SRCARCH)/configs/$@ $(Kconfig)`，这里的命令展开后为`@scripts/kconfig/conf --defconfig=arch/../configs/xxx_defconfig Kconfig`，这里会将处理好的配置输出到`.config`文件中。

## 15.make编译流程

```makefile
# That's our default target when none is given on the command line
PHONY := _all
_all:
```

make在配置好预配置后就可以直接make编译了，如果没有明确指定目标的话会使用默认目标，如上所示：

```makefile
# If building an external module we do not care about the all: rule
# but instead _all depend on modules
PHONY += all
ifeq ($(KBUILD_EXTMOD),)
_all: all
else
_all: modules
endif
```

如果`KBUILD_EXTMOD`为空的话`_all`依赖于`all`。这里不编译模块，所以`KBUILD_EXTMOD`为空，`_all`就依赖于`all`。

```makefile
all:		$(ALL-y)
ifneq ($(CONFIG_SYS_GENERIC_BOARD),y)
	@echo "===================== WARNING ======================"
	@echo "Please convert this board to generic board."
	@echo "Otherwise it will be removed by the end of 2014."
	@echo "See doc/README.generic-board for further information"
	@echo "===================================================="
endif
ifeq ($(CONFIG_DM_I2C_COMPAT),y)
	@echo "===================== WARNING ======================"
	@echo "This board uses CONFIG_DM_I2C_COMPAT. Please remove"
	@echo "(possibly in a subsequent patch in your series)"
	@echo "before sending patches to the mailing list."
	@echo "===================================================="
endif
```

这里可以看出`all`目标依赖`$(ALL-y)`。

```makefile
# Always append ALL so that arch config.mk's can add custom ones
ALL-y += u-boot.srec u-boot.bin u-boot.sym System.map u-boot.cfg binary_size_check

ALL-$(CONFIG_ONENAND_U_BOOT) += u-boot-onenand.bin
ifeq ($(CONFIG_SPL_FSL_PBL),y)
ALL-$(CONFIG_RAMBOOT_PBL) += u-boot-with-spl-pbl.bin
else
ifneq ($(CONFIG_SECURE_BOOT), y)
# For Secure Boot The Image needs to be signed and Header must also
# be included. So The image has to be built explicitly
ALL-$(CONFIG_RAMBOOT_PBL) += u-boot.pbl
endif
endif
ALL-$(CONFIG_SPL) += spl/u-boot-spl.bin
ALL-$(CONFIG_SPL_FRAMEWORK) += u-boot.img
ALL-$(CONFIG_TPL) += tpl/u-boot-tpl.bin
ALL-$(CONFIG_OF_SEPARATE) += u-boot.dtb
ifeq ($(CONFIG_SPL_FRAMEWORK),y)
ALL-$(CONFIG_OF_SEPARATE) += u-boot-dtb.img
endif
ALL-$(CONFIG_OF_HOSTFILE) += u-boot.dtb
ifneq ($(CONFIG_SPL_TARGET),)
ALL-$(CONFIG_SPL) += $(CONFIG_SPL_TARGET:"%"=%)
endif
ALL-$(CONFIG_REMAKE_ELF) += u-boot.elf
ALL-$(CONFIG_EFI_APP) += u-boot-app.efi
ALL-$(CONFIG_EFI_STUB) += u-boot-payload.efi

ifneq ($(BUILD_ROM),)
ALL-$(CONFIG_X86_RESET_VECTOR) += u-boot.rom
endif

# enable combined SPL/u-boot/dtb rules for tegra
ifeq ($(CONFIG_TEGRA)$(CONFIG_SPL),yy)
ALL-y += u-boot-tegra.bin u-boot-nodtb-tegra.bin
ALL-$(CONFIG_OF_SEPARATE) += u-boot-dtb-tegra.bin
endif

# Add optional build target if defined in board/cpu/soc headers
ifneq ($(CONFIG_BUILD_TARGET),)
ALL-y += $(CONFIG_BUILD_TARGET:"%"=%)
endif
```

从上面代码可以看出`ALL-y`包含`u-boot.srec`、`u-boot.bin`、`u-boot.sym`、`System.map`、`u-boot.cfg`和`binary_size_check`这几个文件。根据`uboot`的配置文件也可能包含其他文件。比如`ALL-$(CONFIG_ONENAND_U_BOOT)+=u-boot-onenand.bin`，这个配置项就是`uboot`中跟`ONENAND`配置有关，如果使能了`ONENAND`，那么`.config`的配置文件就会有`CONFIG_ONENAND_U_BOOT=y`。

```makefile
ifeq ($(CONFIG_OF_SEPARATE),y)
u-boot-dtb.bin: u-boot-nodtb.bin dts/dt.dtb FORCE
	$(call if_changed,cat)

u-boot.bin: u-boot-dtb.bin FORCE
	$(call if_changed,copy)
else
u-boot.bin: u-boot-nodtb.bin FORCE
	$(call if_changed,copy)
endif
```

这里先判断`CONFIG_OF_SEPARATE`是否等于`y`，如果`.config`中不存在，`u-boot.bin`就依赖于`if`前面那个`u-boot-dtb.bin`；

```makefile
u-boot-nodtb.bin: u-boot FORCE
	$(call if_changed,objcopy)
	$(call DO_STATIC_RELA,$<,$@,$(CONFIG_SYS_TEXT_BASE))
	$(BOARD_SIZE_CHECK)
```

否则的话就依赖于如上所示的`u-boot-nodtb.bin`。如上所示的`if_changed`是一个函数，定义在`scripts/Kbuild.include`文件中。

```makefile
###
# if_changed      - execute command if any prerequisite is newer than
#                   target, or command line has changed
# if_changed_dep  - as if_changed, but uses fixdep to reveal dependencies
#                   including used config symbols
# if_changed_rule - as if_changed but execute rule instead
# See Documentation/kbuild/makefiles.txt for more info

ifneq ($(KBUILD_NOCMDDEP),1)
# Check if both arguments has same arguments. Result is empty string if equal.
# User may override this check using make KBUILD_NOCMDDEP=1
arg-check = $(strip $(filter-out $(cmd_$(1)), $(cmd_$@)) \
                    $(filter-out $(cmd_$@),   $(cmd_$(1))) )
else
arg-check = $(if $(strip $(cmd_$@)),,1)
endif

# Replace >$< with >$$< to preserve $ when reloading the .cmd file
# (needed for make)
# Replace >#< with >\#< to avoid starting a comment in the .cmd file
# (needed for make)
# Replace >'< with >'\''< to be able to enclose the whole string in '...'
# (needed for the shell)
make-cmd = $(call escsq,$(subst \#,\\\#,$(subst $$,$$$$,$(cmd_$(1)))))

# Find any prerequisites that is newer than target or that does not exist.
# PHONY targets skipped in both cases.
any-prereq = $(filter-out $(PHONY),$?) $(filter-out $(PHONY) $(wildcard $^),$^)

# Execute command if command has changed or prerequisite(s) are updated.
#
if_changed = $(if $(strip $(any-prereq) $(arg-check)),                       \
	@set -e;                                                             \
	$(echo-cmd) $(cmd_$(1));                                             \
	printf '%s\n' 'cmd_$@ := $(make-cmd)' > $(dot-target).cmd)
```

在这里，`if_changed`函数主要是从`u-boot-nodtb.bin`生成`u-boot.bin`。如果之前所示的`CONFIG_OF_SEPARATE`是空的话，`u-boot.bin`依赖的是`if`之外的`u-boot-nodtb.bin`，而`u-boot-nodtb.bin`又是依赖于`u-boot`目标。

```makefile
u-boot:	$(u-boot-init) $(u-boot-main) u-boot.lds FORCE
	$(call if_changed,u-boot__)
ifeq ($(CONFIG_KALLSYMS),y)
	$(call cmd,smap)
	$(call cmd,u-boot__) common/system_map.o
endif
```

目标`u-boot`依赖于`$(u-boot-init)`、`$(u-boot-main)`和`u-boot-lds`，前两个变量定义如下：

```makefile
u-boot-init := $(head-y)
u-boot-main := $(libs-y)
```

其中`$(head-y)`变量是和CPU架构有关的，所以`head-y`在`arch/arm/Makefile`中被指定为`arch/arm/cpu/$(CPU)/start.o`，这里分析的是`arm`架构，根据前面导出变量的分析，`$(CPU)`是`armv7`，所以展开后是`arch/arm/cpu/armv7/start.o`。

```makefile
libs-y += lib/
libs-$(HAVE_VENDOR_COMMON_LIB) += board/$(VENDOR)/common/
libs-$(CONFIG_OF_EMBED) += dts/
libs-y += fs/
libs-y += net/
libs-y += disk/
libs-y += drivers/
libs-y += drivers/dma/
libs-y += drivers/gpio/
libs-y += drivers/i2c/
libs-y += drivers/mmc/
libs-y += drivers/mtd/
libs-$(CONFIG_CMD_NAND) += drivers/mtd/nand/
libs-y += drivers/mtd/onenand/
libs-$(CONFIG_CMD_UBI) += drivers/mtd/ubi/
libs-y += drivers/mtd/spi/
libs-y += drivers/net/
libs-y += drivers/net/phy/
libs-y += drivers/pci/
libs-y += drivers/power/ \
	drivers/power/fuel_gauge/ \
	drivers/power/mfd/ \
	drivers/power/pmic/ \
	drivers/power/battery/ \
	drivers/power/regulator/
libs-y += drivers/spi/
libs-$(CONFIG_FMAN_ENET) += drivers/net/fm/
libs-$(CONFIG_SYS_FSL_DDR) += drivers/ddr/fsl/
libs-$(CONFIG_ALTERA_SDRAM) += drivers/ddr/altera/
libs-y += drivers/serial/
libs-y += drivers/usb/dwc3/
libs-y += drivers/usb/emul/
libs-y += drivers/usb/eth/
libs-y += drivers/usb/gadget/
libs-y += drivers/usb/gadget/udc/
libs-y += drivers/usb/host/
libs-y += drivers/usb/musb/
libs-y += drivers/usb/musb-new/
libs-y += drivers/usb/phy/
libs-y += drivers/usb/ulpi/
libs-y += cmd/
libs-y += common/
libs-$(CONFIG_API) += api/
libs-$(CONFIG_HAS_POST) += post/
libs-y += test/
libs-y += test/dm/
libs-$(CONFIG_UT_ENV) += test/env/

libs-y += $(if $(BOARDDIR),board/$(BOARDDIR)/)

libs-y := $(sort $(libs-y))

u-boot-dirs	:= $(patsubst %/,%,$(filter %/, $(libs-y))) tools examples

u-boot-alldirs	:= $(sort $(u-boot-dirs) $(patsubst %/,%,$(filter %/, $(libs-))))

libs-y		:= $(patsubst %/, %/built-in.o, $(libs-y))
```

而`libs-y`是uboot各个子目录的合集，最后将使用`patsubst`将`libs-y`中的`/`替换为`/built-in.o`，例如`drivers/serial/`就会变成`drivers/serial/built-in.o`，所以`u-boot-main`就相当于所以子目录中`built-in.o`的合集。

```makefile
u-boot.lds: $(LDSCRIPT) prepare FORCE
	$(call if_changed_dep,cpp_lds)
```

最后`u-boot.lds`这个目标相对于以`u-boot.lds`围殴链接脚本将`arch/arm/cpu/armv7/start.o`和各个子目录的`built-in.o`文件链接到一起生成`u-boot`文件。

```makefile
cmd_drivers/gpio/built-in.o :=  /tools/gcc-linaro-7.5.0-2019.12-x86_64_arm-linux-gnueabihf/bin/arm-linux-gnueabihf-ld.bfd     -r -o drivers/gpio/built-in.o drivers/gpio/mxc_gpio.o 
```

以`drivers/gpio/built-in.o`为例，在这个目录下有个`build-in.o.cmd`文件，内容如上所示。可以看出`drivers/gpio/built-in.o`这个文件是使用ld目录由`drivers/gpio/mxc_gpio.o`文件生成的。这里的`mxc_gpio.o`文件是`mxc_gpio.c`文件生成的，这里用到的`-r`选项是产生可重定向的输出。如果产生的文件需要再次作为`ld`命令的输入，余姚用到此选项，这也叫做部分链接。最后这些`built-in.o`文件最终根据链接脚本生成`u-boot.bin`文件。
