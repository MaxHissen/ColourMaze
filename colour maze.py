import pygame
import random
import math

class Cell:
    def __init__(self,upper,lower):
        self.upper = upper
        self.lower = lower

BACKGROUND = (0,0,0)
WALLS = (100,100,100)
RED = (255,0,0)
BLUE = (0,0,255)
GREEN = (0,255,0)
YELLOW = (255,255,0)
PURPLE = (255,0,255)
WHITE = (255,255,255)
NONE = (0,0,0)

WINDOW_WIDTH = 900
WINDOW_HEIGHT = 600

WIDTH = 0
HEIGHT = 0

while WIDTH <= 0:
    try:
        WIDTH = int(input("Pick a Size of Maze: "))
    except:
        print("That maze doesn't exist")

HEIGHT = WIDTH
filename = "mazes("+str(WIDTH)+"x"+str(HEIGHT)+").txt"

CELL_SIZE = min(WINDOW_WIDTH / WIDTH * 0.8, WINDOW_HEIGHT / HEIGHT * 0.8)
LINE_WIDTH = round(max(CELL_SIZE*0.05,1))
DOOR_PERCENTAGE = 0.6
CELL_COLOUR_WIDTH = 0.55
CELL_COLOUR_HEIGHT = 0.15
CELL_COLOUR_HEIGHT_OFFSET = 0.15
PLAYER_SIZE = 0.25


#print(CELL_SIZE)
class Maze:
    def __init__(self, cells, walls, length):
        self.cells = cells
        self.walls = walls
        self.length = length
        
