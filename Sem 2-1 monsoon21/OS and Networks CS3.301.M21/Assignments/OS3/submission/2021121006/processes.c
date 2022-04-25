#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <fcntl.h>
#include <sys/wait.h>
#include <unistd.h>

// #include "builtins.h"
#include "all.h"

struct proc
{
	int number;
	pid_t pid;
	char name[200];
	char status[20];
};

struct proc** procList = NULL;

//gives the executable name for a given PID
void pidToName(int pID, char* name)
{
	//check if pid is in procList
	for(int i = 0; procList[i] != NULL; i++)
		if(procList[i]->pid == pID)
		{
			strcpy(name, procList[i]->name);
			return;
		}

	//if pid not in procList get from /proc/pid/comm
	sprintf(name, "/proc/%d/comm", pID);
	int f;
	f = open(name, O_RDONLY);
	if(f != -1)
	{
		int charsRead = read(f, name, MAX_TOK_SIZE);
		if(charsRead>0)
		{
			name[charsRead-1]='\0';
		}
		else
		{
			strcpy(name, "unknown");
		}	
		close(f);
	}
	return;
}

void listProc(char** inpt)
{
	if(procList == NULL)
	{
		printf("Zero running/stopped processes\n");
		return;
	}
	for(int i = 0; procList[i] != NULL; i++)
	{
		printf("[%d] %s %s [%d]\n",
			procList[i]->number,
			procList[i]->status,
			procList[i]->name,
			procList[i]->pid);
	}
}

//change status of a proc to 0-running 1-stopped 3-foreground
void editProc(int pid, int status)
{
	if(procList != NULL)
	{
		//if pid exists in the procList update its status
		for(int i = 0; procList[i] != NULL; i++)
		{
			if(pid == procList[i]->pid)
			if(status == 0) strcpy(procList[i]->status, "Running");
			else if(status == 1) strcpy(procList[i]->status, "Stopped");
			else if(status == 2) strcpy(procList[i]->status, "Foreground");
		}
	}
}

//adds an item to the process list, if it exists toggle between running and stopped
void addProc(int pid, char** inpt)
{
	//concatenate strings in inpt to get commandString
	int foreG = 1;
	char* commandString = (char*)malloc(1000*sizeof(char));
	strcpy(commandString, "\0");
	for(int i = 0; inpt[i] != NULL; i++)
	{
		if(strcmp(inpt[i], "&") == 0) foreG = 0;
		strcat(commandString, inpt[i]);
		strcat(commandString, " ");
	}
	//get number of procs
	int noOfProcs;
	if(procList == NULL) 
		noOfProcs = 0;
	else
		for(noOfProcs = 0; procList[noOfProcs] != NULL; noOfProcs++);
	//define and initialize new proc
	struct proc* new = (struct proc*)malloc(sizeof(struct proc));
	new->number = noOfProcs+1;
	strcpy(new->name, commandString);
	new->pid = pid;
	if(foreG) strcpy(new->status, "Foreground");
	else strcpy(new->status, "Running");

	//if procList is empty, allocate memory
	if(procList == NULL)
		procList = (struct proc**)calloc(MAX_JOBS, sizeof(struct proc*));
	//find position in procList in alphabetical order
	int pos = -1;
	int i;
	for(i = 0; procList[i] != NULL; i++)
	{
		if(strcmp(new->name, procList[i]->name) > 0)
		{
			continue;
		}
		else if(strcmp(new->name, procList[i]->name) == 0)
		{
			if(new->number<procList[i]->number)
			{
				pos = i;
				break;
			}
			else
				continue;
		}
		else if(strcmp(new->name, procList[i]->name) < 0)
		{
			pos = i;
			break;
		}
	}
	//insert at end
	if(pos == -1)
		pos = i;

	//shift elements and insert
	for(int j = noOfProcs; j > pos; j--)
		procList[j] = procList[j-1];
	procList[pos] = new;

	free(commandString);
}

//Clears procList and frees memory
void clearProc()
{
	if(procList == NULL)
		return;
	for(int i = 0; procList[i] != NULL; i++)
		free(procList[i]);
	free(procList); procList = NULL;
}

//removes pid from the procList
void removeProc(int pid)
{
	//empty list
	if(procList == NULL)
		return;
		
	int i;
	for(i = 0; procList[i] != NULL; i++)
	{
		if(procList[i]->pid == pid)
		{
			//shift all elements after i up
			int j = i+1;
			for(; procList[j] != NULL; j++) *procList[j-1] = *procList[j];
			free(procList[j-1]); procList[j-1] = NULL;
			break;
		}
	}
	//if empty now then clear
	if(procList[0] == NULL)
		clearProc();
}

