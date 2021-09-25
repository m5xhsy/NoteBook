#include <stdio.h>
#include <time.h>
#include <unistd.h>

int main()
{
	time_t time0, time1;

	time(&time0);
	sleep(2);
	time(&time1);

	printf("difftime:%lf\n", difftime(time1, time0));
	return 0;
}