import tkinter as tk
from tkinter import messagebox
import copy

# =====================================
# PART 1: BACKEND
# =====================================

from sudoku_backend import solve, create_sudoku


# =====================================
# PART 2: TKINTER INTERFACE (FRONTEND)
# =====================================

class SudokuGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Sudoku")
    
        self.cell_size = 50
        self.width = self.cell_size * 9
        self.height = self.cell_size * 9
        
        # Game Data
        self.full_solution = [] 
        self.player_board = [] 
        self.original_board = [] 
        self.selected_cell = None 
        
        self.create_widgets()
        self.draw_grid()
        
        # The game starts on easy difficulty by default.
        self.new_game("Easy")

    def create_widgets(self):
        main_frame = tk.Frame(self.root)
        main_frame.pack(padx=10, pady=10)
        
        self.canvas = tk.Canvas(main_frame, width=self.width, height=self.height, bg="white")
        self.canvas.pack(side=tk.LEFT)
        
        menu_frame = tk.Frame(main_frame)
        menu_frame.pack(side=tk.RIGHT, padx=20)
        
        tk.Label(menu_frame, text="Choose Difficulty:", font=("Arial", 12, "bold")).pack(pady=5)
        tk.Button(menu_frame, text="Easy", width=15, command=lambda: self.new_game("Easy")).pack(pady=2)
        tk.Button(menu_frame, text="Medium", width=15, command=lambda: self.new_game("Medium")).pack(pady=2)
        tk.Button(menu_frame, text="Hard", width=15, command=lambda: self.new_game("Hard")).pack(pady=2)
        
        tk.Frame(menu_frame, height=2, bd=1, relief=tk.SUNKEN).pack(fill=tk.X, pady=15) 
        
        # Game control buttons
        tk.Button(menu_frame, text="Check", width=15, bg="lightblue", command=self.check_board).pack(pady=5)
        tk.Button(menu_frame, text="Solve", width=15, bg="lightgreen", command=self.solve_game).pack(pady=5)
        tk.Button(menu_frame, text="Clear", width=15, bg="lightcoral", command=self.clear_board).pack(pady=5)
        
        self.canvas.bind("<Button-1>", self.cell_clicked)
        self.root.bind("<Key>", self.key_pressed)

    def draw_grid(self):
        for i in range(10):
            line_width = 3 if i % 3 == 0 else 1
            
            self.canvas.create_line(i * self.cell_size, 0, i * self.cell_size, self.height, width=line_width)
            self.canvas.create_line(0, i * self.cell_size, self.width, i * self.cell_size, width=line_width)

    def draw_numbers(self):
        self.canvas.delete("numbers") 
        
        for row in range(9):
            for col in range(9):
                num = self.player_board[row][col]
                if num != 0:
                    x = col * self.cell_size + self.cell_size / 2
                    y = row * self.cell_size + self.cell_size / 2
                    
                    if self.original_board[row][col] != 0:
                        self.canvas.create_text(x, y, text=str(num), font=("Arial", 18, "bold"), fill="black", tags="numbers")
                    else:
                        self.canvas.create_text(x, y, text=str(num), font=("Arial", 18), fill="blue", tags="numbers")

    # ==========================================
    # PART 3: GAME MECHANİCS
    # ==========================================

    def new_game(self, difficulty):
        difficulty_map = {"Easy": 30, "Medium": 45, "Hard": 55}
        cells_to_remove = difficulty_map[difficulty]
        
        empty_board = [[0 for _ in range(9)] for _ in range(9)]
        solve(empty_board)
        
        # Copy this correct answer to a secret box (we'll use it later when checking).
        self.full_solution = copy.deepcopy(empty_board)

        create_sudoku(empty_board, cells_to_remove)
    
        self.player_board = copy.deepcopy(empty_board)

        # Note which cells were the original clue so you don't forget.
        self.original_board = copy.deepcopy(empty_board)
        
        self.selected_cell = None
        self.draw_numbers() 
        self.highlight_cell() 

    def cell_clicked(self, event):
        col = event.x // self.cell_size
        row = event.y // self.cell_size
        
        if self.original_board[row][col] == 0:
            self.selected_cell = (row, col)
        else:
            self.selected_cell = None
            
        self.highlight_cell()

    def highlight_cell(self):
        self.canvas.delete("highlight") 
        if self.selected_cell:
            row, col = self.selected_cell
            x1 = col * self.cell_size
            y1 = row * self.cell_size
            x2 = x1 + self.cell_size
            y2 = y1 + self.cell_size
            self.canvas.create_rectangle(x1, y1, x2, y2, fill="lightgray", outline="", tags="highlight")
            self.canvas.tag_lower("highlight")

    def key_pressed(self, event):
        if not self.selected_cell: return 
        
        row, col = self.selected_cell
        char = event.char
        
        if char in "123456789":
            self.player_board[row][col] = int(char)
        elif event.keysym in ["BackSpace", "Delete"]:
            self.player_board[row][col] = 0
            
        self.draw_numbers() 

    # ==========================================
    # PART 4: CHECK
    # ==========================================

    def check_board(self):
        mistakes = 0
        spaces = 0
        
        for r in range(9):
            for c in range(9):
                if self.player_board[r][c] == 0:
                    spaces += 1
                elif self.player_board[r][c] != self.full_solution[r][c]:
                    mistakes += 1
                    
        if mistakes > 0:
            messagebox.showwarning("Status Report", f"So far there are {mistakes} errors! \nCorrect the ones you wrote incorrectly.")
        elif spaces > 0:
            messagebox.showinfo("Status Report, Everything is correct so far! \nKeep it up and complete the puzzle.")
        else:
            messagebox.showinfo("Congratulations! You solved the Sudoku puzzle without any mistakes!")

    def clear_board(self):
        self.player_board = copy.deepcopy(self.original_board)
        self.draw_numbers()

    def solve_game(self):
        self.player_board = copy.deepcopy(self.full_solution)
        self.selected_cell = None
        self.highlight_cell()
        self.draw_numbers()

# Commands that start the application
if __name__ == "__main__":
    root = tk.Tk()
    app = SudokuGame(root)
    root.mainloop() # An infinite loop that keeps the window open.
