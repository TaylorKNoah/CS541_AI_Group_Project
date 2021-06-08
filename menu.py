from Game import Game


class GameMenu:
    def __init__(self, game):
        self.game = game

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
        self.game.heuristic_red = self.heuristic_selection()
        self.game.print_board()
        while not winner:
            if players_turn:
                move = int(input('Enter a column to play (0-6): '))
            else:
                move = self.game.Alpha_Beta_Search(self.game.board)
            players_turn = not players_turn
            if move < 0 or move > 6:
                print('Not a valid move. Try again.')
            else:
                winner = self.game.play_move(move)

    def ai_vs_ai(self):
        print('| AI Player 1 |')
        self.game.heuristic_black = self.heuristic_selection()
        print('| AI Player 2 |')
        self.game.heuristic_red = self.heuristic_selection()

        winner = False
        self.game.print_board()

        while not winner:

            move = self.game.Alpha_Beta_Search(self.game.board)

            if move < 0 or move > 6:
                print('Not a valid move. Try again.')
            else:
                winner = self.game.play_move(move)

    def evaluation(self):
        winner = False
        blacks_turn = True
        player1_score = 0
        player2_score = 0

        print('| AI Player 1 |')
        self.game.heuristic_black = self.heuristic_selection()
        print('| AI Player 2 |')
        self.game.heuristic_red = self.heuristic_selection()

        print('Playing 5,000 games of AI vs. AI')
        print('[', end='')
        for i in range(5000):
            game = Game()
            game.animate = False
            if i % 100 == 0:
                print('=', end='')
            while not winner:
                move = game.Alpha_Beta_Search(game.board)
                winner = game.play_move(move)
                blacks_turn = not blacks_turn

            if blacks_turn:
                player2_score += 1
            else:
                player1_score += 1
            winner = False
        print(']')
        print(f'AI Player 1 won {player1_score / 5000} of the time')
        print(f'AI Player 2 won {player2_score / 5000} of the time')
