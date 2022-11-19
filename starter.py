import planchecker as pc

class WumpusWorld:
    def __init__(self, ptype, map, rooms, wpos = None, plans = None):
        self.wpos = wpos
        self.ptype = ptype
        self.map = map
        self.plans = plans
        self.rooms = rooms


def get_neighbours(x, y):
    return [(x+1, y), (x-1, y), (x, y-1), (x, y+1)]

def mark_connected_room(map, cord, room_num, rooms):
    x, y = cord
    if map[x][y] == " ":
        map[x][y] = room_num
    rooms.add(cord)
    conn_cords = get_neighbours(x, y)
    for cord in conn_cords:
        x, y = cord
        if map[x][y] == " " or map[x][y] == "S":
            mark_connected_room(map, cord, room_num, rooms)


def update_rooms(map):
    room_mapper = {}
    r = 1
    for i in range(len(map)):
        for j in range(len(map[0])):
            if map[i][j] == " ":
                #mark all connected nodes
                rooms = set()
                curr_room = f"R{r}"
                mark_connected_room(map, (i, j), curr_room, rooms)
                room_mapper[curr_room] = rooms
                r += 1

    return room_mapper

def loadWW(filename):
    with open(filename, "r", encoding = 'utf-8') as f:
        lines = f.readlines()
        first_line = lines[0]
        cpos = {}
        # check file for problem type
        if first_line.strip().replace(" ", "") == "CHECKPLAN":
            # all read logic for check plan
            plans = lines[1].strip() # second line plans
            map = []
            for i in range(2, len(lines)):
                map.append(list(lines[i].strip()))

            rooms = update_rooms(map)

            # update cleaner position
            for k, v in rooms.items():
                for cord in v:
                    x, y = cord
                    if map[x][y] == "S":
                        cpos[k] = cord

            return WumpusWorld("CHECKPLAN", map=map, rooms=rooms, wpos=cpos, plans=plans)
        else: # parsing for FIND PLANS
            map = []
            for i in range(1, len(lines)):
                map.append(list(lines[i].strip()))

            rooms = update_rooms(map)

            # update cleaner position
            for k, v in rooms.items():
                for cord in v:
                    x, y = cord
                    if map[x][y] == "S":
                        cpos[k] = cord

            return WumpusWorld("FINDPLAN", map=map, rooms=rooms, wpos=cpos)

if __name__ == "__main__":
    ww = loadWW('example-problem060.txt')
    pc.check_plan_with_cleaner(ww)