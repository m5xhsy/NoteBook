#include <stdio.h>
#include <ctype.h>

int main()
{
	char str[] = "1	a 3>";
	int i;
	for (i = 0; i < 6; i++)
	{
		printf("%c:%s\n", str[i], isgraph(str[i]) ? "true" : "false");
	}
	return 0;
}
