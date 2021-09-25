#include <stdio.h>
#include <ctype.h>

int main()
{
	int i;
	char str[] = "a 1\t>\n";

	for (i = 0; str[i] != 0; i++)
	{
		printf("%c:%s\n", str[i], isspace(str[i]) ? "true" : "false");
	}
	return 0;
}
