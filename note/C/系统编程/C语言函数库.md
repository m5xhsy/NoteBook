# C语言函数

## 1.字符判断函数

### **1.1 isalnum函数**

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

	for(int i=0;str[i]!=0;i++){
		printf("%c:%s\n",str[i],isalnum(str[i])?"true":"false");	
	}
	return 0;
}
```

### **1.2 isalpha函数**

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
    
	for(i=0;str[i]!=0;i++){
		printf("%c:%s\n",str[i],isalpha(str[i])?"true":"false");	
	}
	return 0;
}
```

### **1.3 isascii函数**

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
    
	for(i=1;i<6;i++){
		printf("%d:%s\n",i*40,isascii(i*40)?"true":"false");
	}
	return 0;
}
```

### **1.4 isblank函数**

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
    
	for(i=0;str[i]!=0;i++){
		printf("%c:%s\n",str[i],isblank(str[i])?"true":"flase");
	}
	return 0;
}
```

### **1.5 iscntrl函数**

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
    
	for(i=1;i<6;i++){
		printf("%d:%s\n",i*10,iscntrl(i*10)?"true":"false");
	}
	return 0;
}
```

### **1.6 isdigit函数**

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
    
	for(i=0;str[i]!=0;i++){
		printf("%c:%s\n",str[i],isdigit(str[i])?"true":"false");
	}
	return 0;
}
```

### **1.7 isgraph函数**

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
    int i;
	char str[] = "1	a 3>";

	for(i=0;str[i]!=0;i++){
		printf("%c:%s\n",str[i],isgraph(str[i])?"true":"false");
	}
	return 0;
}
```

### **1.8 islower函数**

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
	
	for(i=0;str[i]!=0;i++){
		printf("%c:%s\n",str[i],islower(str[i])?"true":"false");
	}
	return 0;
}
```

### **1.9 isprint函数**

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

	for(i=0;str[i]!=0;i++){
		printf("%c:%s\n",str[i],isprint(str[i])?"true":"false");
	}
	return 0;
}
```

### **1.10 isspace函数**

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
	
	for(i=0;str[i]!=0;i++){
		printf("%c:%s\n",str[i],isspace(str[i])?"true":"false");
	}
	return 0;
}
```

### **1.11 ispunct函数**

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

	for(i=0;str[i]!=0;i++){
		printf("%c:%s\n",str[i],ispunct(str[i])?"true":"false");
	}
	return 0;
}
```

### **1.12 isupper函数**

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

	for(i=0;str[i]!=0;i++){
		printf("%c:%s\n",str[i],isupper(str[i])?"true":"false");
	}
	return 0;
}
```

### **1.13 isxdigit函数**

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

	for(i=0;str[i]!=0;i++){
		printf("%c:%s\n",str[i],isxdigit(str[i])?"true":"false");
	}
	return 0;
}
```

## 2.数据转换函数

### **2.1 atof函数**

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
	char *a = "  -12.5s";    // 遇到字符s停止转换
	char *b = "105e-2  ";

	printf("a=%.2f\n",atof(a));
	printf("b=%.2f\n",atof(b));
	return 0; 	
}
```

### **2.2 atoi函数**

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

	printf("a=%d\n",atoi(a));
	printf("b=%d\n",atoi(b));
	return 0;
}
```

### **2.3 atol函数**

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

	printf("a=%ld\n",atol(a));
	printf("b=%ld\n",atol(b));
	return 0;
}
```

### **2.4 ecvt函数**

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
	int decpt,sign;
	char *aptr,*bptr;
	double a = 123.456;
	double b = -1.2345;

	aptr = ecvt(a,6,&decpt,&sign);
	printf("decpt=%d sign=%d value=%s\n",decpt,sign,aptr);
	
	bptr = ecvt(b,5,&decpt,&sign);
	printf("decpt=%d sign=%d value=%s\n",decpt,sign,aptr);
	
	return 0;
}
```

### **2.5 fcvt函数**

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
    int decpt,sign;
    char *aptr,*bptr;
    double a = 123.456;
    double b = -1.2345;

    aptr = fcvt(a,3,&decpt,&sign);
    printf("decpt=%d sign=%d value=%s\n",decpt,sign,aptr);

    bptr = fcvt(b,3,&decpt,&sign);
    printf("decpt=%d sign=%d value=%s\n",decpt,sign,aptr);

    return 0;
}
```

### **2.6 gcvt函数**

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
	char aptr[25],bptr[25];   // 这里需要分配空间，不然会报错
	double a = 135.79;
	double b = -135.68;

	gcvt(a, 5, aptr);
	printf("a value=%s\n",aptr);
	
	gcvt(b, 4, bptr);
	printf("b value=%s\n",bptr);
	return 0;
}
```

### **2.7 strod函数**

xxx

### **2.8 strtol函数**

xxx

### **2.9 strtoul函数**

xxx

### **2.10 toascii函数**

xxx

### **2.11 tolower函数**

xxx

### **2.12 toupper函数**

xxx

