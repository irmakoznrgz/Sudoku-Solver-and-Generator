from sudoku import Sudoku

#When you enter a number like seed=100 into Sudoku(), it prints the same Sudoku puzzle every time. 
# Two different players can solve the same Sudoku.
puzzle = Sudoku(3, 3).difficulty(0.5)

puzzle.show()

# The solve() method solves the puzzle in the background and returns a new object containing the solution.

###################################################################################################################

#The py-sudoku library is simply a library that generates Sudoku puzzles. 
# However, its disadvantage is that a single Sudoku puzzle can have more than one solution.
