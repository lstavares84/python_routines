# PPGIa PUCPR 2023
# MATÉRIA: Inteligência Artificial 
# ALUNO: Lucas S. Tavares
# DATA: 26/MAR/2023


#Distance between all cities
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


''' STUDY NOTES OF STUDENT IN BRAZILIAN PORTUGUESE

O bloco de código abaixo nomeado "dijkstra" é responsável por implementar o algoritmo dijkstra
de busca de caminho mais curto em um grafo. O loop while roda enquanto existir nós (ou
"caminhos/paths" conforme nomeados abaixo) no conjunto de nós/paths não visitados (open_set).

A busca começa a partir do nó inicial (start) e segue até encontrar o nó objetivo (end).
A cada iteração do laço, o nó/path com o menor custo distância estimado é selecionado para
continuar a busca. Essa distância total é composto pela distância acumulado para chegar ao
nó atual (g[start]) e pela estimativa de distância para chegar ao objetivo (end) a partir
do nó atual (nó atual = f - g).

Se (IF) o nó (caminho/path) selecionado for o objetivo (end), o caminho é reconstruído
a partir dos nós pais (melhor explicado no parágrafo abaixo) e a resposta de menor
distância é encontrada. Caso contrário, o nó (path) selecionado é removido do conjunto
de nós não visitados (open_set) e adicionado ao conjunto de nós visitados (closed).

Todos os vizinhos desse nó (a.k.a cidade) são explorados e caso ainda não tenham sido
visitados, são atualizados com os novas distâncias e adicionados ao conjunto de nós
não visitados (open_set).

A distância acumulado para chegar até o vizinho é calculado somando a distância
acumulado para chegar ao nó atual com a distância para ir do nó atual até o vizinho.
Se a distância acumulado até o vizinho for menor do que a distância acumulado atual, as
informações do vizinho são atualizadas. O nó atual é definido como pai do vizinho e
a distância acumulado e a distância total estimada para chegar ao objetivo a partir do
vizinho são atualizados.

Se o vizinho ainda não estiver no conjunto de nós não visitados (open_set), ele é
adicionado e esse processo continua até que o nó objetivo (end) seja encontrado ou
até que não existam mais nós não visitados (motivo da existência do "return None" 
ao final do loop/laço).

END OF STUDY NOTES OF STUDENT IN BRAZILIAN PORTUGUESE'''


def dijkstra(start, end, distance): #dijkstra subroutine/function

    #Variables to store the total distance (f) and accumulated distance (g) between the cities definied as START and END
    #QUESTION: What's the difference between total distance and accumulated distance to the solution of problem?
    g = {node: float('inf') for node in distance}
    f = {node: float('inf') for node in distance}
    ''' According bibliography to "node: float('inf')" is used as infinite because it
    ensures that the initial accumulative distance is greater than any other cost that
    might be computed later avoiding a FALSE result in the first loop.
    The distance values will be updated while the loop is running.'''
    
    parents = {node: None for node in distance} #upper node or previously node
    
    #PRE SET of variables before start to calculate
    g[start] = 0 #Total distance (f) and accumulaed distance (g) from the START point
    f[start] = 0 #Total distance (f) and accumulaed distance (g) from the START point
    closed = set() #Variable to store possible paths already tested
    open_set = { start } #Variable to store possible paths TO BE tested
    #END OF PRE SET of variables before start to calculate

    ### LOOP TO CALCULATE THE SHORTEST DISTANCE
    while open_set: #While there are not tested paths...
        # Check the current path where there's the shortest distance between the current city to the neighbor city and keep looking
        current = min(open_set, key=lambda node: f[node])

        # IF the current city (node) is the goal (END), calculate from the end until start the whole path using parents nodes
        if current == end:
            path = []
            while current:
                path.append(current)
                current = parents[current]
            path.reverse()
            return path
        # END OF # IF the current city (node) is the goal (END), calculate from the end until start the whole path using parents nodes

        # To move the node tested from open_set (not tested) to closed (paths tested)
        open_set.remove(current)
        closed.add(current)
        # END OF To move the node tested from open_set (not tested) to closed (paths tested)

        # Identify all the neighborhoos cities of the current city/node
        for neighbor in distance[current]:
            
            # Just a quicky check if the neighbor was tested before or not. IF not tested yet, continue.
            if neighbor in closed:
                continue
            # END OF Just a quicky check if the neighbor was tested before or not. IF not tested yet, continue.

            tentative_g = g[current] + distance[current][neighbor] # Calculate the accumulated distance from the current node/city to the selected neighbor node/city
            
            # IF the accumulated distance until the selected node/city is less (but not equal) to the current accumulated distance, please, update "g[neighbor]"
            # and"f[neighbor]".
            if tentative_g < g[neighbor]:
                parents[neighbor] = current # Define the current node/city as parent of the current neighbor
                g[neighbor] = tentative_g # update the accumulated distance
                f[neighbor] = g[neighbor] # estimate the remaining total distance to reach the end/goal city/node
                
                # Test if the current neighbor wasn't tested before. Move the current neighbor tested from not tested
                if neighbor not in open_set:
                    open_set.add(neighbor)
                # END OF Test if the current neighbor wasn't tested before. Move the current neighbor tested from not tested

            # END OF IF the accumulated distance until the selected node/city is less (but not equal) to the current accumulated distance, please, update "g[neighbor]"
            # and "f[neighbor]".

        # END OF # Identify all the neighborhoos cities of the current city/node

    return None #IF there is NO path from START to END, return None
    ### END OF LOOP TO CALCULATE THE SHORTEST DISTANCE




######### MAIN CODE #########

# USER DEFINITION of FROM (start) and TO (END) as in Google Maps
start = 'arad' #type the name of the city where travel will begins
end = 'vaslui' #type the name of destination city

# Call dijkstra function to calculate the shortest distance
path = dijkstra(start, end, distances)

# Print the solution on screen to user
print('\n\n############## SOLUTION ##############')
print(f'The shortest path from {start} to {end} is:\n{path}\n\n')

######### END OF MAIN CODE #########