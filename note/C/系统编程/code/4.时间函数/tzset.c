#include <stdio.h>
#include <time.h>

extern char *tzname[2];
extern long timezone;
extern int daylight;
int main()
{
	tzset();
	printf("tzname:%s %s\n", tzname[0], tzname[1]);
	printf("timezone:%ld\n", timezone);
	printf("daylight:%d\n", daylight);


	time_t timep;
	time(&timep);
	printf("%ld\n",timep);
	printf("%ld\n",mktime(gmtime(&timep)));
	return 0;
}