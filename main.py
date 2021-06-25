import pygame
from checkers.constants import *
from checkers.board import Board
from checkers.menu import Menu
from checkers.game import Game
from minimax.algorithm import minimax

pygame.init()

# frame refresh rate
FPS = 60

# creating a window for our game
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Checkers')


def get_row_col_from_mouse(pos):
    x, y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col


def main():
    run = True
    clock = pygame.time.Clock()
    game = Game(WIN)
    menu = Menu(WIN)
    Mode = None

    while run:
        # setting refresh rate..
        clock.tick(FPS)

        if Mode and game.winner() != None:
            print({True: "RED", False: "GREEN"}[
                game.winner() == RED] + " WON!!")
            font = pygame.font.Font('freesansbold.ttf', 32)
            text = font.render({True: "RED", False: "GREEN"}[
                               game.winner() == RED] + " WON!!", True, BLACK, WHITE)
            textRect = text.get_rect()
            textRect.center = (WIDTH // 2, WIDTH // 2)
            WIN.fill(WHITE)
            WIN.blit(text, textRect)
            pygame.display.update()
            pygame.time.delay(5000)
            run = False
        if (Mode == 2 or Mode == 3) and game.turn == GREEN:
            value, new_board = minimax(
                game.get_board(), 5, True, game, float('-inf'), float('+inf'))
            pygame.time.delay(1000)
            game.ai_move(new_board)

        if Mode == 3 and game.turn == RED:
            value, new_board = minimax(
                game.get_board(), 5, False, game, float('-inf'), float('+inf'))
            pygame.time.delay(1000)
            game.ai_move(new_board)

        # setting event loop and checking which event happens
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if Mode == None:
                    Mode = menu.selected_mode(pos)
                    print("Selected Mode: "+str(Mode))

                if Mode == 1 or Mode == 2:
                    row, col = get_row_col_from_mouse(pos)
                    game.select(row, col)
        if Mode:
            game.update()

    pygame.quit()


main()
