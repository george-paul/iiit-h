#include <stdio.h>
#include "all.h"

int myGlobal = 0;

int main()
{
	printf("Enter initial myGlobal: ");
	scanf("%d", &myGlobal);
	printf("myGlobal in main: %d\n", myGlobal);
	doublemyGlobal();
	printf("myGlobal after the other file: %d\n", myGlobal);
	return 0;
}