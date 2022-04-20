import math
from queue import PriorityQueue

def shortest_path(M,start,goal):
    print("shortest path called")
    frontier = PriorityQueue()
    frontier_hash = set() # keep track of nodes in frontier
    frontier.put((0,start)) # start node initialized to priority queue
    frontier_hash.add(start) 
    came_from = {} # keep track of previous nodes so as to reconstruct the path at the end
    g_score = {i:math.inf for i in range(len(M.roads))}
    g_score[start] = 0
    
    f_score = {i:math.inf for i in range(len(M.roads))}
    f_score[start] = h(start,goal,M)
    
    while not frontier.empty():
        current_node = frontier.get()[1]
        frontier_hash.remove(current_node)
        
        if current_node == goal:
            return reconstruct_path(came_from,current_node)
        
        for neighbor in M.roads[current_node]:
            tent_g_score = g_score[current_node] + euclidian_distance(M.intersections[current_node],M.intersections[neighbor])
            if tent_g_score < g_score[neighbor]:
                g_score[neighbor] = tent_g_score
                came_from[neighbor] = current_node
                f_score[neighbor] = g_score[neighbor] + h(neighbor,goal,M)
                if neighbor not in frontier_hash:
                    frontier.put((f_score[neighbor],neighbor))
                    frontier_hash.add(neighbor)
    return False

def euclidian_distance(intersection_1,intersection_2):
    return math.sqrt(abs((intersection_1[0] - intersection_2[0]))**2 + abs((intersection_1[1] - intersection_2[1]))**2) 


def h(node,goal,M):
    intersection_1 = M.intersections[node]
    intersection_2 = M.intersections[goal]
    return euclidian_distance(intersection_1,intersection_2)
    
    
def reconstruct_path(came_from,current_node):
    path = []
    path.append(current_node)
    while current_node in came_from.keys():
        current_node = came_from[current_node]
        path.append(current_node)
    path.reverse()
    return path


# Algorithm inspired by pseudo_code provided at https://en.wikipedia.org/w/index.php?title=A*_search_algorithm&oldid=1073628314
# accesed on 2022-04-06, 3:45:15 PM