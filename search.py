#!/usr/bin/python

def breadth_first_search(starting_room):
    path = [] #chemin parcouru
    queue = [starting_room] #file à explorer
    while not queue.empty(): #tant qu'il nous reste quelque chose à explorer
        current_room = queue.pop()
        path.append(current_room)
        if current_room.value != 0: #si on trouve quelque chose, on retourne le chemin parcouru
            return path 
        else: #sinon on rajoute les pièces voisines
            for i in current_room.nb_neighbors:
                queue.append(current_room.neighbors[i])
    return starting_room #si on sort de la boucle sans rien trouver on retourne la pièce actuelle



def a_star_search(starting_room,goal_room): #pas fini
    path = []
    queue = [starting_room]
    cost=0
    
    while not queue.empty():
        current_room = queue.pop()
        path.append(current_room)
        cost= cost + 1 # + sqrt(xi-x)²+(yi-y)²
        if current_room.value != 0:
            break
        else:
            for i in current_room.nb_neighbors:
                queue.append(current_room.neighbors[i])
                #ordonnancer l'append en fonction d'un coût prédit sur l'heuristique
            
    return path
    
