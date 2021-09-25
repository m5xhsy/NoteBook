#include <stdio.h>
#include <time.h>

int main()
{
	int seconds = time((time_t *)NULL);
	printf("now:%d\n", seconds);
	return 0;
}