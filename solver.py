""" GUI based Sudoku Solver

This script allows the user to solve a pre-defined square sudoku board.
The algorithm makes use of backtracking and recursion to quickly solve
the toughest of boards within seconds!

This file does not accept any input. The board has been pre-defined and,
as such, any square sudoku grid may be used instead formatted as a 2D-array.
The empty slots should be replaced with zeroes (0).

This script does not require any additional modules or libraries to be installed.

The following functions are present in this script. Documentation
can be found as docstrings in the respective functions.

    * printBoard - prints sudoku board to the console in a human-readable manner
    * findEmpty - finds an empty slot in the sudoku grid
    * isPossible - determines the validity of adding a number to a specific slot
    * solve - solves the board using backtracking
"""

# pre-defined square sudoku board as a 2D-array
# the zeroes denote empty slots to be filled
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


def printBoard(board):
    """ Prints the sudoku board to the console in a human-readable format

        Parameters
        ----------
        board : 2D-array
            Pre-defined square sudoku board

        Returns
        -------
        None
    """

    print()

    # print horizontal line every three rows
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print("-----------------------")

        # print vertical line every third column
        for j in range(len(board[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(board[i][j]) # move onto new line after each row
            else:
                print(str(board[i][j]) + " ", end="") # stay on same line within the row


def findEmpty(board):
    """ Finds the next empty slot in the sudoku grid

            Empty slots in the grid are denoted by 0. The function first checks for an
            empty slot column-wise starting from the top and then moves on to subsequent rows.

            Parameters
            ----------
            board : 2D-array
                Pre-defined square sudoku board

            Returns
            -------
            position : tuple
                Position of the empty slot in the form (row, column)
            """

    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0: # empty slots are marked with zeroes
                return i, j

def isPossible(board, entry, pos):

    for j in range(len(board[0])):
        if board[pos[0]][j] == entry and pos[1] != j:
            return False

    for i in range(len(board)):
        if board[i][pos[1]] == entry and pos[0] != i:
            return False

    boxPos = ((pos[0] // 3) * 3, (pos[1] // 3) * 3)

    for i in range(boxPos[0], boxPos[0] + 3):
        for j in range(boxPos[1], boxPos[1] + 3):
            if board[i][j] == entry and pos != (i, j):
                return False

    return True

def solve(board):

    empty = findEmpty(board)

    if not empty:
        return True
    else:
        row, col = empty

    for i in range(1, 10):
        if isPossible(board, i, (row, col)):
            board[row][col] = i

            if solve(board):
                return True

            board[row][col] = 0

    return False


printBoard(board)
solve(board)
print()
printBoard(board)



