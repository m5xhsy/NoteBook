#include <stdio.h>
#include <time.h>

int main()
{
	time_t timep;
	struct tm *p;

	time(&timep);
	p = gmtime(&timep);

	printf("%d-%d-%d ", (1900 + p->tm_year), p->tm_mon, p->tm_mday);
	printf("%d:%d:%d\n", p->tm_hour, p->tm_min, p->tm_sec);
	return 0;
}