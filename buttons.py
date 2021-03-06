##############################################################
import pygame
from settings import *
##############################################################


class Button:
##############################################################
    def __init__(self, x, y, width, height, text=None, color=(53, 72, 94), highlightedColor=(255, 235, 240), function=None, parameters=None):
        self.image = pygame.Surface((width, height))
        self.pos = (x, y)
        self.rect = self.image.get_rect()
        self.rect.topleft = self.pos
        self.text = text
        self.color = color
        self.highlightedColor = highlightedColor
        self.function = function
        self.parameters = parameters
        self.highlighted = False
        self.width = width
        self.height = height
##############################################################

#################### HELPER FUNCTIONS ########################

    def update(self, mouse):
        if self.rect.collidepoint(mouse):
            self.highlighted = True
        else:
            self.highlighted = False

    def draw(self, window):
        self.image.fill(self.highlightedColor if self.highlighted else self.color)
        if self.text:
            self.drawText(self.text)
        window.blit(self.image, self.pos)

    def click(self):
        if self.parameters:
            self.function(self.parameters)
        else:
            self.function()

    def drawText(self, text):
        font = pygame.font.SysFont(txtFont, 15 if self.pos == (450, 560) else 20, bold=1)
        text = font.render(text, False, BLACK)
        width, height = text.get_size()
        x = (self.width - width)//2
        y = (self.height - height)//2
        self.image.blit(text, (x, y))

##############################################################
