'''
Use 2D array to represent the board
Blocks can be formed by check horizontal and vertical elements

'''

board_string = input("Enter board string: ")

board = []
for i in range(5):
    board.append(list(board_string[i*4:i*4+4]))
for i in board:
    print(i)
while True:
    move = input("Enter move: ")
    if move == "exit":
        break
    else:
          copy_move = move
          # accept a string of multiple of 2 characters, split it by every two characters first is block sec is direction
          while (len(copy_move) > 0):
            idx_to_move = []
            block = copy_move[0]
            direction = copy_move[1]
            if direction == 'N':
                for rows in range(5):
                    for cols in range(4):
                        if board[rows][cols] == block:
                            idx_to_move.append((rows, cols))
                for (j, k) in idx_to_move:
                    board[j][k], board[j-1][k] = board[j-1][k], board[j][k]
            
            elif direction == 'S':
                for rows in range(5):
                    for cols in range(4):
                        if board[rows][cols] == block:
                            idx_to_move.append((rows, cols))
                for (j, k) in reversed(idx_to_move):
                    board[j][k], board[j+1][k] = board[j+1][k], board[j][k]
            elif direction == "E":
                for rows in range(5):
                    for cols in range(4):
                        if board[rows][cols] == block:
                            idx_to_move.append((rows, cols))
                for (j, k) in reversed(idx_to_move):
                    board[j][k], board[j][k+1] = board[j][k+1], board[j][k]
            elif direction == "W":
                for rows in range(5):
                    for cols in range(4):
                        if board[rows][cols] == block:
                            idx_to_move.append((rows, cols))
                for (j, k) in idx_to_move:
                    board[j][k], board[j][k-1] = board[j][k-1], board[j][k]
            copy_move = copy_move[2:]
          
for i in board:
    for j in i:
        print(j, end = "")