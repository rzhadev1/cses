board = [[] for _ in range(8)]

for i in range(8):
    line = input()
    for x in line:
        if x == '.':
            board[i].append(1)
        elif x =='*':
            board[i].append(0)

# check if placing a queen on board[i][j] 
# will be attacked
def attacked(i, j, board):
    
    # check row
    for x in range(8): 
        if(board[i][x] == 2):
            return True

    # check column
    for y in range(8):
        if(board[y][j] == 2):
            return True

    # check pos diagonal (+1, +1), (-1, -1)
    for mag in range(1, 9):
        if(i + mag < 8 and j + mag < 8):
            if(board[i+mag][j+mag] == 2):
                return True

        if(i - mag >= 0 and j - mag >= 0):
            if(board[i-mag][j-mag] == 2):
                return True

    # check neg diagonal (-1, +1), (+1, -1)
    for mag in range(1, 9):
        if(i + mag < 8 and j - mag >= 0):
            if(board[i+mag][j-mag] == 2):
                return True

        if(i - mag >= 0 and j + mag < 8):
            if(board[i-mag][j+mag] == 2):
                return True

    return False

# n = number of queens remaining
count = 0

def solve(n): 
    global count 
    global board

    if n == 0:
        count += 1    
    else:
        for i in range(8):
            for j in range(8):
                if board[i][j] == 2 or attacked(i,j,board) or board[i][j] == 0: 
                    continue

                board[i][j] = 2
                solve(n-1)
                board[i][j] = 1

solve(8)
print(count)
