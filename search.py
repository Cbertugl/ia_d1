#!/usr/bin/python

import constants
import random
import time

# ==================================================================================================
# EXPLORATION - SEARCH
# ==================================================================================================

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


'''
Returns a list of action to either clean dirt, grab a jewel or both with the Bread First Search method
'''
def breadthFirstSearch(starting_room):
    
    intentions = []             # Contain the chain of action to transfer
    explored = []               # Contain the list of explored rooms
    queue = [starting_room]     # Contain the list of room to explore

    time.sleep(2)               # Simulate exploration time

    # While the queue is not empty
    while queue: 
        
        # We pop the next room to check and append it to the list of explored rooms
        current_room = queue.pop()
        explored.append(current_room)
        
        # We check if there is something in the room (either dust or jewel)
        if current_room.getValue() != constants.NOTHING :
            
            # If so we then call a function to get the chain of action requiered to clean the room and break the while
            intentions = getIntentionsFromGoal(starting_room, current_room)
            break
            
        # Else we add every non-explored neighbors to the queue    
        else:
            for i in range(len(current_room.neighbors)):
                if current_room.neighbors[i] not in explored : queue.append(current_room.neighbors[i])
    
    # We return the intentions of the robot, which are void if the whole mansion is clean
    return intentions


'''
Returns a list of action to either clean dirt, grab a jewel or both with the A* Search method
'''
def aStarSearch(starting_room):
    
    intentions = []             # Contain the chain of action to transfer
    explored = []               # Contain the list of explored rooms
    queue = [starting_room]     # Contain the list of room to explore
    pqueue = [0]                # Contain the priority of each element of the queue
    cost = 0                    # Keep track of the current cost

    time.sleep(2)               # Simulate exploration time

    # While the queue is not empty
    while queue:
        
        # We pop the room stored at the index with the lowest priority score (so high priority for us), appent it to the list of explored room and pop the priority value out of the priority queue
        index=pqueue.index(min(pqueue))
        current_room = queue.pop(index)
        pqueue.pop(index)
        explored.append(current_room)
        
        # We check if there is something in the room (either dust or jewel)
        if current_room.getValue() != constants.NOTHING:
            
            # If so we then call a function to get the chain of action requiered to clean the room and break the while
            intentions = getIntentionsFromGoal(starting_room, current_room)
            break
        
        # Else we add every non-explored neighbors to the queue while giving them a priority score
        else:
            for i in range(len(current_room.neighbors)):
                if current_room.neighbors[i] not in explored :
                    
                    # The priority is based on the cost, iteslf based on the both the cost of movement (always 1) and the heuristic. Here the heuristic helps rooms close to the starting_room to find the closest dirt or jewel thus maximizing the score while lowering the electric cost
                    predicted_cost = cost + 1 + heuristic(starting_room,current_room.neighbors[i]) # a modifier
                    queue.append(current_room.neighbors[i])
                    pqueue.append(predicted_cost)
            
            # We keep track of the cost by incrementing it each time we explore another room
            cost = cost + 1
          
    # We return the intentions of the robot, which are void if the whole mansion is clean      
    return intentions


'''
Return the heuristic for a room regarding a goal
'''    
def heuristic(starting_room, goal_room):
    
    # We return the Taxi distance of the two room
    return abs(goal_room.line-starting_room.line) + abs(goal_room.row-starting_room.row)


'''
Returns a list of action to reach a goal room
This fonction only align the robot on the goal line, then align the robot on the goal row (therefore the robot is in the goal room) and to decide whether to vacuum or grab
'''
def getIntentionsFromGoal(starting_room, goal_room):
    
    intentions = []                 # Contain the chain of action to transfer
    current_room=starting_room      # Keep track of the current room to move accordingly

    # While the robot hasn't reach his goal
    while current_room != goal_room:

        # If the robot is higher than the goal, he moves down one case each time until he is on the same line
        if current_room.line < goal_room.line: 
            intentions.append(constants.MOVE_DOWN)
            for i in range(len(current_room.neighbors)):
                if current_room.line < current_room.neighbors[i].line : next_room = current_room.neighbors[i]
            current_room = next_room
            
        # If the robot is lower than the goal, he moves up one case each time until he is on the same line
        elif current_room.line > goal_room.line: 
            intentions.append(constants.MOVE_UP)
            for i in range(len(current_room.neighbors)):
                if current_room.line > current_room.neighbors[i].line : next_room = current_room.neighbors[i]
            current_room = next_room
        
        # If we are neither higher nor lower than the goal, we are on the same line
        else:
            
            # Then if the robot is to the left of the goal, he moves right one case each time until he is on the same row
            if current_room.row < goal_room.row: 
                intentions.append(constants.MOVE_RIGHT)
                for i in range(len(current_room.neighbors)):
                    if current_room.row < current_room.neighbors[i].row : next_room = current_room.neighbors[i]
                current_room = next_room
                
             # Or if the robot is to the right of the goal, he moves left one case each time until he is on the same row   
            elif current_room.row > goal_room.row: 
                intentions.append(constants.MOVE_LEFT)
                for i in range(len(current_room.neighbors)):
                    if current_room.row > current_room.neighbors[i].row : next_room = current_room.neighbors[i]
                current_room = next_room
                
            # The robot is now on the same line and row than the goal, thus the robot is in the goal room

    # The robot decide to vacuum the room or grab a jewel on the floor depending on the stage of the room
    if goal_room.getValue() == constants.DUST : intentions.append(constants.VACUUM)
    elif goal_room.getValue() == constants.JEWEL : intentions.append(constants.GRAB_JEWEL)
    elif goal_room.getValue() == constants.DUST_AND_JEWEL : 
        intentions.append(constants.GRAB_JEWEL)
        intentions.append(constants.VACUUM)
    
    # The chain of commands is now returned to the robot intentions system
    return intentions
