from config import EMPTY, RED, BLACK, HEIGHT, WIDTH
import utility

# test board
black_good  = [[EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY], 
               [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY], 
               [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY], 
               [EMPTY, EMPTY, EMPTY, BLACK, EMPTY, EMPTY, EMPTY], 
               [EMPTY, EMPTY, BLACK, BLACK, RED,   EMPTY, EMPTY], 
               [EMPTY, EMPTY, BLACK, BLACK, RED,   EMPTY, EMPTY]]

black_win   = [[EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY], 
               [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY], 
               [EMPTY, EMPTY, EMPTY, BLACK, EMPTY, EMPTY, EMPTY], 
               [EMPTY, EMPTY, EMPTY, BLACK, EMPTY, EMPTY, EMPTY], 
               [EMPTY, EMPTY, BLACK, BLACK, RED,   EMPTY, EMPTY], 
               [EMPTY, EMPTY, BLACK, BLACK, RED,   EMPTY, EMPTY]]

just_red   = [[EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY], 
              [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY], 
              [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY], 
              [EMPTY, EMPTY, RED,   RED,   RED,   EMPTY, EMPTY], 
              [EMPTY, EMPTY, RED,   RED,   RED,   EMPTY, EMPTY], 
              [EMPTY, EMPTY, RED,   RED,   RED,   EMPTY, EMPTY]]


# do heuristic tests on multiple boards
def heuristic_tests():
    test_heuristic_on_board(black_good)
    test_heuristic_on_board(black_win)
    test_heuristic_on_board(just_red)

# test the heuristics on a single board
def test_heuristic_on_board(board):
    # print the board
    for i in range(HEIGHT):
        for j in range(WIDTH):
            print(board[i][j], end=" ")
        print()

    # print heuristic values if it's black's turn
    print("Radius and consecutive evaluations if it's O's turn:")
    print(utility.radius_evaluation(board, True))
    print(utility.consecutive_evaluation(board, True))
    # print heuristic values if it's red's turn
    print("Radius and consecutive evaluations if it's X's turn:")
    print(utility.radius_evaluation(board, False))
    print(utility.consecutive_evaluation(board, False))

    print()
    print()

