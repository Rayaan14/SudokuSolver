import pygame, sys
from settings import *
from buttons import *

class App:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((WIDTH, HEIGHT))
        self.running = True
        self.grid = testBoard2
        self.selected = None
        self.mousePos = None
        self.state = "Playing"
        self.font = pygame.font.SysFont(font, cellSize // 2)
        self.playingButtons = []
        self.menuButtons = []
        self.endButtons = []
        self.lockedCells = []
        self.load()

    def run(self):
        while self.running:
            if self.state == "Playing":
                self.playingEvents()
                self.playingUpdate()
                self.playingDraw()
        pygame.quit()
        sys.exit()

########## PLAYING STATE FUNCTIONS ##########

    def playingEvents(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                selected = self.mouseOnGrid()
                if selected:
                    self.selected = selected
                else:
                    self.selected = None
            if event.type == pygame.KEYDOWN:
                if self.selected is not None and list(self.selected) not in self.lockedCells:
                    if self.isInt(event.unicode):
                        self.grid[self.selected[1]][self.selected[0]] = int(event.unicode)

    def playingUpdate(self):
        self.mousePos = pygame.mouse.get_pos()

        for button in self.playingButtons:
            button.update(self.mousePos)

    def playingDraw(self):
        self.window.fill(WHITE)

        for button in self.playingButtons:
            button.draw(self.window)

        if self.selected:
            self.drawSelection(self.window, self.selected)

        self.shadeLockedCells(self.window, self.lockedCells)

        self.drawNumbers(self.window)

        self.drawGrid(self.window)
        pygame.display.update()

########## HELPER FUNCTIONS ##########

    def drawNumbers(self, window):
        for y, row in enumerate(self.grid):
            for x, num in enumerate(row):
                if num != 0:
                    pos = [x * cellSize + gridPos[0], y * cellSize + gridPos[1]]
                    self.textToScreen(window, str(num), pos)

    def drawSelection(self, window, pos):
        pygame.draw.rect(window, LIGHTORANGE, ((pos[0] * cellSize) + gridPos[0], (pos[1] * cellSize) + gridPos[1], cellSize, cellSize))

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
        return (self.mousePos[0] - gridPos[0]) // cellSize, (self.mousePos[1] - gridPos[1]) // cellSize

    def loadButtons(self):
        self.playingButtons.append(Button(20, 40, 100, 40))

    def textToScreen(self, window, text, pos, color=BLACK):
        font = self.font.render(text, False, color)
        fontWidth = font.get_width()
        fontHeight = font.get_height()
        pos[0] += (cellSize - fontWidth) // 2
        pos[1] += (cellSize - fontHeight) // 2
        window.blit(font, pos)

    def load(self):
        self.loadButtons()

        # Setting locked cells
        for y, row in enumerate(self.grid):
            for x, num in enumerate(row):
                if num != 0:
                    self.lockedCells.append([x, y])

    def shadeLockedCells(self, window, locked):
        for cell in locked:
            pygame.draw.rect(window, CORNSILK, (cell[0] * cellSize + gridPos[0], cell[1] * cellSize + gridPos[1], cellSize, cellSize))

    def isInt(self, str):
        try:
            int(str)
            return True
        except:
            return False







