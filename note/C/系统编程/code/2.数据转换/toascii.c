#include <stdio.h>
#include <ctype.h>

int main()
{
	int ret, c = 217;

	printf("%d %c\n", c, c);
	ret = toascii(c);
	printf("%d %c\n", ret, ret);
	return 0;
}