import random
import constants

class Environment:
    
    def __init__(self,size):
        self.x, self.y = size, size #cree un tableau carré d'une taille fixée
        self.hmap = [[Room(i+1,j+1) for i in range(size)] for j in range(size)]
        #for i in range(size): #on initialise les instances des pièces
        #    for j in range(size):
        #        self.hmap[i][j] = Room(i+1,j+1) #note: les pièces vont de 1 à size, le tableau hmap de 0 à size-1
        for i in range(size): #on initialise les voisins des pièces
            for j in range(size):
                nb_neighbors = 0
                neighbors = []
                if i > 0:
                    if j > 0:
                        neighbors.append(self.hmap[i-1][j-1])
                        nb_neighbors = nb_neighbors + 1
                    if j < size-1:
                        neighbors.append(self.hmap[i-1][j+1])
                        nb_neighbors = nb_neighbors + 1
                if i < size-1:
                    if j > 0:
                        neighbors.append(self.hmap[i+1][j-1])
                        nb_neighbors = nb_neighbors + 1
                    if j < size-1:
                        neighbors.append(self.hmap[i+1][j+1])
                        nb_neighbors = nb_neighbors + 1
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
            
        if self.hmap[x][y].value == constants.DUST_AND_JEWEL:
            pass #ne rien faire
                
        elif self.hmap[x][y].value == constants.JEWEL:
            self.hmap[x][y].value = constants.DUST_AND_JEWEL
        else:
            self.hmap[x][y].value = constants.DUST
        
        
    def genjewel(self):
        
        x = random.randint(0,9)
        y = random.randint(0,9)
        
        if self.hmap[x][y].value == constants.DUST_AND_JEWEL:
            pass #ne rien faire
            
        elif self.hmap[x][y].value == constants.DUST:
            self.hmap[x][y].value = constants.DUST_AND_JEWEL
            
        else:
            self.hmap[x][y].value = constants.JEWEL
            
    def display(self):
        
        for i in range(self.x):
            line = ""
            for j in range(self.y):
                # print("Ligne ", i+1, "; Colonne ", j+1, "; Value ", self.hmap[i][j].value, ";")
                if(self.hmap[i][j].value == constants.NOTHING): line += "-"
                elif(self.hmap[i][j].value == constants.JEWEL): line += "J"
                elif(self.hmap[i][j].value == constants.DUST): line += "D"
                elif(self.hmap[i][j].value == constants.DUST_AND_JEWEL): line += "B" # B pour both
                line += " "
            print(line)
        print("")

class Room:
    def __init__(self,posx,posy):
        self.x=posx
        self.y=posy
        self.nb_neighbors = 0
        self.neighbors = []
        self.value = constants.NOTHING
        
    def set_neighbors(self,neighbors,nb_neighbors):
        self.nb_neighbors=nb_neighbors
        for i in range(nb_neighbors):
            self.neighbors.append(neighbors[nb_neighbors-1])
        
    def getValue(self):
        return self.value

    def clean(self):
        self.value = constants.NOTHING

    def removeJewel(self):
        if(self.value == constants.JEWEL): self.value = constants.NOTHING
        elif(self.value == constants.DUST_AND_JEWEL): self.value = constants.DUST
        
