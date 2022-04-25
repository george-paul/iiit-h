#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <dirent.h>
#include <pwd.h>
#include <grp.h>
#include <time.h>
#include <sys/stat.h>
#include <unistd.h>

#include "all.h"

//gets the argument count for a given command input
int getArgc(char** inpt)
{
	int argc = 1;
	while(inpt[argc] != NULL)
	{
		argc++;
	}
	return argc-1;
}

//implements cd on tokenised inpt; if no argument is given, changes into homeDir
void changeDir(char** inpt, char* homeDir)
{
	//static variable to keep track of previous directories for "-" flag
	static char prevDir[MAX_TOK_SIZE] = "/";
	if(getArgc(inpt)>1)
	{
		fprintf(stderr, "Too many arguments.");
		return;
	}

	char* dir = (char*) malloc(MAX_TOK_SIZE * sizeof(char));
	memset(dir, '\0', MAX_TOK_SIZE);
	//check for no arguments, if yes change to home (~)
	if(getArgc(inpt)==0)
	{
		strncpy(dir, homeDir, strlen(homeDir));
	}
	//check for the presence of ~ flag
	else if(inpt[1][0] == '~' || inpt[1] == NULL)
	{
		strncpy(dir, homeDir, strlen(homeDir));
		strcat(dir, &inpt[1][1]);
	}
	//check for - flag
	else if(inpt[1][0] == '-')
	{
		strncpy(dir, prevDir, strlen(prevDir));
	}
	//if no flags then change to the given dir
	else
	{
		strncpy(dir, inpt[1], strlen(inpt[1]));
	}
	//save current path before changing directory for -
	char pDir[MAX_TOK_SIZE];
	getcwd(pDir, MAX_TOK_SIZE);
	//change directory
	if(chdir(dir) != 0)
	{
		perror("Could not change directory.");
		free(dir);
		return;
	}
	//if directory was successfully changed save the old dir to prevDir
	else
	{
		strcpy(prevDir, pDir);		
	}
	free(dir);
}

//implements pwd
void printWD()
{
	char path[MAX_TOK_SIZE];
	getcwd(path, MAX_TOK_SIZE);
	printf("%s\n", path);
}

//implements echo
void echoecho(char** inpt)
{
	int i = 1;
	while(inpt[i] != NULL)
	{
		printf("%s ", inpt[i++]);
	}
	printf("\n");
}

//returns only 1, used for scandir
int all(const struct dirent *a)
{return 1;}

//returns a string according to perms of mode
void permString(mode_t mode, char* buf)
{
	buf[0] = '\0';
	if (S_ISREG(mode)) strcat(buf, "-");
	else if (S_ISLNK(mode)) strcat(buf, "l");
	else if (S_ISDIR(mode)) strcat(buf, "d");
	else if (S_ISBLK(mode)) strcat(buf, "b");
	else if (S_ISCHR(mode)) strcat(buf, "c");
	else if (S_ISFIFO(mode)) strcat(buf, "|");

	(mode & S_IRUSR) ? strcat(buf,"r") : strcat(buf,"-");
	(mode & S_IWUSR) ? strcat(buf,"w") : strcat(buf,"-");
	(mode & S_IXUSR) ? strcat(buf,"x") : strcat(buf,"-");
	(mode & S_IRGRP) ? strcat(buf,"r") : strcat(buf,"-");
	(mode & S_IWGRP) ? strcat(buf,"w") : strcat(buf,"-");
	(mode & S_IXGRP) ? strcat(buf,"x") : strcat(buf,"-");
	(mode & S_IROTH) ? strcat(buf,"r") : strcat(buf,"-");
	(mode & S_IWOTH) ? strcat(buf,"w") : strcat(buf,"-");
	(mode & S_IXOTH) ? strcat(buf,"x") : strcat(buf,"-");
	(mode & S_ISUID) ? strcat(buf,"U") : strcat(buf,"-");
	(mode & S_ISGID) ? strcat(buf,"G") : strcat(buf,"-");
	(mode & S_ISVTX) ? strcat(buf,"S") : strcat(buf,"-");
	return;
}

