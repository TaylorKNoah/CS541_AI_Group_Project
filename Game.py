import time
import random
import config

# animation settings
ANIMATE = True
FRAME_LENGTH = 0.01

# practical positive and negative infinities
INF = 1000000
NINF = -1000000

# creates a connect-4 game object
class Game:
    # initialize the board and set it to black's turn
    def __init__(self):
        self.board = []
        self.initialize_board()
        self.blacks_turn = True

        # added this for ABSearch use
        # to keep seperate from actual game turn
        self.abs_black_turn = True

    # set the board to all empty squares
    def initialize_board(self):
        for i in range(config.HEIGHT):
            row = []
            for j in range(config.WIDTH):
                row.append(config.EMPTY)
            self.board.append(row)

    # print the board
    def print_board(self):
        # clear the console
        for i in range(20):
            print()
        # print the board
        for i in range(config.HEIGHT):
            for j in range(config.WIDTH):
                print(self.board[i][j], end=" ")
            print()
        print()

    # big messy function to play a move of whoever's turn it is, and animate its descent
    def play_move(self, column):
        # if this column is full, return False
        if self.board[0][column] != config.EMPTY:
            return False
        # otherwise, set the top square to black or red according to whose turn it is
        else:
            self.board[0][column] = config.BLACK if self.blacks_turn else config.RED

        # now have it slowly fall down the column
        for i in range(1, config.HEIGHT):
            # print the board if we are animating the move
            if ANIMATE:
                # print the board
                self.print_board()
                # sleep to make it animate smoothly
                time.sleep(FRAME_LENGTH)
            # if this space is taken,  switch whose turn it is and return
            if self.board[i][column] != config.EMPTY:
                # switch whose turn it is
                self.blacks_turn = not self.blacks_turn
                self.print_board()
                # return whether this move won or not
                return self.is_it_winning_move(i - 1, column)
            # set this square to black or red according to whose turn it is
            self.board[i][column] = config.BLACK if self.blacks_turn else config.RED
            # delete our piece from the square above
            self.board[i - 1][column] = config.EMPTY
        # if we made it to the bottom row, switch whose turn it is
        self.blacks_turn = not self.blacks_turn
        # print the board as we leave
        self.print_board()
        # return whether the last move won or not
        return self.is_it_winning_move(config.HEIGHT - 1, column)

    # play a random move
    def random_move(self):
        return self.play_move(random.randint(0, config.WIDTH - 1))

    # check if the newest move won the game or not
    def is_it_winning_move(self, row, column):
        piece = self.board[row][column]
        # check for horizontal win
        furthest_right = 0
        while column + furthest_right + 1 < config.WIDTH and self.board[row][column + furthest_right + 1] == piece:
            furthest_right += 1
        furthest_left = 0
        while column + furthest_left - 1 >= 0 and self.board[row][column + furthest_left - 1] == piece:
            furthest_left -= 1
        if furthest_right - furthest_left >= config.CONNECT_N - 1:
            return piece

        # check for vertical win
        furthest_down = 0
        while row + furthest_down + 1 < config.HEIGHT and self.board[row + furthest_down + 1][column] == piece:
            furthest_down += 1
        furthest_up = 0
        while row + furthest_up - 1 >= 0 and self.board[row + furthest_up - 1][column] == piece:
            furthest_up -= 1
        if furthest_down - furthest_up >= config.CONNECT_N - 1:
            return piece

        # check for right-diagonal win
        furthest_down = 0
        while row + furthest_down + 1 < config.HEIGHT \
                and column + furthest_down + 1 < config.WIDTH \
                and self.board[row + furthest_down + 1][column + furthest_down + 1] == piece:
            furthest_down += 1
        furthest_up = 0
        while row + furthest_up - 1 >= 0 \
                and column + furthest_up - 1 >= 0 \
                and self.board[row + furthest_up - 1][column + furthest_up - 1] == piece:
            furthest_up -= 1
        if furthest_down - furthest_up >= config.CONNECT_N - 1:
            return piece

        # check for left-diagonal win
        furthest_down = 0
        while row + furthest_down + 1 < config.HEIGHT \
                and column - furthest_down - 1 >= 0 \
                and self.board[row + furthest_down + 1][column - furthest_down - 1] == piece:
            furthest_down += 1
        furthest_up = 0
        while row + furthest_up - 1 >= 0 \
                and column - furthest_up + 1 < config.WIDTH \
                and self.board[row + furthest_up - 1][column - furthest_up + 1] == piece:
            furthest_up -= 1
        if furthest_down - furthest_up >= config.CONNECT_N - 1:
            return piece

        # if no winner, return None
        return None


    # Minimax algorithm with Alpha Beta Pruning
    def Alpha_Beta_Search(self, state, utility_func):

        # gets the optimal value of all possible moves
        optimal_value = self.Max_Value(state, INF, NINF)

        # gets available actions
        actions = self.Actions(state)

        # searchs current possibles actions for value equal to optimal
        # if action is legal then this checks to see if it generates the optimal value
        # once found, save the index of the action (aka the column to use)
        for i in range(WIDTH):
            if actions[i] and  optimal_value == utility_func(self.Result(state, actions[i])):
                return i

    # uses game state to determine valid move
    # valid move: there is space in the column at index i
    # returns a boolean list
    def Actions(self, state):
        actions = []
        for i in range(WIDTH):
            if state[0][i] != EMPTY:
                actions.append(False)
            else:
                actions.append(True)

        return actions

    # generates new state from state and action
    # returns resulting state
    def Result(self, state, action):
        new_state = state.copy()

        # apply action to state
        for i in range(HEIGHT):
            if new_state[i][action] != EMPTY:
                new_state[i-1][action] = BLACK if self.abs_black_turn else RED
                break
            elif i == HEIGHT-1:
                new_state[i][action] = BLACK if self.abs_black_turn else RED
                break

        return new_state


