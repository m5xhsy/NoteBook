# UBoot启动流程

## 1.链接脚本

要分析uboot的启动流程首先要分析uboot的链接脚本，对于arm系列的芯片，链接脚本路径为`arch/arm/cpu/uboot.lds`，最终uboot所使用的链接脚本就是在这个文件基础上生成的。首先需要编译运行uboot，编译后会在根目录下生成`uboot.lds`文件，内容如下所示：

```
OUTPUT_FORMAT("elf32-littlearm", "elf32-littlearm", "elf32-littlearm")
OUTPUT_ARCH(arm)
ENTRY(_start)
SECTIONS
{
 . = 0x00000000;
 . = ALIGN(4);
 .text :
 {
  *(.__image_copy_start)
  *(.vectors)
  arch/arm/cpu/armv7/start.o (.text*)
  *(.text*)
 }
 . = ALIGN(4);
 .rodata : { *(SORT_BY_ALIGNMENT(SORT_BY_NAME(.rodata*))) }
 . = ALIGN(4);
 .data : {
  *(.data*)
 }
 . = ALIGN(4);
 . = .;
 . = ALIGN(4);
 .u_boot_list : {
  KEEP(*(SORT(.u_boot_list*)));
 }
 . = ALIGN(4);
 .image_copy_end :
 {
  *(.__image_copy_end)
 }
 .rel_dyn_start :
 {
  *(.__rel_dyn_start)
 }
 .rel.dyn : {
  *(.rel*)
 }
 .rel_dyn_end :
 {
  *(.__rel_dyn_end)
 }
 .end :
 {
  *(.__end)
 }
 _image_binary_end = .;
 . = ALIGN(4096);
 .mmutable : {
  *(.mmutable)
 }
 .bss_start __rel_dyn_start (OVERLAY) : {
  KEEP(*(.__bss_start));
  __bss_base = .;
 }
 .bss __bss_base (OVERLAY) : {
  *(.bss*)
   . = ALIGN(4);
   __bss_limit = .;
 }
 .bss_end __bss_limit (OVERLAY) : {
  KEEP(*(.__bss_end));
 }
 .dynsym _image_binary_end : { *(.dynsym) }
 .dynbss : { *(.dynbss) }
 .dynstr : { *(.dynstr*) }
 .dynamic : { *(.dynamic*) }
 .plt : { *(.plt*) }
 .interp : { *(.interp*) }
 .gnu.hash : { *(.gnu.hash) }
 .gnu : { *(.gnu*) }
 .ARM.exidx : { *(.ARM.exidx*) }
 .gnu.linkonce.armexidx : { *(.gnu.linkonce.armexidx.*) }
}
```

`ENTRY(_start)`表示当前入口为`__start`，这个函数在`arch/arm/lib/vector.S`文件中有定义。在编译后，打开根目录下的`uboot.map`文件，这个文件是uboot的映射文件，找到`__image_copy_start`，内容如下所示：

```lds
Memory Configuration

Name             Origin             Length             Attributes
*default*        0x0000000000000000 0xffffffffffffffff

Linker script and memory map

Address of section .text set to 0x87800000
                0x0000000000000000                . = 0x0
                0x0000000000000000                . = ALIGN (0x4)

.text           0x0000000087800000    0x3f03c
 *(.__image_copy_start)
 .__image_copy_start
                0x0000000087800000        0x0 arch/arm/lib/built-in.o
                0x0000000087800000                __image_copy_start
 *(.vectors)
 .vectors       0x0000000087800000      0x2e8 arch/arm/lib/built-in.o
                0x0000000087800000                _start
                0x0000000087800020                _undefined_instruction
                0x0000000087800024                _software_interrupt
                0x0000000087800028                _prefetch_abort
                0x000000008780002c                _data_abort
                0x0000000087800030                _not_used
                0x0000000087800034                _irq
                0x0000000087800038                _fiq
                0x0000000087800040                IRQ_STACK_START_IN
 arch/arm/cpu/armv7/start.o(.text*)
 .text          0x00000000878002e8       0xb0 arch/arm/cpu/armv7/start.o
                0x00000000878002e8                reset
                0x00000000878002ec                save_boot_params_ret
                0x0000000087800328                c_runtime_cpu_setup
                0x0000000087800338                save_boot_params
                0x000000008780033c                cpu_init_cp15
                0x0000000087800390                cpu_init_crit
 *(.text*)
 .text          0x0000000087800398       0x24 arch/arm/cpu/armv7/built-in.o
                0x0000000087800398                lowlevel_init
                ......
```

