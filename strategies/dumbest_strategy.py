def floor(plateau, player):
    """
    Returns True if player should
    be moving towards the floor of the
    plateau and False otherwise
    :param plateau: The current game field
    :param player: Number of player
    :return: True if player should move towards the floor else False
    """
    if ("O" if player == 1 else "X") in plateau[-1]:
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
    for i in range(2):
        if ("O" if player == 1 else "X") in plateau[i]:
            return False
    return True


def dumbest_strategy(plateau, available_moves, player):
    if len(available_moves) == 0:
        raise EOFError()
    if ceiling(plateau, player):
        best_move = available_moves[0][0]
    elif floor(plateau, player):
        best_move = available_moves[-1][0]
    else:
        available_moves.sort(key=lambda x: x[1])
        best_move = available_moves[0][0]
    return best_move
