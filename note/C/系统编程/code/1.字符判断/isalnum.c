#include <stdio.h>
#include <ctype.h>

int main()
{
	int i;
	char str[] = "<abc123>";

	for (int i = 0; str[i] != 0; i++)
	{
		printf("%c:%s\n", str[i], isalnum(str[i]) ? "true" : "false");
	}
	return 0;
}
