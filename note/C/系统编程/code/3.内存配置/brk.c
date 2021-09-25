#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>

/*
 * 定义未初始化的变量，将会存在于BBS中
 *  BSS是存放程序中未初始化的全局变量的一块静态内存分配区域 
 */
int bssvar;

int main()
{
	char *ptr;
	long heap_gap_bbs;

	ptr = (char *)malloc(32);
	if (ptr == NULL)
	{
		perror("malloc");
		exit(EXIT_FAILURE);
	}
	heap_gap_bbs = (long)ptr - (long)&bssvar - 4;
	printf("ptr1:%p\n", ptr);
	printf("heap_gap_bbs1:%lu\n", heap_gap_bbs);
	free(ptr);

	sbrk(32);

	ptr = (char *)malloc(32);
	if (ptr == NULL)
	{
		perror("malloc");
		exit(EXIT_FAILURE);
	}
	heap_gap_bbs = (long)ptr - (long)&bssvar - 4;
	printf("ptr2:%p\n", ptr);
	printf("heap_gap_bbs2:%lu\n", heap_gap_bbs);
	free(ptr);
	return 0;
}