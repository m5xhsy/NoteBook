#include <stdio.h>
#include <ctype.h>

int main()
{
    int i;
    
	for(i=1;i<6;i++){
		printf("%d:%s\n",i*10,iscntrl(i*10)?"true":"false");
	}
	return 0;
}
