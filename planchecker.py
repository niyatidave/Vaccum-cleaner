import starter as s

def next_move(cord, map, direction):
    # return next possible cordinate
    x, y = cord
    if direction == 'N' and map[x-1][y] != 'X':
        return (x-1, y)

    elif direction == 'E' and map[x][y+1] != 'X':
        return (x, y+1)

    elif direction == 'S' and map[x+1][y] != 'X':
        return (x+1, y)

    elif direction == 'W' and map[x][y-1] != 'X':
        return (x, y-1)

    return cord

def implement_plan(start_cord, plan, room, map):
    # clean as plan
    croom = room.copy()
    croom.remove(start_cord)
    for p in plan:
        ncord = next_move(start_cord, map, p)
        start_cord = ncord
        if start_cord in croom:
            croom.remove(start_cord)

    return croom

def check_plan_with_cleaner(ww):
    for k, v in ww.wpos.items():
        croom = implement_plan(v, ww.plans, ww.rooms[k], ww.map)
        if len(croom) > 0:
            print("BAD PLAN", croom)
        else:
            print("GOOD PLAN", croom)
