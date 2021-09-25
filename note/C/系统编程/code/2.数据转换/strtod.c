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