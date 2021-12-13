#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    This is an example of a bot for the 3rd project.
    ...a pretty bad bot to be honest -_-
"""

from logging import DEBUG, debug, getLogger
import random
# We use the debugger to print messages to stderr
# You cannot use print as you usually do, the vm would intercept it
# You can however do the following:
#
# import sys
# print("HEHEY", file=sys.stderr)

getLogger().setLevel(DEBUG)


# plateau = Figures()
# plateau.height = 10
# plateau.width = 100
# print(plateau.width, plateau.height)
# fig = Figures()
# fig.height = 12
# fig.width = 123
# print(fig.width, fig.height)

def givezero(plateau, new_plateau, player):
    elem = ("O" if player == 1 else "X")
    for i in range(len(plateau)):
        for j in range(len(plateau[0])):
            if plateau[i][j] == elem:
                if new_plateau[i][j] == '.':
                    new_plateau[i] = new_plateau[i][:j] + elem + new_plateau[i][j+1:]
    return new_plateau

def check_available_moves(plateau: list, figure: list, player: int, heigth: int, width: int):
    oldfigs = 0
    opp_count = 0
    my_count = 0
    for i in plateau:
        oldfigs += i.count('.')
        opp_count += i.count("O" if player == 2 else "X")
        my_count += i.count("O" if player == 1 else "X")
    figc = 0
    for i in figure:
        figure[figure.index(i)] = i.replace('.', '@')
        figc += i.count('*')
    possible = []
    for i in range(1, heigth + 1):
        for j in range(3, width + 2):
            newplateau = plateau.copy()
            for f in range(len(figure)):
                if i + f <= len(plateau) - 1:
                    newplateau[i+f] = newplateau[i+f][:j] + figure[f] + newplateau[i+f][j + len(figure[f]):]
                # print(newplateau)
            newplateau = givezero(plateau, newplateau, player)
            newfigs = 0
            new_opp_count = 0
            new_my_count = 0
            for fig in newplateau:
                newfigs += fig.count('.')
                new_opp_count += fig.count("O" if player == 2 else "X")
                new_my_count += fig.count("O" if player == 1 else "X")
            if new_opp_count == opp_count and new_my_count == my_count - 1:
                # print(plateau)
                # print(newplateau, j-4, i-1)
                possible.append(tuple((i, j - 4)))
    return possible

# print(check_available_moves(['     01234567890123456,' '000 .................','001 .................', '002 .................','003 .................','004 .................','005 .................','006 .................','007 ..O..............','008 ..OOO............','009 .................','010 .................','011 .................','012 ..............X..','013 .................','014 .................]'], ['..*.','***.'],1, 15, 17,))
def parse_field_info():
    """
    Parse the info about the field.

    However, the function doesn't do anything with it. Since the height of the field is
    hard-coded later, this bot won't work with maps of different height.

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

    First of all, this function is also responsible for determining the next
    move. Actually, this function should rather only parse the field, and return
    it to another function, where the logic for choosing the move will be.

    Also, the algorithm for choosing the right move is wrong. This function
    finds the first position of _our_ character, and outputs it. However, it
    doesn't guarantee that the figure will be connected to only one cell of our
    territory. It can not be connected at all (for example, when the figure has
    empty cells), or it can be connected with multiple cells of our territory.
    That's definitely what you should address.

    Also, it might be useful to distinguish between lowercase (the most recent piece)
    and uppercase letters to determine where the enemy is moving etc.

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

    :param player int: Represents whether we're the first or second player
    """
    # move = None
    plateau = []
    for i in range(height + 1):
        line = input()
        plateau.append(line)
        # debug(f"Field: {l}")
        # if move is None:
        #     c = l.lower().find("o" if player == 1 else "x")
        #     if c != -1:
        #         move = i - 1, c - 4
    # assert move is not None
    return plateau


def parse_figure():
    """
    Parse the figure.

    The function parses the height of the figure (maybe the width would be
    useful as well), and then reads it.
    It would be nice to save it and return for further usage.

    The input may look like this:

    Piece 2 2:
    **
    ..
    """
    l = input()
    debug(f"Piece: {l}")
    fig_height = int(l.split()[-2])
    fig_width = int(l[:-1].split()[-1])
    figure = []
    for _ in range(fig_height):
        l = input()
        figure.append(l)
        debug(f"Piece: {l}")
    return figure


def find_distance(plateau, figure, available_moves):
    pass


def step(player: int):
    """
    Perform one step of the game.

    :param player int: Represents whether we're the first or second player
    """
    height, width = parse_field_info()
    plateau = parse_field(player, int(height), int(width))
    figure = parse_figure()
    available_moves = check_available_moves(plateau, figure, player, int(height), int(width))
    debug(available_moves)
    # best_move = find_distance(plateau, figure, available_moves)
    best_move = random.choice(available_moves)
    debug(best_move)
    return best_move


def play(player: int):
    """
    Main game loop.

    :param player int: Represents whether we're the first or second player
    """
    while True:
        move = step(player)
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


def main():
    player = parse_info_about_player()
    try:
        play(player)
    except EOFError:
        debug("Cannot get input. Seems that we've lost ):")


# if __name__ == "__main__":
#     main()
