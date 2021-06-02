

class GameMenu:
    def __init__(self, game):
        self.game = game

    def main_menu(self):
        print('Connect 4 AI Program')
        print('====================')
        print('a) human vs. AI')
        print('b) AI vs. AI')
        choice = input('Enter game mode: ')
        choice = choice.lower()
        if choice == 'a':
            self.human_vs_ai()
        elif choice == 'b':
            self.ai_vs_ai()
        else:
            print(f'Please enter either a or b, {choice} isn\'t a valid entry!')
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
        self.game.heuristic_player2 = self.heuristic_selection()

    def ai_vs_ai(self):
        print('| AI Player 1 |')
        self.game.heuristic_player1 = self.heuristic_selection()
        print('| AI Player 2 |')
        self.game.heuristic_player2 = self.heuristic_selection()