//used by listDriver to list files at a given path
void list(char* dir, int opta, int optl)
{
	char fileName[MAX_TOK_SIZE] = "";
	//to check if dir is a file
	struct stat s;
	if(stat(dir,&s) == 0)
	{
		if(s.st_mode & S_IFREG)
		{
			//seek pos to location of last '/'
			int pos;
			for(pos = strlen(dir)-1; pos>=0 && dir[pos] != '/'; pos--);
			//copy file name to fileName
			strcpy(fileName, dir+pos+1);
			if(pos >= 0)
			{
				//modify dir to not have the fileName
				char temp[MAX_TOK_SIZE];
				strncpy(temp, dir, pos+1);
				strcpy(dir, temp);
			}
			//else dir is a file in the working dir
			else
			{
				strcpy(dir, "./");
			}
		}
		//not a dir so print the path
		else
		{
			printf("\n%s:\n", dir);
		}
	}
	else
	{
		perror("Could not read the given path");
		return;
	}

	//save current directory
	char savedDir[MAX_TOK_SIZE];
	getcwd(savedDir, MAX_TOK_SIZE);
	//change cwd to dir
	if(chdir(dir) != 0)
	{
		perror("Could not list given directory");
		return;
	}
	//declare necessary variables for listing
	struct dirent** f;
	int noOfFiles = scandir(".", &f, all, alphasort);
	char buffer[1000];
	struct passwd pw;
	struct passwd* pwp;
	struct group gr;
	struct group* grp;
	struct tm time;
	int totalBlocks = 0;
	//iterate through each file and print details
	if(noOfFiles > 0)
	{
		for (int i=0; i<noOfFiles; i++)
		{
			//if file exists && skip hidden files if no -a && list only fileName if dir is a file
			if (stat(f[i]->d_name, &s) == 0 && (f[i]->d_name[0] != '.' || opta) && ( !strcmp(f[i]->d_name,fileName) || !strcmp(fileName,"") ) )
			{
				//skip verbose details if no -l
				if(optl)
				{
					//add no of blocks to totalBlocks
					totalBlocks += s.st_blocks;
					//permissions
					permString(s.st_mode,buffer);
					printf("%10.10s", buffer);
					//hard links
					printf(" %3ld", s.st_nlink);

					//user
					getpwuid_r(s.st_uid, &pw, buffer, sizeof(buffer), &pwp);
					printf(" %s", pw.pw_name);

					//group
					getgrgid_r(s.st_gid, &gr, buffer, sizeof(buffer), &grp);
					printf(" %s", gr.gr_name);

					//size
					printf(" %*d", 10, (int)s.st_size);

					//modified time
					localtime_r(&s.st_mtime, &time);
					strftime(buffer, sizeof(buffer), "%F %T", &time);
					printf(" %s ", buffer);
				}
				//filename
				printf("%s\n", f[i]->d_name);
			}
			free(f[i]);
		}
		//if option -l is given and path is not a file
		if(optl && !strcmp(fileName,""))
		{
			printf("total: %d\n", totalBlocks);
		}
	}
	else
	{
		perror("Invalid path or empty directory");
	}
	//change directory back to savedDir
	if(chdir(savedDir) != 0)
	{
		perror("error: could not come back to original directory.");
	}
	free(f);
}

//implements ls with -l and -a flags
void listDriver(char** inpt)
{
	int opta = 0, optl = 0;
	char* dir;
	//if no argument is given then list at cwd
	if(getArgc(inpt) == 0)
	{
		dir = (char*)malloc(MAX_TOK_SIZE*sizeof(char));
		getcwd(dir,MAX_TOK_SIZE);
		list(dir, opta, optl);
		free(dir);
	}
	//at least one argument
	else
	{
		for(int i = 1; i<=getArgc(inpt); i++)
		{
			//if argument being scanned is an option
			if(inpt[i][0] == '-')
			{
				//set option flags
				if(strcmp(inpt[i], "-a") == 0) opta = 1;
				else if (strcmp(inpt[i], "-l") == 0) optl = 1;
				else if (strcmp(inpt[i], "-la") == 0 || strcmp(inpt[i], "-al") == 0)
				{
					optl = 1;
					opta = 1;
				}
				else
				{
					fprintf(stderr, "Unrecognised option.\n");
					return;
				}
			}
			//if not option then treat as directory
			else
			{
				dir = inpt[i];
				list(dir, opta, optl);
				opta = 0; optl = 0;
				continue;
			}
			//if the options aren't followed by a directory, list at cwd
			if(inpt[i+1] == NULL)
			{
				dir = (char*)malloc(MAX_TOK_SIZE*sizeof(char));
				getcwd(dir,MAX_TOK_SIZE);
				list(dir, opta, optl);
				opta = 0; optl = 0;
				free(dir);
			}
		}
	}
}