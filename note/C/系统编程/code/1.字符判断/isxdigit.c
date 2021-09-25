#include <stdio.h>
#include <ctype.h>

int main()
{
	int i;
	char str[] = "1F2a&po";

	for (i = 0; str[i] != 0; i++)
	{
		printf("%c:%s\n", str[i], isxdigit(str[i]) ? "true" : "false");
	}
	return 0;
}
