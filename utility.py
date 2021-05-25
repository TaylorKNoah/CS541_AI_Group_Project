import config

def evaluation_fn(state, is_blacks_turn):
    """Evaluates a on the gameboard for a given player.

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
            # segment = [state[row][col:col + CONNECT_N]]
            segment = [state[row][col + i] for i in range(config.CONNECT_N)]
            score += segment_eval(segment, is_blacks_turn)

    # vertical
    for col in range(config.WIDTH):
        for row in range(config.HEIGHT - offset):
            # get segment and evaluate
            segment = [state[row + i][col] for i in range(config.CONNECT_N)]
            score += segment_eval(segment, is_blacks_turn)

    # left leaning diagonal
    for row in range(config.HEIGHT - offset):
        for col in range(config.WIDTH - offset):
            # get diagonal segment
            segment = [state[row + i][col + i] for i in range(config.CONNECT_N)]
            score += segment_eval(segment, is_blacks_turn)

    # right leaning diagonal
    for row in range(config.HEIGHT - offset):
        for col in range(config.WIDTH - offset):
            # get diagonal segment
            segment = [state[row + offset - i][col + i] for i in range(config.CONNECT_N)]
            score += segment_eval(segment, is_blacks_turn)

    return score

def segment_eval(segment, is_blacks_turn):
    """Evaluates a `CONNECT_N` sized segment on the gameboard.

    Args:
        segment (list[list[str]]): A game board.
        is_blacks_turn (bool): Indicates which player is taking the turn.

    Returns:
        An int representing the optimality of the segment. Higher numbers
        should be prioritized over lower.
    """

    score = 0
    max_score = 100

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
        score += max_score
    # 3 in a row with the possibility of 4
    elif piece_count == 3 and empty_count == 1:
        score += 20
    # 2 in a row with the possibility of 3/4
    elif piece_count == 2 and empty_count == 2:
        score += 5


    # subtract points for opponent strings
    if opponent_count == 3 and empty_count == 1:
        score -= 15
    if opponent_count == 2 and empty_count == 2:
        score -= 3

    return score