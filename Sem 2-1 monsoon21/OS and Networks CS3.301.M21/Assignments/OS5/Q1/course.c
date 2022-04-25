#include <stdio.h>
#include <stdlib.h>

#include "all.h"

// course routine - one per thread
void* courseR(void* input)
{
	int* k = (int*)input;
	struct course c = couA[*k];
	printf("starting thread for course %d with name %s.\n", c.cID, c.cName);
	free(input);
}