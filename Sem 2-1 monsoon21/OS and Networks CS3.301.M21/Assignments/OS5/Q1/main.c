#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <pthread.h>

#include "all.h"
// global arrays
struct course couA[MAX_SIZE] = {};
struct stud stuA[MAX_SIZE] = {};
struct lab labA[MAX_SIZE] = {};

int main()
{
	freopen("/home/george/stuff/OS5/input.txt", "r", stdin);	// DEBUG - take input from a file
	// input sizes
	int studentsNo, labsNo, coursesNo;
	scanf("%d %d %d", &studentsNo, &labsNo, &coursesNo);

	// input courses
	for(int i = 0; i<coursesNo; i++)
	{
		struct course newCourse;
		newCourse.cID = i;
		scanf("%s", newCourse.cName);
		scanf("%f", &newCourse.cInterest);
		scanf("%d", &newCourse.cSlots);
		scanf("%d", &newCourse.cLabsNo);
		for(int j = 0; j<newCourse.cLabsNo; j++)
		{
			scanf("%d", &newCourse.cLabs[j]);
		}
		couA[i] = newCourse;
	}

	// input students
	for(int i = 0; i<studentsNo; i++)
	{
		struct stud newStud;
		newStud.sID = i;
		scanf("%f", &newStud.sCal);
		scanf("%d", &newStud.sP1);
		scanf("%d", &newStud.sP2);
		scanf("%d", &newStud.sP3);
		scanf("%d", &newStud.sTime);
		stuA[i] = newStud;
	}

	// input labs
	for(int i = 0; i<labsNo; i++)
	{
		struct lab newLab;
		newLab.lID = i;
		scanf("%s", newLab.lName);
		scanf("%d", &newLab.lTasNo);
		scanf("%d", &newLab.lMaxTaShips);
		labA[i] = newLab;
	}

	// DEBUG - print all courses, students and labs
	// for(int i = 0; i<coursesNo; i++)
	// {
	// 	struct course newCourse = couA[i];
	// 	printf("cID: %d\n", newCourse.cID);
	// 	printf("cName: %s,\t", newCourse.cName);
	// 	printf("cInterest: %f,\t", newCourse.cInterest);
	// 	printf("cSlots: %d,\t", newCourse.cSlots);
	// 	printf("cLabsNo: %d,\ncLabs: ", newCourse.cLabsNo);
	// 	for(int j = 0; j<newCourse.cLabsNo; j++)
	// 	{
	// 		printf("%d, ", newCourse.cLabs[j]);
	// 	}
	// 	printf("\n---\n");
	// }
	// printf("\n----------\n----------\n");
	// for(int i = 0; i<studentsNo; i++)
	// {
	// 	struct stud newStud = stuA[i];
	// 	printf("sID: %d, ",newStud.sID);
	// 	printf("sCal: %f, ", newStud.sCal);
	// 	printf("sP1: %d, ", newStud.sP1);
	// 	printf("sP2: %d,", newStud.sP2);
	// 	printf("sP3: %d,", newStud.sP3);
	// 	printf("sTime: %d\n", newStud.sTime);
	// }
	// printf("\n----------\n----------\n");
	// for(int i = 0; i<labsNo; i++)
	// {
	// 	struct lab newLab = labA[i];
	// 	printf("lID: %d, ", newLab.lID);
	// 	printf("lName: %s, ", newLab.lName);
	// 	printf("lTasNo: %d, ", newLab.lTasNo);
	// 	printf("lMaxTaShips: %d\n", newLab.lMaxTaShips);
	// }
	// printf("\n----------\n----------\n");

	// -------create threads
	pthread_t ct[MAX_SIZE];			//courses
	for(int i = 0; i<coursesNo; i++)
	{
		int* arg = malloc(sizeof(int));	*arg = i;
		if(pthread_create(&ct[i], NULL, courseR, arg) != 0) perror("Couldn't create course thread.");
		// arg freed in courseR
	}
	pthread_t st[MAX_SIZE];			// students
	for(int i = 0; i<studentsNo; i++)
	{
		int* arg = malloc(sizeof(int));	*arg = i;
		if(pthread_create(&st[i], NULL, studentR, arg) != 0) perror("Couldn't create student thread.");
		// arg freed in studentR
	}
	pthread_t lt[MAX_SIZE];			// labs
	for(int i = 0; i<labsNo; i++)
	{
		int* arg = malloc(sizeof(int));	*arg = i;
		if(pthread_create(&lt[i], NULL, labR, arg) != 0) perror("Couldn't create lab thread.");
		// arg freed in labR
	}


	// -------join threads
	for(int i = 0; i<coursesNo; i++)
	{
		if(pthread_join(ct[i], NULL) != 0) perror("Couldn't join course thread.");
		else printf("course ID %d thread joined\n", i);
	}
	for(int i = 0; i<studentsNo; i++)
	{
		if(pthread_join(st[i], NULL) != 0) perror("Couldn't join student thread.");
		else printf("student ID %d thread joined\n", i);
	}
	for(int i = 0; i<labsNo; i++)
	{
		if(pthread_join(lt[i], NULL) != 0) perror("Couldn't join lab thread.");
		else printf("lab ID %d thread joined\n", i);
	}
}