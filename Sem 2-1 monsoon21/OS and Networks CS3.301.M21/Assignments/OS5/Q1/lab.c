#include <stdio.h>
#include <stdlib.h>

#include "all.h"

// lab routine - one per thread
void* labR(void* input)
{
	int* k = (int*)input;
	struct lab l = labA[*k];
	printf("starting thread for lab %d with Tas %d.\n", l.lID, l.lTasNo);
	free(input);
}