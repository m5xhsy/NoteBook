#include <stdio.h>
#include <sys/timeb.h>

int main()
{
	struct timeb tp;
	ftime(&tp);
	printf("%ld,%d,%d,%d\n", tp.time, tp.millitm, tp.timezone, tp.timezone);
	return 0;
}