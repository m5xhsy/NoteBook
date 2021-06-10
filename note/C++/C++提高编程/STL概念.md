# STL概念

## **1.STL起源**

* 长久以来，软件界一直希望建立一种可重复利用的东西。

* C++的**面向对象**和**泛型编程**思想，目的就是**复用性的提升。**

* 大多情况下，数据结构和算法都未能有一套标准,导致被迫从事大量重复工作。

* 为了建立数据结构和算法的一套标准,诞生了**STL**。

## **2.STL基本概念**

* STL(Standard Template Library,**标准模板库**)。
* STL 从广义上分为: **容器(container) 算法(algorithm) 迭代器(iterator)。**
* **容器**和**算法**之间通过**迭代器**进行无缝连接。
* STL 几乎所有的代码都采用了模板类或者模板函数。

## **3.STL六大组件**

STL大体分为六大组件，分别是:**容器、算法、迭代器、仿函数、适配器（配接器）、空间配置器。**

1. 容器：各种数据结构，如vector、list、deque、set、map等,用来存放数据。
2. 算法：各种常用的算法，如sort、find、copy、for_each等。
3. 迭代器：扮演了容器与算法之间的胶合剂。
4. 仿函数：行为类似函数，可作为算法的某种策略。
5. 适配器：一种用来修饰容器或者仿函数或迭代器接口的东西。
6. 空间配置器：负责空间的配置与管理。

## **4.STL中容器、算法、迭代器**

### **4.1 容器**

STL容器就是将运用**最广泛的一些数据结构**实现出来。

常用的数据结构：**数组, 链表,树, 栈, 队列, 集合, 映射表等。**

这些容器分为**序列式容器**和**关联式容器**两种:

- **序列式容器：**强调值的排序，序列式容器中的每个元素均有固定的位置。
- **关联式容器：**二叉树结构，各元素之间没有严格的物理上的顺序关系。

### **4.2 算法**

**有限的步骤，解决逻辑或数学上的问题，这一门学科我们叫做算法(Algorithms)。**

**算法分为两种：**

- **质变算法：**是指运算过程中会更改区间内的元素的内容。例如拷贝，替换，删除等等。

- **非质变算法：**是指运算过程中不会更改区间内的元素内容，例如查找、计数、遍历、寻找极值等等。

### **4.3 迭代器**

**提供一种方法，使之能够依序寻访某个容器所含的各个元素，而又无需暴露该容器的内部表示方式。每个容器都有自己专属的迭代器，迭代器使用非常类似于指针，初学阶段我们可以先理解迭代器为指针。**

**迭代器种类：**

| 种类           | 功能                                                     | 支持运算                                |
| -------------- | -------------------------------------------------------- | --------------------------------------- |
| 输入迭代器     | 对数据的只读访问                                         | 只读，支持++、==、！=                   |
| 输出迭代器     | 对数据的只写访问                                         | 只写，支持++                            |
| 前向迭代器     | 读写操作，并能向前推进迭代器                             | 读写，支持++、==、！=                   |
| 双向迭代器     | 读写操作，并能向前和向后操作                             | 读写，支持++、--，                      |
| 随机访问迭代器 | 读写操作，可以以跳跃的方式访问任意数据，功能最强的迭代器 | 读写，支持++、--、[n]、-n、<、<=、>、>= |

!>常用的容器中迭代器种类为**双向迭代器**和**随机访问迭代器**。

## **5.容器、算法和迭代器初识**

**STL中最常用的容器为Vector，可以理解为数组，下面我们将学习如何向这个容器中插入数据、并遍历这个容器。**

### **5.1 vector存放内置数据类型**

**容器：** `vector`

**算法：**  `for_each`

**迭代器：**`vector<int>::iterator`

**示例：**

```c++
#include <iostream>
#include <vector>
#include <algorithm>  
using namespace std;

void print_info(int val) {
	cout << val << " ";
}

int main() {
	// 创建一个vector容器，相当于数组
	vector<int> vt;
	vt.push_back(11);
	vt.push_back(12);
	vt.push_back(13);

	// 方法一：while循环遍历
	// vt.begin()返回迭代器，这个迭代器指向容器中第一个数据
	vector<int>::iterator itBegin = vt.begin();  

	// vt.end()返回迭代器，这个迭代器指向容器元素的最后一个元素的下一个位置
	vector<int>::iterator itEnd = vt.end();

	while (itBegin != itEnd) {
		cout << *itBegin << " ";
		itBegin++;
	}
	cout << endl;

	// 方法二：for循序变例
	for (vector<int>::iterator it = vt.begin(); it != vt.end(); it++) {
		cout << *it << " ";
	}
	cout << endl;

	// 方法三：利用STL提供的遍历算法（for_each()须包含algorithm头文件）
	for_each(vt.begin(), vt.end(), print_info);
	cout << endl;

	return 0;
}
```

### **5.2 Vector存放自定义数据类型**

```c++
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

class Person {
public:
	Person(string name, int age) :name(name), age(age) {};
	string name;
	int age;
};

ostream& operator<<(ostream& cout,Person p) {
	cout << "{ name:" << p.name;
	cout << ", age:" << p.age << " }";
	return cout;
}

void print(Person p) {
	cout << p;
}

int main() {
	vector<Person> vt;

	Person a("张三", 18);
	Person b("李四", 19);
	Person c("王五", 20);
	Person d("赵六", 21);

	vt.push_back(a);
	vt.push_back(b);
	vt.push_back(c);
	vt.push_back(d);

	for (vector<Person>::iterator it = vt.begin(); it != vt.end(); it++) {
		cout << *it;
		// it->name;   指针获取
		// (*it).name; 解引用获取
	}
	cout << endl;

	for_each(vt.begin(), vt.end(), print);
	cout << endl;
	return 0;
}
```

### **5.3 Vector容器嵌套容器**

```c++
#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

void print_v(int val) {
	cout << val << "\t";
}

void print_vt(vector<int> val) {
	for_each(val.begin(), val.end(), print_v);
	cout << endl;
}

int main() {
	vector<vector<int>> vt;
	vector<int> v1;
	vector<int> v2;
	vector<int> v3;
	vector<int> v4;

	for (int i = 1; i <= 4; i++) {
		v1.push_back(i);
		v2.push_back(i * 2);
		v3.push_back(i * 3);
		v4.push_back(i * 4);
	}

	vt.push_back(v1);
	vt.push_back(v2);
	vt.push_back(v3);
	vt.push_back(v4);

	// 方法一
	for (vector<vector<int>>::iterator i = vt.begin(); i != vt.end(); i++) {
		for (vector<int>::iterator j = i->begin(); j != i->end(); j++) {
			cout << *j << "\t";
		}
		cout << endl;
	}

	// 方法二
	cout << endl;
	for_each(vt.begin(), vt.end(), print_vt);

	return 0;
}
```

