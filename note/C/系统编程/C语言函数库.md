# C语言函数

## 1.字符判断函数

### **isalnum函数**

>**头文件：**`#include <ctype.h>`
>
>**函数定义：**`int isalnum(int c);`
>
>**函数说明：**检查参数是否为英文字母或阿拉伯数字，在标准C中相当于`(isalpha(c)||isdigit(c))`判断。
>
>**返回值：**参数c为数字或字母则返回TRUE，否则返回NULL(0)。
>
>**补充：**该函数为宏定义，并非真正函数。

```c
#include <stdio.h>
#include <ctype.h>

int main()
{
	int i;
	char str[] = "<abc123>";

	for (int i = 0; str[i] != 0; i++)
	{
		printf("%c:%s\n", str[i], isalnum(str[i]) ? "true" : "false");
	}
	return 0;
}
```

### **isalpha函数**

> **头文件：**`#include <ctype.h>`
>
> **函数定义：**`int isalpha(int c);`
>
> **函数说明：**检查参数c是否为英文字母，在标准C中相当于`(isupper(c)||islower(c))`判断。
>
> **返回值：**参数c为英文字母则返回TRUE，否则返回NULL(0)。
>
> **补充：**该函数为宏定义，并非真正函数。

```c
#include <stdio.h>
#include <ctype.h>

int main()
{
	int i;
	char str[] = "<abc123>";

	for (i = 0; str[i] != 0; i++)
	{
		printf("%c:%s\n", str[i], isalpha(str[i]) ? "true" : "false");
	}
	return 0;
}
```

### **isascii函数**

>**头文件：**`#include <ctype.h>`
>
>**函数定义：**`int isascii(int c);`
>
>**函数说明：**检查参数c是否为ASCII码字符，也就是判断字符是否在0到127之间。
>
>**返回值：**参数c为ASCII码字符则返回TRUE，否则返回NULL(0)。
>
>**补充：**该函数为宏定义，并非真正函数。

```c
#include <stdio.h>
#include <ctype.h>

int main()
{
	int i;

	for (i = 1; i < 6; i++)
	{
		printf("%d:%s\n", i * 40, isascii(i * 40) ? "true" : "false");
	}
	return 0;
}
```

### **isblank函数**

> **头文件：**`#include <ctype.h>`
>
> **函数定义：**`int isblank(int c);`
>
> **函数说明：**检查参数c是否为空格字符，也就是判断是否为空格(space ASCII:32)或者定位字符(tab ASCII::9)
>
> **返回值：**参数c为空格字符则返回TRUE，否则返回NULL(0)。
>
> **补充：**该函数为宏定义，并非真正函数。

```c
#include <stdio.h>
#include <ctype.h>

int main()
{
	int i;
	char str[] = "a 1\t?\n";

	for (i = 0; str[i] != 0; i++)
	{
		printf("%c:%s\n", str[i], isblank(str[i]) ? "true" : "flase");
	}
	return 0;
}
```

### **iscntrl函数**

> **头文件：**`#include <ctype.h>`
>
> **函数定义：**`int iscntrl(int c);`
>
> **函数说明：**检查参数c是否为ASCII控制码，也就是判断是否在0到31之间。
>
> **返回值：**参数c为ASCII控制码则返回TRUE，否则返回NULL(0)。
>
> **补充：**该函数为宏定义，并非真正函数。

```c
#include <stdio.h>
#include <ctype.h>

int main()
{
	int i;

	for (i = 1; i < 6; i++)
	{
		printf("%d:%s\n", i * 10, iscntrl(i * 10) ? "true" : "false");
	}
	return 0;
}
```

### **isdigit函数**

> **头文件：**`#include <ctype.h>`
>
> **函数定义：**`int isdigit(int c);`
>
> **函数说明：**检查参数c是否为阿拉伯数字0到9。
>
> **返回值：**参数c为阿拉伯数字则返回TRUE，否则返回NULL(0)。
>
> **补充：**该函数为宏定义，并非真正函数。

```c
#include <stdio.h>
#include <ctype.h>

int main()
{
	int i;
	char str[] = "<1a2b>";

	for (i = 0; str[i] != 0; i++)
	{
		printf("%c:%s\n", str[i], isdigit(str[i]) ? "true" : "false");
	}
	return 0;
}
```

### **isgraph函数**

> **头文件：**`#include <ctype.h>`
>
> **函数定义：**`int isgraph(int c);`
>
> **函数说明：**检查参数c是否为可打印字符(不包含空格和定位字符)。
>
> **返回值：**参数c为可打印且不是空格字符和定位字符则返回TRUE，否则返回NULL(0)。
>
> **补充：**该函数为宏定义，并非真正函数。

