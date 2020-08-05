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

    print()

    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print("-----------------------")

        for j in range(len(board[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ", end="")


def findEmpty(board):

    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
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



