import pygame, sys
from settings import *
from buttons import *

class App:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((WIDTH, HEIGHT))
        self.running = True
        self.grid = testBoard
        self.selected = None
        self.mousePos = None
        self.state = "Playing"
        self.playingButtons = []
        self.menuButtons = []
        self.endButtons = []
        self.loadButtons()

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
        self.drawGrid(self.window)
        pygame.display.update()

########## HELPER FUNCTIONS ##########

    def drawSelection(self, window, pos):
        pygame.draw.rect(window, LIGHTORANGE, ((pos[0] * cellSize) + gridPos[0], (pos[1] * cellSize) + gridPos[1],
                                             cellSize, cellSize))

    def drawGrid(self, window):
        pygame.draw.rect(window, BLACK, (gridPos[0], gridPos[1], WIDTH-150, HEIGHT-150), 2)
        # vertical lines
        for x in range(9):
            if x % 3 == 0:
                pygame.draw.line(window, BLACK, (gridPos[0] + x * cellSize, gridPos[1]),
                                 (gridPos[0] + x * cellSize, gridPos[1] + 450), 2)
            else:
                pygame.draw.line(window, BLACK, (gridPos[0] + x * cellSize, gridPos[1]),
                                 (gridPos[0] + x * cellSize, gridPos[1]+450))
        # horizontal lines
        for x in range(9):
            if x % 3 == 0:
                pygame.draw.line(window, BLACK, (gridPos[0], gridPos[1] + x * cellSize),
                                 (gridPos[0] + 450, gridPos[1] + x * cellSize), 2)
            else:
                pygame.draw.line(window, BLACK, (gridPos[0], gridPos[1] + x * cellSize),
                                 (gridPos[0] + 450, gridPos[1] + x * cellSize))

    def mouseOnGrid(self):
        if self.mousePos[0] < gridPos[0] or self.mousePos[1] < gridPos[1]:
            return False
        if self.mousePos[0] > gridPos[0] + gridSize or self.mousePos[1] > gridPos[1] + gridSize:
            return False
        return (self.mousePos[0] - gridPos[0]) // cellSize, (self.mousePos[1] - gridPos[1]) // cellSize

    def loadButtons(self):
        self.playingButtons.append(Button(20, 40, 100, 40))

