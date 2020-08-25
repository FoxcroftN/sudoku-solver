# sudoku-solver.py

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

def print_board(bs):
    for i in range(len(bs)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - -")
        
        for j in range(len(bs[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(bs[i][j])
            else:
                print(str(bs[i][j]) + " ", end="")


print_board(state)
