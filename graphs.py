import matplotlib.pyplot as plt
import config
import Game

N_ROUNDS = 60
N_GAMES = 50

def test_radius_opponent_value():
    percentage_won_list = []
    opponent_values = []

    heuristic_black = 'radius'
    heuristic_red = 'consecutive'

    for i in range(N_ROUNDS):
        player1_score = 0
        player2_score = 0
        drawn = 0
        opponent_value = -3 + 0.1*i
        opponent_values.append(opponent_value)
        for j in range(N_GAMES):
            game = Game.Game()
            winner = False
            game.animate = False
            game.heuristic_black = heuristic_black
            game.heuristic_red = heuristic_red
            game.opponent_value = opponent_value
            moves = 0
            while not winner and moves < 200:
                move = game.Alpha_Beta_Search(game.board)
                winner = game.play_move(move)
                moves += 1
            if winner == config.BLACK:
                player1_score += 1
            elif winner == config.RED:
                player2_score += 1
            else:
                drawn += 1
        percentage_won_list.append(100 * player1_score / (player1_score + player2_score))

    print(opponent_values)
    print(percentage_won_list)
    graph(opponent_values, percentage_won_list, "Opponent Value", "Percentage Won (%)", "Radius Wins with Varying Opponent Values")


# graph the given info
def graph(x_data, y_data, x_label, y_label, title):
    plt.plot(x_data, y_data)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title)
    plt.show()

