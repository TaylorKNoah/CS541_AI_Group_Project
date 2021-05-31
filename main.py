import Game
import utility
import config
import tests


def main():
    """
    # play a game of up to 50 random moves, and stop once there's a winner.
    game = Game.Game()
    for i in range(50):
        winner = game.random_move()
        if winner:
            print("Winner: ", end="")
            print(winner)
            break
    if not winner:
        print("Cat's game.")
    """
    # run the heuristic tests
    tests.heuristic_tests()


if __name__ == "__main__":
    main()
furthest_down = 0
