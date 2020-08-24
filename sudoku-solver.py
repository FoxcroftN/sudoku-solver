state = [
    [0,0,0,0,0,0,0,0,0], #1
    [0,0,0,0,0,0,0,0,0], #2
    [0,0,0,0,0,0,0,0,0], #3
    [0,0,0,0,0,0,0,0,0], #4
    [0,0,0,0,0,0,0,0,0], #5
    [0,0,0,0,0,0,0,0,0], #6
    [0,0,0,0,0,0,0,0,0], #7
    [0,0,0,0,0,0,0,0,0], #8
    [0,0,0,0,0,0,0,0,0], #9
] 

def check_board_validity(bs):
    print("check")
    #checks if board is valid

def print_board(bs):
    printstring = " "
    print("==================")
    for i in range(len(bs)):
        for j in range(len(bs[0])):
            #print(str(i+1) +" : "+ str(j+1))       # jagged array traversal test
            print(str(bs[i][j]))

print_board(state)
