#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <fcntl.h>
#include <sys/wait.h>
#include <unistd.h>

#include "builtins.h"

//launch a process given by the tokenized inpt
void launchProcess(char** inpt)
{
	//check whether & is given for background
	int backG = 0;
	if(strcmp(inpt[getArgc(inpt)], "&")==0)
	{
		free(inpt[getArgc(inpt)]);
		inpt[getArgc(inpt)] = NULL;
		backG = 1;
	}

	//fork process
	int st;
	pid_t pID, wpID;
	pID = fork();
	//executes in child process
	if(pID==0)
	{
		execvp(inpt[0], inpt);
		perror("Unrecognised executable\n");
		_exit(1);
		return;
	}
	//fork error
	else if (pID<0)
	{
		perror("Could not fork process\n");
		return;
	}
	//in parent fork successful
	else
	{
		//not background
		if(!backG)
		{
			do
			{
				wpID = waitpid(pID, &st, WUNTRACED);
			}while(!WIFEXITED(st));
		}
		//background
		else
		{
			printf("%d\n", pID);
		}
		return;
	}
}

//prints various details about a given pid
void processInfo(char** inpt)
{
	char path[1000];
	char buf[1000];
	int fd;
	int length;

	//assign appropriate pid in case one was not supplied and print it
	pid_t pID;
	if(getArgc(inpt) < 1)
		pID = getpid();
	else if(getArgc(inpt) > 1)
		perror("Too many arguments");
	else
		pID = atoi(inpt[1]);
	printf("\npid -- %d", pID);

	//print process status by opening /proc/<pid>/stat
	sprintf(path, "/proc/%d/stat", pID);
	fd = open(path, O_RDONLY);
	length = read(fd, buf, 1000);
	buf[length] = '\0';
	char* saveptr = buf;
	char* token = strtok_r(buf, " ", &saveptr);
	//ignore first two tokens to get status
	token = strtok_r(NULL, " ", &saveptr);token = strtok_r(NULL, " ", &saveptr);
	printf("\nProcess Status -- %s", token);
	//check foreground
	//ignore first two tokens to get process group id
	token = strtok_r(NULL, " ", &saveptr);token = strtok_r(NULL, " ", &saveptr);
	char pgrp[50];
	strcpy(pgrp, token);
	//ignore three tokens to get foreground group id
	token = strtok_r(NULL, " ", &saveptr);token = strtok_r(NULL, " ", &saveptr);token = strtok_r(NULL, " ", &saveptr);
	if(strcmp(pgrp, token)==0)
		printf("+");

	//print virtual memory size
	for(int i = 0; i<15; i++)
		token = strtok_r(NULL, " ", &saveptr);
	printf("\nVirtual Memory -- %s", token);

	//print executable path by opening /proc/<pid>/exe
	sprintf(path, "/proc/%d/exe", pID);
	length = readlink(path, buf, 1000);
	buf[length] = '\0';
	printf("\nExecutable Path -- %s", buf);

	close(fd);
}