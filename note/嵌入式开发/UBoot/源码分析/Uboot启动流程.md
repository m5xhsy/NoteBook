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

这里主要设置了第7位禁用IRQ，第6位禁用FRQ，以及第4到0位设置处理器运行于SVC模式。补充一点，在启动过程中，中断环境并没有完全准备好，一旦有中断产生，可能会导致预想不到的结果，比如程序跑飞，因此这里需要关闭IRQ和FRQ。

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

第13位表示选择异常中断向量表的基地址，选择0后可以设置偏移的地址，默认的地址是`0x00000000`。接下来将`_start`的地址写入`r0`，再将`r0`中的地址写入`VBAR`寄存器，当发生异常时就偏移到该寄存器中指定的地址执行。设置完异常中断向量表的基地址后，就进入`cpu_init_cp15`函数，对cpu初始化，并将`cpu_init_cp15`函数出来后执行的地址保存到`lr`寄存器中。该函数代码如下所示：

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

	mov	r5, lr			@ Store my Caller								把函数返回的地址写进r5
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

```
mov	r0, #0			@ set up for MCR
mcr	p15, 0, r0, c8, c7, 0	@ invalidate TLBs 			使TLB无效
mcr	p15, 0, r0, c7, c5, 0	@ invalidate icache			使Icache无效	
mcr	p15, 0, r0, c7, c5, 6	@ invalidate BP array		使分支预测无效
mcr p15, 0, r0, c7, c10, 4	@ DSB						
mcr p15, 0, r0, c7, c5, 4	@ ISB						
```

如上代码，首先将0写入`r0`寄存器,`mcr	p15, 0, r0, c8, c7, 0`表示使TBL无效(TBL：变换旁路缓冲区，与内存相关)。这里补充一下，`invalidate`表示使无效，`flash`表示清空，`enable`表示是呢。接着使指令Cache无效，这个前面有解释过；然后使分支预测无效，我们知道ARMV7处理器采用3级流水线结构，包括取指(fetch)、译指(decode)和执行(execute)三个阶段，PC寄存器中总是指向当前执行的地址加8，如果一个循环中已经预加载后面的代码，而实际执行过程中因为条件语句需要往回跳转，那么前面的预加载就会无效，分支预测相当于一个计数器，如果代码运行过程中往前跳的次数比较多，那么就会预先加载前面的指令。使分支预测无效后接下来会进行数据同步隔离操作和指令同步隔离操作，也就是相当于强制清空流水线。这里对DSB和ISB做一下解释：

| 指令 | 解释                                                         |
| ---- | ------------------------------------------------------------ |
| DMB  | 数据存储隔离,保证仅在他前面的存储器器访问操作都执行完后才提交它后面的访问操作 |
| DSB  | 数据同步隔离,比DMB严格,仅当前面所有的存储器访问操作都执行完后才执行后面的指令,(即任何指令都要等待存储器访问操作) |
| ISB  | 指令同步隔离,最严格,会清洗流水线,以保证前面操作都执行完后才执行后面的指令 |

然后是对MMU相关操作：

```
	mrc	p15, 0, r0, c1, c0, 0
	bic	r0, r0, #0x00002000	@ clear bits 13 (--V-)			设置SCTRL(13位)
	bic	r0, r0, #0x00000007	@ clear bits 2:0 (-CAM)			PL1和PL0模式下禁用虚拟内存管理
	orr	r0, r0, #0x00000002	@ set bit 1 (--A-) Align		使能对齐检查
	orr	r0, r0, #0x00000800	@ set bit 11 (Z---) BTB			使能分支预测
#ifdef CONFIG_SYS_ICACHE_OFF
	bic	r0, r0, #0x00001000	@ clear bit 12 (I) I-cache		禁用icache
#else	
	orr	r0, r0, #0x00001000	@ set bit 12 (I) I-cache		使能icache
#endif
	mcr	p15, 0, r0, c1, c0, 0
```

![sctrl](./image/sctrl.png)

首先读取SCTRL寄存器，将第13位清零，前面我们设置了异常中断向量表的基地址，但是这一位也必须设置为0。然后我们将低3位清零，这里的C表示Cache使能，A表示对齐检查使能，M表示启用MMU，这3位清零后，相当于全部关闭了，其中第0位表示PL1和PL0模式下禁用MMU(虚拟内存管理)。然后设置第2位，也就是对其检查，以及第11位分支预测，最后如果定义了`CONFIG_SYS_ICACHE_OFF`这个宏就关闭指令Cache，否则开启。接着分析第3部分：

```
	mov	r5, lr			@ Store my Caller								把跳回的地址写进r5
	mrc	p15, 0, r1, c0, c0, 0	@ r1 has Read Main ID Register (MIDR)	读取MIDR寄存器内容
	mov	r3, r1, lsr #20		@ get variant field							将r1中内容右移20位放入r3
	and	r3, r3, #0xf		@ r3 has CPU variant						获取r3的低4位variant，即处理器的修订号(MIDR寄存器的20-23位)
	and	r4, r1, #0xf		@ r4 has CPU revision						获取r1的低4位rversion，即处理器的补丁号(MIDR寄存器的0-3位)
	mov	r2, r3, lsl #4		@ shift variant field for combined value	r3的值左移4位放进r2
	orr	r2, r4, r2		@ r2 has combined CPU variant + revision		r4的值或上r2放进r2

	......
	
	mov	pc, r5			@ back to my caller								跳转到函数进来前的位置
```

