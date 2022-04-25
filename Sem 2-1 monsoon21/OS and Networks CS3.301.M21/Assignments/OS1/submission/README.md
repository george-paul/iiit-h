# README
CS3.301 - Operating Systems and Networks
Assignment 1 by George Paul (roll no: 2021121006)

## Part 1
- source code for part 1 is contained in q1.c and is written using only system calls (excluding the allowed library functions).
- The program takes one argument *file-path*, reverses the file at *file-path* and writes it to `./Assignment/1_file-path`.
- reversal is done by reading and writing reversed text in chunks of size 400000 bytes.
- Prints the progress of reversal during run time.
- Output file will have read and write permissions for the owner and will be owerwritten if it already exists.
- Directory will have read, write and execute permissions for the owner and will be created if it doesn't exist.
- Assumes a maximum length of 100 characters for *file-path*.

## Part 2
- source code for part 2 is contained in q2.c and is written using only system calls (excluding the allowed library functions).
- The program takes three arguments *file-path*, *parts* and *part-number*.
- takes the text in *file-path* and divides it into *parts* number of parts and reverses and writes the part specified by *part-number*  into `./Assignment/2_file-path`
- Prints the progress of reversal during run time.
- Output file will have read and write permissions for the owner and will be owerwritten if it already exists.
- Directory will have read, write and execute permissions for the owner and will be created if it doesn't exist.
- Assumes a maximum length of 100 characters for *file-path*.
- Assumes that the size of input file is divisible by *parts*.
- *part-number* indexing starts at index 1 for the first part.

## Part 3
- source code for part 3 is contained in q3.c and is written using only system calls (excluding the allowed library functions).
- The program takes one argument *file-path* and lists the read, write and execute permissions given to the User, Group and Others of the files in `./Assignment` that are named `1_filename.txt` and `2_filename.txt`.
- Assumes a maximum length of 105 characters for *file-path*.