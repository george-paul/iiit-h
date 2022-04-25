#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <signal.h>
#include <sys/wait.h>
#include <unistd.h>
#include <fcntl.h>

#include "inputandprompt.h"
#include "builtins.h"
#include "processes.h"

#define MAX_HIST 20

char homeDir[MAX_TOK_SIZE];
char hist[MAX_HIST][MAX_TOK_SIZE] = {""};
int histBott = -1;

//save history to file
void saveHist()
{
	FILE* fd;
	char path[MAX_TOK_SIZE];
	sprintf(path, "/home/%s/DonatelloHist.txt", getUsername());
	fd = fopen(path, "w");
	if(!fd)
	{
		perror("failed to save history to file.");
		return;
	}
	for(int i = 0; i<=histBott; i++)
	{
		fputs(hist[i], fd);
	}
	fclose(fd);
}

//loads history from file
void loadHistory()
{
	FILE* fd;
	char path[MAX_TOK_SIZE];
	sprintf(path, "/home/%s/DonatelloHist.txt", getUsername());
	fd = fopen(path, "r");
	if(!fd)
	{
		return;
	}
	for(int i = 0; 1; i++)
	{
		if(fgets(path, MAX_TOK_SIZE, fd) != NULL)
		{
			strcpy(hist[i], path);
			histBott++;
		}
		else
			break;
	}
	fclose(fd);
}

//pushes a commsList to hist
int pushToHist(char** commsList)
{
	char in[MAX_TOK_SIZE] = "";
	//if only one command then no ;
	if(commsList[1] == NULL)
	{
		strcat(in, commsList[0]);
	}
	//else concatenate ; as well
	else
	{
		for(int i = 0; commsList[i] != NULL; i++)
		{
			strcat(in, commsList[i]);
			if(commsList[i+1] != NULL)
				strcat(in, "; ");
		}
	}
	//if at max capacity, push all hist up once
	if(histBott>=MAX_HIST-1)
	{
		for(int i = 0; i<histBott; i++)
			strcpy(hist[i], hist[i+1]);
	}
	else
	{
		histBott++;
	}
	strcpy(hist[histBott], in);
}

//prints the latest n commands
void printHist(int n)
{
	//due to 0 indexing
	n--;
	//if user is asking for more history than is saved
	if(n > histBott)
	{
		n = histBott;
	}
	for(int i = histBott - n; i<=histBott; i++)
	{
		printf("> %s", hist[i]);
	}
}

//gives the executable name for a given PID
void pidToName(int pID, char* name)
{
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

//handles the sigchild signal when a child process terminates
void sigchldHandler(int signo, siginfo_t *info, void *context)
{
	pid_t pID = info->si_pid;
	int st;
	char name[MAX_TOK_SIZE];
	pidToName(pID, name);
	while ((pID = waitpid(-1, &st, WNOHANG)) != -1)
	{
		fprintf(stderr, "\n%s with pid %d exited", name, pID);
		if(WIFEXITED(st))
			fprintf(stderr, " normally.\n");
		else
			fprintf(stderr, " abnormally.\n");
		PrintPrompt(homeDir);
	}
	return;
}

//executes a given command string accounting for random whitespace
int ExecCommand(char* command)
{
	int toExit = 0;
	char** inpt = parseCommand(command);
	//checks the first word in "inpt" for matching commands and executes
	if(strcmp(inpt[0], "cd") == 0)
		changeDir(inpt, homeDir);
	else if(strcmp(inpt[0], "pwd") == 0)
		printWD();
	else if(strcmp(inpt[0], "echo") == 0)
		echoecho(inpt);
	else if(strcmp(inpt[0], "ls") == 0)
		listDriver(inpt);
	else if(strcmp(inpt[0], "pinfo") == 0)
		processInfo(inpt);
	else if(strcmp(inpt[0], "exit") == 0)
		toExit = 1;
	else if(strcmp(inpt[0], "history") == 0)
	{
		if(inpt[1]==NULL)
		{
			if(histBott <= MAX_HIST/2 - 1)
				printHist(histBott+1);
			else
				printHist(MAX_HIST/2);
		}
		else
			printHist(atoi(inpt[1]));
	}
	else if(strcmp(inpt[0], "repeat") == 0)
	{
		if(getArgc(inpt) < 2)
		{
			perror("Not enough arguments");
		}
		else
		{
			char commToRepeat[MAX_TOK_SIZE] = "";
			for(int i = 2; inpt[i] != NULL; i++)
			{
				strcat(commToRepeat, inpt[i]);
				strcat(commToRepeat, " ");
			}
			for(int i = 0; i < atoi(inpt[1]); i++)
			{
				char temp[MAX_TOK_SIZE];
				strcpy(temp, commToRepeat);
				ExecCommand(temp);
			}
		}
	}
	else
		launchProcess(inpt);
	//free memory allocated to inpt
	for(int i = 0; i<MAX_ARGS; i++) 
	{
		if(inpt[i] != NULL)
			free(inpt[i]);
	}
	free(inpt);

	return toExit;
}

int main()
{
	printf("\033[0;32m~~~ \033[0;35mDonatello\033[0;32m ~~~\033[0m");
	loadHistory();
	//define SIGCHILD signal handler for background process exits
	struct sigaction act = {0};
	act.sa_flags = SA_SIGINFO;
	act.sa_sigaction = sigchldHandler;
	sigaction(SIGCHLD, &act, NULL);
	//copy current directory as home directory
	getcwd(homeDir, sizeof(homeDir));
	char** commsList;
	int toExit = 0;
	do
	{
		PrintPrompt(homeDir);
		commsList = TakeInput();
		pushToHist(commsList);
		for(int i = 0; commsList[i] != NULL && toExit == 0; i++)
		{
			toExit = ExecCommand(commsList[i]);
		}
		//free memory allocated to commsList
		for(int i = 0; i<MAX_ARGS; i++) 
		{
			if(commsList[i] != NULL)
				free(commsList[i]);
		}
		free(commsList);
	}while(toExit == 0);

	commsList = NULL;
	saveHist();
	printf("\n");
	return 0;
}