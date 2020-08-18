# pre-defined square sudoku board as a 2D-array
# the zeroes denote empty slots to be filled in
sample = [
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
                Position of an empty slot of the form (row, column)
            """

    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0: # empty slots are marked with zeroes
                return i, j

def isPossible(board, entry, pos):
    """ Determines the validity of adding a number to a specific slot in the sudoku board

            Parameters
            ----------
            board : 2D-array
                Pre-defined square sudoku board
            entry : Integer
                1 <= entry <= 9
            pos : tuple
                Position of a slot in the board of the form (row, column)

            Returns
            -------
            isValid : boolean
                * True if adding entry to pos results in a valid board
                * False otherwise
            """

    # checks whether entry is present in the same row as pos
    for j in range(len(board[0])):
        if board[pos[0]][j] == entry and pos[1] != j: # we exclude pos itself
            return False

    # checks whether entry is present in the same column as pos
    for i in range(len(board)):
        if board[i][pos[1]] == entry and pos[0] != i:
            return False

    # determines top left position of 3 x 3 square grid pos is within
    boxPos = ((pos[0] // 3) * 3, (pos[1] // 3) * 3)

    # checks whether entry is present in the same 3 x 3 grid as pos
    for i in range(boxPos[0], boxPos[0] + 3):
        for j in range(boxPos[1], boxPos[1] + 3):
            if board[i][j] == entry and pos != (i, j):
                return False

    return True

def solve(board):
    """ Solves the board using backtracking

            Parameters
            ----------
            board : 2D-array
                Pre-defined square sudoku board

            Returns
            -------
            None
        """

    empty = findEmpty(board) # find the next empty slot

    if not empty: # if the board is not empty, it is full and we are done
        return True
    else:
        row, col = empty

    for i in range(1, 10): # possible entries
        if isPossible(board, i, (row, col)):
            board[row][col] = i # set the empty slot to entry

            if solve(board): # recurse to solve the rest of the board
                return True

            board[row][col] = 0 # backtrack if no valid entries

    return False # if no valid entries

# uncomment the calls below and run this script to check the solved and unsolved boards in the console!
"""
print()
print('Initial Board.', end='')
printBoard(sample)
solve(sample)
print()
print('SOLVED!', end='')
printBoard(sample)
"""

