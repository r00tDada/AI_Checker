import pygame
from checkers.constants import *


class Menu:
    def __init__(self, WIND):
        self.WIND = WIND
        self.draw_menu()

    def draw_menu(self):
        font = pygame.font.Font('freesansbold.ttf', 32)
        pygame.draw.rect(self.WIND, WHITE, (170, 150, 300, 60))
        text = font.render(" Human vs Human ", True, BLACK, WHITE)
        textRect = text.get_rect()
        textRect.center = (320, 180)
        self.WIND.blit(text, textRect)

        pygame.draw.rect(self.WIND, WHITE, (170, 250, 300, 60))
        text = font.render(" Human vs AI ", True, BLACK, WHITE)
        textRect = text.get_rect()
        textRect.center = (320, 280)
        self.WIND.blit(text, textRect)

        pygame.draw.rect(self.WIND, WHITE, (170, 350, 300, 60))
        text = font.render(" AI vs AI ", True, BLACK, WHITE)
        textRect = text.get_rect()
        textRect.center = (320, 380)
        self.WIND.blit(text, textRect)

        pygame.display.update()

    def selected_mode(self, pos):

        x, y = pos
        if x >= 170 and x <= 470 and y >= 150 and y <= 210:
            return 1
        if x >= 170 and x <= 470 and y >= 250 and y <= 310:
            return 2
        if x >= 170 and x <= 470 and y >= 350 and y <= 410:
            return 3
        return None
