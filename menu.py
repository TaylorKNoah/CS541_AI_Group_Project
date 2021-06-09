from Game import Game
from config import N_EVALUATION_GAMES


class GameMenu:
    def __init__(self):
        pass

    def main_menu(self):
        print('Connect 4 AI Program')
        print('====================')
        print('a) human vs. AI')
        print('b) AI vs. AI')
        print('c) Evaluation Mode')
        choice = input('Enter game mode: ')
        choice = choice.lower()
        if choice == 'a':
            self.human_vs_ai()
        elif choice == 'b':
            self.ai_vs_ai()
        elif choice == 'c':
            self.evaluation()
        else:
            print(f'Please enter either a, b, or c {choice} isn\'t a valid entry!')
            self.main_menu()

    def heuristic_selection(self):
        print('Select a heuristic')
        print('==================================')
        print('a) radius - Evaluates status of the board by looking at matching pieces within n. radius')
        print('b) consecutive - Evaluates status of the board by looking at consecutive pieces of the same color')
        choice = input('Enter heuristic mode: ')
        choice = choice.lower()
        if choice == 'a':
            return "consecutive"
        elif choice == 'b':
            return "radius"
        else:
            print(f'Please enter either a or b, {choice} isn\'t a valid entry!')
            self.heuristic_selection()

    def human_vs_ai(self):
        winner = False
        players_turn = True
        game = Game()
        game.heuristic_red = self.heuristic_selection()
        game.print_board()
        while not winner:
            if players_turn:
                move = int(input('Enter a column to play (0-6): '))
            else:
                move = game.Alpha_Beta_Search(game.board)
            players_turn = not players_turn
            if move < 0 or move > 6:
                print('Not a valid move. Try again.')
            else:
                winner = game.play_move(move)

    def ai_vs_ai(self):
        game = Game()
        print('| AI Player 1 |')
        game.heuristic_black = self.heuristic_selection()
        print('| AI Player 2 |')
        game.heuristic_red = self.heuristic_selection()

        winner = False
        game.print_board()

        while not winner:

            move = game.Alpha_Beta_Search(game.board)

            if move < 0 or move > 6:
                print('Not a valid move. Try again.')
            else:
                winner = game.play_move(move)

    def evaluation(self):
        winner = False
        blacks_turn = True
        player1_score = 0
        player2_score = 0

        print('| AI Player 1 |')
        heuristic_black = self.heuristic_selection()
        print('| AI Player 2 |')
        heuristic_red = self.heuristic_selection()

        print('Playing {N_EVALUATION_GAMES} games of AI vs. AI')
        for i in range(N_EVALUATION_GAMES):
            game = Game()
            game.animate = False
            game.heuristic_black = heuristic_black
            game.heuristic_red = heuristic_red
            if i % 100 == 0:
                print(f'{i} games done')
            while not winner:
                move = game.Alpha_Beta_Search(game.board)
                winner = game.play_move(move)
                blacks_turn = not blacks_turn

            if blacks_turn:
                player2_score += 1
            else:
                player1_score += 1
            winner = False
        print(f'AI Player 1 won {100 * player1_score / N_EVALUATION_GAMES}% of the time')
        print(f'AI Player 2 won {100 * player2_score / N_EVALUATION_GAMES}% of the time')
