# Sudoku Solver
This project primarily consists of a sudoku solver utilizing the backtracking algorithm. It includes a GUI based game as well as a text based version.

Run main.py to play sudoku! 

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
    
# For the Graphical User Interface (GUI.py) ...
The GUI based version involves a simple interface to play sudoku as a game. **To do this simply run the main.py file.** This will
open a separate window consisting of a grid and a few buttons that can be found below. 
    
    * SOLVE - solves the board for the user with backtracking 
    * Easy - retrieves a board of easy difficulty
    * Medium - retrieves a board of medium difficulty
    * Hard - retrieves a board of hard difficulty
    * Expert - retrieves a board of expert difficulty
    * Check - can be toggled on or off for live validity checking
    * Clear - resets the board to its original arrangement
    
A few libraries have been used for the development of this game that can be found below.

    * pygame - designed for writing simple video games
    * beautifulsoup4 - useful for web-scraping and parsing HTML and XML documents
    * requests - makes HTTP requests simpler and more user-friendly
    * sys - used to manipulate python run-time environment

To play, select a square to enter a number between 1 and 9. Use the check button to catch errors while solving (or turn it off if you enjoy the challenge!). 
Stuck on a board? Change difficulty or click SOLVE and observe how even the toughest of boards are solved with ease by the backtracking algorithm.
Since the boards are generated from an online service, an active internet connection is required as well. Enjoy!

    

