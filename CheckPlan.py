import sys
import numpy as np
import collections

global clean_list
clean_list = []
global paths
paths=[]

def reset_clean_list():
    del clean_list[:]

def reset_paths():
    del paths[:]

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
    return grid_world, start_r,start_c, N, dirt_locations

def move_plan2(plan1, r, c, grid_world):
    temp_r, temp_c, actio = move(r, c, plan1)
    #print(temp_r,temp_c)


    #print(temp_r, temp_c)
    if temp_r<12 and temp_c<16:
        if grid_world[temp_r][temp_c] == ' ':
            clean_list.append((temp_r, temp_c))
            paths.append(actio)
            return temp_r,temp_c
            #print(clean_list)
    #print(r,c)
    return r,c


def create_goal_state(data):
    copy_map = []
    grid_map, r, c, N, dirt_list = map(grid_world_raw)

    for r in range(0, len(data)):
        line = []
        copy_map.append(line)
        for c in range(0, len(data[r])):
            if data[r][c].isdigit():
                line.append(' ')
            else:
                line.append(data[r][c])
    return copy_map
#goal_state = create_goal_state(grid_world)

class Node:
    def find_path(self):
        def reverse_list(got_list):
            temp = []
            while got_list:
                temp.append(got_list.pop())
            return temp

        path = [self.action]
        current_node = self.parent
        while current_node.parent is not None:
            path.append(current_node.action)
            current_node = current_node.parent
        return reverse_list(path)

def move(r, c, action):

    if action == 'N':
        r = r-1
        c = c
        actio = 'N'
    if action == 'S':
        r = r+1
        c = c
        actio ='S'
    if action == 'E':
        r = r
        c = c+1
        actio ='E'
    if action == 'W':
        r = r
        c = c-1
        actio ='W'
    return r, c, actio

def action_(plan, grid_world, r, c):
    temp_r=r
    temp_c=c
    for i in range(len(plan)):
        #print(i)
        temp_r, temp_c=move_plan2(plan[i], temp_r, temp_c, grid_world)
        #print(temp_r,temp_c)

def readInput():
    f = open('matrix.txt', 'r')
    list = f.readlines()
    list1 = np.array(list)
    #print(list1)
    if list1[0] == 'CHECK PLAN\n':
        plane=list1[1][:-1]
        grid_world_raw= list1[2:]
        grid_map, r, c,N, dirt_list = map(grid_world_raw)
        #print(r)
        #print(dirt_list[6][1])
        if r== None:
            #r=dirt_list[0][0]
            #c=dirt_list[0][1]
            x = np.array(grid_map)

            listofgrp = find_groups(x)
            #print(listofgrp)
            #global res
            res= []
            t_paths=[]
            for i in listofgrp:
                reset_clean_list()
                reset_paths()
                action_(plane,grid_map,i[0],i[1])
                #print(clean_list)
                a= clean_list
                a.append((i[0],i[1]))
                #print(a)
                res.append(a)

                #print(clean_list)
            print(res[0])
            good_plan=[]
            bad_plan=[]
            for i in res:
                g=[]

                [g.append(x) for x in i if x not in g]
                #print(g)
                #print(collections.Counter(dirt_list),collections.Counter(g))
                if collections.Counter(dirt_list) == collections.Counter(g):
                    good_plan.append('GOOD PLAN')
                    print("GOOD PLAN")
                else:
                    l3 = [x for x in dirt_list if x not in g]
                    bad_plan.append(l3)
                    print("BAD PLAN")
                    #print(l3)
            print(good_plan,min(bad_plan, key=len))


        else:
            action_(plane,grid_map,r,c)
            #(action_(plane,grid_map,r,c))
            #print(dirt_list)
            #print(grid_world_raw)
            print(paths)
            if collections.Counter(dirt_list) == collections.Counter(clean_list):
                print("GOOD PLAN")
            else:
                l3 = [x for x in dirt_list if x not in clean_list]
                print("BAD PLAN")
                print(l3)
        #print(N)

        #print(grid_world_raw)

    elif list1[0] == 'FIND PLAN\n':
        grid_world=list1[1:]
        plane = list1[1][:-1]
        grid_world_raw = list1[1:]
        grid_map, r, c, N, dirt_list = map(grid_world_raw)
        #bfs(r,c)
        b=create_goal_state(grid_world_raw)
        print(b)


def bfs(r,c):
    print(r,c)
    visited = []
    queue = [r,c]
    while queue:
        current_node = queue.pop(0)

        if current_node.state[1] == goal_state:
            return len(visited), current_node.find_path(), current_node.cost

        if current_node.state not in visited:
            visited.append(current_node.state)

        children = actions(current_node)




def find_groups(x, min_size=3, value=' '):
  # Compute a sequential label for groups in each row.
  xc = (x != value).cumsum(1)

  # Count the number of occurances per group in each row.
  counts = np.apply_along_axis(
      lambda x: np.bincount(x, minlength=1 + xc.max()),
      axis=1, arr=xc)

  # Filter by minimum number of occurances.
  i, j = np.where(counts >= min_size)

  # Compute the median index of each group.
  return [
    (ii, int(np.ceil(np.median(np.where(xc[ii] == jj)[0]))))
    for ii, jj in zip(i, j)
  ]

f = open('matrix.txt', 'r')
list = f.readlines()
list1 = np.array(list)
plane=list1[1][:-1]
grid_world_raw= list1[2:]
grid_map, r, c,N, dirt_list = map(grid_world_raw)



readInput()