这里会将`lr`寄存器中保存的函数返回地址保存到`r5`寄存器中，然后读取`MIDR`寄存器中的内容，这一部分内容主要是将CPU的版本号保存到`r2`寄存器中，接着将`r5`寄存器中的地址写进pc寄存器中。在对CPU和CP15寄存器相关的内容初始化后，就会进入`cpu_init_crit`函数，其内容如下：

```
ENTRY(cpu_init_crit)
	/*
	 * Jump to board specific initialization...
	 * The Mask ROM will have already initialized
	 * basic memory. Go here to bump up clock rate and handle
	 * wake up conditions.
	 */
	b	lowlevel_init		@ go setup pll,mux,memory()
ENDPROC(cpu_init_crit)
```

该函数中只有一条指令，即跳进`lowlevel_init`函数，这个函数下一节分析。

## 3.lowlevel_init函数

`lowlevel_init`函数定义在`arch/arm/cpu/armv7/lowlevel_init.S`文件中，内容如下所示：

```
#include <asm-offsets.h>
#include <config.h>
#include <linux/linkage.h>

ENTRY(lowlevel_init)
	/*
	 * Setup a temporary stack. Global data is not available yet.
	 */
	ldr	sp, =CONFIG_SYS_INIT_SP_ADDR
	bic	sp, sp, #7 /* 8-byte alignment for ABI compliance */
#ifdef CONFIG_SPL_DM
	mov	r9, #0
#else
	/*
	 * Set up global data for boards that still need it. This will be
	 * removed soon.
	 */
#ifdef CONFIG_SPL_BUILD
	ldr	r9, =gdata
#else
	sub	sp, sp, #GD_SIZE
	bic	sp, sp, #7
	mov	r9, sp
#endif
#endif
	/*
	 * Save the old lr(passed in ip) and the current lr to stack
	 */
	push	{ip, lr}

	/*
	 * Call the very early init function. This should do only the
	 * absolute bare minimum to get started. It should not:
	 *
	 * - set up DRAM
	 * - use global_data
	 * - clear BSS
	 * - try to start a console
	 *
	 * For boards with SPL this should be empty since SPL can do all of
	 * this init in the SPL board_init_f() function which is called
	 * immediately after this.
	 */
	bl	s_init
	pop	{ip, pc}
ENDPROC(lowlevel_init)
```

`sp`是用于保存堆栈指针的寄存器，`CONFIG_SYS_INIT_SP_ADDR`这个宏定义在`include/configs/mx6ullevk.h`，`lowleve_init.S`文件会导入`include/config.h`，这个文件只有编译后才能找到，编译时会根据配置文件导入`include/configs`文件夹中的头文件。其内容如下所示：

```
/* Automatically generated - do not edit */
#define CONFIG_IMX_CONFIG	board/freescale/mx6ullevk/imximage.cfg
#define CONFIG_MX6ULL_EVK_EMMC_REWORK	1
#define CONFIG_BOARDDIR board/freescale/mx6ullevk
#include <config_defaults.h>
#include <config_uncmd_spl.h>
#include <configs/mx6ullevk.h>
#include <asm/config.h>
#include <config_fallbacks.h>
```

因为这里使用的是IMX6U系列芯片，所以导入的就是`configs/mx6ullevk.h`，我们找到该文件，可以看到`CONFIG_SYS_INIT_SP_ADDR`这个宏的定义如下：

```
#define CONFIG_SYS_INIT_RAM_ADDR	IRAM_BASE_ADDR
#define CONFIG_SYS_INIT_RAM_SIZE	IRAM_SIZE

#define CONFIG_SYS_INIT_SP_OFFSET \
	(CONFIG_SYS_INIT_RAM_SIZE - GENERATED_GBL_DATA_SIZE)
#define CONFIG_SYS_INIT_SP_ADDR \
	(CONFIG_SYS_INIT_RAM_ADDR + CONFIG_SYS_INIT_SP_OFFSET)
```

我们将上面宏展开：

```
CONFIG_SYS_INIT_SP_ADDR = (IRAM_BASE_ADDR + (IRAM_SIZE - GENERATED_GBL_DATA_SIZE))  
```

其中`IRAM_BASE_ADDR`和`IRAM_SIZE`的定义可以在`arch/arm/include/asn/arch/imx-regs.h`文件中：

```
#define IRAM_BASE_ADDR			0x00900000
	
	......

#if !(defined(CONFIG_MX6SX) || \
	defined(CONFIG_MX6UL) || defined(CONFIG_MX6ULL) || \
	defined(CONFIG_MX6SLL) || defined(CONFIG_MX6SL))
#define IRAM_SIZE                    0x00040000
#else
#define IRAM_SIZE                    0x00020000
#endif
#define FEC_QUIRK_ENET_MAC
```

这里由于定义了`CONFIG_MX6ULL`，所以`IRAM_SIZE`大小为`0x00020000`，`IRAM_BASE_ADDR`大小为`0x00900000`，而`GENERATED_GBL_DATA_SIZE`这个宏定义在`include/generated/generic-asm-offsets.h`文件中（这个文件所在的目录是编译后产生的），这个文件是由`Kbuild`构建的，内容如下：

