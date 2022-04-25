#include "kernel/types.h"
#include "kernel/stat.h"
#include "user.h"

int main(int argc, char* argv[])
{
	if(argc != 3)
  {
    printf("Invalid number of arguments\n");
    exit(0);
  }
  set_priority(atoi(argv[1]), atoi(argv[2]));
  exit(0);
}