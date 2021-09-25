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
