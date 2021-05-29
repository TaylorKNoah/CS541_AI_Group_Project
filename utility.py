import config

def evaluation_fn(state, is_blacks_turn):
    """Wrapper function to call an evaluation function
    Args:
        state (list[list[str]]): A game board.
        is_blacks_turn (bool): Indicates which player is taking the turn.

    Returns:
        An int representing the optimality of the state. Higher numbers
        should be prioritized over lower.
    """
    if config.HEURISTIC == "consecutive":
        return consecutive_evaluation(state, is_blacks_turn)
    elif config.HEURISTIC == "radius":
        return radius_evaluation(state, is_blacks_turn)



# radius evaluation functions

def radius_evaluation(state, is_blacks_turn):
    """Evaluates status of the board by looking at matching pieces within n. radius
    Args:
        state (list[list[str]]): A game board.
        is_blacks_turn (bool): Indicates which player is taking the turn.

    Returns:
        An int representing the optimality of the state. Higher numbers
        should be prioritized over lower.
    """
    score = 0
    # go through each row and column of the board
    for row in range(config.HEIGHT):
        for col in range(config.WIDTH):
            # if it's not an empty space, add the piece's radius value to the total score
            if state[row][col] != config.EMPTY:
                score += single_piece_radius(state, is_blacks_turn, row, col)
    return score

def single_piece_radius(state, is_blacks_turn, row, col):
    """Evaluates status of a single piece by looking at others within n. radius
    Args:
        state (list[list[str]]): A game board.
        is_blacks_turn (bool): Indicates which player is taking the turn.
        row (int): Which row the piece is in.
        col (int): Which column the piece is in.

    Returns:
        An int representing the optimality of the state. Higher numbers
        should be prioritized over lower.
    """
    # starting score
    score = 0
    # color of center piece
    current_color = state[row][col]
    # check if the center piece is the opponent or not
    if (is_blacks_turn and current_color == config.BLACK) or ((not is_blacks_turn) and current_color == config.RED):
        center_isnt_opponent = True
    else:
        center_isnt_opponent = False

    # go through each row within RADIUS spaces
    for i in range(row - config.RADIUS, row + config.RADIUS + 1):
        # skip if illegal row
        if i < 0 or i >= config.HEIGHT:
            continue
        # go through each column within RADIUS spaces
        for j in range(col - config.RADIUS, col + config.RADIUS + 1):
            # skip if illegal column, or it's the center piece
            if j < 0 or j >= config.WIDTH or (i == row and j == col):
                continue
            # increment the score according to the square's color
            if state[i][j] == current_color:
                score += config.SAME_COLOR_SCORE
            elif state[i][j] == config.EMPTY:
                score += config.EMPTY_SQUARE_SCORE
            else:
                score += config.OPPONENT_COLOR_SCORE
    # return the score, or the negative/lessened version of the score if it's the opponent's turn
    return score if center_isnt_opponent else int(config.OPPONENT_VALUE * score)



# consecutive evaluation functions

def consecutive_evaluation(state, is_blacks_turn):
    """Evaluates status of the board by looking at consecutive pieces of the same color
    Args:
        state (list[list[str]]): A game board.
        is_blacks_turn (bool): Indicates which player is taking the turn.

    Returns:
        An int representing the optimality of the state. Higher numbers
        should be prioritized over lower.
    """
    score = 0
    offset = config.CONNECT_N - 1

    # iterate over all possible segments of 4 pieces
    
    # horizontal
    for row in range(config.HEIGHT):
        for col in range(config.WIDTH - offset):
            # get segment and evaluate
            segment = [state[row][col + i] for i in range(config.CONNECT_N)]
            score += consecutive_segment_eval(segment, is_blacks_turn)

    # vertical
    for col in range(config.WIDTH):
        for row in range(config.HEIGHT - offset):
            # get segment and evaluate
            segment = [state[row + i][col] for i in range(config.CONNECT_N)]
            score += consecutive_segment_eval(segment, is_blacks_turn)

    # left leaning diagonal
    for row in range(config.HEIGHT - offset):
        for col in range(config.WIDTH - offset):
            # get diagonal segment
            segment = [state[row + i][col + i] for i in range(config.CONNECT_N)]
            score += consecutive_segment_eval(segment, is_blacks_turn)

    # right leaning diagonal
    for row in range(config.HEIGHT - offset):
        for col in range(config.WIDTH - offset):
            # get diagonal segment
            segment = [state[row + offset - i][col + i] for i in range(config.CONNECT_N)]
            score += consecutive_segment_eval(segment, is_blacks_turn)

    return score

def consecutive_segment_eval(segment, is_blacks_turn):
    """Evaluates a `CONNECT_N` sized segment on the gameboard.

    Args:
        segment (list[str]): A game board.
        is_blacks_turn (bool): Indicates which player is taking the turn.

    Returns:
        An int representing the optimality of the segment. Higher numbers
        should be prioritized over lower.
    """

    score = 0

    if is_blacks_turn:
        piece = config.BLACK
        opponent = config.RED
    else:
        piece = config.RED
        opponent = config.BLACK

    piece_count = segment.count(piece)
    opponent_count = segment.count(opponent)
    empty_count = segment.count(config.EMPTY)

    # 4 in a row then give maximum score
    if piece_count == 4:
        score += config.MAX_SCORE
    # 3 in a row with the possibility of 4
    elif piece_count == 3 and empty_count == 1:
        score += config.THREE_SCORE
    # 2 in a row with the possibility of 3/4
    elif piece_count == 2 and empty_count == 2:
        score += config.TWO_SCORE


    # subtract points for opponent strings
    if opponent_count == 3 and empty_count == 1:
        score += config.OPPONENT_THREE_SCORE
    if opponent_count == 2 and empty_count == 2:
        score += config.OPPONENT_TWO_SCORE

    return score
