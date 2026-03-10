import random
import numpy as np

matrix = np.zeros((9, 9), dtype=int)

# Function that checks rows, columns, and a 3x3 matrix.
def is_valid(board, row, col, num):
    start_row = (row // 3) * 3
    start_col = (col // 3) * 3
    for i in range(3):
        for j in range(3):
            if board[start_row + i][start_col + j] == num:
                return False
    for i in range(9):
        if board[row][i] == num:
            return False
    for j in range(9):
        if board[j][col] == num:
            return False
    return True

# Matrix that finds empty cells
def find_empty(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return i, j
    return None

# It fills the empty cells in the matrix according to the rules.
def solve(board):
    empty = find_empty(board)
    if empty ==  None:
        return True
    else:
         row, col = empty
         
         numbers = list(range(1,10))
         random.shuffle(numbers)
         for e in numbers:
            if is_valid(board, row, col, e):
                board[row][col] = e
                if solve(board):
                    return True
                board[row][col] = 0
         return False

# A function that deletes cells and creates the game according to the difficulty of Sudoku.
def create_sudoku(board, delete_cell):
    deleted = 0

    while deleted < delete_cell:
        r = random.randint(0,8)
        c = random.randint(0,8)
        if board[r][c] != 0:
            board[r][c] = 0
            deleted += 1
        # else:
        #     board[r][c] == 0
        #     pass







 