如上所示代码中，`.__iamge_copy_start`所指向的文件是`arch/arm/lib/built-in.o`，我们进入该目录下用`grep`命令搜索`__image_copy_start`，结果如下：

```
./relocate.S:   ldr     r1, =__image_copy_start /* r1 <- SRC &__image_copy_start */
./relocate_64.S:        ldr     x1, =__image_copy_start /* x1 <- SRC &__image_copy_start */
./sections.c:char __image_copy_start[0] __attribute__((section(".__image_copy_start")));
```

其中`sections.c`中有如下定义：

```c
char __bss_start[0] __attribute__((section(".__bss_start")));
char __bss_end[0] __attribute__((section(".__bss_end")));
char __image_copy_start[0] __attribute__((section(".__image_copy_start")));
char __image_copy_end[0] __attribute__((section(".__image_copy_end")));
char __rel_dyn_start[0] __attribute__((section(".__rel_dyn_start")));
char __rel_dyn_end[0] __attribute__((section(".__rel_dyn_end")));
char __secure_start[0] __attribute__((section(".__secure_start")));
char __secure_end[0] __attribute__((section(".__secure_end")));
char _end[0] __attribute__((section(".__end")));
```

`attribute`为GNU C中用于声明一个函数、变量或类型的特殊关键字，主要用于指导编译器在编译程序时进行特点方面的优化或代码检查，例如`aligned`来声明对齐等等。我们知道在源代码编译生成可执行文件的过程中函数和变量是放在不同段的，全局未初始化的变量是放在`bss`段的，通过`int val __attribute__((section(".data")))`可以来指定将这个变量放到`.data`段。所以`__attribute__((section(".__image_copy_start")))`的意思就是将`__image_copy_start[0]`放到链接脚本中的`.__iamge_copy_start`段了，并且数组长度为零，不占内存。通过分析链接脚本文件可以得知，`__image_copy_start`在链接脚本中位置在`.text`段的前面，而`__iamge_copy_end`在`.data`段的后面。也就是说这两个地址分别表示uboot要拷贝的起始地址和结束地址。

```
/*
 * void relocate_code(addr_moni)
 *
 * This function relocates the monitor code.
 *
 * NOTE:
 * To prevent the code below from containing references with an R_ARM_ABS32
 * relocation record type, we never refer to linker-defined symbols directly.
 * Instead, we declare literals which contain their relative location with
 * respect to relocate_code, and at run time, add relocate_code back to them.
 */

ENTRY(relocate_code)
	ldr	r1, =__image_copy_start	/* r1 <- SRC &__image_copy_start */
	subs	r4, r0, r1		/* r4 <- relocation offset */
	beq	relocate_done		/* skip relocation */
	ldr	r2, =__image_copy_end	/* r2 <- SRC &__image_copy_end */

copy_loop:
	ldmia	r1!, {r10-r11}		/* copy from source address [r1]    */
	stmia	r0!, {r10-r11}		/* copy to   target address [r0]    */
	cmp	r1, r2			/* until source end address [r2]    */
	blo	copy_loop
```

我们再打开`relocate.S`文件，内容如上所示，`r1`寄存器保存拷贝的起始地址，`r2`寄存器保存拷贝的结束地址，`r4`寄存器保存偏移地址，然后`copy_loop`函数进行来拷贝。再回到链映射文件中，可以看出`__image_copy_start`和`__start`的地址都是`0x0000000087800000 `，也说明了前面`__image_copy_start[0]`不占位置。`.vectors`段也是在`arch/arm/lib/built-in.o`中，在同级目录下找到`vectors.S`文件，部分内容如下：

```c
.globl _start

/*
 *************************************************************************
 *
 * Vectors have their own section so linker script can map them easily
 *
 *************************************************************************
 */

	.section ".vectors", "ax"

/*
 *************************************************************************
 *
 * Exception vectors as described in ARM reference manuals
 *
 * Uses indirect branch to allow reaching handlers anywhere in memory.
 *
 *************************************************************************
 */

_start:

#ifdef CONFIG_SYS_DV_NOR_BOOT_CFG
	.word	CONFIG_SYS_DV_NOR_BOOT_CFG
#endif

	b	reset
	ldr	pc, _undefined_instruction
	ldr	pc, _software_interrupt
	ldr	pc, _prefetch_abort
	ldr	pc, _data_abort
	ldr	pc, _not_used
	ldr	pc, _irq
	ldr	pc, _fiq
```

