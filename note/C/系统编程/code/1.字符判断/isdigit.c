#include <stdio.h>
#include <ctype.h>

int main()
{
    int i;
	char str[] = "<1a2b>";
    
	for(i=0;str[i]!=0;i++){
		printf("%c:%s\n",str[i],isdigit(str[i])?"true":"false");
	}
	return 0;
}
