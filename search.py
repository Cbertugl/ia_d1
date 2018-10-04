#!/usr/bin/python

def breadth_first_search(starting_room, goal_room):
    path = [] #chemin parcouru
    queue = [starting_room] #file à explorer
    while not queue.empty(): #tant qu'il nous reste quelque chose à explorer
        current_room = queue.pop()
        path.append(current_room)
        if current_room == goal_room: #si on trouve notre but, on arrête l'exploration
            break
        else: #sinon on rajoute les pièces voisines dans le file
            for i in current_room.nb_neighbors:
                queue.append(current_room.neighbors[i])
    return path


def a_star_search(starting_room, goal_room): #pas fini
    path = []
    queue = [starting_room]
    cost= abs(goal_room.x-starting_room.x) + abs(goal_room.x-starting_room.x)
    
    while not queue.empty():
        current_room = queue.pop()
        path.append(current_room)
        cost = cost + 1 #poids uniforme pour chaque pièce 
        if current_room == goal_room:
            break
        else:
            for i in current_room.nb_neighbors:
                queue.append(current_room.neighbors[i])
                #ordonnancer l'append en fonction d'un coût prédit sur l'heuristique
                # => créer une nouvelle fnction comme append avec une notion de priorité ?
            
    return path
    
