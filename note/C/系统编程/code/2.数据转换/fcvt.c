#include <stdio.h>
#include <stdlib.h>

int main()
{
    int decpt,sign;
    char *aptr,*bptr;
    double a = 123.456;
    double b = -1.2345;

    aptr = fcvt(a,3,&decpt,&sign);
    printf("decpt=%d sign=%d value=%s\n",decpt,sign,aptr);

    bptr = fcvt(b,3,&decpt,&sign);
    printf("decpt=%d sign=%d value=%s\n",decpt,sign,aptr);

    return 0;
}
