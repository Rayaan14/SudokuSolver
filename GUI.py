##############################################################
import sys
import requests
from solver import *
from buttons import *
from settings import *
from bs4 import BeautifulSoup
##############################################################


class App:
##############################################################
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((WIDTH, HEIGHT))
        self.running = True
        self.selected = [0, 0]
        self.mousePos = None
        self.finished = False
        self.check = True
        self.font = pygame.font.SysFont(numFont, cellSize // 2)
        self.clock = pygame.time.Clock()
        self.timer, self.dt = 0, 0
        self.playingButtons = []
        self.lockedCells, self.incorrectCells = [], []
        self.grid = []
        self.getPuzzle("1")
        self.load()
##############################################################

##############################################################
    def run(self):
        while self.running:
            self.playingEvents()
            self.playingUpdate()
            self.playingDraw()
        pygame.quit()
        sys.exit()
##############################################################

############### PLAYING STATE FUNCTIONS ######################

    def playingEvents(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                selected = self.mouseOnGrid()
                if selected:
                    self.selected = selected
                else:
                    self.selected = [0, 0]
                    for button in self.playingButtons:
                        if button.highlighted:
                            button.click()

            if event.type == pygame.KEYDOWN:
                if self.selected is not None and list(self.selected) not in self.lockedCells and self.isInt(event.unicode) and not self.finished:
                    self.grid[self.selected[1]][self.selected[0]] = int(event.unicode)

                if event.key == pygame.K_LEFT and self.selected[0] > 0:
                    self.selected[0] -= 1
                if event.key == pygame.K_RIGHT and self.selected[0] < 8:
                    self.selected[0] += 1
                if event.key == pygame.K_UP and self.selected[1] > 0:
                    self.selected[1] -= 1
                if event.key == pygame.K_DOWN and self.selected[1] < 8:
                    self.selected[1] += 1

                if event.key == pygame.K_BACKSPACE and self.selected not in self.lockedCells and not self.finished:
                    self.grid[self.selected[1]][self.selected[0]] = 0

    def playingUpdate(self):
        self.mousePos = pygame.mouse.get_pos()

        if not self.finished:
            self.timer += self.dt

        for button in self.playingButtons:
            button.update(self.mousePos)

        if self.check:
            self.incorrectCells = []
            self.checkAllCells()
        else:
            self.incorrectCells = []

        if self.allCellsDone():
            if len(self.incorrectCells) == 0:
                self.finished = True

    def playingDraw(self):
        self.window.fill(WHITE)

        for button in self.playingButtons:
            button.draw(self.window)

        self.shadeLockedCells(self.window, self.lockedCells)

        if self.selected:
            self.drawSelection(self.window, self.selected)

        self.shadeIncorrectCells(self.window, self.incorrectCells)
        self.drawNumbers(self.window) if not self.finished else self.drawNumbers(self.window, SOLVE)
        self.drawGrid(self.window)
        self.drawTimer(self.window)

        pygame.display.update()
##############################################################

################## HELPER FUNCTIONS ##########################

    def getPuzzle(self, diff):
        htmlDoc = requests.get("https://grid.websudoku.com/?level={}".format(diff)).content
        soup = BeautifulSoup(htmlDoc, features='html.parser')
        ids = ['f00', 'f01', 'f02', 'f03', 'f04', 'f05', 'f06', 'f07', 'f08', 'f10', 'f11', 'f12', 'f13', 'f14', 'f15',
               'f16', 'f17', 'f18', 'f20', 'f21', 'f22', 'f23', 'f24', 'f25', 'f26', 'f27', 'f28', 'f30', 'f31', 'f32',
               'f33', 'f34', 'f35', 'f36', 'f37', 'f38', 'f40', 'f41', 'f42', 'f43', 'f44', 'f45', 'f46', 'f47', 'f48',
               'f50', 'f51', 'f52', 'f53', 'f54', 'f55', 'f56', 'f57', 'f58', 'f60', 'f61', 'f62', 'f63', 'f64', 'f65',
               'f66', 'f67', 'f68', 'f70', 'f71', 'f72', 'f73', 'f74', 'f75', 'f76', 'f77', 'f78', 'f80', 'f81', 'f82',
               'f83', 'f84', 'f85', 'f86', 'f87', 'f88']

        data = []
        for cid in ids:
            data.append(soup.find('input', id=cid))

        board = [[0 for x in range(9)] for x in range(9)]

        for ind, dat in enumerate(data):
            try:
                board[ind // 9][ind % 9] = int(dat['value'])
            except:
                pass

        self.grid = board
        self.timer = 0
        self.selected = [0, 0]
        self.load()

    def drawNumbers(self, window, color=BLACK):
        for y, row in enumerate(self.grid):
            for x, num in enumerate(row):
                if num != 0:
                    pos = [x * cellSize + gridPos[0], y * cellSize + gridPos[1]]
                    self.textToScreen(window, str(num), pos, color)

    def drawSelection(self, window, pos):
        pygame.draw.rect(window, LOCKED if pos in self.lockedCells else ORANGE, ((pos[0] * cellSize) + gridPos[0], (pos[1] * cellSize) + gridPos[1], cellSize, cellSize))

    def drawGrid(self, window):
        pygame.draw.rect(window, BLACK, (gridPos[0], gridPos[1], WIDTH-150, HEIGHT-150), 2)

        for x in range(9):
            pygame.draw.line(window, BLACK, (gridPos[0] + x * cellSize, gridPos[1]), (gridPos[0] + x * cellSize, gridPos[1] + 450), 2 if x % 3 == 0 else 1)
            pygame.draw.line(window, BLACK, (gridPos[0], gridPos[1] + x * cellSize), (gridPos[0] + 450, gridPos[1] + x * cellSize), 2 if x % 3 == 0 else 1)

    def mouseOnGrid(self):
        if self.mousePos[0] < gridPos[0] or self.mousePos[1] < gridPos[1]:
            return False
        if self.mousePos[0] > gridPos[0] + gridSize or self.mousePos[1] > gridPos[1] + gridSize:
            return False
        return [(self.mousePos[0] - gridPos[0]) // cellSize, (self.mousePos[1] - gridPos[1]) // cellSize]

    def loadButtons(self):
        self.playingButtons.append(Button(20, 40, WIDTH//7, 40, function=self.solveBoard, color=SOLVE, text="SOLVE"))
        self.playingButtons.append(Button(140, 40, WIDTH//7, 40, function=self.getPuzzle, color=EASY, parameters="1", text="Easy"))
        self.playingButtons.append(Button(WIDTH//2-(WIDTH//7)//2, 40, WIDTH//7, 40, function=self.getPuzzle, color=MEDIUM, parameters="2", text="Medium"))
        self.playingButtons.append(Button(380, 40, WIDTH//7, 40, function=self.getPuzzle, color=HARD, parameters="3", text="Hard"))
        self.playingButtons.append(Button(500, 40, WIDTH // 7, 40, function=self.getPuzzle, color=EXPERT, parameters="4", text="Expert"))
        self.playingButtons.append(Button(450, 560, WIDTH // 8, 30, function=self.toggleCheck, color=CHECK_ON, text="Check: On"))
        self.playingButtons.append(Button(350, 560, WIDTH // 8, 30, function=self.clearBoard, color=CLEAR, text="Clear"))


    def textToScreen(self, window, text, pos, color=BLACK):
        font = self.font.render(text, False, color)
        fontWidth = font.get_width()
        fontHeight = font.get_height()
        pos[0] += (cellSize - fontWidth) // 2
        pos[1] += (cellSize - fontHeight) // 2
        window.blit(font, pos)

    def load(self):
        self.playingButtons = []
        self.loadButtons()
        self.lockedCells = []
        self.incorrectCells = []
        self.finished = False

        for y, row in enumerate(self.grid):
            for x, num in enumerate(row):
                if num != 0:
                    self.lockedCells.append([x, y])

    def shadeLockedCells(self, window, locked):
        for cell in locked:
            pygame.draw.rect(window, SILK, (cell[0] * cellSize + gridPos[0], cell[1] * cellSize + gridPos[1], cellSize, cellSize))

    def shadeIncorrectCells(self, window, incorrect):
        for cell in incorrect:
            pygame.draw.rect(window, RED, (cell[0] * cellSize + gridPos[0], cell[1] * cellSize + gridPos[1], cellSize, cellSize))

    def isInt(self, str):
        try:
            int(str)
            return True
        except:
            return False

    def convert(self, s):
        min, sec = divmod(s, 60)
        hour, min = divmod(min, 60)
        return "%d:%02d:%02d" % (hour, min, sec)

    def toggleCheck(self):
        self.check = not self.check

        if self.check:
            self.playingButtons[5].text = "Check: On"
            self.playingButtons[5].color = CHECK_ON
        else:
            self.playingButtons[5].text = "Check: Off"
            self.playingButtons[5].color = CHECK_OFF

    def clearBoard(self):
        if not self.finished:
            for x in range(9):
                for y in range(9):
                    if [x, y] not in self.lockedCells:
                        self.grid[y][x] = 0

    def allCellsDone(self):
        for row in self.grid:
            for num in row:
                if num == 0:
                    return False
        return True

    def checkAllCells(self):
        _ = [self.incorrectCells.append([x, y]) for y, row in enumerate(self.grid) for x, num in enumerate(row) if not isPossible(self.grid, num, (y, x)) if num != 0]
        return all([isPossible(self.grid, num, (y, x)) for y, row in enumerate(self.grid) for x, num in enumerate(row)])

    def drawTimer(self, window):
        txt = self.font.render(self.convert(round(self.timer, 2)), True, BLACK if not self.finished else RED)
        window.blit(txt, (75, 560))
        self.dt = self.clock.tick(30) / 1000

    def solveBoard(self):
        self.clearBoard()
        solve(self.grid)

##############################################################

