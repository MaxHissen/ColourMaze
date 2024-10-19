WIDTH = 4  # < 10
HEIGHT = 4 # < 10

class Maze:
    def __init__(self, cells, walls, length):
        self.cells = cells
        self.walls = walls
        self.length = length

def solve_maze(maze_code):
        maze = decode_maze(maze_code)

        path_heads = [(0,0,0,0,"")] #xpos ypos bottomcolour topcolour
        seen_heads = {}
        length = 0
        while True:
            new_path_heads = []
            for head in path_heads:
                #move right
                try:
                    if head[2] == maze.walls[(head[0] + 0.5, head[1])] or head[3] == maze.walls[(head[0] + 0.5, head[1])]:
                        new_head = (head[0]+1, head[1], head[2], head[3], head[4]+"R")
                        try:
                            if seen_heads[(new_head[0], new_head[1], new_head[2], new_head[3])] == True:
                                pass
                        except:
                            seen_heads[(new_head[0], new_head[1], new_head[2], new_head[3])] = True
                            new_path_heads.append(new_head)
                except:
                    pass
                
                #move left
                try:
                    if head[2] == maze.walls[(head[0] - 0.5, head[1])] or head[3] == maze.walls[(head[0] - 0.5, head[1])]:
                        new_head = (head[0]-1, head[1], head[2], head[3], head[4]+"L")
                        try:
                            if seen_heads[(new_head[0], new_head[1], new_head[2], new_head[3])] == True:
                                pass
                        except:
                            seen_heads[(new_head[0], new_head[1], new_head[2], new_head[3])] = True
                            new_path_heads.append(new_head)
                except:
                    pass
                
                #move up
                try:
                    if head[2] == maze.walls[(head[0], head[1] - 0.5)] or head[3] == maze.walls[(head[0], head[1] - 0.5)]:
                        new_head = (head[0], head[1]-1, head[2], head[3], head[4]+"U")
                        try:
                            if seen_heads[(new_head[0], new_head[1], new_head[2], new_head[3])] == True:
                                pass
                        except:
                            seen_heads[(new_head[0], new_head[1], new_head[2], new_head[3])] = True
                            new_path_heads.append(new_head)
                except:
                    pass
                
                #move down
                try:
                    if head[2] == maze.walls[(head[0], head[1] + 0.5)] or head[3] == maze.walls[(head[0], head[1] + 0.5)]:
                        new_head = (head[0], head[1]+1, head[2], head[3], head[4]+"D")
                        try:
                            if seen_heads[(new_head[0], new_head[1], new_head[2], new_head[3])] == True:
                                pass
                        except:
                            seen_heads[(new_head[0], new_head[1], new_head[2], new_head[3])] = True
                            new_path_heads.append(new_head)
                except:
                    pass
                
                #change top
                if maze.cells[(head[0], head[1])][1] != 0 and maze.cells[(head[0], head[1])][1] != head[3]:
                    new_head = (head[0], head[1], head[2], maze.cells[(head[0], head[1])][1], head[4]+"T")
                    try:
                        if seen_heads[(new_head[0], new_head[1], new_head[2], new_head[3])] == True:
                            pass
                    except:
                        seen_heads[(new_head[0], new_head[1], new_head[2], new_head[3])] = True
                        new_path_heads.append(new_head)
                        
                #change bottom
                if maze.cells[(head[0], head[1])][0] != 0 and maze.cells[(head[0], head[1])][0] != head[2]:
                    new_head = (head[0], head[1], maze.cells[(head[0], head[1])][0], head[3], head[4]+"B")
                    try:
                        if seen_heads[(new_head[0], new_head[1], new_head[2], new_head[3])] == True:
                            pass
                    except:
                        seen_heads[(new_head[0], new_head[1], new_head[2], new_head[3])] = True
                        new_path_heads.append(new_head)

                if head[0] == WIDTH-1 and head[1] == HEIGHT-1:
                    #print("length:",length)
                    return length, head[4]
                        
                
            if len(new_path_heads) <= 0:
                #print("Dead end")
                return 0
            
            path_heads = new_path_heads.copy()

            length += 1

    
def decode_maze(maze_code):
    cells = maze_code.split("|")[0]
    walls = maze_code.split(":")[0]
    walls = walls.split("|")[1]
    length = int(maze_code.split(":")[1])

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


    maze_to_test = Maze(maze_cells,maze_walls,length)
            
    return maze_to_test

maze_code = str(input("Enter maze code: "))
length, path = solve_maze(maze_code)
print("Solution Length",length)
print(path)
