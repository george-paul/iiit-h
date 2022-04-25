#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <unistd.h>
#include <errno.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

#define maxInMemory 400000

//prints using system calls
void prSys(char* toPrint)
{
	write(1, toPrint, strlen(toPrint));
}

int main(int argc, char* argv[])
{
	//check argument count
	if(argc<1)
	{
		perror("Not enough arguments.\n");
		exit(EXIT_FAILURE);
	}
	//open file to read from
	int rf = open(argv[1], O_RDWR);
	if(rf == -1)
	{
		perror("Invalid file path.\n");
		exit(EXIT_FAILURE);
	}
	//get file size and compute number of chunks
	int rfSize = lseek(rf, 0, SEEK_END) -1;
	lseek(rf, 0, SEEK_SET);
	int noOfChunks = (rfSize/maxInMemory)+1;
	int sizeOfChunk = maxInMemory;

	//create output file with input file name
	mkdir("./Assignment", 0700);
	char rFilePath[100];
	strcpy(rFilePath, argv[1]);
	char* tok = strtok(rFilePath, "/");
	char prevtok[100];
	while(tok != NULL)
	{
		strcpy(prevtok, tok);
		tok = strtok(NULL, "/");
	}
	char wFilePath[200] = "./Assignment/1_";
	strcat(wFilePath, prevtok);

	int wf = open(wFilePath, O_RDWR | O_CREAT | O_TRUNC, 0600);
	if(wf == -1)
	{
		perror("Output file not created.\n");
		exit(EXIT_FAILURE);
	}

	//read, reverse and write chunk-wise
	char* chunk = (char*)malloc(sizeOfChunk * sizeof(char));
	char* toWrite = (char*)malloc(sizeOfChunk * sizeof(char));
	lseek(rf, 0, SEEK_END);
	float progress = 0;
	char progStr[12];
	while(1)
	{
		if(sizeOfChunk >= lseek(rf, 0, SEEK_CUR))
		{
			break;
		}
		lseek(rf, -sizeOfChunk, SEEK_CUR);
		read(rf, chunk, sizeOfChunk);
		//reverse
		int chunkLen = strlen(chunk);
		for(int i = 0; i<chunkLen; i++)
		{
			toWrite[chunkLen-i-1] = chunk[i];
		}
		write(wf, toWrite, strlen(toWrite));
		progress = (float)(rfSize - lseek(rf, -sizeOfChunk, SEEK_CUR))/rfSize ;
		sprintf(progStr,"\r%.2f%%", progress*100);
		prSys(progStr);
	}
	int lastPos = lseek(rf, 0, SEEK_CUR);
	lseek(rf, 0, SEEK_SET);
	char* rchunk = (char*)malloc(lastPos);
	char* rtoWrite = (char*)malloc(lastPos);
	read(rf, rchunk, lastPos);
	//reverse
	for(int i = 0; i<lastPos; i++)
	{
		rtoWrite[lastPos-i-1] = rchunk[i];
	}
	write(wf, rtoWrite, lastPos);
	progress = 100.00f;
	sprintf(progStr,"\r%3.2f%%\n", progress);
	prSys(progStr);

	exit(EXIT_SUCCESS);
	return 0;
}