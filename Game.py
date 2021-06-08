import time
import random
import config
from utility import consecutive_evaluation, radius_evaluation, term_test
import copy

# animation settings
FRAME_LENGTH = 0.01


# creates a connect-4 game object
class Game:
    # initialize the board and set it to black's turn
    def __init__(self):
        self.animate = True
        self.board = []
        self.initialize_board()
        self.blacks_turn = True
        self.heuristic_black = None
        self.heuristic_red = None

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
            if self.animate:
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
    def Alpha_Beta_Search(self, state):
        # gets the optimal value of all possible moves
        _, optimal_action = self.Max_Value(state, config.NINF, config.INF, config.DEPTH)


        return optimal_action

        '''

        # gets available actions
        actions = self.Actions(state)

        # searchs current possibles actions for value equal to optimal
        # if action is legal then this checks to see if it generates the optimal value
        # once found, save the index of the action (aka the column to use)
        for i in range(config.WIDTH):
            if actions[i] and optimal_value == self.evaluation_fn(self.Result(state, actions[i]), self.blacks_turn):
                return i
        '''

    def Max_Value(self, state, alpha, beta, depth):
        opt_action = 0
        if depth == 0:
            return self.evaluation_fn(state, self.blacks_turn), opt_action

        # decrease depth
        depth -= 1

        # check if at term state - ret util
        if term_test(state):
            return self.evaluation_fn(state, self.blacks_turn), opt_action

        # set value to -inf
        value = config.NINF
        # get valid actions
        actions = self.Actions(state)

        # iterate through actions looking for valid actions
        # keep a list of action values and either choose the best
        # or choose at random
        possibilities = [config.NINF for i in range(config.WIDTH)]
        for i in range(len(actions)):
            if actions[i]:
                self.abs_black_turn = self.blacks_turn
                # get val of next possible move given action[i]
                temp = self.Min_Value(self.Result(state, i), copy.copy(alpha), copy.copy(beta), copy.copy(depth))

                # update valid action values in possibilities for exploration
                possibilities[i] = temp

                # update value with greatest return value from Min_Value
                if temp > value:
                    opt_action = i
                    value = temp

                # prune if val greate than beta
                # max will return a number no less than value
                # but min will never take this return val
                # bc beta(min-so-far) is less than value
                if value >= beta:
                    return value, opt_action

                # update alpha with MAX(value, alpha)
                if value > alpha:
                    alpha = value

        # at last action comparison before returning to ABS
        # chance for "exploration action"
        # random val between 0 and 1, if less that epsilon, choose rand
        if depth == config.DEPTH - 1:
            rval = (random.randint(1, 100) / 100)
            if rval < config.EPSILON:
                rval = random.randint(0, config.WIDTH - 1)
                # ensure rnad action is valid
                while(possibilities[rval] == config.NINF):
                    rval = random.randint(0, config.WIDTH)

                config.RMOVES += 1
                # return rand action + value
                return possibilities[rval], rval

        # return optimal action and value
        return value, opt_action

    def Min_Value(self, state, alpha, beta, depth):
        if depth == 0:
            return self.evaluation_fn(state, self.blacks_turn)

        depth -= 1

        # check if at term state - ret util
        if term_test(state):
            return self.evaluation_fn(state, self.blacks_turn)

        # set value to -inf
        value = config.INF
        # get valid actions
        actions = self.Actions(state)

        # iterate through actions looking for valid actions
        for i in range(len(actions)):
            if actions[i]:
                self.abs_black_turn = not self.blacks_turn
                # get val of next possible move given action[i]
                temp, _ = self.Max_Value(self.Result(state, i), copy.copy(alpha), copy.copy(beta), copy.copy(depth))
                # update value with least return value from Max_Value
                if temp < value:
                    value = temp

                # prune if val less than alpha
                # min will return a number no greater than value
                # but max will never take this return val
                # bc alpha(max-so-far) is greater than value
                if value <= alpha:
                    return value

                # update beta with MIN(value, beta)
                if value < beta:
                    beta = value
        return value

    # uses game state to determine valid move
    # valid move: there is space in the column at index i
    # returns a boolean list
    def Actions(self, state):
        actions = []
        for i in range(config.WIDTH):
            if state[0][i] != config.EMPTY:
                actions.append(False)
            else:
                actions.append(True)

        return actions

    # generates new state from state and action
    # returns resulting state
    def Result(self, state, action):
        new_state = copy.deepcopy(state)

        # apply action to state
        for i in range(config.HEIGHT):
            if new_state[i][action] != config.EMPTY:
                new_state[i - 1][action] = config.BLACK if self.abs_black_turn else config.RED
                break
            elif i == config.HEIGHT - 1:
                new_state[i][action] = config.BLACK if self.abs_black_turn else config.RED
                break

        self.abs_black_turn = not self.abs_black_turn

        return new_state

    def evaluation_fn(self, state, is_blacks_turn):
        """Wrapper function to call an evaluation function
        Args:
            state (list[list[str]]): A game board.
            is_blacks_turn (bool): Indicates which player is taking the turn.

        Returns:
            An int representing the optimality of the state. Higher numbers
            should be prioritized over lower.
        """
        if is_blacks_turn:
            if self.heuristic_black == "consecutive":
                return consecutive_evaluation(state, is_blacks_turn)
            elif self.heuristic_black == "radius":
                return radius_evaluation(state, is_blacks_turn)
        else:
            if self.heuristic_red == "consecutive":
                return consecutive_evaluation(state, is_blacks_turn)
            elif self.heuristic_red == "radius":
                return radius_evaluation(state, is_blacks_turn)


