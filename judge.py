import os


def get_strategies() -> list:
    def filter_func(file: str):
        return file.endswith('.py') and not file.startswith('__init__')
    strategies = list(filter(filter_func, os.listdir('strategies/')))
    strategies = [strat[:-3] for strat in strategies]
    return strategies


def get_maps() -> list:
    maps = os.listdir('maps/')
    return sorted(maps)


def get_bot_filename(strategy_name: str) -> str:
    return f'{strategy_name}_bot.py'


def get_winner() -> str:
    pass


def generate_bot(strategy_name: str) -> None:
    bot_template = ''
    with open('bots/bot_template.py') as fin:
        bot_template = fin.read()

    bot_code = bot_template.replace('REPLACE_ME', strategy_name)
    with open(f'bots/{get_bot_filename(strategy_name)}', 'w') as fout:
        fout.write(bot_code)


def allow_bot_executions() -> None:
    os.system('chmod +x bots/*')


def execute_game(map, p1, p2) -> None:
    os.system(
        f'./filler_vm -f ./maps/{map} \
            -p1 ./bots/{get_bot_filename(p1)} \
            -p2 ./bots/{get_bot_filename(p2)} > out'
    )


def execute_games(map, p1, p2, game_count) -> None:
    print(f'>>> fighting : {p1} vs {p2}')
    for game_id in range(game_count):
        execute_game(map, p1, p2)
        winner = get_winner()
        print(f'> game #{game_id + 1} : {winner} won')
    print('----------------\n')


def select_judge_mode():
    print('select the judge mode:')
    print('[1] fight between two chosen strategies')
    print('[2] fight between one chosen strategy and all the others')
    print('[3] fight between every pair of strategies')
    mi = int(input())
    if mi == 1:
        return judge_chosen_two
    if mi == 2:
        return judge_chosen_one
    if mi == 3:
        return judge_everyone
    raise ValueError(f'No judge mode: {mi}')


def select_from_list(selection_list, select_what):
    if len(selection_list) == 0:
        raise ValueError(f'List of {select_what}s is empty')
    print(f'Select the number of {select_what} from given list:')
    for i, value in enumerate(selection_list):
        print(f'[{i+1}] {value}')
    uinput = int(input('Your selection:'))
    if uinput not in range(1, len(selection_list) + 1):
        raise ValueError(f'{select_what} with #{uinput} does not exist')
    return selection_list[uinput - 1]


def select_strategy(strategies):
    return select_from_list(strategies, 'strategy')


def select_map(maps):
    return select_from_list(maps, 'map')


def judge_chosen_two(strategies, maps) -> None:
    map = select_map(maps)
    p1 = select_strategy(strategies)
    p2 = select_strategy(strategies)
    game_count = int(input('game count : '))
    execute_games(map, p1, p2, game_count)


def judge_chosen_one(strategies, maps) -> None:
    pass


def judge_everyone(strategies, maps) -> None:
    pass


def app():
    # Preparations
    strategies = get_strategies()
    maps = get_maps()
    for strategy in strategies:
        generate_bot(strategy)
    allow_bot_executions()

    # Choose judge mode and execute it
    judge_mode = select_judge_mode()
    judge_mode(strategies, maps)


if __name__ == '__main__':
    try:
        app()
    except Exception as err:
        print(f'JUDGE ERR')
        if (f'{err}'):
            print(f'ERR MSG: {err}')