def decode_mazes():
    
    mazes_file = open(filename, "r")
    
    maze_list = mazes_file.readlines()
    
    for maze in maze_list:
        cells = maze.split("|")[0]
        walls = maze.split(":")[0]
        walls = walls.split("|")[1]
        length = int(maze.split(":")[1])

        #decode cells
        cells_length = len(cells)
        #print(cells_length)
        maze_cells = {}
        
        for i in range(cells_length//4):
            maze_cells[(int(cells[4*i]),  int(cells[4*i+1]))] = (int(cells[4*i+2]),int(cells[4*i+3]))
        #print(maze_cells)

        #decode walls
        maze_walls = {}
        
        walls_length = WIDTH*(HEIGHT-1) + HEIGHT*(WIDTH-1)
        walls = walls.split("_")

        for wall in walls:
            if len(wall) == 0:
                break
            x = wall.split(",")[0]
            y = wall.split(",")[1]
            y = y.split(" ")[0]
            c = wall.split(" ")[1]
            
            maze_walls[((int(x)/2),int(y)/2)] = int(c)

        try:
            if stored_mazes[length]:
                pass
        except:
            stored_mazes[length] = Maze(maze_cells,maze_walls,length)
            
    #print(stored_mazes)

def draw_maze():
    #draw grid
    for x in range(HEIGHT + 1):
        xpos = WINDOW_WIDTH/2 - CELL_SIZE*WIDTH/2
        ypos = WINDOW_HEIGHT/2 - CELL_SIZE*HEIGHT/2 + CELL_SIZE*x

        pygame.draw.rect(window,WALLS,(xpos,ypos,CELL_SIZE*WIDTH + LINE_WIDTH,LINE_WIDTH))

    for y in range(WIDTH + 1):
        xpos = WINDOW_WIDTH/2 - CELL_SIZE*WIDTH/2 + CELL_SIZE*y
        ypos = WINDOW_HEIGHT/2 - CELL_SIZE*HEIGHT/2

        pygame.draw.rect(window,WALLS,(xpos,ypos,LINE_WIDTH,CELL_SIZE*HEIGHT + LINE_WIDTH))

    #draw doors
    for x in range(WIDTH):
        for y in range(HEIGHT - 1):
            xpos = WINDOW_WIDTH/2 - CELL_SIZE*WIDTH/2 + CELL_SIZE*(x) + CELL_SIZE*(1-DOOR_PERCENTAGE)/2
            ypos = WINDOW_HEIGHT/2 - CELL_SIZE*HEIGHT/2 + CELL_SIZE*(y+1)
            pygame.draw.rect(window,walls[(x,y+0.5)],(xpos,ypos,(CELL_SIZE + LINE_WIDTH + 1)*DOOR_PERCENTAGE,LINE_WIDTH))

    for x in range(WIDTH-1):
        for y in range(HEIGHT):
            xpos = WINDOW_WIDTH/2 - CELL_SIZE*WIDTH/2 + CELL_SIZE*(x+1)
            ypos = WINDOW_HEIGHT/2 - CELL_SIZE*HEIGHT/2 + CELL_SIZE*(y) + CELL_SIZE*(1-DOOR_PERCENTAGE)/2
            pygame.draw.rect(window,walls[(x+0.5,y)],(xpos,ypos,LINE_WIDTH,(CELL_SIZE + LINE_WIDTH + 1)*DOOR_PERCENTAGE))

    #draw cell colours
    for x in range(WIDTH):
        for y in range(HEIGHT):
            xpos = WINDOW_WIDTH/2 - CELL_SIZE*WIDTH/2 + CELL_SIZE*x
            ypos = WINDOW_HEIGHT/2 - CELL_SIZE*HEIGHT/2 + CELL_SIZE*y

            pygame.draw.rect(window,cells[(x,y)][1],(xpos + CELL_SIZE*(1-CELL_COLOUR_WIDTH)/2 + LINE_WIDTH/2,ypos + CELL_SIZE*CELL_COLOUR_HEIGHT_OFFSET + LINE_WIDTH/2,CELL_SIZE*CELL_COLOUR_WIDTH,CELL_SIZE*CELL_COLOUR_HEIGHT))
            pygame.draw.rect(window,cells[(x,y)][0],(xpos + CELL_SIZE*(1-CELL_COLOUR_WIDTH)/2 + LINE_WIDTH/2,ypos + CELL_SIZE*(1-CELL_COLOUR_HEIGHT_OFFSET-CELL_COLOUR_HEIGHT) + LINE_WIDTH/2,CELL_SIZE*CELL_COLOUR_WIDTH,CELL_SIZE*CELL_COLOUR_HEIGHT))

    
            
    pygame.display.flip()

def draw_player(old_pos, new_pos):
    if old_pos:
        xpos = WINDOW_WIDTH/2 - CELL_SIZE*WIDTH/2 + CELL_SIZE*old_pos[0] + CELL_SIZE/2 - CELL_SIZE*PLAYER_SIZE/2 + LINE_WIDTH/2
        ypos = WINDOW_HEIGHT/2 - CELL_SIZE*HEIGHT/2 + CELL_SIZE*old_pos[1] + CELL_SIZE/2 - CELL_SIZE*PLAYER_SIZE/2 + LINE_WIDTH/2
        pygame.draw.rect(window,BACKGROUND,(xpos,ypos,CELL_SIZE * PLAYER_SIZE,CELL_SIZE * PLAYER_SIZE))
    
    xpos = WINDOW_WIDTH/2 - CELL_SIZE*WIDTH/2 + CELL_SIZE*new_pos[0] + CELL_SIZE/2 - CELL_SIZE*PLAYER_SIZE/2 + LINE_WIDTH/2
    ypos = WINDOW_HEIGHT/2 - CELL_SIZE*HEIGHT/2 + CELL_SIZE*new_pos[1] + CELL_SIZE/2 - CELL_SIZE*PLAYER_SIZE/2 + LINE_WIDTH/2

    pygame.draw.rect(window,colour[1],(xpos,ypos,CELL_SIZE * PLAYER_SIZE,CELL_SIZE * PLAYER_SIZE/2))
    pygame.draw.rect(window,colour[0],(xpos,ypos + CELL_SIZE*PLAYER_SIZE/2,CELL_SIZE * PLAYER_SIZE,CELL_SIZE * PLAYER_SIZE/2))
    pygame.display.flip()
        

def move(position, dx, dy):
    old_position = position.copy()
    #print((position[0] + dx/2, position[1] + dy/2))
    try:
        wall_colour = (walls[(position[0] + dx/2, position[1] + dy/2)])
    except:
        #print("error")
        return old_position
    
    if (wall_colour == colour[0] and colour[0] != WALLS) or (wall_colour == colour[1] and colour[1] != WALLS):
        position = [position[0] + dx, position[1] + dy]
        draw_player(old_position, position)
        #print("G")
        
        return position
    #print("no")
    return old_position

def translate_maze():
    cells = stored_mazes[decided_length].cells
    walls = stored_mazes[decided_length].walls
    for choice in cells:
        cell = cells[choice]
        lower = cell[0]
        upper = cell[1]
        if lower == 0:
            lower = NONE
        if lower == 1:
            lower = RED
        if lower == 2:
            lower = BLUE
        if lower == 3:
            lower = GREEN
        if lower == 4:
            lower = YELLOW
        if lower == 5:
            lower = PURPLE
        if lower == 6:
            lower = WHITE

        if upper == 0:
            upper = NONE
        if upper == 1:
            upper = RED
        if upper == 2:
            upper = BLUE
        if upper == 3:
            upper = GREEN
        if upper == 4:
            upper = YELLOW
        if upper == 5:
            upper = PURPLE
        if upper == 6:
            upper = WHITE

        cells[choice] = (lower, upper)

    for choice in walls:
        wall = walls[choice]

        if wall == 1:
            wall = RED
        if wall == 2:
            wall = BLUE
        if wall == 3:
            wall = GREEN
        if wall == 4:
            wall = YELLOW
        if wall == 5:
            wall = PURPLE
        if wall == 6:
            wall = WHITE
        if wall == 9:
            wall = WALLS

        walls[choice] = wall

    return cells, walls

stored_mazes = {}
decode_mazes()

for key in stored_mazes:
    print(key)
    
decided_length = 0
while decided_length <= 0:
    try:
        decided_length = int(input("Pick a Length of Maze: "))
    except:
        print("That maze doesn't exist")

cells, walls = translate_maze()

window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('My Game!')

draw_maze()

position = [0,0]
colour = [WALLS, WALLS] #lower, upper
clock = pygame.time.Clock()
pygame.key.set_repeat(0, 300)

draw_player(None, position)

running = True
while running:
    clock.tick(60)

    if position[0] == WIDTH-1 and position[1] == HEIGHT-1:
        print("Congrats!")
        pygame.quit()
        running = False
    
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                position = move(position, -1, 0)

            if event.key == pygame.K_s:
                position = move(position, 0, 1)

            if event.key == pygame.K_d:
                position = move(position, 1, 0)

            if event.key == pygame.K_w:
                position = move(position, 0, -1)


            if event.key == pygame.K_p:
                if cells[(position[0], position[1])][1] != NONE:
                    colour[1] = cells[(position[0], position[1])][1]
                    draw_player(None, position)

            if event.key == pygame.K_l:
                if cells[(position[0], position[1])][0] != NONE:
                    colour[0] = cells[(position[0], position[1])][0]
                    draw_player(None, position)
    
