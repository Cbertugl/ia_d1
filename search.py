#!/usr/bin/python

import constants
import random
import time

'''
Returns a random serie of 20 actions
'''
def mockSearch():
    time.sleep(2) # Simulate exploration time
    intentions = []
    for i in range(20):
        rand = random.randint(0, 6)
        if(rand == 0): action = constants.VACUUM
        elif(rand == 1): action = constants.GRAB_JEWEL
        elif(rand == 2): action = constants.MOVE_UP
        elif(rand == 3): action = constants.MOVE_DOWN
        elif(rand == 4): action = constants.MOVE_LEFT
        elif(rand == 5): action = constants.MOVE_RIGHT
        elif(rand == 6): action = constants.DO_NOTHING
        intentions.append(action)

    return intentions

def breadthFirstSearch(starting_room):
    intentions = []
    explored = []
    queue = [starting_room] #file à explorer
    
    time.sleep(2)

    while queue: #tant qu'il nous reste quelque chose à explorer
        current_room = queue.pop()
        explored.append(current_room)
        #print("Infinity 1")
        
        if current_room.getValue() != constants.NOTHING : #si on trouve notre but, on arrête l'exploration
            #on se déplace jusqu'à la bonne ligne puis la bonne colonne
            intentions = getIntentionsFromGoal(starting_room, current_room)
            break
            
        else: #sinon on rajoute les pièces voisines dans le file
            for i in range(len(current_room.neighbors)):
                #print("Balise X")
                if current_room.neighbors[i] not in explored : queue.append(current_room.neighbors[i])

    return intentions


def aStarSearch(starting_room): #pas fini
    intentions = []
    queue = [starting_room]
    pqueue = [O]
    cost = 0
    
    while queue:
        index=pqueue.index(min(pqueue))
        current_room = queue.pop(index)
        pqueue.pop(index)
        
        if current_room != constants.NOTHING:
            intentions = getIntentionsFromGoal(starting_room, current_room)
            break
        
        else:
            for i in range(current_room.neighbors):
                predicted_cost = cost + 1 + heuristic(starting_room,current_room.neighbors[i]) # a modifier
                
                queue.append(current_room.neighbors[i])
                pqueue.append(predicted_cost)
            cost = cost + 1
          
    return intentions
    
def heuristic(starting_room, goal_room):
    return abs(goal_room.line-starting_room.line) + abs(goal_room.row-starting_room.row)

def getIntentionsFromGoal(starting_room, goal_room):
    intentions = []
    current_room=starting_room
    
    while current_room != goal_room:
        #print("Infinity 2")
        
        if current_room.line < goal_room.line: 
            intentions.append(constants.MOVE_DOWN)
            for i in range(len(current_room.neighbors)):
                if current_room.line < current_room.neighbors[i].line : next_room = current_room.neighbors[i]
            current_room = next_room
        elif current_room.line > goal_room.line: 
            intentions.append(constants.MOVE_UP)
            for i in range(len(current_room.neighbors)):
                if current_room.line > current_room.neighbors[i].line : next_room = current_room.neighbors[i]
            current_room = next_room
        else:
            if current_room.row < goal_room.row: 
                intentions.append(constants.MOVE_RIGHT)
                for i in range(len(current_room.neighbors)):
                    if current_room.row < current_room.neighbors[i].row : next_room = current_room.neighbors[i]
                current_room = next_room
            elif current_room.line > goal_room.line: 
                intentions.append(constants.MOVE_LEFT)
                for i in range(len(current_room.neighbors)):
                    if current_room.row > current_room.neighbors[i].row : next_room = current_room.neighbors[i]
                current_room = next_room

        
    if goal_room.getValue() == constants.DUST : intentions.append(constants.VACUUM)
    elif goal_room.getValue() == constants.JEWEL : intentions.append(constants.GRAB_JEWEL)
    elif goal_room.getValue() == constants.DUST_AND_JEWEL : 
        intentions.append(constants.GRAB_JEWEL)
        intentions.append(constants.VACUUM)

    return intentions
