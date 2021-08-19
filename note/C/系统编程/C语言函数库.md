# C语言函数

## 1.字符判断函数

### **1.1 isalnum函数**

> **头文件：**`#include <ctype.h>`
> **函数定义：**`int isalnum(int c);`
> **函数说明：**检测函数是否为英文字母或阿拉伯数字，在标准C中相当于`(isalpha(c)||isdigit(c))`判断。
> **返回值：**参数c为数字或字母则返回TRUE，否则返回NULL(0)。
> **补充：**该函数为宏定义，并非真正函数。

```c
#include <stdio.h>
#include <ctype.h>

int main()
{
	char str[] = "<abc123>";

	for(int i=0;str[i]!='\0';i++){
		printf("%c:%d\n",str[i],isalnum(str[i])?"true":"false");	
	}
	return 0;
}
```

### **1.2 isalpha函数**

> **头文件：**`#include <ctype.h>`
>
> **函数定义：**`int isalpha(int c);`
>
> **函数说明：**检测函数是否为英文字母，在标准C中相当于`(isupper(c)||islower(c))`判断。
>
> **返回值：**参数c为英文字母则返回TRUE，否则返回NULL(0)。
>
> **补充：**该函数为宏定义，并非真正函数。

```c
#include <stdio.h>
#include <ctype.h>

int main()
{
	char str[] = "<abc123>";
	
	for(int i=0;str[i]!='\0';i++){
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
>**函数说明：**检测参数c是否为ASCII码字符，也就是判断字符是否在0到127之间。
>
>**返回值：**参数c为ASCII码字符则返回TRUE，否则返回NULL(0)。
>
>**补充：**该函数为宏定义，并非真正函数。

```c
#include <stdio.h>
#include <ctype.h>

int main()
{
	for(int i=1;i<6;i++){
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
> **函数说明：**检测参数c是否为空格字符，也就是判断是否为空格(space ASCII:32)或者定位字符(tab ASCII::9)
>
> **返回值：**参数c为空格字符则返回TRUE，否则返回NULL(0)。
>
> **补充：**该函数为宏定义，并非真正函数。

```c
#include <stdio.h>
#include <ctype.h>

int main()
{
	char str[6] = "a 1	?";
	for(int i=0;i<5;i++){
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
> **函数说明：**检测参数c是否为ASCII控制码，也就是判断是否在0到31之间。
>
> **返回值：**参数c为ASCII控制码则返回TRUE，否则返回NULL(0)。
>
> **补充：**该函数为宏定义，并非真正函数。

```c
#include <stdio.h>
#include <ctype.h>

int main()
{
	for(int i=1;i<6;i++){
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
> **函数说明：**检测参数c是否为阿拉伯数字0到9。
>
> **返回值：**参数c为阿拉伯数字则返回TRUE，否则返回NULL(0)。
>
> **补充：**该函数为宏定义，并非真正函数。

```c
#include <stdio.h>
#include <ctype.h>

int main()
{
	char str[6] = "<1a2b>";

	for(int i=0;i<6;i++){
		printf("%c:%s\n",str[i],isdigit(str[i])?"true":"false");
	}
	return 0;
}
```

### **1.7 isgraph函数**

xxx

### **1.8 islower函数**

xxx

### **1.9 isprint函数**

xxx

### **1.10 isspace函数**

xxx

### **1.11 ispunct函数**

xxx

### **1.12 isupper函数**

xxx

### **1.13 isxdigit函数**

xxx

## 2.数据转换函数

### **2.1 atof函数**

xxx

### **2.2 atoi函数**

xxx

### **2.3 atol函数****

xxx

### **2.4 ecvt函数**

xxx

### **2.5 fcvt函数**

xxx

### **2.6 gcvt函数**

xxx

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

