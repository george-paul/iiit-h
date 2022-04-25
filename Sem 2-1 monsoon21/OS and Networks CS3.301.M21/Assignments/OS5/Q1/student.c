#include <stdio.h>
#include <stdlib.h>

#include "all.h"

// student routine - one per thread
void* studentR(void* input)
{
	int* k = (int*)input;
	struct stud s = stuA[*k];
	printf("starting thread for student %d with Cal %f.\n", s.sID, s.sCal);
	free(input);
}