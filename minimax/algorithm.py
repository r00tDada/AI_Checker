from copy import deepcopy
import pygame

RED = (255, 0, 0)
GREEN = (0, 255, 0)


def minimax(position, depth, max_player, game, alpha, beta):

    if depth == 0 or position.winner() != None:
        return position.heurestic_score(), position

    if max_player:
        maxEval = float('-inf')
        best_move = None

        for move in get_all_moves(position, GREEN, game):
            evalution = minimax(move, depth-1, False, game, alpha, beta)[0]
            maxEval = max(maxEval, evalution)

            if maxEval == evalution:
                best_move = move

            alpha = max(alpha, maxEval)
            if beta <= alpha:
                maxEval = float('+inf')
                break

        return maxEval, best_move
    else:
        minEval = float('+inf')
        best_move = None

        for move in get_all_moves(position, RED, game):
            evalution = minimax(move, depth-1, True, game, alpha, beta)[0]
            minEval = min(minEval, evalution)

            if minEval == evalution:
                best_move = move

            beta = min(beta, minEval)
            if beta <= alpha:
                minEval = float('-inf')
                break

        return minEval, best_move


def simulate_move(piece, move, board, game, skip):
    board.move(piece, move[0], move[1])
    if skip:
        board.remove(skip)
    return board


def get_all_moves(board, color, game):

    moves = []
    for piece in board.get_all_pieces(color):
        valid_moves = board.get_valid_moves(piece)
        for move, skip in valid_moves.items():
            # draw_moves(game, board, piece)
            temp_board = deepcopy(board)
            tmp_piece = temp_board.get_peice(piece.row, piece.col)
            new_board = simulate_move(tmp_piece, move, temp_board, game, skip)
            moves.append(new_board)

    return moves


def draw_moves(game, board, piece):
    valid_moves = board.get_valid_moves(piece)
    board.draw(game.window)
    pygame.draw.circle(game.window, (138, 43, 226), (piece.x, piece.y), 30, 5)
    game.draw_valid_moves(valid_moves.keys())
    pygame.display.update()
    # pygame.time.delay(100)
