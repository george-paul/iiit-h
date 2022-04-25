#ifndef INPUTANDPROMPT
#define INPUTANDPROMPT

#define MAX_TOK_SIZE 1000 			//maximum size for directories, names and input
#define MAX_ARGS 50					//maximum number of arguments

void PrintPrompt(char*);
char** parseCommand(char*);
char** TakeInput();
char* getUsername();

#endif