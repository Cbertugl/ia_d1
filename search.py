#!/usr/bin/python

def breadth_first_search(starting_room)
    path = []
    queue = [starting_room]
    nothing_found = 1
    while nothing_found:
        current_room = queue.pop
        path.append(current_room)
        if current_room.value == 0
            for i in current_room.nb_neighbors
                queue.append(current_room.neighbors[i])
        else
            nothing_found = 0
    return path

def a_star_search(starting_room)
    
