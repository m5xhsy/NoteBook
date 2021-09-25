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