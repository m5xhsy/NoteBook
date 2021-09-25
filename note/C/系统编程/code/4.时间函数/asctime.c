#include <stdio.h>
#include <time.h>

int main()
{
	time_t timep;
	time(&timep);
	printf("now:%s\n", asctime(localtime(&timep)));
	return 0;
}