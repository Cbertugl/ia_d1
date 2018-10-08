import random
import constants

class Environment:
    # ==============================================================================================
    # CONSTRUCTOR
    # ==============================================================================================
    def __init__(self, size):
        self.__size = size
        self.hmap = [[Room(j+1,i+1) for i in range(size)] for j in range(size)]
        #for i in range(size): #on initialise les instances des pièces
        #    for j in range(size):
        #        self.hmap[i][j] = Room(i+1,j+1) #note: les pièces vont de 1 à size, le tableau hmap de 0 à size-1
        for i in range(size): #on initialise les voisins des pièces
            for j in range(size):
                neighbors = []
                if i > 0:
                    neighbors.append(self.hmap[i-1][j])
                if i < size-1:
                    neighbors.append(self.hmap[i+1][j])
                if j > 0:
                    neighbors.append(self.hmap[i][j-1])
                if j < size-1:
                    neighbors.append(self.hmap[i][j+1])   
                self.hmap[i][j].setNeighbors(neighbors)

    # ==============================================================================================
    # GETTERS AND SETTERS
    # ==============================================================================================
    def getSize(self):
        return self.__size
    
    def getRoom(self, line, row):
        return self.hmap[line - 1][row - 1]

    def getMap(self):
        return self.hmap

    # ==============================================================================================
    # GENERATORS
    # ==============================================================================================    
    
    '''
    One time generation to start the environment with some dirt and jewels
    '''
    def initElements(self):
        for i in range(15):
            self.gen()
            
    '''
    Generate either dust or jewel randomly
    '''
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
            
        if self.hmap[x][y].value == constants.DUST_AND_JEWEL: pass
        elif self.hmap[x][y].value == constants.JEWEL: self.hmap[x][y].value = constants.DUST_AND_JEWEL
        else: self.hmap[x][y].value = constants.DUST
        
        
    def genjewel(self):
        
        x = random.randint(0,9)
        y = random.randint(0,9)
        
        if self.hmap[x][y].value == constants.DUST_AND_JEWEL: pass
        elif self.hmap[x][y].value == constants.DUST: self.hmap[x][y].value = constants.DUST_AND_JEWEL
        else: self.hmap[x][y].value = constants.JEWEL
            
    # ==============================================================================================
    # DISPLAY
    # ==============================================================================================
    def display(self, robotLine = -1, robotRow = -1):
        for i in range(self.__size):
            line = ""
            for j in range(self.__size):
                if((self.hmap[i][j].line == robotLine) and (self.hmap[i][j].row == robotRow)): line += ">"
                elif((self.hmap[i][j].line == robotLine) and (self.hmap[i][j].row - 1 == robotRow)): line += ""
                else: line += " "

                if(self.hmap[i][j].getValue() == constants.NOTHING): line += "-"
                elif(self.hmap[i][j].getValue() == constants.JEWEL): line += "J"
                elif(self.hmap[i][j].getValue() == constants.DUST): line += "D"
                elif(self.hmap[i][j].getValue() == constants.DUST_AND_JEWEL): line += "B" # B pour both

                if((self.hmap[i][j].line == robotLine) and (self.hmap[i][j].row == robotRow)): line += "<"
            print(line)
        print("")

class Room:
    # ==============================================================================================
    # CONSTRUCTOR
    # ==============================================================================================
    def __init__(self, line, row):
        self.line = line
        self.row = row
        self.neighbors = []
        self.value = constants.NOTHING
     
    # ==============================================================================================
    # GETTERS AND SETTERS
    # ============================================================================================== 
    def setNeighbors(self,neighbors):
        for i in range(len(neighbors)):
            self.neighbors.append(neighbors[i])
        
    def getPosition(self):
        return (self.line, self.row)

    def getValue(self):
        return self.value

    def setValue(self, value):
        self.value = value
        
    # ==============================================================================================
    # ACTIONS
    # ==============================================================================================
    
    '''
    Void the room
    '''
    def clean(self):
        self.value = constants.NOTHING
    
    '''
    Remove only jewels in the room
    '''
    def removeJewel(self):
        if(self.value == constants.JEWEL): self.value = constants.NOTHING
        elif(self.value == constants.DUST_AND_JEWEL): self.value = constants.DUST
        
