#include "kernel/types.h"
#include "kernel/stat.h"
#include "user.h"

int main(int argc, char* argv[])
{
	if(argc<3)
  {
    printf("Invalid number of arguments\n");
    exit(0);
  }
  int childPid = fork();
  // fork errored
  if(childPid < 0)
  {
    printf("Could not fork\n");
    exit(0);
  }
  // in child
  else if(childPid != 0)
  {
    trace(atoi(argv[1]));
    exec(argv[2], argv+2);
    // if exec returns then it has erred
    printf("couldn't execute %s\n", argv[1]);
    exit(0);
  }
  // in parent
	exit(0);
}