```c
#include <stdio.h>
#include <ctype.h>

int main()
{
	char str[] = "1	a 3>";
	int i;
	for (i = 0; i < 6; i++)
	{
		printf("%c:%s\n", str[i], isgraph(str[i]) ? "true" : "false");
	}
	return 0;
}
```

### **islower函数**

> **头文件：**`#include <ctype.h>`
>
> **函数定义：**`int islower(int c);`
>
> **函数说明：**检查参数c是否为小写英文字母。
>
> **返回值：**参数c为小写英文字母则返回TRUE，否则返回NULL(0)。
>
> **补充：**该函数为宏定义，并非真正函数。

```c
#include <stdio.h>
#include <ctype.h>

int main()
{
	int i;
	char str[] = "Ass";

	for (i = 0; str[i] != 0; i++)
	{
		printf("%c:%s\n", str[i], islower(str[i]) ? "true" : "false");
	}
	return 0;
}
```

### **isprint函数**

> **头文件：**`#include <ctype.h>`
>
> **函数定义：**`int isprint(int c);`
>
> **函数说明：**检查参数c是否为可打印字符(包含空格，但是不包含定位字符等)。
>
> **返回值：**参数c为可打印或空格且不是定位字符则返回TRUE，否则返回NULL(0)。
>
> **补充：**该函数为宏定义，并非真正函数。

```c
#include <stdio.h>
#include <ctype.h>

int main()
{
	int i;
	char str[] = "1\ta 3>\n";

	for (i = 0; str[i] != 0; i++)
	{
		printf("%c:%s\n", str[i], isprint(str[i]) ? "true" : "false");
	}
	return 0;
}
```

### **isspace函数**

> **头文件：**`#include <ctype.h>`
>
> **函数定义：**`int isspace(int c);`
>
> **函数说明：**检查参数c是否为空格(' ')、定位字符('\t')、CR('\r')、换行('\n')、垂直定位字符('\v')或者翻页('\f')等。
>
> **返回值：**参数c为空格字符则返回TRUE，否则返回NULL(0)。
>
> **补充：**该函数为宏定义，并非真正函数。

```c
#include <stdio.h>
#include <ctype.h>

int main()
{
	int i;
	char str[] = "a 1\t>\n";

	for (i = 0; str[i] != 0; i++)
	{
		printf("%c:%s\n", str[i], isspace(str[i]) ? "true" : "false");
	}
	return 0;
}
```

### **ispunct函数**

> **头文件：**`#include <ctype.h>`
>
> **函数定义：**`int ispunct(int c);`
>
> **函数说明：**检查参数c是否为标点符号或特殊符号(也就是非空格、数字和字母)。
>
> **返回值：**参数c为标点符号或特殊符号则返回TRUE，否则返回NULL(0)。
>
> **补充：**该函数为宏定义，并非真正函数。

```c
#include <stdio.h>
#include <ctype.h>

int main()
{
	int i;
	char str[] = "1 s&*;sa\n";

	for (i = 0; str[i] != 0; i++)
	{
		printf("%c:%s\n", str[i], ispunct(str[i]) ? "true" : "false");
	}
	return 0;
}
```

### **isupper函数**

> **头文件：**`#include <ctype.h>`
>
> **函数定义：**`int isupper(int c);`
>
> **函数说明：**检查参数c是否为大写英文字母。
>
> **返回值：**参数c为大写英文字母则返回TRUE，否则返回NULL(0)。
>
> **补充：**该函数为宏定义，并非真正函数。

```c
#include <stdio.h>
#include <ctype.h>

int main()
{
	int i;
	char str[] = "A-b";

	for (i = 0; str[i] != 0; i++)
	{
		printf("%c:%s\n", str[i], isupper(str[i]) ? "true" : "false");
	}
	return 0;
}
```

### **isxdigit函数**

> **头文件：**`#include <ctype.h>`
>
> **函数定义：**`int isxdigit(int c);`
>
> **函数说明：**检查参数c是否为16进制数字，也就是是否属于0到9或A到F这个范围。
>
> **返回值：**参数c为为16进制数字则返回TRUE，否则返回NULL(0)。
>
> **补充：**该函数为宏定义，并非真正函数。

```c
#include <stdio.h>
#include <ctype.h>

int main()
{
	int i;
	char str[] = "1F2a&po";

	for (i = 0; str[i] != 0; i++)
	{
		printf("%c:%s\n", str[i], isxdigit(str[i]) ? "true" : "false");
	}
	return 0;
}
```

## 2.数据转换函数

### **atof函数**

