#include <stdio.h>
#include <sys/time.h>

int main()
{
	struct timeval tv;

	tv.tv_sec = 1234567890;
	tv.tv_usec = 0;
	settimeofday(&tv, NULL);
	perror("settimeofday");

	gettimeofday(&tv, NULL);
	printf("tv_sec:%ld\n", tv.tv_sec);
	printf("tv_usec:%ld\n", tv.tv_usec);
	return 0;
}
