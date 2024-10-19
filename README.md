# ColourMaze
This is a game that I made in 2021. While it could have been written better, I've decided to upload it as is to show authenticity.

I first got the idea when me and my dad were thinking about multi-dimensional mazes and how they could be displayed in 2D. The final product looks pretty cool though and is fun to play as well, although incredibly difficult.


## colour maze.py
File that runs the mazes

### how to play:
To play the game, just run the "colour maze.py" file. It requires pygame and the maze txt files to run.<br>

**Controls:** <br>
WASD to move<br>
P - Select top colour<br>
L - Select bottom colour<br>
The goal is to reach the bottom right of the maze

To pass through a wall, your top or bottom needs to be that colour. For example a red wall can only be moved through if your top and/or bottom is red. If your top is red and bottom is blue, that will allow you to pass through walls that are either red or blue.

**Warning:** there is no undo or restart, so if you get stuck you'll need to kill the program and run it again. **I also can't stress enough how hard this game gets**


# Problems
There's little error handling when inputting desired maze size and length, and when inputting the code of the maze to find the solution for.

The program also just crashes when you solve it; there's no "Yay you won!" message, it's just a hard out. But the point wasn't to make a beautiful game, it was more to toy around with encoding mazes and generating possible ones so I'm ok if it's rough around the edges.




