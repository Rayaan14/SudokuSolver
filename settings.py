# Dimensions
WIDTH = 600
HEIGHT = 600

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
LIGHTORANGE = (250, 171, 83)
CORNSILK = (255, 248, 220)

# Fonts
font = 'lato'

# Boards
testBoard1 = [[0 for x in range(9)] for x in range(9)]
testBoard2 = board = [
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

# Positions and Sizes
gridPos = (75, 100)
cellSize = 50
gridSize = cellSize * 9