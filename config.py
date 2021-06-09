# size of the game board
WIDTH = 7
HEIGHT = 6

# characters for the game pieces
RED = "X"
BLACK = "O"
EMPTY = "."

# how many in a row needed to win
CONNECT_N = 4

# practical positive and negative infinities
INF = 1000000
NINF = -1000000

# epsilon value for exploration moves
# currently at 10%
EPSILON = 0.13
DEPTH = 2
RMOVES = 0

# radius heuristic constants
# how big the radius is for the radius heuristic
RADIUS = 2
SAME_COLOR_SCORE = 10
EMPTY_SQUARE_SCORE = 2
OPPONENT_COLOR_SCORE = -10
OPPONENT_VALUE = -1.3


# consecutive heuristic constants
MAX_SCORE = 1000
THREE_SCORE = 20
TWO_SCORE = 5
OPPONENT_THREE_SCORE = -40
OPPONENT_TWO_SCORE = -6

# how many evaluation games to play
N_EVALUATION_GAMES = 500
