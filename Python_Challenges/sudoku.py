
puzzle=[[5,3,0,0,7,0,0,0,0],
        [6,0,0,1,9,5,0,0,0],
        [0,9,8,0,0,0,0,6,0],
        [8,0,0,0,6,0,0,0,3],
        [4,0,0,8,0,3,0,0,1],
        [7,0,0,0,2,0,0,0,6],
        [0,6,0,0,0,0,2,8,0],
        [0,0,0,4,1,9,0,0,5],
        [0,0,0,0,8,0,0,7,9]]



"""
solving=[[5,3,0  ,0,7,0  ,0,0,0],2
        [0,8,0  ,4,1,9  ,6,0,5],
        [0,4,0  ,0,8,0  ,0,7,9]]
13223--mising
"""
def solve_sudoku(puzzle):

    for line in puzzle:
        for i in range(0,len(line)):
            if line[i]==0:
                column=[]
                for other_line in puzzle:
                    column.append(other_line[i])
                missing=[]
                for j in range(1,10):
                    if j not in column:
                        missing.append(j)
                print("column examined is {}".format(column))
                print("missing numbers for column are {}".format(missing))
                possibilities=[]
                for k in missing:
                    possible=[]
                    for e in range(0,9):
                        if column[e]==0 and  k not in puzzle[e]:
                            
                            possible.append(e)
                    possibilities.append(possible)

                print("POSSIBILITIES",possibilities)
                print(puzzle)

solve_sudoku(puzzle)
