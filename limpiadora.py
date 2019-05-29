import random
'''
0 limpio
1 sucio
7 clean
8 right
9 left
'''


class Agent:
    def __init__ (self):
        self.i = 0
        self.j = 0
    
    def left (self):
        self.j = 0
        self.i = self.i + 1
        return
    
    def right (self):
        self.j = 1
        return
        
    def clean (self,arr):
        while (self.i!=4):
            if(arr[self.i][self.j] == 1):
                self.suck(arr)
            elif (self.j == 0):
                self.right()
            else:
                self.left()
        self.restart()
        
    def suck(self,arr):
        arr[self.i][self.j] = 0
        return
    
    def restart(self):
        self.i = 0
        self.j = 0
        
matrix=[]

def generateRandom():
    return random.randint(0,1)

def getDirt():
    for i in range(0,4):
        matrix.append([generateRandom(),generateRandom()])
    return matrix

agent = Agent()

for j in range(0,4):
    matrix = getDirt()
    print(matrix)
    agent.clean(matrix)
    print(matrix)
    matrix=[]