其中`.section ".vectors", "ax"`表示下面的代码会被编译进`.vectors`段中，`ax`为`allocation execute`，表示该节区可分配且可执行。我们再对应到`uboot.map`文件中，`.vectors`段映射的就是`_start`、`IRQ_STACK_START_IN`以及异常中断向量表，而`start.o`则被映射到`.text`段了，这里后面详细分析。

| 符号               | 地址       | 描述                 |
| ------------------ | ---------- | -------------------- |
| __image_copy_start | 0x87800000 | uboot拷贝首地址      |
| __image_copy_end   | 0x8785dd54 | uboot 拷贝的结束地址 |
| __rel_dyn_start    | 0x8785dd54 | .rel.dyn 段起始地址  |
| __rel_dyn_end      | 0x878668f4 | .rel.dyn 段结束地址  |
| _image_binary_end  | 0x878668f4 | 镜像结束地址         |
| __bss_start        | 0x8785dd54 | .bss 段起始地址      |
| __bss_end          | 0x878a8e74 | .bss 段结束地址      |

如上所示是链接脚本中一些符号的值，可以从`uboot.map`中查到，这里的地址并不是一定是这些值，代码的变动、编译优化等级等都会影响到这些值。

## 2.reset函数

从上述分析中可以得知入口是`arch/arm/lib/vectors.S`文件中的`_start`，代码如下所示：

```
_start:

#ifdef CONFIG_SYS_DV_NOR_BOOT_CFG
	.word	CONFIG_SYS_DV_NOR_BOOT_CFG
#endif

	b	reset
	ldr	pc, _undefined_instruction
	ldr	pc, _software_interrupt
	ldr	pc, _prefetch_abort
	ldr	pc, _data_abort
	ldr	pc, _not_used
	ldr	pc, _irq
	ldr	pc, _fiq

/*
 *************************************************************************
 *
 * Indirect vectors table
 *
 * Symbols referenced here must be defined somewhere else
 *
 *************************************************************************
 */

	.globl	_undefined_instruction
	.globl	_software_interrupt
	.globl	_prefetch_abort
	.globl	_data_abort
	.globl	_not_used
	.globl	_irq
	.globl	_fiq

_undefined_instruction:	.word undefined_instruction
_software_interrupt:	.word software_interrupt
_prefetch_abort:	.word prefetch_abort		
_data_abort:		.word data_abort
_not_used:		.word not_used
_irq:			.word irq
_fiq:			.word fiq

	.balignl 16,0xdeadbeef
```

`b reset`的意思是跳转到`reset`函数中，`reset`函数在`arch/arm/armv7/start.S`里面。剩下后面的部分表示中断向量表，这里补充一点`.balignl 16,0xdeadbeef`表示以当前的地址开始，到后面第一个能被16整除的地址中间填充`0xdeadbeef`，也就是十六字节对齐，这里也可以对照`uboot.map`文件，可以看出`_fiq`到后空了8个字节，而函数只占4个字节。进入`start.S`文件中，`reset`函数内容如下：

```

	.globl	reset
	.globl	save_boot_params_ret

reset:
	/* Allow the board to save important registers */
	b	save_boot_params
```

在`reset`函数中只有一句跳转指令，在文件中搜索`save_boot_params`，该函数定义如下：

```
/*************************************************************************
 *
 * void save_boot_params(u32 r0, u32 r1, u32 r2, u32 r3)
 *	__attribute__((weak));
 *
 * Stack pointer is not yet initialized at this moment
 * Don't save anything to stack even if compiled with -O0
 *
 *************************************************************************/
ENTRY(save_boot_params)
	b	save_boot_params_ret		@ back to my caller
ENDPROC(save_boot_params)
	.weak	save_boot_params
```

这里有几个宏定义，根据头文件引用我们可以在``include/linux/linkage.h`中找到，最终展开如下所示

```
.globl save_boot_params;   					@声明全局变量
.align		4;								@4字节对齐
save_boot_params:			
	b	save_boot_params_ret				@ 跳转到save_boot_params_ret函数
