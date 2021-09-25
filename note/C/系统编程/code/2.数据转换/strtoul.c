#include <stdio.h>
#include <stdlib.h>

int main()
{
	unsigned long int ret_d, ret_b, ret_h;
	char *endptr_d, *endptr_b, *endptr_h;

	char *nptr_d = " 1911456461aa";
	char *nptr_b = " 10010110105sa";
	char *nptr_h = "1af226adfcgrgrr";

	ret_d = strtoul(nptr_d, &endptr_d, 10);
	ret_b = strtoul(nptr_b, &endptr_b, 2);
	ret_h = strtoul(nptr_h, &endptr_h, 16);

	printf("d nptr:%s\tenptr:%s\tret:%ld\n", nptr_d, endptr_d, ret_d);
	printf("b nptr:%s\tenptr:%s\tret:%ld\n", nptr_b, endptr_b, ret_b);
	printf("h nptr:%s\tenptr:%s\tret:%ld\n", nptr_h, endptr_h, ret_h);
	return 0;
}