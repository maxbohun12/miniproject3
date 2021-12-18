import random


def random_strategy(plateau, available_moves, player):
    if len(available_moves) == 0:
        raise EOFError
    return random.choice(available_moves)[0]
