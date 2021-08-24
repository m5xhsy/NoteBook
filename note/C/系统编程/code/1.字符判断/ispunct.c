#include <stdio.h>
#include <ctype.h>

int main()
{
	int i;
	char str[] = "1 s&*;sa\n";

	for(i=0;str[i]!=0;i++){
		printf("%c:%s\n",str[i],ispunct(str[i])?"true":"false");
	}
	return 0;
}
