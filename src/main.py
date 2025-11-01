import random
from termcolor import colored


class TicTacToe:
    """A command-line implementation of the Tic Tac Toe game.

    This class handles the logic and flow of a Tic Tac Toe game,
    allowing the player to either play solo (against the computer)
    or with a friend (two-player mode).

    :param mode: Game mode; either ``'solo'`` for single-player or ``'two-player'`` for two-player mode.
    """

    def __init__(self, mode: str):
        self.mode = mode
        self.board = list(map(str, range(10))) # 0th index is not used
        self.player_turn = self.get_random_first_player()
        self.win_combinations = [
            [1, 2, 3], [4, 5, 6], [7, 8, 9],  # Rows
            [1, 4, 7], [2, 5, 8], [3, 6, 9],  # Columns
            [1, 5, 9], [3, 5, 7]              # Diagonals
        ]
        self.__winner = ''
        self.__loser = ''

    def get_random_first_player(self) -> str:
        """Randomly select which player starts first ('X' or 'O').

        :return: A string representing the player who starts first ('X' or 'O').
        """
        return random.choice(['X', 'O'])

    def show_board(self):
        """Display the current state of the game board in a 3x3 grid format.
        """
        print()
        print(colored(f" {self.board[1]} | {self.board[2]} | {self.board[3]} ", color= 'white', on_color= 'on_light_magenta'))
        print(colored("---+---+---", color= 'white', on_color= 'on_light_magenta'))
        print(colored(f" {self.board[4]} | {self.board[5]} | {self.board[6]} ", color= 'white', on_color= 'on_light_magenta'))
        print(colored("---+---+---", color= 'white', on_color= 'on_light_magenta'))
        print(colored(f" {self.board[7]} | {self.board[8]} | {self.board[9]} ", color= 'white', on_color= 'on_light_magenta'))
        print()

    def fix_spot(self, spot: int, player: str):
        """Place the player's mark on the chosen spot of the board.

        :param spot: The position (1-9) on the board where the player wants to place their mark.
        :param player: The player's mark ('X' or 'O').
        """
        self.board[spot] = player

    def has_player_won(self, player: str) -> bool:
        """Check whether the given player has won the game.

        :param player: The player's mark ('X' or 'O') to check for a win.
        :return: True if the player wins, otherwise False.
        """

        return any((all((self.board[i] == player for i in combo)) for combo in self.win_combinations))

    def is_board_filled(self) -> bool:
        """Determine if the game board is completely filled.

        :return: True if all spots are taken, otherwise False.
        """
        return not any([i.isdigit() for i in self.board[1:]])

    def swap_player_turn(self):
        """Switch the current player's turn between 'X' and 'O'.
        """
        self.player_turn = 'X' if self.player_turn == 'O' else 'O'

    def find_best_move(self, player):
        for combo in self.win_combinations:
            if sum([i for i in combo if self.board[i] == player]):
                return [i for i in combo if self.board[i].isdigit()].pop()
        return None

    def get_computer_choice(self, computer: str, valid_options: list) -> int:
        """Determines the computer's next move in the Tic-Tac-Toe game.

        The method first checks if the computer can win in the current turn by completing
        any of the winning combinations. If not, it checks whether the user is about to win
        and blocks that move. If neither condition applies, it selects a random available option.

        :param computer: Symbol representing the computer player (e.g., 'X' or 'O').
        :param valid_options: List of available cell positions where a move can be made.
        :return: The index (position) of the cell where the computer will place its symbol.
        """
        user = 'X' if computer == 'O' else 'O'

        # Try to win
        move = self.find_best_move(computer)
        if move:
            return move

        # Block user
        move = self.find_best_move(user)
        if move:
            return move

        # Random move
        return random.choice(valid_options)

    def get_user_symbol(self) -> str:
        """Ask the user to choose their preferred symbol ('X' or 'O').

        Handles invalid input and allows '0' as an alternative for 'O'.

        :return: The user's chosen symbol ('X' or 'O').
        """
        while True:
            user = input("\nWhich would you like to be? 'X' or 'O' ? ").strip().upper()
            if user not in {'X', 'O', '0'}:
                print('Invalid input!')
                continue
            elif user == '0':
                user = 'O'
            break
        print(colored(f'You are {repr(user)}', color= 'white', on_color= 'on_light_cyan'))
        return user

    def get_move(self, valid_options: list, user2: str) -> int:
        """Get the next move depending on the current player and game mode.

        If the mode is 'solo' and it's the computer's turn,
        it automatically selects a move using the computer's strategy.
        Otherwise, it asks the human player for input.

        :param valid_options: List of currently available positions.
        :param user2: Symbol of the second player (or computer).
        :return: The chosen position (1-9) as an integer.
        """
        while True:
            if self.mode == 'solo' and self.player_turn == user2:
                spot = self.get_computer_choice(user2, valid_options)
            else:
                spot = input('\nChoose a spot: ')
            try:
                spot = int(spot)
            except ValueError:
                print('Invalid input! Input must be an integer between 1 and 9.')
                continue
            if not (1 <= spot <= 9):
                print('Invalid input! Input must be between 1 and 9.')
                continue
            elif not (spot in valid_options):
                print(f'Invalid input!\nValid options: {", ".join(map(str, valid_options))}')
                continue
            break
        return spot

    def determine_winner(self, user1: str, user2: str) -> str:
        """Determine the winner of the current Tic Tac Toe game and store it internally.

        This method checks if either player has won the game. For solo mode,
        it will return 'You' if the human player wins or 'Computer' if the computer wins.
        In two-player mode, it returns the winning player's symbol ('X' or 'O').
        If there is no winner yet, the internal winner remains an empty string.

        :param user1: Symbol of the first player (or human in solo mode).
        :param user2: Symbol of the second player (or computer in solo mode).
        """
        if self.has_player_won(user1):
            self.__winner = 'You' if self.mode == 'solo' else user1
            self.__loser = 'Computer' if self.mode == 'solo' else user2

        elif self.has_player_won(user2):
            self.__winner = 'Computer' if self.mode == 'solo' else user2
            self.__loser = 'You' if self.mode == 'solo' else user1

    def get_scores(self) -> dict:
        """
        Return a dictionary containing scores based on who won the round.

        :return: :return: A dictionary mapping player names to their score for this round (1 for winner, 0 for loser).
        """
        if self.__winner and self.__loser:
            return {self.__winner: 1, self.__loser: 0}
        else:
            if self.mode == 'solo':
                return {'You': 0, 'Computer': 0}
            else:
                return {'X': 0, 'O': 0}

    def show_result(self, user1: str, user2: str):
        """Display the final result of the game.

        Prints a congratulatory message for the winner or
        announces a draw if the board is filled without a winner.

        :param user1: Symbol of the first player.
        :param user2: Symbol of the second player (or computer).
        """
        self.determine_winner(user1, user2)

        if not self.__winner:
            print(colored('Game over!\nThis game had no winner!', color= 'white', on_color= 'on_dark_grey'))
        elif self.__winner == 'Computer':
            print(colored('Oh, no!😟\nThe computer won!', color= 'white', on_color= 'on_red'))
        else:
            print(colored(f'🎉Congratulations!\n{repr(self.__winner)} won!', color= 'white', on_color= 'on_light_green'))

    def start(self):
        """Start and control the flow of the Tic Tac Toe game.

        Handles the main game loop — alternating turns between players,
        validating moves, updating the board, and checking for a winner
        until the game concludes.
        """
        user1 = self.get_user_symbol() if self.mode == 'solo' else self.player_turn
        user2 = 'X' if user1 == 'O' else 'O'

        print(f'\n{repr(self.player_turn)} starts first!')

        while not any([self.is_board_filled(), self.has_player_won(user1), self.has_player_won(user2)]):
            valid_options = [i for i in range(1, 10) if self.board[i].isdigit()]

            print(f"\nIt's {self.player_turn}'s turn.")
            self.show_board()

            spot = self.get_move(valid_options, user2)
            self.fix_spot(spot, self.player_turn)
            print(f'\n{repr(self.player_turn)} chose spot {spot}!')

            self.swap_player_turn()

        self.show_board()
        self.show_result(user1, user2)


if __name__ == '__main__':
    # Play the game once
    game = TicTacToe(mode= 'solo')
    game.start()
