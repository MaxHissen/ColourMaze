# ColourMaze
This is a game that I made in 2021. While it could have been written better, I've decided to upload it as is to show authenticity.

I first got the idea when me and my dad were thinking about multi-dimensional mazes and how they could be displayed in 2D. The final product looks pretty cool though and is fun to play as well, although incredibly difficult.<br>

Game is played through "**colour maze.py**"<br>
Mazes are found via "**discover mazes.py**"<br>
You can cheat the solution with "**solve maze.py**"<br>

<br>
<br>

## colour maze.py
File that runs the mazes

### how to play:
**Warning:** <br>
To play the game, just run the "colour maze.py" file. It requires pygame and the maze txt files to run.<br>
there is no undo or restart, so if you get stuck you'll need to kill the program and run it again. **I also can't stress enough how hard this game gets** <br>

**Controls:** <br>
WASD to move<br>
P - Select top colour<br>
L - Select bottom colour<br>
The goal is to reach the bottom right of the maze

To pass through a wall, your top or bottom needs to be that colour. For example a red wall can only be moved through if your top and/or bottom is red. If your top is red and bottom is blue, that will allow you to pass through walls that are either red or blue. **Grey walls cannot be passed through.**

<br>
<br>

## solve maze.py

The solve maze.py program is not very user-friendly, because it was only really meant to be a debugger<br>
It does work perfectly though, so if you are stuck on a maze, below are steps on how to use it<br>

### how to use:<br>

Edit the program to have the size of maze to solve.<br><br>
![image](https://github.com/user-attachments/assets/95528b7d-00e5-4e9f-8869-a7f78f898f1c)


run the program, and copy-paste in the code for the maze you want to solve. Mazes can be easily told apart by their length at the end of the respective line.<br><br>
![image](https://github.com/user-attachments/assets/b318bae9-973a-4d17-9af6-1fe008ffcb16)

paste the resulting line into the solver:<br>
<br>
![image](https://github.com/user-attachments/assets/63cec88c-3079-40e7-b0d4-41ac7a610e0d)
<br>
<br>
![image](https://github.com/user-attachments/assets/e701aa91-b6d7-4e8f-b16a-00c8add3ab3c)


press enter and the program will decode the maze, solve it from scratch, and output what you need to do to solve it (in the shortest way. **There will always be a longer way to solve a maze**).<br>
Take the solution for 3x3 length 14 as in the screenshots above:<br><br>
![image](https://github.com/user-attachments/assets/361ffa4b-91d0-4106-93c0-27910da6748b)


Sanity check: the length of solution should equal the length that the maze code said.<br>

### reading the solution
UDLR - Up, Down, Left, Right<br>
T - get cell top colour<br>
B - get cell bottom colour<br>

This should take n button presses, where n is the length of the solution<br>

<br>
<br>

## discover mazes.py

### How it works:
The maze generation first reads out all the mazes of that size from the text file, and stores them in a dictionary.<br>
It then randomly sets mazes of that size, and tries to solve them. If it finds a maze that has a solution not yet found, it gets added to the dictionary.<br>
At the end, it clears the file and writes the dictionary in order

### how to use:<br>

Edit parameters as you see fit<br><br>
![image](https://github.com/user-attachments/assets/4e7e5722-8c5d-43f1-9447-f6dc5608ef0f)<br><br>
wall_colours and cell_colours are the colours that the maze will choose from when creating the next random maze to test. The more of each there are the more biased the maze will be towards that colour. 1=RED, 2=BLUE, 3=GREEN, 4=YELLOW, 5=PURPLE, 6=WHITE.<br>
grey walls are 9, a cell with no colour is 0.<br>
If wall_colours has 3 1's in it, any given wall is 3x more likely to be red when creating the random maze.<br>

# Problems
There's little error handling when inputting desired maze size and length, and when inputting the code of the maze to find the solution for.

The program also just crashes when you solve it; there's no "Yay you won!" message, it's just a hard out. But the point wasn't to make a beautiful game, it was more to toy around with encoding mazes and generating possible ones so I'm ok if it's rough around the edges.