//send signal to a child
void sendSignal(char ** inpt)
{
	if(getArgc(inpt) != 2)
	{
		fprintf(stderr, "Invalid number of arguments. \n");
		return;
	}

	int jobNo = atoi(inpt[1]);
	int sigNo = atoi(inpt[2]);
	int pidToSend = -1;
	
	//get pid corresponding to jobNo
	for(int i = 0; procList[i] != NULL; i++)
		if(procList[i]->number == jobNo)
			pidToSend = procList[i]->pid;
	if(pidToSend == -1)
	{
		fprintf(stderr, "Could not find given job.\n");
		return;
	}
	
	kill(pidToSend, sigNo);
}

//returns pid of foreground proc
int getForeProc()
{
	if(procList == NULL)
		return -1;
	int forePid = -1;
	for(int i = 0; procList[i] != NULL; i++)
		if(strcmp(procList[i]->status, "Foreground") == 0) forePid = procList[i]->pid;
	
	return forePid;
}

void makeFG(char** inpt)
{
	if(getArgc(inpt) != 1)
	{
		fprintf(stderr, "Invalid number of arguments.\n");
		return;
	}
	if(procList == NULL)
	{
		fprintf(stderr, "No background processes.\n");
		return;
	}
	
	//get pid for job number
	int jobNo = atoi(inpt[1]);
	pid_t pid = -1;
	for(int i = 0; procList[i] != NULL; i++)
		if(procList[i]->number == jobNo)
			pid = procList[i]->pid;

	//make process foreground
	
	tcsetpgrp(STDIN_FILENO, pid);
	//send SIGCONT
	kill(-pid, SIGCONT);
	sleep(1);
	editProc(pid, 2);
	// sigset_t sigs;
	// int sig;
	// sigfillset(&sigs);
	// sigdelset(&sigs, SIGTTOU);
	// sigwait(&sigs, &sig);

	// pause();
	int status;
	waitpid(pid, &status, WUNTRACED|WSTOPPED);
	signal(SIGTTOU, SIG_IGN);
    tcsetpgrp(0, getpid());
    signal(SIGTTOU, SIG_DFL);
	return;
}

void makeBG(char** inpt)
{
	if(getArgc(inpt) != 1)
	{
		fprintf(stderr, "Invalid number of arguments.\n");
		return;
	}
	if(procList == NULL)
	{
		fprintf(stderr, "No background processes.\n");
		return;
	}
	
	//get pid for job number
	int jobNo = atoi(inpt[1]);
	pid_t pid = -1;
	for(int i = 0; procList[i] != NULL; i++)
		if(procList[i]->number == jobNo)
			pid = procList[i]->pid;
	
	//send SIGCONT
	kill(-pid, SIGCONT);
	sleep(1);

	signal(SIGTTOU, SIG_IGN);
	tcsetpgrp(0, getpid());
	signal(SIGTTOU, SIG_DFL);

	return;
}

//launch a process given by the tokenized inpt
void launchProcess(char** inpt)
{

	//fork process
	int st;
	pid_t pID, wpID;
	pID = fork();
	//add proc to list
	addProc(pID, inpt);
	//check whether & is given for background
	int backG = 0;
	if(strcmp(inpt[getArgc(inpt)], "&")==0)
	{
		backG = 1;
		//remove '&'
		free(inpt[getArgc(inpt)]);
		inpt[getArgc(inpt)] = NULL;
	}
	//fork error
	if (pID<0)
	{
		removeProc(pID);
		perror("Could not fork process\n");
		return;
	}
	//executes in child process
	else if(pID==0)
	{

		setpgid(pID, pID);
		signal(SIGQUIT, SIG_DFL);
		signal(SIGINT, SIG_DFL);
		signal(SIGCHLD, SIG_DFL);
		signal(SIGTSTP, SIG_DFL);
		signal(SIGTTIN, SIG_DFL);
		signal(SIGTTOU, SIG_DFL);
		//background
		if(backG == 1)
		{
			// //remove '&'
			// free(inpt[getArgc(inpt)]);
			// inpt[getArgc(inpt)] = NULL;
		}
		//foreground
		else
		{
		}
		execvp(inpt[0], inpt);
		perror("Unrecognised executable\n");
		_exit(1);
		return;
	}
	//in parent fork successful
	else
	{
		setpgid(pID, pID);
		//foreground
		if(!backG)
		{
			tcsetpgrp(STDIN_FILENO, pID);
			// pause();
			int status;
			waitpid(pID, &status, WUNTRACED|WSTOPPED);
			signal(SIGTTOU, SIG_IGN);
			tcsetpgrp(0, getpid());
			signal(SIGTTOU, SIG_DFL);
            //signal(SIGTTOU, SIG_DFL);
			//wpID = waitpid(pID, &st, WUNTRACED);
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

	//assign shell pid in case one was not supplied and print it
	pid_t pID;
	if(getArgc(inpt) < 1)
		pID = getpid();
	else if(getArgc(inpt) > 1)
	{
		fprintf(stderr, "Too many arguments");
		return;
	}
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