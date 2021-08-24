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
