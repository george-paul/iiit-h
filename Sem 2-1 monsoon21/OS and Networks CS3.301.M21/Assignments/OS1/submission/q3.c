#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <unistd.h>
#include <errno.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

//prints using system calls
void prSys(char* toPrint)
{
	write(1, toPrint, strlen(toPrint));
}

int main(int argc, char* argv[])
{
	//check argument count >1
	if(argc<1)
	{
		perror("Not enough arguments.\n");
		exit(EXIT_FAILURE);
	}

	//get file name
	char filePath[100];
	strcpy(filePath, argv[1]);
	char* tok = strtok(filePath, "/");
	char fileName[100];
	while(tok != NULL)
	{
		strcpy(fileName, tok);
		tok = strtok(NULL, "/");
	}

	//assign file paths
	char f1path[120] = "./Assignment/1_";
	strcat(f1path, fileName);
	char f2path[120] = "./Assignment/2_";
	strcat(f2path, fileName);
	char dipath[120] = "./Assignment";
	//printf("\n f1: %s\n f2: %s\n d : %s\n", f1path, f2path, dipath);			//DBG

	//get stats
	struct stat f1;
	struct stat f2;
	struct stat di;

	//if directory doesn't exist
	if(stat(dipath, &di) == -1)
	{
		prSys("Directory is created: No\n");
		exit(EXIT_SUCCESS);
	}
	else
	{
		prSys("Directory is created: Yes\n");
	}

	//check file permissions
	char st[300];

	//output_file_1
	if(stat(f1path, &f1) == -1)
	{
		perror("Invalid file 1 path.\n");
	}
	else
	{
		sprintf(st, "\nUser has read permission on output_file_1: %s\n", (f1.st_mode & S_IRUSR)?"Yes":"No"); prSys(st);
		sprintf(st, "User has write permission on output_file_1: %s\n", (f1.st_mode & S_IWUSR)?"Yes":"No"); prSys(st);
		sprintf(st, "User has execute permission on output_file_1: %s\n\n", (f1.st_mode & S_IXUSR)?"Yes":"No"); prSys(st);

		sprintf(st, "Group has read permission on output_file_1: %s\n", (f1.st_mode & S_IRGRP)?"Yes":"No"); prSys(st);
		sprintf(st, "Group has write permission on output_file_1: %s\n", (f1.st_mode & S_IWGRP)?"Yes":"No"); prSys(st);
		sprintf(st, "Group has execute permission on output_file_1: %s\n\n", (f1.st_mode & S_IXGRP)?"Yes":"No"); prSys(st);

		sprintf(st, "Others has read permission on output_file_1: %s\n", (f1.st_mode & S_IROTH)?"Yes":"No"); prSys(st);
		sprintf(st, "Others has write permission on output_file_1: %s\n", (f1.st_mode & S_IWOTH)?"Yes":"No"); prSys(st);
		sprintf(st, "Others has execute permission on output_file_1: %s\n\n", (f1.st_mode & S_IXOTH)?"Yes":"No"); prSys(st);
	}

	//output_file_2
	if(stat(f2path, &f2) == -1)
	{
		perror("Invalid file 2 path.\n");
	}
	else
	{
		sprintf(st, "\nUser has read permission on output_file_2: %s\n", (f2.st_mode & S_IRUSR)?"Yes":"No"); prSys(st);
		sprintf(st, "User has write permission on output_file_2: %s\n", (f2.st_mode & S_IWUSR)?"Yes":"No"); prSys(st);
		sprintf(st, "User has execute permission on output_file_2: %s\n\n", (f2.st_mode & S_IXUSR)?"Yes":"No"); prSys(st);

		sprintf(st, "Group has read permission on output_file_2: %s\n", (f2.st_mode & S_IRGRP)?"Yes":"No"); prSys(st);
		sprintf(st, "Group has write permission on output_file_2: %s\n", (f2.st_mode & S_IWGRP)?"Yes":"No"); prSys(st);
		sprintf(st, "Group has execute permission on output_file_2: %s\n\n", (f2.st_mode & S_IXGRP)?"Yes":"No"); prSys(st);

		sprintf(st, "Others has read permission on output_file_2: %s\n", (f2.st_mode & S_IROTH)?"Yes":"No"); prSys(st);
		sprintf(st, "Others has write permission on output_file_2: %s\n", (f2.st_mode & S_IWOTH)?"Yes":"No"); prSys(st);
		sprintf(st, "Others has execute permission on output_file_2: %s\n\n", (f2.st_mode & S_IXOTH)?"Yes":"No"); prSys(st);
	}
	
	//directory
	sprintf(st, "\nUser has read permission on directory: %s\n", (di.st_mode & S_IRUSR)?"Yes":"No"); prSys(st);
	sprintf(st, "User has write permission on directory: %s\n", (di.st_mode & S_IWUSR)?"Yes":"No"); prSys(st);
	sprintf(st, "User has execute permission on directory: %s\n\n", (di.st_mode & S_IXUSR)?"Yes":"No"); prSys(st);

	sprintf(st, "Group has read permission on directory: %s\n", (di.st_mode & S_IRGRP)?"Yes":"No"); prSys(st);
	sprintf(st, "Group has write permission on directory: %s\n", (di.st_mode & S_IWGRP)?"Yes":"No"); prSys(st);
	sprintf(st, "Group has execute permission on directory: %s\n\n", (di.st_mode & S_IXGRP)?"Yes":"No"); prSys(st);

	sprintf(st, "Others has read permission on directory: %s\n", (di.st_mode & S_IROTH)?"Yes":"No"); prSys(st);
	sprintf(st, "Others has write permission on directory: %s\n", (di.st_mode & S_IWOTH)?"Yes":"No"); prSys(st);
	sprintf(st, "Others has execute permission on directory: %s\n\n", (di.st_mode & S_IXOTH)?"Yes":"No"); prSys(st);

	exit(EXIT_SUCCESS);
	return 0;
}