.type save_boot_params STT_FUNC;			@ 声明save_boot_params是一个函数
.size save_boot_params, .-save_boot_params	@ 声明函数大小为当前位置减去save_boot_params全局标号的位置(.表示当前位置)
.weak	save_boot_params					@ 弱标号，表示如果其他地方声明了这个函数就跳转到其他地方去
```

从上面可以知道`save_boot_params`会跳转到`save_boot_params_ret`函数中去，该函数定义在`reset`下面，内容如下：

```
save_boot_params_ret:
	/*
	 * disable interrupts (FIQ and IRQ), also set the cpu to SVC32 mode,
	 * except if in HYP mode already
	 */
	mrs	r0, cpsr			@ 读取cpsr寄存器内容到r0
	and	r1, r0, #0x1f		@ r0中获取低5位写入r1中
	teq	r1, #0x1a			@ 判断r1是否与0x1a相等(这里1a位11010,也就是HYP模式)
	bicne	r0, r0, #0x1f	@ 如果不等于的话清除低5位
	orrne	r0, r0, #0x13	@ 然后或上0x13(也就是只要不是HYP模式，就都进入SVC模式)
	orr	r0, r0, #0xc0		@ 将第六七位设置位1，禁用FRQ和IRQ
	msr	cpsr,r0				@ 最后写入cpsr中 (1101 0011)
```

这里需要参考`ARMV7`的编程手册的CPSR寄存器部分：

![cpsr](./image/cpsr.png)

这里主要设置了第第7位禁用IRQ，第6位禁用FRQ，以及第4到0位设置处理器运行于SVC模式。补充一点，在启动过程中，中断环境并没有完全准备好，一旦有中断产生，可能会导致预想不到的结果，比如程序跑飞，因此这里需要关闭IRQ和FRQ。

```
/*
 * Setup vector:
 * (OMAP4 spl TEXT_BASE is not 32 byte aligned.
 * Continue to use ROM code vector only in OMAP4 spl)
 */
#if !(defined(CONFIG_OMAP44XX) && defined(CONFIG_SPL_BUILD))
	/* Set V=0 in CP15 SCTLR register - for VBAR to point to vector */
	mrc	p15, 0, r0, c1, c0, 0	@ Read CP15 SCTLR Register // 选择异常向量表的基址
	bic	r0, #CR_V		@ V = 0
	mcr	p15, 0, r0, c1, c0, 0	@ Write CP15 SCTLR Register 

	/* Set vector address in CP15 VBAR register */
	ldr	r0, =_start
	mcr	p15, 0, r0, c12, c0, 0	@Set VBAR // 设置_start地址到VBAR
#endif

	/* the mask ROM code should have PLL and others stable */
#ifndef CONFIG_SKIP_LOWLEVEL_INIT
	bl	cpu_init_cp15
	bl	cpu_init_crit
#endif

	bl	_main
```

然后就是对CP15协处理器进行配置了。这里补充一点，CP寄存器除了CP15以外还有CP0到CP14，其中CP14用于DBUG调试，CP13和CP12保留，CP11用于双精度浮点计算，CP10用于单精度浮点计算，CP9和CP8保留，CP7到CP0留给生产厂家使用。在特权模式下，CP15协处理器读写方式如图所示：

![cp15](./image/cp15.png)

接下来分析代码，首先会判断是不是使用了OMAR44的芯片，并且定义了`CONFIG_SPL_BUILD`，如果都满足的话就不会走这里(SPL即`Secondary Program Loader`，第二阶段程序加载器，对于有些SOC来说，他的内部SRAM比较小，无法装载整个uboot镜像，那么就需要SPL来负责初始化RAM和环境，并加载真正的uboot在外部RAM中来执行)，通过查询手册可以知道`mrc p15, 0, r0, c1, c0, 0`访问的是`SCTLR`寄存器，这个寄存器只能`PL1`或更高的权限才可以访问。将这个寄存器的值读取到`r0`寄存器中后，对第13位进行了清零操作(这个宏定义在`arch/arm/include/asm/system.h`中，值位`(1<<13)`)。

![sctlr](./image/sctlr.png)

第13位表示选择异常中断向量表的基地址，选择0后可以设置偏移的地址，默认的地址是`0x00000000`。接下来将`_start`的地址写入`r0`，再将`r0`中的地址写入`VBAR`寄存器，当发生异常时就偏移到该寄存器中指定的地址执行。设置完异常中断向量表的基地址后，就进入`cpu_init_cp15`函数，对cpu初始化，该函数代码如下所示：

```
/*************************************************************************
 *
 * cpu_init_cp15
 *
 * Setup CP15 registers (cache, MMU, TLBs). The I-cache is turned on unless
 * CONFIG_SYS_ICACHE_OFF is defined.
 *
 *************************************************************************/
