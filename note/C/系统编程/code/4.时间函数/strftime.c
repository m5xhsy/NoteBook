#include <stdio.h>
#include <time.h>

int main()
{
	time_t timep;
	char buf[30];
	struct tm *tm;
	char *format[] = {"%I:%M:%S %p %m/%d %a", "%x %X %Y"};

	time(&timep);
	tm = localtime(&timep);

	strftime(buf, sizeof(buf), format[0], tm);
	printf("%s -> %s\n", format[0], buf);

	strftime(buf, sizeof(buf), format[1], tm);
	printf("%s -> %s\n", format[1], buf);
	return 0;
}