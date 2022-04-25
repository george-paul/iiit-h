#ifndef ALL
#define ALL


//-------------builtins.c-------------
void changeDir(char **, char*);
void printWD();
void echoecho(char**);
void listDriver(char**);
int getArgc(char**);


//-------------processes.c-------------
#define MAX_JOBS 20					//maximum number of jobs stored

void pidToName(int, char*);
void listProc(char**);
void editProc(int, int);
void addProc(int, char **);
void clearProc();
void removeProc(int);
void sendSignal(char**);
int getForeProc();

void makeFG(char**);
void makeBG(char**);
void launchProcess(char **);
void processInfo(char**);


//-------------inputandprompt.h-------------
#define MAX_TOK_SIZE 1000 			//maximum size for directories, names and input
#define MAX_ARGS 50					//maximum number of arguments

void PrintPrompt(char*);
char** parseCommand(char*);
char** TakeInput();
char* getUsername();

#endif