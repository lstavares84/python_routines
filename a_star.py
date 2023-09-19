# PPGIa PUCPR 2023
# MATÉRIA: Inteligência Artificial 
# ALUNO: Lucas Santos Tavares
# DATA: 26/MAR/2023

from heapq import heappop, heappush

# Distâncias em linha reta entre cada cidade e Bucharest (heurística)
heuristic = {
    'arad': 366,
    'bucharest': 0,
    'craiova': 160,
    'dobreta': 242,
    'eforie': 161,
    'fagaras': 178,
    'giurgiu': 77,
    'hirsova': 151,
    'iasi': 226,
    'lugoj': 244,
    'mehadia': 241,
    'neamt': 234,
    'oradea': 380,
    'pitesti': 98,
    'rimnicu vikea': 193,
    'sibiu': 253,
    'timisoara': 329,
    'urziceni': 80,
    'vaslui': 199,
    'zerind': 374,
}

# Distâncias reais entre as cidades
distances = {
    'oradea': {'zerind': 71, 'sibiu': 151},
    'zerind': {'oradea': 71, 'arad': 75},
    'arad': {'zerind': 75, 'sibiu': 140, 'timisoara': 118},
    'timisoara': {'arad': 118, 'lugoj': 111},
    'lugoj': {'timisoara': 111, 'mehadia': 70},
    'mehadia': {'lugoj': 70, 'dobreta': 75},
    'dobreta': {'mehadia': 75, 'craiova': 120},
    'craiova': {'dobreta': 120, 'pitesti': 138, 'rimnicu vikea': 146},
    'rimnicu vikea': {'craiova': 146, 'sibiu': 80, 'pitesti': 97},
    'sibiu': {'arad': 140, 'oradea': 151, 'rimnicu vikea': 80, 'fagaras': 99},
    'fagaras': {'sibiu': 99, 'bucharest': 211},
    'bucharest': {'fagaras': 211, 'pitesti': 101, 'urziceni': 85, 'giurgiu': 90},
    'pitesti': {'craiova': 138, 'rimnicu vikea': 97, 'bucharest': 101},
    'giurgiu': {'bucharest': 90},
    'urziceni': {'bucharest': 85, 'vaslui': 142, 'hirsova': 98},
    'vaslui': {'urziceni': 142, 'iasi': 92},
    'iasi': {'neamt': 87, 'vaslui': 92},
    'neamt': {'iasi': 87},
    'eforie': {'hirsova': 86},
    'hirsova': {'eforie': 86, 'urziceni': 98}
}

def a_star(start, goal, distances, heuristic):
    frontier = [(0, start)]
    explored = set()
    parents = {start: None}

    g = {start: 0}
    f = {start: heuristic[start]}

    while frontier:
        current_cost, current_node = heappop(frontier)

        if current_node == goal:
            path_tested = [current_node]
            parent = parents[current_node]
            while parent:
                path_tested.append(parent)
                parent = parents[parent]
            path_tested.reverse()
            print(" -> ".join(path_tested))
            return current_cost, path_tested

        explored.add(current_node)

        for neighbor, cost in distances[current_node].items():
            if neighbor not in explored:
                new_cost = g[current_node] + cost
                if neighbor not in g or new_cost < g[neighbor]:
                    g[neighbor] = new_cost
                    f[neighbor] = new_cost + heuristic[neighbor]
                    heappush(frontier, (f[neighbor], neighbor))
                    parents[neighbor] = current_node
                    
    
    return None



######### MAIN CODE #########

# USER DEFINITION of FROM (start) and TO (END) as in Google Maps
start = 'arad'
end = 'bucharest'

# Call A* function to calculate the shortest distance
path = a_star(start, end, distances, heuristic)
# Print the solution on screen to user
print('\n\n############## SOLUTION ##############')
print(f'The shortest path from {start} to {end} is:\n{path}\n\n')

######### END OF MAIN CODE #########