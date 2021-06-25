import pygame
from .constants import *


class Piece:
    PADDING = 15
    OUTLINE = 2

    def __init__(self, row, col, color) -> None:
        self.row = row
        self.col = col
        self.color = color
        self.king = False
        self.x = 0
        self.y = 0
        self.calc_position()

    def calc_position(self):
        self.x = SQUARE_SIZE*self.col + SQUARE_SIZE//2
        self.y = SQUARE_SIZE*self.row + SQUARE_SIZE//2

    def make_king(self):
        self.king = True

    def move(self, row, col):
        self.row = row
        self.col = col
        self.calc_position()

    def draw(self, window):
        radius = SQUARE_SIZE//2 - self.PADDING
        king_radius = radius//2
        pygame.draw.circle(window, GREY,
                           (self.x, self.y), radius+self.OUTLINE)
        pygame.draw.circle(window, self.color, (self.x, self.y), radius)
        if self.king:
            pygame.draw.circle(window, YELLOW,
                               (self.x, self.y), king_radius)

    def __repr__(self):
        return str(self.color)