```
#ifndef __GENERIC_ASM_OFFSETS_H__
#define __GENERIC_ASM_OFFSETS_H__
/*
 * DO NOT MODIFY.
 *
 * This file was generated by Kbuild
 */

#define GENERATED_GBL_DATA_SIZE 256 /* (sizeof(struct global_data) + 15) & ~15	@ */
#define GENERATED_BD_INFO_SIZE 80 /* (sizeof(struct bd_info) + 15) & ~15	@ */
#define GD_SIZE 248 /* sizeof(struct global_data)	@ */
#define GD_BD 0 /* offsetof(struct global_data, bd)	@ */
#define GD_MALLOC_BASE 192 /* offsetof(struct global_data, malloc_base)	@ */
#define GD_RELOCADDR 48 /* offsetof(struct global_data, relocaddr)	@ */
#define GD_RELOC_OFF 68 /* offsetof(struct global_data, reloc_off)	@ */
#define GD_START_ADDR_SP 64 /* offsetof(struct global_data, start_addr_sp)	@ */

#endif
```

这里`GENERATED_GBL_DATA_SIZE`值为256，这里补充一下，这个宏表示的是`global_data`结构体的大小，这里注释的意思是为了保证16字节对齐，因为保证对齐所占的内存必须大于结构体的大小，所以需要加上15，在与上`~15`清除低4位。我们知道这几个宏的大小后就可以计算出`CONFIG_SYS_INIT_SP_ADDR`的大小了。

```
CONFIG_SYS_INIT_SP_ADDR = (0x00900000 + (0x00020000 - 256)) = 0x0091FF00
```

再回到`lowlevel_init`函数中，此时SP指针指向`0x0091FF00`，这个地址属于`IMX6ULL`内部的RAM，接下来对该地址进行8字节对齐，也就是将sp指针调整到最近可以被8整除的位置上，因为`IMX6ULL(Cortex-A7)`的堆栈是向低地址增长的，所以对齐后地址更低，也就是清除低3位(注意是位操作，不要理解成字节)。

```
#ifdef CONFIG_SPL_DM
	mov	r9, #0
#else
	/*
	 * Set up global data for boards that still need it. This will be
	 * removed soon.
	 */
#ifdef CONFIG_SPL_BUILD
	ldr	r9, =gdata
#else
	sub	sp, sp, #GD_SIZE
	bic	sp, sp, #7
	mov	r9, sp
#endif
#endif
```

这里的`CONFIG_SPL_DM`和`CONFIG_SPL_BUILD`都是没有定义的，所以会走最下面的代码。这里的`GD_SIZE`宏在前面`include/generated/generic-asm-offsets.h`中有定义，值为248，是结构体`global_data`的大小，所以此时的sp指向的地址是`0x0091FF0`减去248，也就是`0x0091FE08`，然后进行8字节对齐，此时该地址已经对齐了，接着将SP指针的地址保存进`r9`寄存器，分析后的结构如图所示：

![SP](./image/sp01.png)

回到`lowlevel_init`函数中，首先将`ip`和`lr`压栈，再用`bl`跳转语句跳转进`s_init`函数。这个函数返回后，将`ip`和`lr`出栈，并将`lr`赋值给`pc`。我们将这里`lr`分析一下，因为这里的`lowlevel_init`函数是用`b`语句跳转进来的，所以再往前分析，`lr`寄存器中保存的就是`cpu_init_crit`的返回地址，这样的话，执行完这一语句后，就到了`start.S`文件中`save_boot_params_ret`函数里面的`b _main`语句了。

```
	/*
	 * Save the old lr(passed in ip) and the current lr to stack
	 */
	push	{ip, lr}

	/*
	 * Call the very early init function. This should do only the
	 * absolute bare minimum to get started. It should not:
	 *
	 * - set up DRAM
	 * - use global_data
	 * - clear BSS
	 * - try to start a console
	 *
	 * For boards with SPL this should be empty since SPL can do all of
	 * this init in the SPL board_init_f() function which is called
	 * immediately after this.
	 */
	bl	s_init
	pop	{ip, pc}
ENDPROC(lowlevel_init)
```

## 4.s_init函数

`s_init`函数定义在`arch/arm/cpu/armv7/mx6/soc.c`文件中，定义如下：

