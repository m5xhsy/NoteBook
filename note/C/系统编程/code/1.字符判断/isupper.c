#include <stdio.h>
#include <ctype.h>

int main()
{
	int i;
	char str[] = "A-b";

	for(i=0;str[i]!=0;i++){
		printf("%c:%s\n",str[i],isupper(str[i])?"true":"false");
	}
	return 0;
}

