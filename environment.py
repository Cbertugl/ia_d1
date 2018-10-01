import random

class Environment:
    
    def __init__(self):
        self.x, self.y = 10, 10; #cree un tableau 2D de 10 par 10
        self.hmap= [[0 for i in range(self.x)] for j in range(self.y)] #initialise le tableau a 0
        #on considere 0 = rien, 1 = poussiere, 2 = bijou, 3 = poussiere et bijou
        
    def gen(self):
        
        randomint = random.randint(0,10)
        
        if randomint < 6:
            pass #ne rien faire
            
        elif randomint <10:
            self.gendust
            
        else:
           self.genjewel 
        
    def gendust(self):
        
        x = random.randint(0,10)
        y = random.randint(0,10)
            
        if self.hmap[x][y] == 3:
            pass #ne rien faire
                
        elif self.hmap[x][y] == 2:
            self.hmap[x][y] = 3
        
        else:
            self.hmap[x][y] = 1
        
        
    def genjewel(self):
        
        x = random.randint(0,10)
        y = random.randint(0,10)
        
        if self.hmap[x][y] == 3:
            pass #ne rien faire
            
        elif self.hmap[x][y] == 1:
            self.hmap[x][y] = 3
            
        else:
            self.hmap[x][y] = 2
            
    def display(self):
        
        for i in range(self.x):
            for j in range(self.y):
                print("Ligne ", i+1, "; Colonne ", j+1, "; Value ", self.hmap[i][j], ";")
