import pygame
import random

random.seed(100)

WIDTH = 9
HEIGHT = 9

WINDOW_WIDTH = 900
WINDOW_HEIGHT = 600
cell_size = min(WINDOW_WIDTH / WIDTH * 0.8, WINDOW_HEIGHT / HEIGHT * 0.8)

window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('My Game!')


for x in range(WIDTH+1):
    XSTART = WINDOW_WIDTH/2 - (x-WIDTH/2)*cell_size
    XEND = XSTART

    YSTART = WINDOW_HEIGHT/2 - (HEIGHT/2)*cell_size
    YEND = YSTART + HEIGHT*cell_size
    
    pygame.draw.line(window,(100,100,100),(XSTART,YSTART),(XEND,YEND))

for y in range(HEIGHT+1):
    XSTART = WINDOW_WIDTH/2 - (WIDTH/2)*cell_size
    XEND = XSTART + WIDTH*cell_size

    YSTART = WINDOW_HEIGHT/2 - (y-HEIGHT/2)*cell_size
    YEND = YSTART
    
    pygame.draw.line(window,(100,100,100),(XSTART,YSTART),(XEND,YEND))

untravelled_cells = []
for x in range(WIDTH):
    for y in range(HEIGHT):
        untravelled_cells.append([x+1,y+1])

leading_cell = [random.randint(1,WIDTH), random.randint(1,HEIGHT)]
maze_section = [leading_cell] #start with random cell

print(leading_cell)

for i in range(1):
    direction = [1,2,3,4]
    for choice in direction:
        if choice == 1: #right
            if [leading_cell[0]+1, leading_cell[1]] in untravelled_cells:

                XSTART = WINDOW_WIDTH/2 - (-leading_cell[0]+WIDTH/2)*cell_size - cell_size/2
                XEND = XSTART + cell_size

                YSTART = WINDOW_HEIGHT/2 - (HEIGHT/2-2)*cell_size + cell_size/2
                YEND = YSTART

                print(XSTART,YSTART)

                pygame.draw.line(window,(0,200,0),(XSTART,YSTART),(XEND,YEND),int(cell_size)-2)

                leading_cell = [leading_cell[0]+1, leading_cell[1]]

    maze_section.append(leading_cell)






pygame.display.flip()






    