```c
void s_init(void)
{
	struct anatop_regs *anatop = (struct anatop_regs *)ANATOP_BASE_ADDR;
	struct mxc_ccm_reg *ccm = (struct mxc_ccm_reg *)CCM_BASE_ADDR;
	u32 mask480;
	u32 mask528;
	u32 reg, periph1, periph2;

	if (is_cpu_type(MXC_CPU_MX6SX) || is_cpu_type(MXC_CPU_MX6UL) ||
	    is_cpu_type(MXC_CPU_MX6ULL) || is_cpu_type(MXC_CPU_MX6SLL))
		return;

	/* Due to hardware limitation, on MX6Q we need to gate/ungate all PFDs
	 * to make sure PFD is working right, otherwise, PFDs may
	 * not output clock after reset, MX6DL and MX6SL have added 396M pfd
	 * workaround in ROM code, as bus clock need it
	 */

	mask480 = ANATOP_PFD_CLKGATE_MASK(0) |
		ANATOP_PFD_CLKGATE_MASK(1) |
		ANATOP_PFD_CLKGATE_MASK(2) |
		ANATOP_PFD_CLKGATE_MASK(3);
	mask528 = ANATOP_PFD_CLKGATE_MASK(1) |
		ANATOP_PFD_CLKGATE_MASK(3);

	reg = readl(&ccm->cbcmr);
	periph2 = ((reg & MXC_CCM_CBCMR_PRE_PERIPH2_CLK_SEL_MASK)
		>> MXC_CCM_CBCMR_PRE_PERIPH2_CLK_SEL_OFFSET);
	periph1 = ((reg & MXC_CCM_CBCMR_PRE_PERIPH_CLK_SEL_MASK)
		>> MXC_CCM_CBCMR_PRE_PERIPH_CLK_SEL_OFFSET);

	/* Checking if PLL2 PFD0 or PLL2 PFD2 is using for periph clock */
	if ((periph2 ! 0x2) && (periph1 != 0x2))
		mask528 |= ANATOP_PFD_CLKGATE_MASK(0);

	if ((periph2 != 0x1) && (periph1 != 0x1) &&
		(periph2 != 0x3) && (periph1 != 0x3))
		mask528 |= ANATOP_PFD_CLKGATE_MASK(2);

	writel(mask480, &anatop->pfd_480_set);
	writel(mask528, &anatop->pfd_528_set);
	writel(mask480, &anatop->pfd_480_clr);
	writel(mask528, &anatop->pfd_528_clr);
}
```

这里因为CPU的类型是`MX6ULL`，所以这里会直接返回出去，根据上一小节最后的分析，这里返回后就执行到`save_boot_params_ret`函数里面的`b _main`语句了。

## 5._main函数

`_main`函数定义在`arch/arm/lib/crt0.S`文件中，内容如下所示：

```c
ENTRY(_main)

/*
 * Set up initial C runtime environment and call board_init_f(0).
 */

#if defined(CONFIG_SPL_BUILD) && defined(CONFIG_SPL_STACK)
	ldr	sp, =(CONFIG_SPL_STACK)
#else
	ldr	sp, =(CONFIG_SYS_INIT_SP_ADDR)
#endif
#if defined(CONFIG_CPU_V7M)	/* v7M forbids using SP as BIC destination */
	mov	r3, sp
	bic	r3, r3, #7
	mov	sp, r3
#else
	bic	sp, sp, #7	/* 8-byte alignment for ABI compliance */
#endif
	mov	r0, sp
	bl	board_init_f_alloc_reserve
	mov	sp, r0
	/* set up gd here, outside any C code */
	mov	r9, r0
	bl	board_init_f_init_reserve

	mov	r0, #0
	bl	board_init_f

#if ! defined(CONFIG_SPL_BUILD)

/*
 * Set up intermediate environment (new sp and gd) and call
 * relocate_code(addr_moni). Trick here is that we'll return
 * 'here' but relocated.
 */

	ldr	sp, [r9, #GD_START_ADDR_SP]	/* sp = gd->start_addr_sp */
#if defined(CONFIG_CPU_V7M)	/* v7M forbids using SP as BIC destination */
	mov	r3, sp
	bic	r3, r3, #7
	mov	sp, r3
#else
	bic	sp, sp, #7	/* 8-byte alignment for ABI compliance */
#endif
	ldr	r9, [r9, #GD_BD]		/* r9 = gd->bd */
	sub	r9, r9, #GD_SIZE		/* new GD is below bd */

	adr	lr, here
	ldr	r0, [r9, #GD_RELOC_OFF]		/* r0 = gd->reloc_off */
	add	lr, lr, r0
#if defined(CONFIG_CPU_V7M)
	orr	lr, #1				/* As required by Thumb-only */
#endif
	ldr	r0, [r9, #GD_RELOCADDR]		/* r0 = gd->relocaddr */
	b	relocate_code
here:
/*
 * now relocate vectors
 */

	bl	relocate_vectors

/* Set up final (full) environment */

	bl	c_runtime_cpu_setup	/* we still call old routine here */
#endif
#if !defined(CONFIG_SPL_BUILD) || defined(CONFIG_SPL_FRAMEWORK)
# ifdef CONFIG_SPL_BUILD
	/* Use a DRAM stack for the rest of SPL, if requested */
	bl	spl_relocate_stack_gd
	cmp	r0, #0
	movne	sp, r0
	movne	r9, r0
# endif
	ldr	r0, =__bss_start	/* this is auto-relocated! */

#ifdef CONFIG_USE_ARCH_MEMSET
	ldr	r3, =__bss_end		/* this is auto-relocated! */
	mov	r1, #0x00000000		/* prepare zero to clear BSS */

	subs	r2, r3, r0		/* r2 = memset len */
	bl	memset
#else
	ldr	r1, =__bss_end		/* this is auto-relocated! */
	mov	r2, #0x00000000		/* prepare zero to clear BSS */

clbss_l:cmp	r0, r1			/* while not at end of BSS */
#if defined(CONFIG_CPU_V7M)
	itt	lo
#endif
	strlo	r2, [r0]		/* clear 32-bit BSS word */
	addlo	r0, r0, #4		/* move to next */
	blo	clbss_l
#endif

#if ! defined(CONFIG_SPL_BUILD)
	bl coloured_LED_init
	bl red_led_on
#endif
	/* call board_init_r(gd_t *id, ulong dest_addr) */
	mov     r0, r9                  /* gd_t */
	ldr	r1, [r9, #GD_RELOCADDR]	/* dest_addr */
	/* call board_init_r */
#if defined(CONFIG_SYS_THUMB_BUILD)
	ldr	lr, =board_init_r	/* this is auto-relocated! */
	bx	lr
#else
	ldr	pc, =board_init_r	/* this is auto-relocated! */
#endif
	/* we should not return here. */
#endif

ENDPROC(_main)
```

