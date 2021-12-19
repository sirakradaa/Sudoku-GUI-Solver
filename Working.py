

#Board
board = [
    [7, 8, 0, 4, 0, 0, 1, 2, 0],
    [6, 0, 0, 0, 7, 5, 0, 0, 9],
    [0, 0, 0, 6, 0, 1, 0, 7, 8],
    [0, 0, 7, 0, 4, 0, 2, 6, 0],
    [0, 0, 1, 0, 5, 0, 9, 3, 0],
    [9, 0, 4, 0, 6, 0, 0, 0, 5],
    [0, 7, 0, 3, 0, 0, 0, 1, 2],
    [1, 2, 0, 0, 0, 7, 4, 0, 0],
    [0, 4, 9, 2, 0, 6, 0, 0, 7]
]

def solve(board):
    
    find = check_Empty(board)
    
    if not find:
        return True
    else: 
        row, column = find
        
    for i in range(1,10):
        if (valid(board, i, (row, column))):
                board[row][column] = i
                
                if(solve(board)):
                    return True
                
                board[row][column] = 0
                
    return False

#Check if valid
def valid(board, number, position):
    #Check row
    for i in range(len(board[0])):
        if (number == board[position[0]][i] and i != position[1]):
            return False
        
    #Check column
    for i in range(len(board)):
        if (number == board[i][position[1]] and i != position[0]):
            return False    
        
    #Check box
    x = position[1] // 3
    y = position[0] // 3
    
    for i in range(y*3, y*3 + 3):
        for j in range(x*3, x*3 + 3):
            if (number == board[i][j] and (i, j) != position):
                return False
    return True

#Print board
def print_Board(board):
    for i in range(len(board)):
        if (i % 3 == 0):
            print('-------------------')
        for j in range(len(board[0])):
            if (j % 3 == 0 and j != 0) or j == 0:
                print('|', end='')            
            if (j == 8):
                print('{0}|'.format(board[i][j]))
            else:
                if(j % 3 == 0 or j % 3 == 1):
                    print('{0} '.format(board[i][j]), end='')
                else:
                    print('{0}'.format(board[i][j]), end='')
        if (i == 8):
            print('-------------------')
            
#Find Empty boxes and return row, column
def check_Empty(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if (board[i][j] == 0):
                return (i, j)
            
    return None
    

    
print_Board(board)
solve(board)
print_Board(board)

#Backtrack