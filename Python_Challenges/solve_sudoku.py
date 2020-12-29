
def check_line(puzzle,i,k):
    if k not in puzzle[i]:
        return True
    else:
        return False
def check_column(puzzle,d,k):
    column=[]
    for line in puzzle:
        column.append(line[d])
    if k not in column:
        return True
    else:
        return False

def solve_sudoku(puzzle):
    i=0
    j=0
    changed=True
    while(changed==True):
        changed=False
        i=0
        j=0
        for m in range(0,3):
            j=0
            for n in range(0,3):
                #print(j)
                box=[puzzle[i][j],puzzle[i][j+1],puzzle[i][j+2],
                    puzzle[i+1][j],puzzle[i+1][j+1],puzzle[i+1][j+2],
                    puzzle[i+2][j],puzzle[i+2][j+1],puzzle[i+2][j+2]]
                included=[number for number in box if number!=0]
                #print("included in box",included)
                missing=[number for number in [1,2,3,4,5,6,7,8,9] if number not in included]
                #print("missing from box",missing)

                for k in missing:
                    n_of_positions=0

                    for row in range(i,i+3):
                        for column in range(j,j+3):
                            if puzzle[row][column]==0:
                                res1=check_line(puzzle,row,k)
                                res2=check_column(puzzle,column,k)
                                if res1 and res2:
                                    #print("Available position for {} at row {} column {}".format(k,row,column))
                                    n_of_positions=n_of_positions+1
                                    pos=(row,column)
                    #print("DONE WITH {}, number of positions {}".format(k,n_of_positions))
                    if n_of_positions==1:
                        #print("ONE POSITION FOR {}, AT {}".format(k,pos))
                        puzzle[pos[0]][pos[1]]=k
                        changed=True
                j=j+3
            i=i+3
    return puzzle

puzzle=[[5,3,0,0,7,0,0,0,0],
        [6,0,0,1,9,5,0,0,0],
        [0,9,8,0,0,0,0,6,0],
        [8,0,0,0,6,0,0,0,3],
        [4,0,0,8,0,3,0,0,1],
        [7,0,0,0,2,0,0,0,6],
        [0,6,0,0,0,0,2,8,0],
        [0,0,0,4,1,9,0,0,5],
        [0,0,0,0,8,0,0,7,9]]


solved=solve_sudoku(puzzle)
for line in solved:
    print(line)