> **头文件：**`#include <stdlib.h>`
>
> **函数定义：**`double atof(const char *nptr);`
>
> **函数说明：**atof函数会扫描nptr字符串，跳过前面的空格字符，直到遇到数字或者正负号才开始转换,直到遇到非数字或者字符串及'\0'才停止转换，并将结果返回。参数nptr字符串可包括正负号，小数点或E(e)表示指数。
>
> **返回值：**返回转换后的浮点型数。
>
> **补充：**`atof(nptr);`与使用`strtod(nptr,(char **)NULL);`结果相同。

```c
#include <stdio.h>
#include <stdlib.h>

int main()
{
	char *a = "  -12.5s";
	char *b = "105e-2 v ";

	printf("a=%.2f\n", atof(a));
	printf("b=%.2f\n", atof(b));
	return 0;
}
```

### **atoi函数**

> **头文件：**`#include <stdlib.h>`
>
> **函数定义：**`int atoi(const char *nptr);`
>
> **函数说明：**atoi函数会扫描nptr字符串，跳过前面的空格字符，直到遇到数字或者正负号才开始转换,直到遇到非数字或者字符串及'\0'才停止转换，并将结果返回。
>
> **返回值：**返回转换后的整型数。
>
> **补充：**`atoi(nptr);`与使用`strtol(nptr,(char **)NULL,10);`结果相同。

```c
#include <stdio.h>
#include <stdlib.h>

int main()
{
	char *a = " 80%";
	char *b = "-20 ";

	printf("a=%d\n", atoi(a));
	printf("b=%d\n", atoi(b));
	return 0;
}
```

### **atol函数**

> **头文件：**`#include <stdlib.h>`
>
> **函数定义：**`long atol(const char *nptr);`
>
> **函数说明：**atol函数会扫描nptr字符串，跳过前面的空格字符，直到遇到数字或者正负号才开始转换,直到遇到非数字或者字符串及'\0'才停止转换，并将结果返回。
>
> **返回值：**返回转换后的长整型数。
>
> **补充：**`atoi(nptr);`与使用`strtol(nptr,(char **)NULL,10);`结果相同。

```c
#include <stdio.h>
#include <stdlib.h>

int main()
{
	char *a = " 123456789";
	char *b = "-987654321";

	printf("a=%ld\n", atol(a));
	printf("b=%ld\n", atol(b));
	return 0;
}
```

### **ecvt函数**

>**头文件：**`#include <stdlib.h>`
>
>**函数定义：**`char *ecvt(double number, int ndigits, int *decpt, int *sign);`
>
>**函数说明：**ecvt函数将参数number转换成ASCII码字符串，参数ndigits表示总共显示的位数。若转换成功，参数decpt所指的变量会返回数值中小数点的位置(从左到右算起)，而参数sign指针所指的变量则表示数值正还是负，若为正则表示为0，否则为1。
>
>**返回值：**返回字符串指针，此字符串声明为static，若再调用ecvt或fcvt，此字符串内容会被覆盖。
>
>**补充：**建议使用`sprintf( )`做转换

```c
#include <stdio.h>
#include <stdlib.h>

int main()
{
    int decpt, sign;
    char *aptr, *bptr;
    double a = 123.456;
    double b = -1.2345;

    aptr = ecvt(a, 6, &decpt, &sign);
    printf("decpt=%d sign=%d value=%s\n", decpt, sign, aptr);

    bptr = ecvt(b, 5, &decpt, &sign);
    printf("decpt=%d sign=%d value=%s\n", decpt, sign, aptr);

    return 0;
}
```

### **fcvt函数**

> **头文件：**`#include <stdlib.h>`
>
> **函数定义：**`char *fcvt(double number, int ndigits, int *decpt, int *sign)`
>
> **函数说明：**ecvt函数将参数number转换成ASCII码字符串，参数ndigits表示小数点后显示的位数(区别ecvt)。若转换成功，参数decpt所指的变量会返回数值中小数点的位置(从左到右算起)，而参数sign指针所指的变量则表示数值正还是负，若为正则表示为0，否则为1。
>
> **返回值：**返回字符串指针，此字符串声明为static，若再调用ecvt或fcvt，此字符串内容会被覆盖。
>
> **补充：**建议使用`sprintf( )`做转换

```c
#include <stdio.h>
#include <stdlib.h>

int main()
{
    int decpt, sign;
    char *aptr, *bptr;
    double a = 123.456;
    double b = -1.2345;

    aptr = fcvt(a, 3, &decpt, &sign);
    printf("decpt=%d sign=%d value=%s\n", decpt, sign, aptr);

    bptr = fcvt(b, 3, &decpt, &sign);
    printf("decpt=%d sign=%d value=%s\n", decpt, sign, aptr);

    return 0;
}
```

### **gcvt函数**

