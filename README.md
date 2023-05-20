# Minesweeper

## Goal 
Find the empty fields and avoid the mines. The faster you clear the board, the better your score.

## Board
The board contains 225 fields (15x15), with 40 bombs placed at random.

## How to play
The rules of Minesweeper are simple:

* If you discover a mine, it's game over.

* If you discover an empty square, the game continues.

* If a number appears, it tells you how many mines are hidden in the eight squares that surround it. You use this information to deduce which nearby squares are safe to click on.

* If you discover all the fields that didn't have mines, congratulations you've won the game.

## Hints
* **Mark the mines:** If you suspect that a square contains a mine, click on the flag and mark it.

* **Study the patterns:** If three squares in a row display the numbers 2, 3, and 2, there are probably three mines lined up next to those numbers. If a square shows the number 8, all squares surrounding it are mined.

* **Explore the unknown:** Not sure where to click next? Try to clear some unexplored territory. It's better to click in the middle of unmarked squares than in an area you suspect is mined.

## Technical information
The game was developed in Python language, using the QT Designer library to create the graphical interface.

## Releases

## Author
- [@thiagoservulo](https://github.com/ThiagoServulo)

- 05/20/2023