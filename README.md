# Sudoku Solver
This is a sudoku solver utilizing the backtracking algorithm. It includes a graphical GUI as well as a text based version.

Run GUI.py to play sudoku! (Work in Progress)

This script allows the user to solve a simple square sudoku board.
The algorithm makes use of backtracking and recursion to quickly solve
the toughest of boards within seconds!

# For the text-based version (solver.py) ...
This file does not accept any input. The board has been pre-defined and,
as such, any square sudoku grid may be used instead formatted as a 2D-array.
The empty slots should be replaced with zeroes (0).

This script does not require any additional modules or libraries to be installed.

The following functions are present in this script. Documentation
can be found as docstrings for the respective functions.

    * printBoard - prints sudoku board to the console in a human-readable manner
    * findEmpty - finds an empty slot in the sudoku grid
    * isPossible - determines the validity of adding a number to a specific slot
    * solve - solves the board using backtracking
