class Agent:
    
    def __init__(self,x,y):
        
        self.posx = x #position du robot sur l'axe x
        self.posy = y #position du robot sur l'axe y
        self.dbag_dirt = 0 #nombre de poussiere dans le sac a poussiere
        self.dbag_jewel = 0 #nombre de bijoux dans le sac a poussiere
        self.jbag = 0 #nombre de bijoux dans le sac a bijou
        self.energy = 0 #energie consommee

    def aspire(self,e): #aspire le contenu de la piece dans le sac a poussiere
        
        if e.hmap[self.posx][self.posy] == 1:
            self.dbag_dirt = self.dbag_dirt + 1
        
        elif e.hmap[self.posx][self.posy] == 2:
            self.dbag_jewel = self.dbag_jewel + 1
        
        elif e.hmap[self.posx][self.posy] == 3:
            self.dbag_dirt = self.dbag_dirt + 1
            self.dbag_jewel = self.dbag_jewel + 1
        
        #todo: mettre a jour l'etat de la piece
        self.energy = self.energy +1
        
        
    def grab(self,e): #ramasse le contenu de la piece dans le sac a bijou

        if e.hmap[self.posx][self.posy] == 2 or e.hmap[self.posx][self.posy] == 3:
            self.jbag = self.jbag + 1
        #todo: mettre a jour l'etat de la piece
            
        self.energy = self.energy + 1
        
        
    def move(self,direction,e): #se deplace dans la direction voulue
        
        if direction == up and self.posy < len(e.y):
            self.posy = self.posy + 1
            
        elif direction == down and self.posy > 0:
            self.posy = self.posy - 1
        
        elif direction == left and self.posx > 0:
            self.posy = self.posx + 1
        
        elif direction == right and self.posx < len(e.x):
            self.posy = self.posx - 1
            
        else:
            print("Invalid moving order")
        
        self.energy = self.energy + 1
        
        
class Captor:
    def __init__(self):
        print("todo")
    
class Effector:
    def __init__(self):
        print("todo")
    
    

        
