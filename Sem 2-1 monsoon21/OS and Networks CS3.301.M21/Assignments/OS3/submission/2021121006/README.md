# README

CS3.301 - Operating Systems and Networks
Assignment 2 by George Paul (roll no: 2021121006)

## Donatello

Donatello is a custom made Linux Shell with implementations of some built in commands and the capability to start any user defined executable.

### Instructions to Run

When in `/2021121006_Assignment2`. Run `make` and then `./out`.

### Built-in commands:

* `cd <path>` - Changes the current working directory of the shell to `path`. If no path is specified, changes to the home directory.
* `pwd` - Prints the current working directory.
* `echo <args>` - Prints `args` exactly as given after processing whitespaces.
* `ls -<options> <paths>` - Lists all the files at `paths` augmented by the options `-l` and `-a`.
  * `-l` prints verbose details about the files such as date modified and permissions.
  * `-a` prints all files and directories including hidden ones.
* `pinfo <pid>` - Prints information about a process specified by `pid`. If no `pid` is given then prints the information about the shell process.
* `history <num>` - Prints the latest `num`(max 20) commands that were entered. If no `num` is supplied then print the latest 10 commands.
* `repeat <num> <comm>` - Repeats `<comm>`, a command, `<num>` times.
* `replay -<opts> <args>` - Replays a given command.
  * `-command <com>` specifies the command to replay.
  * `-interval <inter>` replays the command every `inter` seconds.
  * `-period <per>` replays the command until `per` seconds have passed.
* `jobs -<options>` - Lists all the background processes.
  * `-r` prints only the running processes.
  * `-s` prints only the stopped processes.
* `sig <jobNo> <sigNum>` - Sends the signal number `sigNum` to the process with job number `jobNo`
* `fg <jobNo>` - Makes the process specified by `jobNo` come to the foreground, blocking IO till it stops/exits.
* `bg <jobNo>` - Starts running the process specified by `jobNo` in the background. IO is not blocked.
* `exit` - Exits the shell.

### Other Executables

If none of the built-in commands are recognized then the shell will attempt to launch the executable according to the supplied command in the foreground. IO will resume when the program exits.

### Special Symbols

* If an `&` is appended at the end of of the command then the executable is started in the background so that IO is not paused. _This symbol is not supported by built-in commands_.
* The `|` symbol given between commands indicates a pipe. The output from the left hand command will be given as input to the right hand command.
* `<` indicates Input Redirection. The input for the command will be given by the file specified on the right hand.
* `>` indicates Output Redirection. The output for the command will be written to the file specified on the right hand. The file is created if it does not exist (with `0644` permissions).
* `>>` indicates Output Redirection. The output for the command will be written to the file specified on the right hand. The output is appended to the existing file contents and the file must exist. 

### About the source code:

#### The Shell `./shell.c`

* `main()` starts with a shell initialization(viz. signal handling) and calls IO functions to take input and print prompts.
* Each input is parsed for `;` and run separately. Each token is then considered a job.
* If a job has `|` then pipes are created in `runJob()` and each command is executed in `ExecCommand()` with particular input and output file descriptors.
* `ExecCommand()` also checks for Input and Output redirection (`<`, `>`, `>>`) and respectively modifies the input and output file descriptors. Then it runs the particular command.
* Signal handlers for `SIGCHLD` and `SIGNINT` are defined here. They make sure any child processes are not left as zombies and that a `SIGINT` is delivered to the running child process but not the shell itself.
* The `history`, `repeat` and `replay`  built-in commands are also implemented in this file.

#### Input and Output `./inputandoutput.c`

* The source code for IO is in `./inputandoutput.c`.
* `PrintPrompt()` prints the prompt for the shell along with the current working directory.
* `TakeInput()` reads input from the user and parses it into `;` separated tokens.
* The home directory of the shell (signified by `~`) is the directory in which Donatello starts.
* The prompt consists of `[<username>@<hostname>]:[<workingDirectory>]>>`.
* Input can consist of `;` separated commands, followed by arguments.
* Maximum input size is 1000 characters.

#### Built-in Commands `./builtin.c`

* The source code for all built-in commands is in `./builtin.c`.
* Functions for each of the some of the shown built-in commands are defined in `./builtin.c`. Namely - `cd`, `pwd`, `echo`, `ls`.

#### Processes `./processes.c`

* The source code for all process control is in `./processes.c`.
* `pinfo`, `sig `, `jobs`, `fg` and `bg` commands are also implemented here.
* Various job control functions to maintain the background process list are also found here.
* `launchProcess()` launches a user defined executable and depending on whether `&` was appended, the program continues to take IO after it launches.