> **头文件：**`#include <stdlib.h>`
>
> **函数定义：**`char *gcvt(double number, int ndigit, char *buf);`
>
> **函数说明：**ecvt函数将参数number转换成ASCII码字符串，参数ndigits表示小数点后显示的位数(区别ecvt)。gcvt与ecvt和fcvt不同的地方在于，gcvt所转换后的字符串包含小数点或正负符号。转换成功后的字符串会放在参数buf指针所指的空间。
>
> **返回值：**返回字符串指针，此地址为buf指针。
>
> **补充：**强烈建议使用`sprintf( )`做转换，这个函数容易出问题。

```c
#include <stdio.h>
#include <stdlib.h>

int main()
{
	char aptr[25], bptr[25];
	double a = 135.79;
	double b = -135.68;

	gcvt(a, 5, aptr);
	printf("a value=%s\n", aptr);

	gcvt(b, 4, bptr);
	printf("b value=%s\n", bptr);
	return 0;
}
```

### **strtod函数**

> **头文件：**`#include <stdlib.h>`
>
> **函数定义：**`double strtod(const char *nptr, char **endptr);`
>
> **函数说明：**strtod会扫描参数nptr字符串，跳过前面的空格字符，直到遇到数字或正负符号才开始转换，遇到非数字或字符串结束符('\0')时才结束转换，并将结果返回。若endptr不为NULL，则会遇到不合条件而终止的nptr中字符指针由endptr传回。参数nptr字符串包括正负号、小数点和指数e表示指数部分。
>
> **返回值：**返回转换后的浮点型数
>
> **补充：**参考atof()

```c
#include <stdio.h>
#include <stdlib.h>

int main()
{
	double ret;
	char nptr[30] = " -1.256asd";
	char *endptr;

	ret = strtod(nptr, &endptr);
	printf("ret:%f\nendptr:%s\n", ret, endptr);
	return 0;
}
```

### **strtol函数**

> **头文件：**`#include <stdlib.h>`
>
> **函数定义：**`long int strtol(const char *nptr, char **endptr, int base);`
>
> **函数说明：**strtol()会将参数你nptr字符串根据参数base来转换成长整型数。参数base范围从2到36或者为0。参数base代表采用的进制方式，如base为10则采用10进制，若base值为16则采用16进制等。当base值为0时则采用10进制作为转换，但是如果遇到0x前置字符则会使用16进制做转换。一开始strtol()会扫描参数nptr字符串，跳过前面的空格字符，直到遇到数字或正符符号才开始转换，再遇到非数字字符或字符串结束符('\0')才结束转换，并将结果返回。若参数endptr不为NULL，则会遇到不合条件而终止的nptr中字符指针由endptr传回。
>
> **返回值：**返回转换后的长整型数，否则返回ERANGE并将错误代码存如errno中。
>
> **补充：**ERANGE指定的转换字符超出合法范围。

```shell
#include <stdio.h>
#include <stdlib.h>

int main()
{
	long int ret_d, ret_b, ret_h;
	char *endptr_d, *endptr_b, *endptr_h;

	char *nptr_d = " -1911456461aa";
	char *nptr_b = " 10010110105sa";
	char *nptr_h = "1af226adfcgrgrr";

	ret_d = strtol(nptr_d, &endptr_d, 10);
	ret_b = strtol(nptr_b, &endptr_b, 2);
	ret_h = strtol(nptr_h, &endptr_h, 16);

	printf("d nptr:%s\tenptr:%s\tret:%ld\n", nptr_d, endptr_d, ret_d);
	printf("b nptr:%s\tenptr:%s\tret:%ld\n", nptr_b, endptr_b, ret_b);
	printf("h nptr:%s\tenptr:%s\tret:%ld\n", nptr_h, endptr_h, ret_h);
	return 0;
}
```

### **strtoul函数**

> **头文件：**`#include <stdlib.h>`
>
> **函数定义：**`unsigned long int strtoul(const char *nptr, char **endptr, int base);`
>
> **函数说明：**strtoul()会将参数你nptr字符串根据参数base来转换成无符号的长整型数。参数base范围从2到36或者为0。参数base代表采用的进制方式，如base为10则采用10进制，若base值为16则采用16进制等。当base值为0时则采用10进制作为转换，但是如果遇到0x前置字符则会使用16进制做转换。一开始strtoul()会扫描参数nptr字符串，跳过前面的空格字符，直到遇到数字或正符符号才开始转换，再遇到非数字字符或字符串结束符('\0')才结束转换，并将结果返回。若参数endptr不为NULL，则会遇到不合条件而终止的nptr中字符指针由endptr传回。
>
> **返回值：**返回转换后的长整型数，否则返回ERANGE并将错误代码存如errno中。
>
> **补充：**ERANGE指定的转换字符超出合法范围。

