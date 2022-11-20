import starter
import planchecker as pc
import copy
import random

def next_valid_move(map, cpos, room):
    x, y = cpos
    vmoves = [n for n in starter.get_neighbours(x, y) if n in room]
    for move in vmoves:
        x, y = move
        if map[x][y] != 'C':
            return move
    return random.choice(vmoves)

def get_direction_by_move(pmove, nmove):
    x1, y1 = pmove
    x2, y2 = nmove
    if x2 - x1 == 1 and y2 - y1 == 0:
        return 'S'
    elif x1 - x2 == 1 and y1 - y2 == 0:
        return 'N'
    elif x1 - x2 == 0 and y2 - y1 == 1:
        return 'E'
    elif x1 - x2 == 0 and y1 - y2 == 1:
        return 'W'

def find_plan_with_cleaner_position(map, cpos, room):
    cmap = copy.deepcopy(map)
    croom = copy.deepcopy(room)
    x, y = cpos
    croom.remove(cpos)
    cmap[x][y] = 'C'
    plan = ""
    while len(croom) > 0: # goal state will be all tile is cleaned
        nmove = next_valid_move(cmap, cpos, room)
        x, y = nmove
        plan += get_direction_by_move(cpos, nmove)
        if cmap[x][y] != 'C':
            cmap[x][y] = 'C'
            croom.remove(nmove)
        cpos = nmove

    return plan

def find_plan(ww):
    map = ww.map
    # check if position not avaliable
    # call method with one position
    ncleaner = len(ww.wpos)
    if ncleaner == 1:
        cpos = list(ww.wpos.values())[0]
        room = list(ww.rooms.values())[0]
        return find_plan_with_cleaner_position(map, cpos, room)
    elif ncleaner == 2:
        # two cleaner means two rooms
        #TODO: please do for two rooms
        pass
    elif ncleaner == 0:
        # now room number might be one or two
        if len(ww.rooms) == 1:
            room = list(ww.rooms.values())[0]
            rcpos = random.choice(list(room))
            return find_plan_with_cleaner_position(map, rcpos, room)
        elif len(ww.rooms) == 2:
            #TODO: Please do for two diff rooms
            pass

    else:
        return "Something went wrong!"