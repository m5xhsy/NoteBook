#include <stdio.h>
#include <time.h>

int main()
{

	int i, b;
	
	b = clock() / CLOCKS_PER_SEC;

	for (i = 0; i < 3; i++)
	{
		i = clock() / CLOCKS_PER_SEC;
		i = i - b;
	}
	return 0;
}
