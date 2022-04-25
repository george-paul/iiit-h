#ifndef _ALL_H
#define _ALL_H

#define MAX_SIZE 50

struct course
{
	int cID;
	char cName[MAX_SIZE];
	float cInterest;
	int cSlots;
	int cLabsNo;
	int cLabs[MAX_SIZE];
};

struct stud
{
	int sID;
	float sCal;
	int sP1;
	int sP2;
	int sP3;
	int sTime;
};

struct lab
{
	int lID;
	char lName[MAX_SIZE];
	int lTasNo;
	int lMaxTaShips;
};

extern struct course couA[MAX_SIZE];
extern struct stud stuA[MAX_SIZE];
extern struct lab labA[MAX_SIZE];

void* courseR(void*);
void* studentR(void*);
void* labR(void*);

#endif