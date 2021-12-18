import random


def first_strategy(plateau, available_moves, player):
    if len(available_moves) == 0:
        raise EOFError
    return available_moves[0][0]
