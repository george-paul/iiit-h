#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <unistd.h>
#include <errno.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define maxInMemory 400000

//prints using system calls
void prSys(char* toPrint)
{
	write(1, toPrint, strlen(toPrint));
}

int main(int argc, char* argv[])
{
	//check argument count
	if(argc<3)
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
	int rfSize = lseek(rf, 0, SEEK_END)+1;
	lseek(rf, 0, SEEK_SET);
	int partSize = rfSize / (*argv[2] - '0');
	int pEnd = partSize * (*argv[3]-'0') - 1;
	int pStart = pEnd - partSize + 1;

	//create output file acc to input file name
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
	char wFilePath[200] = "./Assignment/2_";
	strcat(wFilePath, prevtok);

	int wf = open(wFilePath, O_RDWR | O_CREAT | O_TRUNC, 0600);
	if(wf == -1)
	{
		perror("Output file not created.\n");
		exit(EXIT_FAILURE);
	}

	//read, reverse and write chunk-wise
	char* chunk = (char*)malloc(maxInMemory * sizeof(char));
	char* toWrite = (char*)malloc(maxInMemory * sizeof(char));
	lseek(rf, pEnd+1, SEEK_SET);
	float progress = 0;
	char progStr[12];

	while(partSize>maxInMemory)
	{
		if(pStart+maxInMemory >= lseek(rf, 0, SEEK_CUR))
		{
			break;
		}
		lseek(rf, -maxInMemory, SEEK_CUR);
		read(rf, chunk, maxInMemory);
		//reverse
		int chunkLen = strlen(chunk);
		for(int i = 0; i<chunkLen; i++)
		{
			toWrite[chunkLen-i-1] = chunk[i];
		}
		progress = (float)(lseek(rf, -maxInMemory, SEEK_CUR) - pStart)/(pEnd - pStart);
		write(wf, toWrite, strlen(toWrite));
		sprintf(progStr,"\r%3.2f%%", progress*100);
		prSys(progStr);
	}
	int lastPos = lseek(rf, 0, SEEK_CUR);
	lseek(rf, pStart, SEEK_SET);
	char* rchunk = (char*)malloc(lastPos-pStart);
	char* rtoWrite = (char*)malloc(lastPos-pStart);
	read(rf, rchunk, lastPos-pStart);
	//reverse
	for(int i = 0; i<lastPos-pStart; i++)
	{
		rtoWrite[lastPos-pStart-i-1] = rchunk[i];
	}
	write(wf, rtoWrite, lastPos-pStart);
	progress = 100.00f;
	sprintf(progStr,"\r%3.2f%%\n", progress);
	prSys(progStr);

	exit(EXIT_SUCCESS);
	return 0;
}