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
