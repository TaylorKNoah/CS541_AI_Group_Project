# CS541-AI---Group-Project
| Members | | | |  
| --- | --- | --- | --- |
| Taylor Noah | Jesse Rapoport | Adam Shih | Joel Williams |

Repo for the group project portion of CS541.  We will create an AI which  plays Connect 4.
We implement two versions of the minimax algorithm, each with a different hueristic. The user will be able to play against the two  
algorithms or have the AIs play themselves.

### Code

The game.py file provides an interface for playing Connect 4. The code itself is a bit messy, but using it is clean. Here are the functions you can import:

- Game(): creates a blank connect-4 game object.
- print_board(): print the board object. 
- play_move(column): whoever's turn it is, play a piece in the specified column. If that move made a player win, return the name of that player: X, O, or None.
- random_move(): whoever's turn it is, play a random move.

You can adjust the size of the game board, the connect-n game number, and whether/how fast you want the games to be animated, via constants at the top of the file.
