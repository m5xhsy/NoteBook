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
