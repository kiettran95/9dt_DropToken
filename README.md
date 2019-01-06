# 9dt_DropToken
#### Author: Kiet Tran

## Rules of the Game
Drop Token takes place on a 4x4 grid. A token is dropped along a column (labeled 1-4) and said token goes to the lowest unoccupied row of the board. A player wins when they have 4 tokens next to each other either along a row, in a column, or on a diagonal. If the board is filled, and nobody has won then the game is a draw. Each player takes a turn, starting with player 1, until the game reaches either win or draw. If a player tries to put a token in a column that is already full, that results in an error state, and the player must play again until the play a valid move.

## Interface
CLI that loops over stdIn taking commands, and prints out responses based on those commands.

### Commands
  - `PUT <column>` 
    - (OK | ERROR | WIN | DRAW)
  - `GET` 
    - List of columns that have been successfully put to 
  - `BOARD` 
    - a 4x4 matrix that shows the board state
  - `EXIT` 
    - Exit the program.
  
  
## Execute
  Use Python version 3.7.0. 
  Navigate to parent directory and run command:
  ```python 9dt.py```
      
