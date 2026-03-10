# Sudoku Solver & Generator (with Tkinter GUI)

A complete Sudoku game built from scratch using Python. This project features a custom-built **Backtracking algorithm** to generate playable Sudoku boards and solve them automatically, wrapped in a user-friendly Tkinter graphical interface.

## Features
* **Custom Backend Algorithm:** Uses a recursive Backtracking approach (`sudoku_backend.py`) to validate rules, generate fully randomized boards, and carve out puzzles.
* **Interactive GUI:** Built with `Tkinter` (`main.py`). Players can input numbers via keyboard, check their mistakes, or let the AI solve the puzzle instantly.
* **Difficulty Levels:** Generates puzzles dynamically based on Easy, Medium, and Hard difficulty selections.
* **External Library Comparison:** Includes an additional script (`py-sudoku.py`) demonstrating how to generate puzzles using the external `py-sudoku` library for learning and comparison purposes.

##  Project Structure
* `main.py`: The frontend application containing the Tkinter GUI and game mechanics.
* `sudoku_backend.py`: The core engine containing the mathematical logic, board validation, and Backtracking solver.
* `py-sudoku.py`: An alternative demonstration using the `py-sudoku` external package.
* `requirements.txt`: List of dependencies required to run the external scripts.

##  Installation & How to Run
1. Clone the repository:
   ```bash
   git clone [https://github.com/irmakoznrgz/Sudoku-Solver-and-Generator.git](https://github.com/irmakoznrgz/Sudoku-Solver-and-Generator.git)

## 🧠 What I Learned
Through this project, I deeply understood how Recursion and Backtracking algorithms work in practice. I also learned how to separate Backend logic from Frontend interfaces (Modularity) and how to manage GUI states using Object-Oriented Programming (OOP) with Tkinter.