```shell
#include <stdio.h>
#include <stdlib.h>

int main()
{
	unsigned long int ret_d, ret_b, ret_h;
	char *endptr_d, *endptr_b, *endptr_h;

	char *nptr_d = " 1911456461aa";
	char *nptr_b = " 10010110105sa";
	char *nptr_h = "1af226adfcgrgrr";

	ret_d = strtoul(nptr_d, &endptr_d, 10);
	ret_b = strtoul(nptr_b, &endptr_b, 2);
	ret_h = strtoul(nptr_h, &endptr_h, 16);

	printf("d nptr:%s\tenptr:%s\tret:%ld\n", nptr_d, endptr_d, ret_d);
	printf("b nptr:%s\tenptr:%s\tret:%ld\n", nptr_b, endptr_b, ret_b);
	printf("h nptr:%s\tenptr:%s\tret:%ld\n", nptr_h, endptr_h, ret_h);
	return 0;
}
```

### **toascii函数**

> **头文件：**`#include <ctype.h>`
>
> **函数定义：**`int toascii(int c);`
>
> **函数说明：**toascii会将参数c转换成7位的unsigned char值，第八位则会被清除，此字符则会被转换位ASCII码字符(相当于与127相与)。
>
> **返回值：**将转换成功的ASCII字符值返回。

```shell
#include <stdio.h>
#include <ctype.h>

int main()
{
	int ret, c = 217;
	
	printf("%d %c\n", c, c);
	ret = toascii(c);
	printf("%d %c\n", ret, ret);
	return 0;
}
```

### **tolower函数**

> **头文件：**`#include <ctype.h>`
>
> **函数定义：**`int tolower(int c);`
>
> **函数说明：**若参数c为大写字符则转换为对应小写字符返回。
>
> **返回值：**返回转换后的小写字符，若不转换则返回参数c。

```shell
#include <stdio.h>
#include <ctype.h>

int main()
{
	char s[] = "aBcdEfghIJkLMno;@#$";
	int i;

	printf("Before：%s\n", s);
	for (i = 0; i < sizeof(s); i++)
	{
		s[i] = tolower(s[i]);
	}
	printf("After：%s\n", s);
	return 0;
}
```

### **toupper函数**

> **头文件：**`#include <ctype.h>`
>
> **函数定义：**`int toupper(int c);`
>
> **函数说明：**若参数c位小写字符则转换为对应大写字符返回。
>
> **返回值：**返回转换后的大写字符，若不转换则返回参数c。

```shell
#include <stdio.h>
#include <ctype.h>

int main()
{
	char s[] = "aBcdEfghIJkLMno;@#$";
	int i;

	printf("Before：%s\n", s);
	for (i = 0; i < sizeof(s); i++)
	{
		s[i] = toupper(s[i]);
	}
	printf("After：%s\n", s);
	return 0;
}
```

## 3.内存配置函数

### **alloca函数**

> **头文件：**`#include <stdlib.h>`或`#include <alloca.h>`
>
> **函数定义：**`void *alloca(size_t size);`
>
> **函数说明：**用来配置size个字节的内存空间，和malloc/calloc不同的是，alloca是从当前函数的栈区(stack)中配置内存，因此函数结束时会自动释放此空间。
>
> **返回值：**成功返回一指针，失败返回NULL。
>
> **补充：**alloca() 不具可移植性, 在没有传统堆栈的机器上很难实现。 

```shell
#include <stdio.h>
#include <stdlib.h>

int main()
{
	char *ret;

	ret = (char *)alloca(3);
	sprintf(ret,"abc");
	printf("%s\n", ret);
	return 0;
}
```

### **brk函数**

> **头文件：**`#include <stdlib.h>`或`#include <unistd.h>`
>
> **函数定义：**`int brk(void *addr);`
>
> **函数说明：**
>
> **返回值：**
>
> **补充：**

### **calloc函数**

### **free函数**

### **getpagesize函数**

### **malloc函数**

### **mmap函数**

### **munmap函数**

### **realloc函数**

### **sbrk函数**

## 4.时间函数

### **time函数**

> **头文件：**`#include <time.h>`
>
> **函数定义：**`time_t time(time_t *tloc);`
>
> **函数说明：**此函数会返回从公元1970年1月1日的UTC时间从0时0分0秒算起到现在所经过的秒数。如果t 并非空指针的话，此函数也会将返回值存到t指针所指的内存。
>
> **返回值：**成功则返回秒数，失败则返回((time_t)-1)值，错误原因存于errno中。

```c
#include <stdio.h>
#include <time.h>

int main()
{
	int seconds = time((time_t *)NULL);
	printf("now:%d\n", seconds);
	return 0;
}
```

### **ctime函数**

