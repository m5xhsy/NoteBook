#include <stdio.h>
#include <ctype.h>

int main()
{
	char s[] = "aBcdEfghIJkLMno;@#$";
	int i;

	printf("Before：%s\n", s);
	for (i = 0; i < sizeof(s); i++)
	{
		s[i] = toupper(s[i]);
	}
	printf("After：%s\n", s);
	return 0;
}