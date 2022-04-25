# README

CS3.301 - Operating Systems and Networks
Assignment 2 by George Paul (roll no: 2021121006)

## Donatello

Donatello is a custom made Linux Shell with implementations of some built in commands and the capability to start any user defined executable.

### Instructions to Run

When in `/2021121006_Assignment2`. Run `make` and then `./out`.

### Input and Output

> The source code for IO is in `./inputandoutput.c`.
>
> `PrintPrompt()` prints the prompt for the shell along with the current working directory.
>
> `TakeInput()` reads input from the user and parses it into `;` separated tokens.

* The home directory of the shell (signified by `~`) is the directory in which Donatello starts.
* The prompt consists of `[<username>@<hostname>]:[<workingDirectory>]>>`.
* Input can consist of `;` separated commands, followed by arguments.
* Maximum input size is 1000 characters.

### Built-in Commands

> The source code for all built-in commands is in `./builtin.c`.

* `cd <path>` - Changes the current working directory of the shell to `path`. If no path is specified, changes to the home directory.
* `pwd` - Prints the current working directory.
* `echo <args>` - Prints `args` exactly as given after processing whitespaces.
* `ls -<options> <paths>` - Lists all the files at `paths` augmented by the options `-l` and `-a`.
  * `-l` prints verbose details about the files such as date modified and permissions.
  * `-a` prints all files and directories including hidden ones.
* `pinfo <pid>` - Prints information about a process specified by `pid`. If no `pid` is given then prints the information about the shell process.
* `history <num>` - Prints the latest `num`(max 20) commands that were entered. If no `num` is supplied then print the latest 10 commands.
* `repeat <num> <comm>` - Repeats `<comm>`, a command, `<num>` times.
* `exit` - Exits the shell.

### Processes

> The source code for all process control is in `./processes.c`.
>
> `pinfo` command is also implemented here.
>
> `launchProcess()` launches a user defined executable and depending on whether `&` was appended, the program continues to take IO after it launches.

If none of the built-in commands are recognized then the shell will attempt to launch the executable according to the supplied command in the foreground. IO will resume when the program exits.
If an `&` is at the end of of the command then the executable is started in the background and IO is not paused.