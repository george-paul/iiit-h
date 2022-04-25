out: shell.o inputandprompt.o builtins.o processes.o
	gcc shell.o inputandprompt.o builtins.o processes.o -o out

shell.o: shell.c
	gcc -c shell.c

processes.o: processes.c
	gcc -c processes.c

builtins.o: builtins.c
	gcc -c builtins.c

inputandprompt.o: inputandprompt.c
	gcc -c inputandprompt.c

clean:
	rm *.o out