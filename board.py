# 
board = [['_', '_', '_'],
         ['_', '_', '_'],
         ['_', '_', '_']]

tmp = " _____"
        
for i in range(len(board[0])):
    tmp += "\n|"
    for j in range(len(board[0])):
        tmp += board[i][j] + "|"

tmp += "\n -----"

print(tmp)
