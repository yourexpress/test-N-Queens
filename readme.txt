readme
#N_Queens
#Test environment:
#----MacOS ----Python 3.6 ----Sublime
The heuristic function of this implementation is as following:
	c(x) ----- conflicts caused by Queen x
	f(x) = c(x)
x means the xth queen, x is any integer between 0 and n-1.( n means the number of Queens).
c(x) means the conflicts caused by Queen x.

The frame of my solution is to choose any one of Queen which is not the Queen that cuase least conflicts, then move that queen to a better random position where causes less conflicts.

Repeat this process again and again until find out the solution.

The way to run this code:
Variable n means the scale of this problem. Variable n can be from 4 to 40.
Set the variable ‘filepath’, in function main(), to 1 or 2 can enter two mod:
	Set filepath == 1 can read a file whose directory is filepath, then generate a list to keep locations of N Queens on a n*n board, which is associated with the input file.
	Set filepaht == 2 can generate a list to keep locations of N Queens on a n*n board.

Then the code can run and output the solution which is a list that stores the index of row where each Queen is.
