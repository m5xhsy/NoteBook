#include <stdio.h>
#include <ctype.h>

int main()
{
	int i;
	char str[] = "Ass";

	for (i = 0; str[i] != 0; i++)
	{
		printf("%c:%s\n", str[i], islower(str[i]) ? "true" : "false");
	}
	return 0;
}
