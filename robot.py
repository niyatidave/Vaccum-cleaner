import queue
import numpy as np

global clean_list
clean_list = []

def readInput():
    f = open('matrix.txt', 'r')
    list = f.readlines()
    list1 = np.array(list)

    if list1[0] == 'FIND PLAN\n':
        grid_world=list1[1:]
        plane = list1[1][:-1]
        grid_world_raw = list1[1:]
        grid_map, r, c, N, dirt_list = map(grid_world_raw)

def printMaze(maze, j, i,path=""):
    pos = set()
    for move in path:
        if move == "W":
            i -= 1

        elif move == "E":
            i += 1

        elif move == "N":
            j -= 1

        elif move == "S":
            j += 1
        pos.add((j, i))

    for j, row in enumerate(maze):
        for i, col in enumerate(row):
            if (j, i) in pos:
                print("+ ", end="")
            else:
                print(col + " ", end="")
        print()


def valid(maze, moves,j,i):

    for move in moves:
        if move == "W":
            i -= 1

        elif move == "E":
            i += 1

        elif move == "N":
            j -= 1

        elif move == "S":
            j += 1

        if not (0 <= i < len(maze[0]) and 0 <= j < len(maze)):
            return False
        elif (maze[j][i] == "X"):
            return False

    return True

def findEnd(maze, moves,j,i):
    for move in moves:
        if move == "W":
            i -= 1

        elif move == "E":
            i += 1

        elif move == "N":
            j -= 1

        elif move == "S":
            j += 1

    if maze[j][i] == "O":
        print("Found: " + moves)
        printMaze(maze,j,i, moves)
        return True

    return False

def map(grid_world_raw):
    start_r = None
    start_c = None

    N = 0  # Number of dirts in the grid world.

    dirt_locations = []
    grid_world = []
    for r in range(len(grid_world_raw)):
        line = []
        if grid_world_raw[r][-1] == '\n':
            grid_world_raw[r] = grid_world_raw[r][:-1]
        grid_world.append(line)
        for c in range(len(grid_world_raw[r])):
            line.append(grid_world_raw[r][c])
            if grid_world_raw[r][c] == 'S':
                grid_world[r][c] = ' '
                start_r = r
                start_c = c
                N += 1
                current_position = (r,c)
                dirt_locations.append((r, c))
                #print(current_position)
            if grid_world_raw[r][c] == ' ':
                dirt_locations.append((r, c))
                N += 1
    if start_r != None and start_c !=None:
        clean_list.append((start_r, start_c))
        #print(dirt_locations)
    return grid_world, start_r,start_c, N, dirt_locations

f = open('matrix.txt', 'r')
list = f.readlines()
list1 = np.array(list)
gride=list1[1:]
# MAIN ALGORITHM

nums = queue.Queue()
nums.put("")
add = ""
maze, r,c, N, dirt_loc = map(gride)
#print(dirt_loc)

while not findEnd(maze, add,r,c):

    add = nums.get()
    #print(add)
    for j in ["W", "E", "N", "S"]:
        put = add + j
        if valid(maze, put,r,c):
            nums.put(put)