### 5.1 board_init_f函数

```c
/*
 * Set up initial C runtime environment and call board_init_f(0).
 */

#if defined(CONFIG_SPL_BUILD) && defined(CONFIG_SPL_STACK)
	ldr	sp, =(CONFIG_SPL_STACK)
#else
	ldr	sp, =(CONFIG_SYS_INIT_SP_ADDR)
#endif
#if defined(CONFIG_CPU_V7M)	/* v7M forbids using SP as BIC destination */
	mov	r3, sp
	bic	r3, r3, #7
	mov	sp, r3
#else
	bic	sp, sp, #7	/* 8-byte alignment for ABI compliance */
#endif
	mov	r0, sp
	bl	board_init_f_alloc_reserve
	mov	sp, r0
	/* set up gd here, outside any C code */
	mov	r9, r0
	bl	board_init_f_init_reserve

	mov	r0, #0
	bl	board_init_f
```

根据之前解析，`CONFIG_SPL_BUILD`这个宏没有被定义，所以sp寄存器中保存`CONFIG_SYS_INIT_SP_ADDR`这个宏的值，也就是`0x0091FF00`，接着对sp寄存器中的值进行8字节对齐，并将其写进r0寄存器中作为`board_init_f_alloc_reserve`函数的参数传入。这个函数定义在`common/init/board_init.c`文件中，内容如下：

```c
ulong board_init_f_alloc_reserve(ulong top) // top = 0x0091FF00
{
	/* Reserve early malloc arena */
#if defined(CONFIG_SYS_MALLOC_F)  
	top -= CONFIG_SYS_MALLOC_F_LEN;		// top = 0x0091FF00 - 0x400 = 0x0091FB00
#endif
	/* LAST : reserve GD (rounded up to a multiple of 16 bytes) */
	top = rounddown(top-sizeof(struct global_data), 16); 

	return top;
}
```

`CONFIG_SYS_MALLOC_F`和`CONFIG_SYS_MALLOC_F_LEN`这2个宏定义在`include/generated/autoconf.h`文件汇中，其中`CONFIG_SYS_MALLOC_F_LEN`值为`0x400`，此时的`top`为`0x0091FB00`。接下来对`top`又减去`global_data`的大小248字节，即`0x91FB00-248=0x0091FA08`，并进行向下16字节对齐。最终，该函数返回值`top`为`0x0091FA00`。在回到`_main`函数中，函数的返回值保存到sp寄存器和r9寄存器中，又跳转到`board_init_f_init_reserve`函数中去了，内容如下：

```c
void board_init_f_init_reserve(ulong base)
{
	struct global_data *gd_ptr;
#ifndef _USE_MEMCPY
	int *ptr;
#endif

	/*
	 * clear GD entirely and set it up.
	 * Use gd_ptr, as gd may not be properly set yet.
	 */

	gd_ptr = (struct global_data *)base;
	/* zero the area */
#ifdef _USE_MEMCPY
	memset(gd_ptr, '\0', sizeof(*gd));
#else
	for (ptr = (int *)gd_ptr; ptr < (int *)(gd_ptr + 1); )
		*ptr++ = 0;
#endif
	/* set GD unless architecture did it already */
#if !defined(CONFIG_ARM)  // 定义了CONFIG_ARM，所以不走
	arch_setup_gd(gd_ptr);
#endif
	/* next alloc will be higher by one GD plus 16-byte alignment */
	base += roundup(sizeof(struct global_data), 16);

	/*
	 * record early malloc arena start.
	 * Use gd as it is now properly set for all architectures.
	 */

#if defined(CONFIG_SYS_MALLOC_F) // 定义了CONFIG_SYS_MALLOC_F
	/* go down one 'early malloc arena' */
	gd->malloc_base = base;
	/* next alloc will be higher by one 'early malloc arena' size */
	base += CONFIG_SYS_MALLOC_F_LEN;
#endif
}
```

这个函数也在`common/init/board_init.c`文件中，首先让`gd_ptr`指向`base`也就是`r0`寄存器中的`0x0091FA00`地址。然后对这个结构体进行`memset`操作(清零)。接着`base`加上`global_data`大小，并向上16字节对齐后，此时`base`指向`malloc`的基地址，将其赋值给`gd->malloc_base`后又加上`0x400`，这个函数就到此结束了。此时内存分布如下所示：

![](./image/sp02.png)

回到`_main`函数中，将0写入`r0`寄存器后，又调用了`board_init_f`函数，这个函数定义在`common/board_f.c`文件中，内容如下：

```c
void board_init_f(ulong boot_flags)
{
#ifdef CONFIG_SYS_GENERIC_GLOBAL_DATA // 没有定义CONFIG_SYS_GENERIC_GLOBAL_DATA
	/*
	 * For some archtectures, global data is initialized and used before
	 * calling this function. The data should be preserved. For others,
	 * CONFIG_SYS_GENERIC_GLOBAL_DATA should be defined and use the stack
	 * here to host global data until relocation.
	 */
	gd_t data;

	gd = &data;

	/*
	 * Clear global data before it is accessed at debug print
	 * in initcall_run_list. Otherwise the debug print probably
	 * get the wrong vaule of gd->have_console.
	 */
	zero_global_data();
#endif

	gd->flags = boot_flags; // 0
	gd->have_console = 0;

	if (initcall_run_list(init_sequence_f))
		hang();

#if !defined(CONFIG_ARM) && !defined(CONFIG_SANDBOX) && \
		!defined(CONFIG_EFI_APP)
	/* NOTREACHED - jump_to_copy() does not return */
	hang();
#endif
}
```

