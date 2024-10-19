import random
#random.seed(2229)

WIDTH = 7  # < 10
HEIGHT = 7 # < 10

iterations = 10000000

filename = "mazes("+str(WIDTH)+"x"+str(HEIGHT)+").txt"

wall_colours = [1, 2, 3, 4, 5, 6, 9, 9]
cell_colours = [1, 2, 3, 4, 5, 6, 0, 0]

stored_mazes = {}

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
    
def encode_mazes():
    keys = []
    for code in stored_mazes:
        keys.append(code)
    keys.sort()

    mazes_to_add = []
    for code in keys:
        cells = stored_mazes[code].cells
        walls = stored_mazes[code].walls
        length = stored_mazes[code].length
        
        mazes_file = open(filename, "w")
        
        maze = ""
        for choice in cells:
            maze += str(choice[0]) + str(choice[1]) +  str(cells[choice][0]) + str(cells[choice][1])
        
        maze += "|"
        
        for choice in walls:
            maze += str(int(choice[0]*2)) + "," + str(int(choice[1]*2)) + " " + str(walls[choice]) + "_"
        
        maze += ":" + str(length)

        maze += '\n'

        mazes_to_add.append(maze)

        
    mazes_file.writelines(mazes_to_add)
    mazes_file.close()

def generate_random_maze(cells, walls):
    walls = {}
    for x in range(WIDTH-1):
        for y in range(HEIGHT):
            walls[(x+0.5,y*1.0)] = random.choice(wall_colours)

    for x in range(WIDTH):
        for y in range(HEIGHT-1):
            walls[(x*1.0,y+0.5)] = random.choice(wall_colours)

    cells = {}
    for x in range(WIDTH):
        for y in range(HEIGHT):
            cells[(x,y)] = (random.choice(cell_colours), random.choice(cell_colours))
    cells[(WIDTH-1,HEIGHT-1)] = (0,0)#end cell needs no colours

    return cells, walls

def test_maze(cells, walls):
        path_heads = [(0,0,0,0)] #xpos ypos bottomcolour topcolour
        seen_heads = {}
        length = 0
        while True:
            new_path_heads = []
            for head in path_heads:
                #move right
                try:
                    if head[2] == walls[(head[0] + 0.5, head[1])] or head[3] == walls[(head[0] + 0.5, head[1])]:
                        new_head = (head[0]+1, head[1], head[2], head[3])
                        try:
                            if seen_heads[new_head] == True:
                                pass
                        except:
                            seen_heads[new_head] = True
                            new_path_heads.append(new_head)
                except:
                    pass
                
                #move left
                try:
                    if head[2] == walls[(head[0] - 0.5, head[1])] or head[3] == walls[(head[0] - 0.5, head[1])]:
                        new_head = (head[0]-1, head[1], head[2], head[3])
                        try:
                            if seen_heads[new_head] == True:
                                pass
                        except:
                            seen_heads[new_head] = True
                            new_path_heads.append(new_head)
                except:
                    pass
                
                #move up
                try:
                    if head[2] == walls[(head[0], head[1] - 0.5)] or head[3] == walls[(head[0], head[1] - 0.5)]:
                        new_head = (head[0], head[1]-1, head[2], head[3])
                        try:
                            if seen_heads[new_head] == True:
                                pass
                        except:
                            seen_heads[new_head] = True
                            new_path_heads.append(new_head)
                except:
                    pass
                
                #move down
                try:
                    if head[2] == walls[(head[0], head[1] + 0.5)] or head[3] == walls[(head[0], head[1] + 0.5)]:
                        new_head = (head[0], head[1]+1, head[2], head[3])
                        try:
                            if seen_heads[new_head] == True:
                                pass
                        except:
                            seen_heads[new_head] = True
                            new_path_heads.append(new_head)
                except:
                    pass
                
                #change top
                if cells[(head[0], head[1])][1] != 0 and cells[(head[0], head[1])][1] != head[3]:
                    new_head = (head[0], head[1], head[2], cells[(head[0], head[1])][1])
                    try:
                        if seen_heads[new_head] == True:
                            pass
                    except:
                        seen_heads[new_head] = True
                        new_path_heads.append(new_head)
                        
                #change bottom
                if cells[(head[0], head[1])][0] != 0 and cells[(head[0], head[1])][0] != head[2]:
                    new_head = (head[0], head[1], cells[(head[0], head[1])][0], head[3])
                    try:
                        if seen_heads[new_head] == True:
                            pass
                    except:
                        seen_heads[new_head] = True
                        new_path_heads.append(new_head)

                if head[0] == WIDTH-1 and head[1] == HEIGHT-1:
                    #print("length:",length)
                    return length
                        
                
            if len(new_path_heads) <= 0:
                #print("Dead end")
                return 0
            
            path_heads = new_path_heads.copy()

            length += 1
    
def create_mazes():
    solution_length = 0
    mazes = 0
    for i in range(iterations):
        if i % 100000 == 0:
            print(str(int(i/iterations*100))+"%")
        mazes += 1
        
        cells = {}
        walls = {}
        cells,walls = generate_random_maze(cells, walls)

        walls[(0.5, 0.0)] = 1
        
        
        solution_length = test_maze(cells, walls)

        if solution_length != 0:
            try:
                stored_mazes[solution_length]
            except:
                stored_mazes[solution_length] = Maze(cells, walls, solution_length)
                print("NEW MAZE:", solution_length)
    
    print("took",mazes,"mazes")





decode_mazes()
create_mazes()
encode_mazes()
