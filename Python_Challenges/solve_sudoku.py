puzzle=[[5,3,0,0,7,0,0,0,0],
        [6,0,0,1,9,5,0,0,0],
        [0,9,8,0,0,0,0,6,0],
        [8,0,0,0,6,0,0,0,3],
        [4,0,0,8,0,3,0,0,1],
        [7,0,0,0,2,0,0,0,6],
        [0,6,0,0,0,0,2,8,0],
        [0,0,0,4,1,9,0,0,5],
        [0,0,0,0,8,0,0,7,9]]


def solve_sudoku(puzzle):
    i=0
    j=0
    for m in range(0,3):
        j=0
        for n in range(0,3):
            print(j)
            box=[puzzle[i][j],puzzle[i][j+1],puzzle[i][j+2],
                puzzle[i+1][j],puzzle[i+1][j+1],puzzle[i+1][j+2],
                puzzle[i+2][j],puzzle[i+2][j+1],puzzle[i+2][j+2]]
            included=[number for number in box if number!=0]
            print("included in box",included)
            missing=[number for number in [1,2,3,4,5,6,7,8,9] if number not in included]
            print("missing from box",missing)

            for k in missing:
                val=0
                flag1=False
                flag2=False
                flag3=False
                if  k not in puzzle[i]:
                    val=val+1
                    flag1=True
                if k not in puzzle[i+1]:
                    val=val+1
                    flag2=True
                if k not in puzzle[i+2]:
                    val=val+1
                    flag3=True
                if val==1:
                    if flag1==True:
                        print("We can replace {} at line {}".format(k,i))
                    elif flag2==True:
                        print("We can replace {} at line {}".format(k,i+1))
                    elif flag3==True:
                        print("We can replace {} at line {}".format(k,i+2))
            j=j+3
        i=i+3


solve_sudoku(puzzle)
