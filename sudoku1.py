sudoku = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

def print_board(sudoku):  
    for i in range(len(sudoku)):
        if i % 3 == 0 and i != 0:
            print("----------------------")
        for j in range(len(sudoku[0])):
            if j % 3 == 0 and j != 0:
                print("|", end=' ')
            print(sudoku[i][j], end=' ')
        print("")

def solve(sudoku):
    find = check_empty_space(sudoku)
    
    if not find:
        return True
    else: 
        row, column = find

    for i in range(1,10):
        val = check_valid(sudoku,row,column,i)
        if val:
            sudoku[row][column] = i

            if solve(sudoku):
                return True
            
            sudoku[row][column] = 0
            
    return False
            
            


def check_valid(sudoku,row,column,number): 
    #check row
    if number in sudoku[row]:
        return False
    
    #check column
    for i in range(len(sudoku)):
        if sudoku[i][column] == number:
            return False
        
    #check box
    x = column // 3
    y = row // 3

    for i in range(y * 3, y * 3 + 3):
        for j in range(x*3, x*3+3):
            if sudoku[i][j] == number and (i,j) != (row,column):
                return False
        
    return True
        
def check_empty_space(sudoku):
    for i in range(len(sudoku)):
        for j in range(len(sudoku[0])):
            if sudoku[i][j] == 0:
                return (i,j)
    return None
             
print_board(sudoku)
solve(sudoku)
print("")
print_board(sudoku)

'''
number = 1
while check_empty_space(sudoku):
    row, column = check_empty_space(sudoku)
    check_valid(sudoku,row,column,number)
    solve(sudoku, row,column,number)

print("--------------------------")
print(" ")
print_board(sudoku)


def count_empty_space(sudoku):
    counter = 0
    for i in range(len(sudoku)):
        for j in range(len(sudoku[0])):
            if sudoku[i][j] == 0:
                counter += 1
    return counter
'''