#include <stdio.h>
#include <ctype.h>

int main()
{
	int i;
	char str[] = "1\ta 3>\n";

	for (i = 0; str[i] != 0; i++)
	{
		printf("%c:%s\n", str[i], isprint(str[i]) ? "true" : "false");
	}
	return 0;
}
