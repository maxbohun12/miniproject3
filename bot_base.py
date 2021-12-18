"""
    This is an example of a bot for the 3rd project.
    ...a pretty bad bot to be honest -_-
"""
import sys
from logging import ERROR, debug, getLogger

getLogger().setLevel(ERROR)


def dist(x1, y1, x2, y2):
    """
    >>> dist(1,1,3,3)
    2.8284271247461903
    Measure the distance between two points
    :param x1: X coordinate of the opponent's figure
    :param y1: Y coordinate of the opponent's figure
    :param x2: X coordinate of the newly placed figure
    :param y2: Y coordinate of the newly placed figure
    :return: distance between two points
    """
    return ((int(x2)-int(x1))**2 + (int(y2)-int(y1))**2)**0.5


def dominance(plateau, player, i, j):
    """
    Get as close as possible to the opponent.
    Measures the distance from the newly placed figure
    to the closest opponent's figure.
    :param plateau: The plateau with the newly placed figure
    :param i: X coordinate of the newly placed figure
    :param player: Number of player
    :param j: Y coordinate of the newly placed figure
    :return: distance from the newly placed figure to the
    closest opponent's figure.
    """
    distances = []
    notmine = ("O" if player == 2 else "X")
    for string in range(len(plateau)):
        for elem in range(len(plateau[string])):
            if plateau[string][elem] == notmine:
                distances.append(dist(int(i), int(j), string, elem))
    return min(distances)


def check_available_moves(plateau: list, figure: list, player: int, heigth: int, width: int):
    """
    This function returns all of the possible ways to place a figure on a plateau
    :param plateau: The current game plateau
    :param figure: The figure we have to place
    :param player: Number of player
    :param heigth: Height of the plateau
    :param width: Width of the plateau
    :return: A list of possible moves and the number
    of player's figures on the field
    """
    opp_count = 0
    my_count = 0
    for i in range(len(plateau)):
        plateau[i] = plateau[i].replace('x', 'X').replace('o', 'O')
        opp_count += plateau[i].count("O" if player == 2 else "X")
        my_count += plateau[i].count("O" if player == 1 else "X")
    possible = []
    for i in range(1, heigth + 2 - len(figure)):
        for j in range(4, len(plateau[1]) - len(figure[0]) + 1):
            total_O = 0
            total_X = 0
            for fi, line in enumerate(figure):
                for fj, char in enumerate(line):
                    if char == '*':
                        if plateau[i + fi][j + fj] == 'X':
                            total_X += 1
                        elif plateau[i + fi][j + fj] == 'O':
                            total_O += 1
            good = False
            if player == 1:
                if total_O == 1 and total_X == 0:
                    good = True
            if player == 2:
                if total_O == 0 and total_X == 1:
                    good = True
            if good:
                distance = dominance(plateau, player, i-1, j-4)
                possible.append(tuple(((i - 1, j - 4), distance)))
    return possible


def parse_field_info():
    """
    Parse the info about the field.

    The input may look like this:

    Plateau 15 17:
    """
    info = input()
    width = info[:-1].split()[-1]
    height = info.split()[-2]
    debug(f"Description of the field: {info}")
    return height, width


def parse_field(player: int, height, width):
    """
    Parse the field.

    The input may look like this:

        01234567890123456
    000 .................
    001 .................
    002 .................
    003 .................
    004 .................
    005 .................
    006 .................
    007 ..O..............
    008 ..OOO............
    009 .................
    010 .................
    011 .................
    012 ..............X..
    013 .................
    014 .................

    :param player: Represents whether we're the first or second player
    """
    plateau = []
    for i in range(height + 1):
        line = input()
        plateau.append(line)
    return plateau


def parse_figure():
    """
    Parse the figure.

    The function parses the height of the figure and then reads it.

    The input may look like this:

    Piece 2 2:
    **
    ..
    """
    l = input()
    debug(f"Piece: {l}")
    fig_height = int(l.split()[-2])
    figure = []
    for _ in range(fig_height):
        l = input()
        figure.append(l)
        debug(f"Piece: {l}")
    return figure


def floor(plateau, player):
    """
    Returns True if player should
    be moving towards the floor of the
    plateau and False otherwise
    :param plateau: The current game field
    :param player: Number of player
    :return: True if player should move towards the floor else False
    """
    for i in range(1, 3):
        if ("O" if player == 1 else "X") in plateau[-i]:
            return False
    return True


def ceiling(plateau, player):
    """Returns True if player should
    be moving towards the ceiling of the
    plateau and False otherwise
    :param plateau: The current game field
    :param player: Number of player
    :return: True if player should move towards the top else False
    """
    for i in range(3):
        if ("O" if player == 1 else "X") in plateau[i]:
            return False
    return True


def step(player: int, strategy):
    """
    Perform one step of the game.
    The strategy is simple:
    1. If the top of the plateau isn't yet filled with out figures, we move towards it.
    2. If the top is filled, we move towards the floor.
    3. If the top and the floor is filled, which means we already cut off a piece
    of the field from our opponent, we move as close to him as possible.

    :param player: Represents whether we're the first or second player
    """
    height, width = parse_field_info()
    plateau = parse_field(player, int(height), int(width))
    figure = parse_figure()
    available_moves = check_available_moves(
        plateau, figure, player, int(height), int(width))
    best_move = strategy(plateau, available_moves, player)
    return best_move


def play(player: int, strategy):
    """
    Main game loop.

    :param player: Represents whether we're the first or second player
    """
    while True:
        move = step(player, strategy)
        print(*move)


def parse_info_about_player():
    """
    This function parses the info about the player

    It can look like this:

    $$$ exec p2 : [./player1.py]
    """
    i = input()
    debug(f"Info about the player: {i}")
    return 1 if "p1 :" in i else 2


def main(strategy):
    player = parse_info_about_player()
    try:
        play(player, strategy)
    except EOFError:
        debug("Cannot get input. Seems that we've lost ):")
