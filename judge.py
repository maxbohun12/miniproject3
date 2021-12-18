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


def judge_chosen_two(strategies, maps) -> None:
    pass


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
