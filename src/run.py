from main import TicTacToe
from termcolor import colored


def get_mode():
    print("\nChoose a mode:\n")
    while True:
        print("1. Solo (Play with computer)")
        print("2. With a friend")

        choice = input("\nEnter 1 or 2: ").strip()
        if choice not in {'1', '2', ''}:
            print('Invalid input!')
            continue
        break

    return 'solo' if choice in {'1', ''} else 'two-player'


def run():
    """Run the Tic Tac Toe game.

    This function initializes and manages the main game loop.
    It starts a new Tic Tac Toe game, handles replay logic,
    and gracefully exits when the player chooses to stop.
    """
    scores = {}
    print(colored('Welcome to Tic Tac Toe Game!', color= 'white', on_color= 'on_light_cyan'))

    mode = get_mode()
    while True:
        game = TicTacToe(mode)
        game.start()
        one_round_scores = game.get_scores()

        print(colored('\nCurrent scores: ', color= 'white', on_color= 'on_light_magenta'))

        for player, score in one_round_scores.items():
            scores[player] = scores.get(player, 0) + score

            print(colored(f'    - {player}: {score}', color= 'white', on_color= 'on_light_magenta'))

        while True:
            print('\nWould you like to play again?\n')
            print('1. Play again in the same mode.')
            print('2. Play again and change mode.')
            print('3. Quit')
            replay = input('Enter 1, 2 or 3: ').strip()
            if replay not in {'1', '2', '3'}:
                print('Invalid input!')
                continue
            break

        if replay == '1':
            continue
        elif replay == '2':
            scores.clear()
            mode = 'solo' if mode == 'two-player' else 'two-player'
            continue

        else:
            print(colored('Thank you for playing!', color= 'white', on_color= 'on_light_blue'))
            print(colored('\nFinal scores: ', color= 'white', on_color= 'on_light_blue'))
            for player, score in scores.items():
                print(colored(f'    - {player}: {score}', color= 'white', on_color= 'on_light_blue'))
            print(colored('\nGood bye!', color= 'white', on_color= 'on_light_blue'))
            break


if __name__ == '__main__':
    run()