这里的全局变量`gd`是由`board_f.c`文件顶部`DECLARE_GLOBAL_DATA_PTR;`定义的，这个宏在`arch/arm/include/asm/global_data.h`中，内容如下：

```c
#ifdef CONFIG_ARM64
#define DECLARE_GLOBAL_DATA_PTR		register volatile gd_t *gd asm ("x18")
#else
#define DECLARE_GLOBAL_DATA_PTR		register volatile gd_t *gd asm ("r9")
#endif
#endif
```

之前有解析r9寄存器中保存的地址是`0x0091FA00`，也就是`global_data`的首地址。这个`gd`变量一直到`uboot`重定位之前一直有效。然后设置`gd->flags`和`gd->have_console`为0，最后调用`initcall_run_list`函数,这里的参数`init_sequence_f`是应该函数列表，去掉宏定义后如下所示：

```c
static init_fnc_t init_sequence_f[] = {
	setup_mon_len, 
	initf_malloc, 
	initf_console_record,
	arch_cpu_init,		
	initf_dm,			
	arch_cpu_init_dm,		
	mark_bootstage,			
	board_early_init_f,	
	timer_init,			
	board_postclk_init,    
	get_clocks,			
	env_init,			
	init_baud_rate,		 
	serial_init,	
	console_init_f,			
	display_options,		
	display_text_info,		
	print_cpuinfo,	
	show_board_info,		
	init_func_i2c,		
	announce_dram_init,		
	dram_init,			
	setup_dest_addr,	
	reserve_round_4k,	
	reserve_mmu,		
	reserve_trace,		
	reserve_uboot,		
	reserve_malloc,			
	reserve_board,		
	setup_machine,			
	reserve_global_data,	
	reserve_fdt,		
	reserve_arch,			
	reserve_stacks,			
	setup_dram_config,		
	show_dram_config,		
	display_new_sp,			
	reloc_fdt,				
	setup_reloc,			
	NULL
};
```

**1.setup_mon_len函数**

这个函数用于计算uboot的大小，并将其赋值给`gd->mon_led`，定义在`common/board_f.c`文件中，内容如下所示：

```c
static int setup_mon_len(void)
{
#if defined(__ARM__) || defined(__MICROBLAZE__)
	gd->mon_len = (ulong)&__bss_end - (ulong)_start;  // 定义了__ARM__ (此项目分析值为0xA8E74，仅供参考)
#elif defined(CONFIG_SANDBOX) || defined(CONFIG_EFI_APP)
	gd->mon_len = (ulong)&_end - (ulong)_init;
#elif defined(CONFIG_BLACKFIN) || defined(CONFIG_NIOS2)
	gd->mon_len = CONFIG_SYS_MONITOR_LEN;
#elif defined(CONFIG_NDS32)
	gd->mon_len = (ulong)(&__bss_end) - (ulong)(&_start);
#else
	/* TODO: use (ulong)&__bss_end - (ulong)&__text_start; ? */
	gd->mon_len = (ulong)&__bss_end - CONFIG_SYS_MONITOR_BASE;
#endif
	return 0;
}
```

**2.initf_malloc函数**

这个函数用于初始化`gd`中关于`malloc`的一些变量，定义在`common/dlmalloc.c`文件中，内容如下所示：

```c
int initf_malloc(void)
{
#ifdef CONFIG_SYS_MALLOC_F_LEN
	assert(gd->malloc_base);	/* Set up by crt0.S 补充：common/init/board_init.c`中`board_init_f_init_reserve`函数有设置 */
	gd->malloc_limit = CONFIG_SYS_MALLOC_F_LEN;  /* 0x400 */
	gd->malloc_ptr = 0;
