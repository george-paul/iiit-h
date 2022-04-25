#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
#include <string.h>
#include <unistd.h>
#include <sys/types.h>
#include <pwd.h>
#include <errno.h>

#include "all.h"

//get the username of the calling user
char* getUsername()
{
	int u = getuid();
	struct passwd* p = getpwuid(u);
	return (p->pw_name);
}

//prints the prompt for input with username, hostname and working dir
void PrintPrompt(char* homeDir)
{
	//get current working directory
	char cwd[MAX_TOK_SIZE];
	getcwd(cwd, MAX_TOK_SIZE);
	//get user name
	char usrName[MAX_TOK_SIZE];
	strcpy(usrName, getUsername());
	//get hostname
	char hName[MAX_TOK_SIZE];
	gethostname(hName,MAX_TOK_SIZE);
	//substitute home directory with '~'
	char* wdWithHome;
	wdWithHome = strstr(cwd, homeDir);
	if(wdWithHome != NULL)
	{
		wdWithHome += strlen(homeDir)-1;
		wdWithHome[0] = '~';
		printf("\n\033[0;32m[\033[0;35m%s@%s\033[0;32m]\033[0;35m:\033[0;32m[\033[0;35m%s\033[0;32m]\033[0;35m>>\033[0m", usrName, hName, wdWithHome);
	}
	//not in home directory
	else
	{
		printf("\n\033[0;32m[\033[0;35m%s@%s\033[0;32m]\033[0;35m:\033[0;32m[\033[0;35m%s\033[0;32m]\033[0;35m>>\033[0m", usrName, hName, cwd);
	}
}

//parse space separated tokens
char** parseCommand(char* command)
{
	char** inpt = (char**)calloc(MAX_ARGS, sizeof(char*));
	char* token;
	char* saveptr = command;
	token = strtok_r(command, " \t\r\n", &saveptr);
	int i = 0;
	while(token != NULL)
	{
		inpt[i] = (char*)malloc(MAX_TOK_SIZE*sizeof(char));
		strcpy(inpt[i++], token);
		token = strtok_r(NULL, " \t\r\n", &saveptr);
	}
	//if the string is empty or only contains whitespace
	if(inpt[0]==NULL)
	{
		inpt[0] = (char*)malloc(MAX_TOK_SIZE*sizeof(char));
		strcpy(inpt[0],"");
	}
	return inpt;
}

//reads input from stdin and tokenises with ;
char** TakeInput()
{
	fflush(stdin);
	char in[MAX_TOK_SIZE];
	//read input
	//fgets must take input since often if a signal is handled input is skipped so this loop exists:
	char* l=0;
	do
	{
		l = fgets(in, MAX_TOK_SIZE, stdin);
		if(errno == 0 && l == NULL)
		{
			fprintf(stderr, "\nReceived Ctrl+D. Exiting...\n");
			_exit(1);
		}
	}while(l==NULL);

	//tokenise with ; delimiter
	char** commsList = (char**)calloc(MAX_ARGS, sizeof(char*));
	char* token;
	char* saveptr = in;
	token = strtok_r(in, ";", &saveptr);
	int i = 0;
	//if input is '\n'
	if(strcmp(in, "\n") == 0)
	{
		commsList[0] = (char*)malloc(MAX_TOK_SIZE*sizeof(char));
		strcpy(commsList[0], "");
		return commsList;
	}
	while(token != NULL)
	{
		commsList[i] = (char*)malloc(MAX_TOK_SIZE*sizeof(char));
		strcpy(commsList[i++], token);
		token = strtok_r(NULL, ";", &saveptr);
	}

	//if no memory was assigned
	if(commsList[0]==NULL)
	{
		commsList[0] = (char*)malloc(MAX_TOK_SIZE*sizeof(char));
		strcpy(commsList[0],"");
	}
	return commsList;
}