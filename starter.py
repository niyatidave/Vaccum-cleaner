class WumpusWorld:
    def __init__(self, ptype, map, rooms, wpos = None, plans = None):
        self.wpos = wpos
        self.ptype = ptype
        self.map = map
        self.plans = plans
        self.rooms = rooms


def loadWW(filename):
    with open(filename, "r", encoding = 'utf-8') as f:
        lines = f.readlines()
        first_line = lines[0]
        wpos = None
        # check file for problem type
        if first_line.strip().replace(" ", "") == "CHECKPLAN":
            # all read logic for check plan
            plans = lines[1].strip() # second line plans
            map = []
            for i in range(2, len(lines)):
                if 'S' in lines[i]:
                    wpos = ()
                map.append(list(lines[i].strip()))

            #TODO: update room number into map

            return WumpusWorld("CHECKPLAN", map=map, )
        else:
            
    pass

if __name__ == "__main__":
    ww = loadWW('example-problem060.txt')