#endif
    
	return 0;
}
```

**3.initf_console_record函数**

因为没有定义`CONFIG_CONSOLE_RECORD`，这个函数直接`return 0`了，定义在`common/dlmalloc.c`文件中，内容如下所示：

```c
static int initf_console_record(void)
{
#if defined(CONFIG_CONSOLE_RECORD) && defined(CONFIG_SYS_MALLOC_F_LEN)
	return console_record_init();
#else
	return 0;
#endif
}
```

**4.arch_cpu_init函数**

这个函数用于初始化CPU的一些设置，定义在`arch/arm/cpu/armv7/mx6/soc.c`文件中，内容如下：

```c
int arch_cpu_init(void)
{
	if (!is_cpu_type(MXC_CPU_MX6SL) && !is_cpu_type(MXC_CPU_MX6SX)
	    && !is_cpu_type(MXC_CPU_MX6UL) && !is_cpu_type(MXC_CPU_MX6ULL)
	    && !is_cpu_type(MXC_CPU_MX6SLL)) {
		/*
		 * imx6sl doesn't have pcie at all.
		 * this bit is not used by imx6sx anymore
		 */
		u32 val;

		/*
		 * There are about 0.02% percentage, random pcie link down
		 * when warm-reset is used.
		 * clear the ref_ssp_en bit16 of gpr1 to workaround it.
		 * then warm-reset imx6q/dl/solo again.
		 */
		val = readl(IOMUXC_BASE_ADDR + 0x4);
		if (val & (0x1 << 16)) {
			val &= ~(0x1 << 16);
			writel(val, IOMUXC_BASE_ADDR + 0x4);
			reset_cpu(0);
		}
	}

	init_aips();

	/* Need to clear MMDC_CHx_MASK to make warm reset work. */
	clear_mmdc_ch_mask();

	/*
	 * Disable self-bias circuit in the analog bandap.
	 * The self-bias circuit is used by the bandgap during startup.
	 * This bit should be set after the bandgap has initialized.
	 */
	init_bandgap();

	if (!is_cpu_type(MXC_CPU_MX6UL) && !is_cpu_type(MXC_CPU_MX6ULL)) {
		/*
		 * When low freq boot is enabled, ROM will not set AHB
		 * freq, so we need to ensure AHB freq is 132MHz in such
		 * scenario.
		 */
		if (mxc_get_clock(MXC_ARM_CLK) == 396000000)
			set_ahb_rate(132000000);
	}

	if (is_cpu_type(MXC_CPU_MX6UL)) {
		if (is_soc_rev(CHIP_REV_1_0)) {
			/*
			 * According to the design team's requirement on i.MX6UL,
			 * the PMIC_STBY_REQ PAD should be configured as open
			 * drain 100K (0x0000b8a0).
			 */
			writel(0x0000b8a0, IOMUXC_BASE_ADDR + 0x29c);
		} else {
			/*
			 * From TO1.1, SNVS adds internal pull up control for POR_B,
			 * the register filed is GPBIT[1:0], after system boot up,
			 * it can be set to 2b'01 to disable internal pull up.
			 * It can save about 30uA power in SNVS mode.
			 */
			writel((readl(MX6UL_SNVS_LP_BASE_ADDR + 0x10) & (~0x1400)) | 0x400,
				MX6UL_SNVS_LP_BASE_ADDR + 0x10);
		}
	}

	if (is_cpu_type(MXC_CPU_MX6ULL)) {
		/*
		 * GPBIT[1:0] is suggested to set to 2'b11:
		 * 2'b00 : always PUP100K
		 * 2'b01 : PUP100K when PMIC_ON_REQ or SOC_NOT_FAIL
		 * 2'b10 : always disable PUP100K
		 * 2'b11 : PDN100K when SOC_FAIL, PUP100K when SOC_NOT_FAIL
		 * register offset is different from i.MX6UL, since
		 * i.MX6UL is fixed by ECO.
		 */
		writel(readl(MX6UL_SNVS_LP_BASE_ADDR) |
			0x3, MX6UL_SNVS_LP_BASE_ADDR);
	}

		/* Set perclk to source from OSC 24MHz */
#if defined(CONFIG_MX6SL)
	set_preclk_from_osc();
#endif

	if (is_cpu_type(MXC_CPU_MX6SX))
		set_uart_from_osc();

	imx_set_wdog_powerdown(false); /* Disable PDE bit of WMCR register */

	if (!is_cpu_type(MXC_CPU_MX6SL) && !is_cpu_type(MXC_CPU_MX6UL) &&
	    !is_cpu_type(MXC_CPU_MX6ULL) && !is_cpu_type(MXC_CPU_MX6SLL))
		imx_set_pcie_phy_power_down();

	if (!is_mx6dqp() && !is_cpu_type(MXC_CPU_MX6UL) &&
	    !is_cpu_type(MXC_CPU_MX6ULL) && !is_cpu_type(MXC_CPU_MX6SLL))
		imx_set_vddpu_power_down();

#ifdef CONFIG_APBH_DMA
	/* Start APBH DMA */
	mxs_dma_init();
#endif

	init_src();

	if (is_mx6dqp())
		writel(0x80000201, 0xbb0608);

	return 0;
}
```

**5.initf_dm函数**

这个函数主要用于初始化驱动模型，不做具体分析，定义在`common/board_f.c`文件中，内容如下：

```c
static int initf_dm(void)
{
#if defined(CONFIG_DM) && defined(CONFIG_SYS_MALLOC_F_LEN)
	int ret;

	ret = dm_init_and_scan(true);
	if (ret)
		return ret;
#endif
#ifdef CONFIG_TIMER_EARLY
	ret = dm_timer_init();
	if (ret)
		return ret;
#endif

	return 0;
}
```

**6.arch_cpu_init_dm函数**

这个函数没有在其他文件定义，所以走的是`common/board_f.c`文件中的空函数，内容如下：

```c
__weak int arch_cpu_init_dm(void)
{
	return 0;
}
```

**7.mark_bootstage函数**

定义在`common/board_f.c`文件中，记录`board_init_f`引导阶段(调用在`arch_cpy_init`之后)，内容如下所示：

```c
static int mark_bootstage(void)
{
	bootstage_mark_name(BOOTSTAGE_ID_START_UBOOT_F, "board_init_f");

	return 0;
}
```

**8.board_early_init_f函数**

imx早期板子初始化设置，这里`IMX6ULL`用于初始化串口相关(UART)，函数定义在`board/freescale/mx6ullevk/mx6ullevk.c`文件中，内容如下所示：

```c
static void setup_iomux_uart(void)
{
	imx_iomux_v3_setup_multiple_pads(uart1_pads, ARRAY_SIZE(uart1_pads));
}


