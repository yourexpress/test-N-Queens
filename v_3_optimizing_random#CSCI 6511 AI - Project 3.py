#CSCI 6511 AI - Project 3
#N-Queen Problem
#Runyu Ma Apr/1st/2018
#--Python 3.6.3 --Sublime --Mac OS
import random
#O(n)
def detect_conf(queens):
    total = 0
    n = len(queens)
    row = [0  for i in range(n)]
    lrdiag = [0  for i in range(n*2-1)]
    rldiag = [0  for i in range(n*2-1)]

#row
    for j in range(n):
        i = queens[j]
        row[i]+=1
    for k in range(n):
        total+=row[k]*(row[k]-1)
#rldiag
    for j in range(n):
        i = queens[j]
        rldiag[i+j]+=1       
    for k in range(len(rldiag)):
        total+=rldiag[k]*(rldiag[k]-1)
#lrdiag
    
    for j in range(n):
        i = queens[j]
        lrdiag[(n-1)-(i-j)]+=1
    for k in range(len(lrdiag)):
        total+=lrdiag[k]*(lrdiag[k]-1)
    

    return row,lrdiag,rldiag,total
#O(n)
def conflicts_of_a_queen(queens,k,row,rldiag,lrdiag):
    #return number of conflicts in the kth column(Queen k)
    total = 0
    n = len(queens)
    i = queens[k]
    a = row[i]
    b = rldiag[i+k]
    c = lrdiag[(n-1)-(i-k)]

    total = a*(a-1)+b*(b-1)+c*(c-1)
    return total

def iterate_n_queens(queens,row,lrdiag,rldiag,number):
    #return 0    
    n = len(queens)
    #If there are conflicts in the board.
    if number > 0:
        #find a random queen
        j = random_queen = random.randint(0,n-1)
        oldrow = queens[random_queen]
        original = conflicts_of_a_queen(queens,j,row,rldiag,lrdiag)
        #print('------------') 
        #print('original conflicts of queen k',original) 

        while(True):
            newrow = random.randint(0,len(queens)-1)
            row[oldrow]-=1
            rldiag[oldrow+j]-=1
            lrdiag[(n-1)-(oldrow-j)]-=1

            queens[j] = newrow
            row[newrow]+=1
            rldiag[newrow+j]+=1
            lrdiag[(n-1)-(newrow-j)]+=1
            t = conflicts_of_a_queen(queens,j,row,rldiag,lrdiag)
            #print('new conflicts of queen k',t)
            #print('------------') 
            oldrow = newrow
            if original >= t:
                break

        number = detect_conf(queens)[3]
        #return num_of_conf(queens)
        return number
    #If it does not, quit
    else:
        return 0

def file2queens(filepath):
    #Read a file and generate a list to keep locations of queens.
    queenlist = []
    with open(filepath,'r') as f:
        remap = {
            ord('\t') : None,
            ord('\n') : None
        }
        for line in f.readlines():
            queenlist.append(line.translate(remap))
        #print(queenlist)

    row = len(queenlist)
    column = len(queenlist[0])
    queens = []
    for j in range(column):
        for i in range(row):
            if int(queenlist[i][j]) == 1:
                queens.append(i)
    return queens

#main()
SCALE = 60
def main(argv = None):
    #return 0
    #scale = SCALE
    filepath = '/Users/runyu/Documents/GWU/课件/AI/Assignment/P3/n-queen.txt'
    mod = 2
    #If read a file plz set mod == 1
    #if wanna test a random board plz set mod ==2
    if mod == 1:
        queens = file2queens(filepath)
        #scale = len(queens)
    elif mod == 2:
        queens = [random.randint(0,SCALE-1) for i in range(SCALE)]
    #In list "queens", elements' value mean the row where the ith queen locates
    print('Original queens:',queens)
    flag = False
    count = 0
    row,lrdiag,rldiag,number = detect_conf(queens)
    while(flag == False):
        number = iterate_n_queens(queens,row,lrdiag,rldiag,number)
        #print('Conflicts:[',number,']')
        count+=1
        '''
        if count>10000:
            queens = [random.randint(0,SCALE-1) for i in range(SCALE)]
            row,lrdiag,rldiag,number = detect_conf(queens)
        '''
        print('Conflicts:[',number,']',count)
        if number == 0:
            #It means there is no conflict on the board.
            flag = True
            print('Succeed. Solution is as following:')
            print(queens)
    
    if flag == True:
        board = [['O' for j in range(len(queens))] for i in range(len(queens))]
        for i in range(len(queens)):
            for j in range(len(queens)):
                if queens[j] == i:
                    board[i][j] = 'X'
    print('This is the board:')
    for row in board:
        print(row)
    
    print('End')
    return 0

if __name__ == "__main__":
    main()
