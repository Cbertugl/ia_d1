import random

class Environment:
    
    def __init__(self,size):
        self.x, self.y = size, size; #cree un tableau carré d'une taille fixée
        for i in range(size): #on initialise les instances des pièces
            for j in range(size):
                self.hmap[i][j] = Room(i+1,j+1) #note: les pièces vont de 1 à size, le tableau hmap de 0 à size-1
        for i in range(size): #on initialise les voisins des pièces
            for j in range(size):
                nb_neighbors = 0
                if i > 0:
                    if j > 0:
                        neighbors.append(self.hmap[i-1][j-1])
                        nb_neighbors++
                    if j < size-1:
                        neighbors.append(self.hmap[i-1][j+1])
                        nb_neighbors++
                if i < size-1:
                    if j > 0:
                        neighbors.append(self.hmap[i+1][j-1])
                        nb_neighbors++
                    if j < size-1:
                        neighbors.append(self.hmap[i+1][j+1])
                        nb_neighbors++
                self.hmap[i][j].set_neighbors(neighbors,nb_neighbors)
        
    def gen(self):
        
        randomint = random.randint(1,10)
        
        if randomint < 6:
            pass #ne rien faire
            
        elif randomint <10:
            self.gendust()
            
        else:
            self.genjewel() 
        
    def gendust(self):
        
        x = random.randint(0,9)
        y = random.randint(0,9)
            
        if self.hmap[x][y].value == 3:
            pass #ne rien faire
                
        elif self.hmap[x][y].value == 2:
            self.hmap[x][y].value = 3
        else:
            self.hmap[x][y].value = 1
        
        
    def genjewel(self):
        
        x = random.randint(0,9)
        y = random.randint(0,9)
        
        if self.hmap[x][y].value == 3:
            pass #ne rien faire
            
        elif self.hmap[x][y].value == 1:
            self.hmap[x][y].value = 3
            
        else:
            self.hmap[x][y].value = 2
            
    def display(self):
        
        for i in range(self.x):
            for j in range(self.y):
                print("Ligne ", i+1, "; Colonne ", j+1, "; Value ", self.hmap[i][j].value, ";")

class Room:
    def __init__(self,posx,posy):
        self.x=posx
        self.y=posy
        self.nb_neighbors = 0
        self.neighbors = []
        self.value = 0 #on considere 0 = rien, 1 = poussiere, 2 = bijou, 3 = poussiere et bijou
        
    def set_neighbors(neighbors,nb_neighbors)
        self.nb_neighbors=nb_neighbors
        self.neighbors[neighbors[nb.neighbors-1] for i in range(nb_neighbors)]
        
        
        