> **头文件：**`#include <time.h>`
>
> **函数定义：**`char *ctime(const time_t *timep);`
>
> **函数说明：**ctime()将参数timep所指的time_t结构中的信息转换成真实世界所使用的时间日期表示方法，然后将结果以字符串形态返回。此函数已经由时区转换成当地时间，字符串格式为"Wed Jun 30 21 :49 :08 1993\n"。
>
> **返回值：**返回一字符串表示目前当地的时间日期。
>
> **补充：**若再调用相关的时间日期函数，此字符串可能会被破坏。

```c
#include <stdio.h>
#include <time.h>

int main()
{
	time_t timep;
	time(&timep);
	printf("now:%s", ctime(&timep));
	return 0;
}
```

### **asctime函数**

> **头文件：**`#include <time.h>`
>
> **函数定义：**`char *asctime(const struct tm *tm);`
>
> **函数说明：**asctime()将参数timeptr所指的tm结构中的信息转换成真实世界所使用的时间日期表示方法，然后将结果以字符串形态返回。此函数已经由时区转换成当地时间，字符串格式为:"Wed Jun 30 21:49:08 1993\n"
>
> **返回值：**返回经过的秒数。
>
> **补充：**若再调用相关的时间日期函数，此字符串可能会被破坏。此函数与ctime不同处在于传入的参数是不同的结构。

```c
#include <stdio.h>
#include <time.h>

int main()
{
	time_t timep;
	time(&timep);
	printf("now:%s", asctime(localtime(&timep)));
	return 0;
}
```

### **ftime函数**

> **头文件：**`#include <sys/timeb.h>`
>
> **函数定义：**`int ftime(struct timeb *tp);`
>
> **函数说明：**这个函数以秒和毫秒的形式返回当前时间，从纪元1970-01-01 00:00:00 +0000 (UTC)开始。
>
> **返回值：**成功返回0
>
> **补充：**此函数已被弃用(可以使用gettimeofday获取微秒; clock_gettime获取纳秒)

```c
struct timeb
{
	time_t time;			// 纪元到现在的秒数
	unsigned short millitm;	// 表示毫秒
	short timezone;			// 当前时区
	short dstflag;			// 1表示启用夏时令
};
```

```c
#include <stdio.h>
#include <sys/timeb.h>

int main()
{
	struct timeb tp;
	ftime(&tp);
	printf("%ld,%d,%d,%d\n", tp.time, tp.millitm, tp.timezone, tp.timezone);
	return 0;
}
```

### **gmtime函数**

> **头文件：**`#include <time.h>`
>
> **函数定义：**`struct tm *gmtime(const time_t *timep);`
>
> **函数说明：**gmtime()将参数timep 所指的time_t 结构中的信息转换成真实世界所使用的时间日期表示方法，然后将结果由结构tm返回。
>
> **返回值：**返回结构tm代表目前UTC 时间。(未经时区转换)

```c
struct tm
{
    int tm_sec; 	// 代表目前秒数，正常范围为0-59，但允许至61秒
    int tm_min;		// 代表目前分数，范围0-59
    int tm_hour;	// 从午夜算起的时数，范围为0-23
    int tm_mday;	// 目前月份的日数，范围01-31
    int tm_mon;		// 代表目前月份，从一月算起，范围从0-11
    int tm_year;	// 从1900 年算起至今的年数
    int tm_wday;	// 一星期的日数，从星期一算起，范围为0-6
	int tm_yday;	// 从今年1月1日算起至今的天数，范围为0-365
	int tm_isdst;	// 夏时令标志，1表示启用
};
```

```c
#include <stdio.h>
#include <time.h>

int main()
{
	time_t timep;
	struct tm *p;

	time(&timep);
	p = gmtime(&timep);

	printf("%d-%d-%d ", (1900 + p->tm_year), p->tm_mon, p->tm_mday);
	printf("%d:%d:%d\n", p->tm_hour, p->tm_min, p->tm_sec);
	return 0;
}
```

### **localtime函数**

> **头文件：**`#include <time.h>`
>
> **函数定义：**`struct tm *localtime(const time_t *timep);`
>
> **函数说明：**localtime()将参数timep 所指的time_t 结构中的信息转换成真实世界所使用的时间日期表示方法，然后将结果由结构tm返回。
>
> **返回值：**返回结构tm代表当前时区的时间。

```c
struct tm
{
    int tm_sec; 	// 代表目前秒数，正常范围为0-59，但允许至61秒
    int tm_min;		// 代表目前分数，范围0-59
    int tm_hour;	// 从午夜算起的时数，范围为0-23
    int tm_mday;	// 目前月份的日数，范围01-31
    int tm_mon;		// 代表目前月份，从一月算起，范围从0-11
    int tm_year;	// 从1900 年算起至今的年数
    int tm_wday;	// 一星期的日数，从星期一算起，范围为0-6
	int tm_yday;	// 从今年1月1日算起至今的天数，范围为0-365
	int tm_isdst;	// 日光节约时间的旗标
};
```