ENTRY(cpu_init_cp15)
	/*
	 * Invalidate L1 I/D
	 */
	mov	r0, #0			@ set up for MCR
	mcr	p15, 0, r0, c8, c7, 0	@ invalidate TLBs 			使TLBs无效
	mcr	p15, 0, r0, c7, c5, 0	@ invalidate icache			使Icache无效
	mcr	p15, 0, r0, c7, c5, 6	@ invalidate BP array		使分支预测无效
	mcr p15, 0, r0, c7, c10, 4	@ DSB						s
	mcr p15, 0, r0, c7, c5, 4	@ ISB						强制清空流水线

	/*
	 * disable MMU stuff and caches
	 */
	mrc	p15, 0, r0, c1, c0, 0
	bic	r0, r0, #0x00002000	@ clear bits 13 (--V-)			设置SCTRL	
	bic	r0, r0, #0x00000007	@ clear bits 2:0 (-CAM)			PL1和PL0模式下禁用虚拟内存管理
	orr	r0, r0, #0x00000002	@ set bit 1 (--A-) Align		使能对齐检查
	orr	r0, r0, #0x00000800	@ set bit 11 (Z---) BTB			使能分支预测
#ifdef CONFIG_SYS_ICACHE_OFF
	bic	r0, r0, #0x00001000	@ clear bit 12 (I) I-cache		禁用icache
#else	
	orr	r0, r0, #0x00001000	@ set bit 12 (I) I-cache		使能icache
#endif
	mcr	p15, 0, r0, c1, c0, 0

	......

	mov	r5, lr			@ Store my Caller								把跳回的地址写进r5
	mrc	p15, 0, r1, c0, c0, 0	@ r1 has Read Main ID Register (MIDR)	读取MIDR寄存器内容
	mov	r3, r1, lsr #20		@ get variant field							将r1中内容右移20位放入r3
	and	r3, r3, #0xf		@ r3 has CPU variant						获取r3的低4位variant，即处理器的修订号(MIDR寄存器的20-23位)
	and	r4, r1, #0xf		@ r4 has CPU revision						获取r1的低4位rversion，即处理器的补丁号(MIDR寄存器的0-3位)
	mov	r2, r3, lsl #4		@ shift variant field for combined value	r3的值左移4位放进r2
	orr	r2, r4, r2		@ r2 has combined CPU variant + revision		r4的值或上r2放进r2

	......
	
	mov	pc, r5			@ back to my caller								跳转到函数进来前的位置
ENDPROC(cpu_init_cp15)
```

上述代码中一些包含`CONFIG_ARM_ERRATA_`的宏定义通过加错误打印，发现并没有走这部分内容，所以省略了，这些选项是用于配置ARM的勘误表，后续可以根据实际情况选择是否开启。这里首先分析L1的`I/D cache`相关内容，CPU的工作速率是非常快的，而外部SRAM的工作速率很慢，所以CPU对内存访问时，要等待内存访问结束，这会导致浪费很多实间，所以在CPU和主存中加一个Cache。当CPU写数据写到内存中时，就会先写进Cache中，再由Cache写入主存中；读数据时CPU会先去Cache中读，如果Cache中没有数据再从主存中读，这样就加快了CPU的运行速率。Cache是通过CP15协处理器控制的，刚上电时CPU还不能直接管理Cache，且CPU访问的都是实际的物理地址，如初始化外设这些，所以MMU也不需要开启。由于指令Cache访问的都是物理地址，所以可以关闭，也可以不关闭，而数据Cache必须关闭，一是这个时候CPU去Cache中取数据时，数据还没中主存中Cache过来，预取失败会导致系统出问题；二是如果数据发生了改变，CPU读取的数据就不正确，我们知道C语言中的`volatile`关键字是告诉编译器不要对代码进行优化，这个优化就包括将常用的数据放入Cache中，这个时候CPU每次读取的都是Cache中的数据，如果实际物理地址数据发生了改变，那么CPU就感受不到这个变化，所以我们需要关闭数据Cache，让CPU读取物理地址上真实的数据。







