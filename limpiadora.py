import time
import random



class Place:
    def __init__ (self,par_location,par_dirty):
        self.location = par_location
        if(par_dirty == 1):
            self.status = 'Dirty'
        else:
            self.status = 'Clean'


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
            if(arr[self.i][self.j].status == 'Dirty'):
                self.suck(arr)
            elif (arr[self.i][self.j].location == 'A'):
                self.right()
            else:
                self.left()
        self.restart()
        
    def suck(self,arr):
        arr[self.i][self.j].status = 'Clean'
        return
    
    def restart(self):
        self.i = 0
        self.j = 0
        
def PrintMatrix(matrix):
    for row in matrix:
        for Lugar in row:
            print(Lugar.status)
    
    
matrix=[]

def generateRandom():
    return random.randint(0,1)

def getDirt():
    for i in range(0,4):
        matrix.append([Place('A',generateRandom()),Place('B',generateRandom())])
    return matrix

agent = Agent()

for j in range(0,4):
    matrix = getDirt()
    matrix[0][0].status = 'Dirty'
    print("Antes de limpiar")
    PrintMatrix(matrix)
    starting_point = time.time()
    agent.clean(matrix)
    elapsed_time = time.time () - starting_point
    print("Despues de limpiar, y tardo",elapsed_time,"segundos")
    PrintMatrix(matrix)
    print("Corrida numero",j)
    matrix=[]
    