```c
#include <stdio.h>
#include <time.h>

int main()
{
	time_t timep;
	struct tm *p;

	time(&timep);
	p = localtime(&timep);

	printf("%d-%d-%d ", (1900 + p->tm_year), p->tm_mon, p->tm_mday);
	printf("%d:%d:%d\n", p->tm_hour, p->tm_min, p->tm_sec);
	return 0;
}
```

### **mktime函数**

> **头文件：**`#include <time.h>`
>
> **函数定义：**`time_t mktime(struct tm *tm);`
>
> **函数说明：**mktime()用来将参数tm所指的tm结构数据转换成从公元1970年1月1日0时0分0秒到tm结构储存的时间所经过的秒数。
>
> **返回值：**返回经过的秒数。

```c
#include <stdio.h>
#include <time.h>

int main()
{
	time_t timep;
	time(&timep);
	printf("UTC:%ld\n", localtime(gmtime(&timep)));
	return 0;
}
```

### **strftime函数**

> **头文件：**`#include <time.h>`
>
> **函数定义：**`size_t strftime(char *s, size_t max, const char *format, const struct tm *tm);`
>
> **函数说明：**strftime()会将参数tm的时间结构，依照format所指定的字符串格式做转换，转换后的字符串内容将复制到参数s所指的数组中，该字符传的最大参数由参数max所控制。
>
> **返回值：**返回复制到参数s所指的字符串数组的总字符数，不包括字符串结束符号。如果返回0，表示未复制字符串到参数s内，但不一定有错误发生。
>
> **说明：**环境变量后面的TZ和TC_TIME会影响此函数结果。

```
%a		当地星期日期的名字缩写，如Sun。
%A		当地星期日期的完整名称，如Sunday。
%b		当地月份的缩写。
%B		当地月份的完整名称。
%c		当地适当的日期与时间表示法。
%C		以year/100表示年份。
%d		月里的天数，表示法为01-31。
%D		相当于"%m/%d/%y"格式。
%e		如同%d为一个月的天数，表示法为1-31。
%h		和%b相同。
%H		以24小时制表示小时数(00-23)。
%I		以12小时制表示小时数(01-12)。
%j		一年中的天数(001-366)。
%k		以24小时制表示小时数(0-23)。
%l		以12小时制表示小时数(1-12)。
%m		月份(01-12)。
%M		分钟(00-59)。
%n		同\n。
%p		显示对应的AM或PM表示。
%P		显示对应的am或pm表示。
%r		相当于使用"%I:%M:%S %p"格式。
%R		相当于使用"%H:%M"格式。
%s		从1970-01-01 00:00:00 UTC算起迄今的秒数。
%S		秒数(00-61)。
%t		同\t。
%T		24小时表示法，相当于"%H:%M:%S"格式。
%u		一星期中的星期日期，范围1-7，星期一从1开始。
%U		一年中的星期数(00-53)，一月第一个星期日开始为01.
%w		一星期中的星期日期，范围0-6，星期一从1开始。
%W		一年中的星期数(00-53)，一月第一个星期一开始为01.
%x		当地适当的日期表示。
%X		当地适当的时间表示。
%y		一世纪中的年份(00-99)。
%Y		完整的公元年份表示。
%Z		使用的时区名称
%%		相当于%号
```

```c
#include <stdio.h>
#include <time.h>

int main()
{
	time_t timep;
	char buf[30];
	struct tm *tm;
	char *format[] = {"%I:%M:%S %p %m/%d %a", "%x %X %Y"};

	time(&timep);
	tm = localtime(&timep);

	strftime(buf, sizeof(buf), format[0], tm);
	printf("%s -> %s\n", format[0], buf);

	strftime(buf, sizeof(buf), format[1], tm);
	printf("%s -> %s\n", format[1], buf);
	return 0;
}
```

### **difftime函数**

> **头文件：**`#include <time.h>`
>
> **函数定义：**`double difftime(time_t time1, time_t time0);`
>
> **函数说明：**用来计算参数time1和time0所代表的时间差距，结果以double型精确值返回。两个参数皆是以1970-01-01 00:00:00算起的UTC时间
>
> **返回值：**返回精确的时间差距秒数

```c
#include <stdio.h>
#include <time.h>
#include <unistd.h>

int main()
{
	time_t time0, time1;

	time(&time0);
	sleep(2);
	time(&time1);

	printf("difftime:%lf\n", difftime(time1, time0));
	return 0;
}
```