int board_early_init_f(void)
{
	setup_iomux_uart();

	return 0;
}
```

**9.timer_init函数**

初始化定时器，`Cortex-A7`内核有一个定时器，为`Uboot`提供时间，这个函数定义在`arch/arm/imx-common/syscounter.c`文件中，内容如下所示：

```c
int timer_init(void)
{
	struct sctr_regs *sctr = (struct sctr_regs *)SCTR_BASE_ADDR;
	unsigned long val, freq;

	freq = CONFIG_SC_TIMER_CLK;
	asm("mcr p15, 0, %0, c14, c0, 0" : : "r" (freq));

	writel(freq, &sctr->cntfid0);

	/* Enable system counter */
	val = readl(&sctr->cntcr);
	val &= ~(SC_CNTCR_FREQ0 | SC_CNTCR_FREQ1);
	val |= SC_CNTCR_FREQ0 | SC_CNTCR_ENABLE | SC_CNTCR_HDBG;
	writel(val, &sctr->cntcr);

	gd->arch.tbl = 0;
	gd->arch.tbu = 0;

	return 0;
}
```

**10.board_postclk_init函数**

初始化`VDDSOC`电压，该函数定义在`arch/arm/cpu/armv7/mx6/soc.c`文件中，内容如下所示：

```c
int board_postclk_init(void)
{
	/* NO LDO SOC on i.MX6SLL */
	if (is_cpu_type(MXC_CPU_MX6SLL))
		return 0;

	set_ldo_voltage(LDO_SOC, 1175);	/* Set VDDSOC to 1.175V */

	return 0;
}
```

**11.get_clocks函数**

用于获取时钟，`IMX6ULL`获取的是`sdhc_clk`时钟，也就是SD卡外设的时钟。该函数定义在`arch/arm/imx-common/speed.c`文件中，内容如下所示：

```c
int get_clocks(void)
{
#ifdef CONFIG_FSL_ESDHC
#ifdef CONFIG_FSL_USDHC
#if CONFIG_SYS_FSL_ESDHC_ADDR == USDHC2_BASE_ADDR
	gd->arch.sdhc_clk = mxc_get_clock(MXC_ESDHC2_CLK);   //该函数定义在arch/arm/cpu/armv7/mx6/clock.c
#elif CONFIG_SYS_FSL_ESDHC_ADDR == USDHC3_BASE_ADDR
	gd->arch.sdhc_clk = mxc_get_clock(MXC_ESDHC3_CLK);
#elif CONFIG_SYS_FSL_ESDHC_ADDR == USDHC4_BASE_ADDR
	gd->arch.sdhc_clk = mxc_get_clock(MXC_ESDHC4_CLK);
#else
	gd->arch.sdhc_clk = mxc_get_clock(MXC_ESDHC_CLK);
#endif
#else
#if CONFIG_SYS_FSL_ESDHC_ADDR == MMC_SDHC2_BASE_ADDR
	gd->arch.sdhc_clk = mxc_get_clock(MXC_ESDHC2_CLK);
#elif CONFIG_SYS_FSL_ESDHC_ADDR == MMC_SDHC3_BASE_ADDR
	gd->arch.sdhc_clk = mxc_get_clock(MXC_ESDHC3_CLK);
#elif CONFIG_SYS_FSL_ESDHC_ADDR == MMC_SDHC4_BASE_ADDR
	gd->arch.sdhc_clk = mxc_get_clock(MXC_ESDHC4_CLK);
#else
	gd->arch.sdhc_clk = mxc_get_clock(MXC_ESDHC_CLK);
#endif
#endif
#endif
	return 0;
}
```

**12.env_init函数**

设置`gd->env_addr`环境变量的保存地址，以及`gd->env_valid`，这个函数定义在`common/env_mmc.c`文件中，内容如下所示：

```c
int env_init(void)
{
	/* use default */
	gd->env_addr	= (ulong)&default_environment[0];
	gd->env_valid	= 1;

	return 0;
}
```

**13.init_baud_rate函数**



```c
```

**14.serial_init函数**



```c
```

**15.console_init_f函数**



```c
```

**16.display_options函数**



```c
```

**17.display_text_info函数**



```c
```

**18.print_cpuinfo函数**



```c
```

**19.show_board_info函数**



```c
```

**20.init_func_i2c函数**



```c
```

**21.announce_dram_init函数**



```c
```

**22.dram_init函数**



```c
```

**23.setup_dest_addr函数**



```c
```

**24.reserve_round_4k函数**



```c
```

**25.reserve_mmu函数**



```c
```

**26.reserve_trace函数**



```c
```

**27.reserve_uboot函数**



```c
```

**28.reserve_malloc函数**



```c
```

**29.reserve_board函数**



```c
```

**30.setup_machine函数**



```c
```

**31.reserve_global_data函数**



```c
```

**32.reserve_fdt函数**



```c
```

**33.reserve_arch函数**



```c
```

**34.reserve_stacks函数**



```c
```

**35.setup_dram_config函数**



```c
```

**36.show_dram_config函数**



```c
```

**37.display_new_sp函数**



```c
```

**38.reloc_fdt函数**



```c
```

**29.setup_reloc函数**



```c
```

