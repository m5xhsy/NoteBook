#include <stdio.h>
#include <time.h>

int main()
{
	time_t timep;
	time(&timep);
	printf("%ld\n", mktime(gmtime(&timep)));
	return 0;
}