### **tzset函数**

> **头文件：**`#include <time.h>`
>
> **函数定义：**`void tzset (void);`
>
> **函数说明：**tzset()用来将环境变量TZ设给全局变量tzname、timezone和daylight，也就是从环境变量中获取当前地区的时区信息。时间转换函数会自动调用此函数。若环境变量TZ未设置，全局变量tzname会依照/etc/localtime找出最接近当前地区的时区。如果环境变量TZ的值为NULL，或是无法辨认，则使用UTC时区。
>
> **返回值：**此函数总是调用成功。

```c
#include <stdio.h>
#include <time.h>

extern char *tzname[2];	// 时区
extern long timezone;	// 和UTC相差的秒数
extern int daylight;	// 夏时令

int main()
{
	tzset();
	printf("tzname:%s %s\n", tzname[0], tzname[1]);
	printf("timezone:%ld\n", timezone);
	printf("daylight:%d\n", daylight);
	return 0;
}
```

### **gettimeofday函数**

> **头文件：**`#include <sys/time.h>`
>
> **函数定义：**`int gettimeofday(struct timeval *tv, struct timezone *tz);`
>
> **函数说明：** gettimeofday()会把目前的时间有tv所指的结构返回，当地时区的信息则放到tz所指的结构中。
>
> **返回值：**成功则返回0，失败返回－1。
>
> **补充：**错误代码存于errno，EFAULT表示指针tv和tz所指的内存空间超出存取权限。

```c
struct timeval
{
    long tv_sec;	//秒
    long tv_usec;	//微秒
};

struct timezone
{
	int tz_minuteswest; // 和格林威治时间差了多少分钟
	int tz_dsttime; 	// 日光节约时间的状态
};

// tz_dsttime所代表状态如下
DST_NONE	// 不使用
DST_USA		// 美国
DST_AUST	// 澳洲
DST_WET		// 西欧
DST_MET		// 中欧
DST_EET		// 东欧
DST_CAN		// 加拿大
DST_GB		// 大不列颠
DST_RUM		// 罗马尼亚
DST_TUR		// 土耳其
DST_AUSTALT	// 澳洲（1986年以后）
```

```c
#include <stdio.h>
#include <sys/time.h>

int main()
{
	struct timeval tv;
	struct timezone tz;

    // 这里tz时区信息测试时没获取出来，不知道什么原因
    // 如果对时区信息不感兴趣，可以传入NULL，如gettimeofday(&tv, NULL); 
	gettimeofday(&tv, &tz); 

	printf("tv_sec:%ld\n", tv.tv_sec);
	printf("tv_usec:%ld\n", tv.tv_usec);
	printf("tz_minuteswest:%d\n", tz.tz_minuteswest);
	printf("tz_dsttime:%d\n", tz.tz_dsttime);
	return 0;
}
```

### **settimeofday函数**

> **头文件：**`#include <sys/time.h>`
>
> **函数定义：**`int settimeofday(const struct timeval *tv, const struct timezone *tz);`
>
> **函数说明：** settimeofday()会把目前时间设成由tv所指的结构信息，当地时区信息则设成tz所指的结构。详细的说明请参考gettimeofday()。注意，只有root权限才能使用此函数修改时间。
>
> **返回值：**成功则返回0，失败返回－1。
>
> **补充：**错误代码存于errno，EFAULT：tv或tz其中某一项指向的空间不可访问；EINVAL：时区格式无效；EPERM：权限不足，调用进程不允许使用settimeofday设置当前时间和时区值。

```c
#include <stdio.h>
#include <sys/time.h>

int main()
{
	struct timeval tv;

	tv.tv_sec = 1234567890;
	tv.tv_usec = 0;
    
	settimeofday(&tv, NULL);
	perror("settimeofday");

	gettimeofday(&tv, NULL);
    
	printf("tv_sec:%ld\n", tv.tv_sec);
	printf("tv_usec:%ld\n", tv.tv_usec);
	return 0;
}
```

### **clock函数**

> **头文件：**`#include <time.h>`
>
> **函数定义：**`clock_t clock(void);`
>
> **函数说明：** 获取进程开始到调用clock()所占cpu的大约时间
>
> **返回值：**返回进程所占cpu的大约时间
>
> **补充：**在time.h文件中，还定义了一个常量CLOCKS_PER_SEC，它用来表示一秒钟会有多少个时钟计时单元。

```c
#include <stdio.h>
#include <time.h>

int main()
{
	int i, b;
	
	b = clock() / CLOCKS_PER_SEC;

	for (i = 0; i < 3; i++)
	{
		i = clock() / CLOCKS_PER_SEC;
		i = i - b;
	}
	return 0;
}
```
