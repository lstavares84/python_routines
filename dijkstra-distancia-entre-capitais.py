#Tabela de distância entre as capitais
distancias = {
'SE':{'SE': 0,'PA': None,'MG': None,'RR': None,'DF': None,'MS': None,'MT': None,'PR': None,'SC': None,'CE': None,'GO': None,'PB': None,'AP': None,'AL': 294,'AM': None,'RN': None,'TO': None,'RS': None,'RO': None,'PE': None,'AC': None,'RJ': None,'BA': 356,'MA': None,'SP': None,'PI': None,'ES': None},
'PA':{'SE': None,'PA': 0,'MG': None,'RR': 6083,'DF': 716,'MS': None,'MT': 2941,'PR': None,'SC': None,'CE': None,'GO': None,'PB': None,'AP': None,'AL': None,'AM': 5298,'RN': None,'TO': 1283,'RS': None,'RO': None,'PE': None,'AC': None,'RJ': None,'BA': None,'MA': 806,'SP': None,'PI': None,'ES': None},
'MG':{'SE': None,'PA': None,'MG': 0,'RR': None,'DF': None,'MS': 1453,'MT': None,'PR': None,'SC': None,'CE': None,'GO': 906,'PB': None,'AP': None,'AL': None,'AM': None,'RN': None,'TO': None,'RS': None,'RO': None,'PE': None,'AC': None,'RJ': 434,'BA': 1372,'MA': None,'SP': 586,'PI': None,'ES': 524},
'RR':{'SE': None,'PA': None,'MG': None,'RR': 0,'DF': None,'MS': None,'MT': None,'PR': None,'SC': None,'CE': None,'GO': None,'PB': None,'AP': None,'AL': None,'AM': 785,'RN': None,'TO': None,'RS': None,'RO': None,'PE': None,'AC': None,'RJ': None,'BA': None,'MA': None,'SP': None,'PI': None,'ES': None},
'DF':{'SE': None,'PA': None,'MG': 716,'RR': None,'DF': 0,'MS': 1134,'MT': 1133,'PR': None,'SC': None,'CE': None,'GO': 209,'PB': None,'AP': None,'AL': None,'AM': None,'RN': None,'TO': 973,'RS': None,'RO': None,'PE': None,'AC': None,'RJ': None,'BA': 1446,'MA': None,'SP': None,'PI': None,'ES': None},
'MS':{'SE': None,'PA': None,'MG': 1453,'RR': None,'DF': 1134,'MS': 0,'MT': 694,'PR': 991,'SC': None,'CE': None,'GO': 935,'PB': None,'AP': None,'AL': None,'AM': None,'RN': None,'TO': None,'RS': None,'RO': None,'PE': None,'AC': None,'RJ': None,'BA': None,'MA': None,'SP': 1014,'PI': None,'ES': None},
'MT':{'SE': None,'PA': None,'MG': None,'RR': None,'DF': 1133,'MS': 694,'MT': 0,'PR': None,'SC': None,'CE': None,'GO': 934,'PB': None,'AP': None,'AL': None,'AM': 2357,'RN': None,'TO': 1784,'RS': None,'RO': 1456,'PE': None,'AC': None,'RJ': None,'BA': None,'MA': None,'SP': None,'PI': None,'ES': None},
'PR':{'SE': None,'PA': None,'MG': None,'RR': None,'DF': None,'MS': 991,'MT': None,'PR': 0,'SC': 300,'CE': None,'GO': None,'PB': None,'AP': None,'AL': None,'AM': None,'RN': None,'TO': None,'RS': None,'RO': None,'PE': None,'AC': None,'RJ': None,'BA': None,'MA': None,'SP': 408,'PI': None,'ES': None},
'SC':{'SE': None,'PA': None,'MG': None,'RR': None,'DF': None,'MS': None,'MT': None,'PR': 300,'SC': 0,'CE': None,'GO': None,'PB': None,'AP': None,'AL': None,'AM': None,'RN': None,'TO': None,'RS': 476,'RO': None,'PE': None,'AC': None,'RJ': None,'BA': None,'MA': None,'SP': None,'PI': None,'ES': None},
'CE':{'SE': None,'PA': None,'MG': None,'RR': None,'DF': None,'MS': None,'MT': None,'PR': None,'SC': None,'CE': 0,'GO': None,'PB': 688,'AP': None,'AL': None,'AM': None,'RN': None,'TO': None,'RS': None,'RO': None,'PE': 800,'AC': None,'RJ': None,'BA': None,'MA': None,'SP': None,'PI': 634,'ES': None},
'GO':{'SE': None,'PA': None,'MG': 906,'RR': None,'DF': 209,'MS': 935,'MT': 934,'PR': None,'SC': None,'CE': None,'GO': 0,'PB': None,'AP': None,'AL': None,'AM': None,'RN': None,'TO': 874,'RS': None,'RO': None,'PE': None,'AC': None,'RJ': None,'BA': 1643,'MA': None,'SP': None,'PI': None,'ES': None},
'PB':{'SE': None,'PA': None,'MG': None,'RR': None,'DF': None,'MS': None,'MT': None,'PR': None,'SC': None,'CE': 688,'GO': None,'PB': 0,'AP': None,'AL': None,'AM': None,'RN': 185,'TO': None,'RS': None,'RO': None,'PE': 120,'AC': None,'RJ': None,'BA': None,'MA': None,'SP': None,'PI': None,'ES': None},
'AP':{'SE': None,'PA': None,'MG': None,'RR': None,'DF': None,'MS': None,'MT': None,'PR': None,'SC': None,'CE': None,'GO': None,'PB': None,'AP': 0,'AL': None,'AM': None,'RN': None,'TO': None,'RS': None,'RO': None,'PE': None,'AC': None,'RJ': None,'BA': None,'MA': None,'SP': None,'PI': None,'ES': None},
'AL':{'SE': 294,'PA': None,'MG': None,'RR': None,'DF': None,'MS': None,'MT': None,'PR': None,'SC': None,'CE': None,'GO': None,'PB': None,'AP': None,'AL': 0,'AM': None,'RN': None,'TO': None,'RS': None,'RO': None,'PE': 285,'AC': None,'RJ': None,'BA': 632,'MA': None,'SP': None,'PI': None,'ES': None},
'AM':{'SE': None,'PA': 5298,'MG': None,'RR': 785,'DF': None,'MS': None,'MT': 2357,'PR': None,'SC': None,'CE': None,'GO': None,'PB': None,'AP': None,'AL': None,'AM': 0,'RN': None,'TO': None,'RS': None,'RO': 901,'PE': None,'AC': 1445,'RJ': None,'BA': None,'MA': 5335,'SP': None,'PI': None,'ES': None},
'RN':{'SE': None,'PA': None,'MG': None,'RR': None,'DF': None,'MS': None,'MT': None,'PR': None,'SC': None,'CE': 537,'GO': None,'PB': 185,'AP': None,'AL': None,'AM': None,'RN': 0,'TO': None,'RS': None,'RO': None,'PE': None,'AC': None,'RJ': None,'BA': None,'MA': None,'SP': None,'PI': None,'ES': None},
'TO':{'SE': None,'PA': 1283,'MG': None,'RR': None,'DF': 973,'MS': None,'MT': 1784,'PR': None,'SC': None,'CE': None,'GO': 874,'PB': None,'AP': None,'AL': None,'AM': None,'RN': None,'TO': 0,'RS': None,'RO': None,'PE': None,'AC': None,'RJ': None,'BA': 1454,'MA': 1386,'SP': None,'PI': 1401,'ES': None},
'RS':{'SE': None,'PA': None,'MG': None,'RR': None,'DF': None,'MS': None,'MT': None,'PR': None,'SC': 476,'CE': None,'GO': None,'PB': None,'AP': None,'AL': None,'AM': None,'RN': None,'TO': None,'RS': 0,'RO': None,'PE': None,'AC': None,'RJ': None,'BA': None,'MA': None,'SP': None,'PI': None,'ES': None},
'RO':{'SE': None,'PA': None,'MG': None,'RR': None,'DF': None,'MS': None,'MT': 1456,'PR': None,'SC': None,'CE': None,'GO': None,'PB': None,'AP': None,'AL': None,'AM': 901,'RN': None,'TO': None,'RS': None,'RO': 0,'PE': None,'AC': 544,'RJ': None,'BA': None,'MA': None,'SP': None,'PI': None,'ES': None},
'PE':{'SE': None,'PA': None,'MG': None,'RR': None,'DF': None,'MS': None,'MT': None,'PR': None,'SC': None,'CE': 800,'GO': None,'PB': 120,'AP': None,'AL': None,'AM': None,'RN': None,'TO': None,'RS': None,'RO': None,'PE': 0,'AC': None,'RJ': None,'BA': 839,'MA': None,'SP': None,'PI': None,'ES': None},
'AC':{'SE': None,'PA': None,'MG': None,'RR': None,'DF': None,'MS': None,'MT': None,'PR': None,'SC': None,'CE': None,'GO': None,'PB': None,'AP': None,'AL': None,'AM': None,'RN': None,'TO': None,'RS': None,'RO': 544,'PE': None,'AC': 0,'RJ': None,'BA': None,'MA': None,'SP': None,'PI': None,'ES': None},
'RJ':{'SE': None,'PA': None,'MG': 434,'RR': None,'DF': None,'MS': None,'MT': None,'PR': None,'SC': None,'CE': None,'GO': None,'PB': None,'AP': None,'AL': None,'AM': None,'RN': None,'TO': None,'RS': None,'RO': None,'PE': None,'AC': None,'RJ': 0,'BA': None,'MA': None,'SP': 429,'PI': None,'ES': 521},
'BA':{'SE': 356,'PA': None,'MG': 1372,'RR': None,'DF': 1446,'MS': None,'MT': None,'PR': None,'SC': None,'CE': None,'GO': 1643,'PB': None,'AP': None,'AL': 632,'AM': None,'RN': None,'TO': None,'RS': None,'RO': None,'PE': 839,'AC': None,'RJ': None,'BA': 0,'MA': None,'SP': None,'PI': 1163,'ES': 1202},
'MA':{'SE': None,'PA': 806,'MG': None,'RR': None,'DF': None,'MS': None,'MT': None,'PR': None,'SC': None,'CE': None,'GO': None,'PB': None,'AP': None,'AL': None,'AM': None,'RN': None,'TO': 1386,'RS': None,'RO': None,'PE': None,'AC': None,'RJ': None,'BA': None,'MA': 0,'SP': None,'PI': 446,'ES': None},
'SP':{'SE': None,'PA': None,'MG': 586,'RR': None,'DF': None,'MS': 1014,'MT': None,'PR': 408,'SC': None,'CE': None,'GO': None,'PB': None,'AP': None,'AL': None,'AM': None,'RN': None,'TO': None,'RS': None,'RO': None,'PE': None,'AC': None,'RJ': 429,'BA': None,'MA': None,'SP': 0,'PI': None,'ES': None},
'PI':{'SE': None,'PA': None,'MG': None,'RR': None,'DF': None,'MS': None,'MT': None,'PR': None,'SC': None,'CE': 634,'GO': None,'PB': None,'AP': None,'AL': None,'AM': None,'RN': None,'TO': None,'RS': None,'RO': None,'PE': None,'AC': None,'RJ': None,'BA': 1163,'MA': 446,'SP': None,'PI': 0,'ES': None},
'ES':{'SE': None,'PA': None,'MG': 524,'RR': None,'DF': None,'MS': None,'MT': None,'PR': None,'SC': None,'CE': None,'GO': None,'PB': None,'AP': None,'AL': None,'AM': None,'RN': None,'TO': None,'RS': None,'RO': None,'PE': None,'AC': None,'RJ': 521,'BA': 1202,'MA': None,'SP': None,'PI': None,'ES': 0}

}

# Tabela de preços do óleo diesel por estado
tabela_preco_diesel = {
    "AC": 6.52,
    "AL": 4.75,
    "AM": 5.16,
    "AP": 5.06,
    "BA": 5.12,
    "CE": 5.04,
    "DF": 4.79,
    "ES": 4.89,
    "GO": 4.80,
    "MA": 4.74,
    "MG": 4.79,
    "MS": 5.04,
    "MT": 5.12,
    "PA": 5.37,
    "PB": 4.75,
    "PE": 5.13,
    "PI": 4.87,
    "PR": 4.82,
    "RJ": 5.06,
    "RN": 5.02,
    "RO": 5.35,
    "RR": 5.37,
    "SC": 4.96,
    "SP": 4.91,
    "SE": 4.93,
    "TO": 4.95,
}



def dijkstra(start, end, distancias):
    # Variáveis para armazenar a distância total (f) e a distância acumulada (g) entre as cidades definidas como INÍCIO e FIM
    g = {node: float('inf') for node in distancias}
    f = {node: float('inf') for node in distancias}

    parents = {node: None for node in distancias} # nó superior ou nó anterior

    # PREDEFINIÇÃO de variáveis antes de começar a calcular
    g[start] = 0 # Distância total (f) e distância acumulada (g) a partir do ponto de INÍCIO
    f[start] = 0 # Distância total (f) e distância acumulada (g) a partir do ponto de INÍCIO
    closed = set() # Variável para armazenar os caminhos possíveis já testados
    open_set = {start} # Variável para armazenar os caminhos possíveis A SEREM testados

    ### LOOP PARA CALCULAR A MENOR DISTÂNCIA
    while open_set: # Enquanto houver caminhos não testados...
        # Verifica o caminho atual com a menor distância entre a cidade atual e a cidade vizinha e continue procurando
        current = min(open_set, key=lambda node: f[node])

        # SE a cidade atual (nó) for o destino (FIM), calcule do fim até o início o caminho completo usando os nós pais
        if current == end:
            path = []
            while current:
                path.append(current)
                current = parents[current]
            path.reverse()

            # Calcula a distância total percorrida
            total_distance = g[end]

            # Imprime a solução na tela para o usuário
            print('\n\n############## SOLUÇÃO ##############')
            print(f'O caminho mais curto de {start} para {end} é:')
            print(f'Caminho: {path}')
            print(f'Distância total percorrida: {total_distance}\n')

            # Calcula e imprime as distâncias entre os nós ao longo do caminho
            print('Distâncias entre os nós ao longo do caminho:')
            for i in range(len(path) - 1):
                node1 = path[i]
                node2 = path[i + 1]
                distance = distancias[node1][node2]
                print(f'Distância de {node1} para {node2}: {distance}')

            return path

        # FIM DE # SE a cidade atual (nó) for o destino (FIM), calcule do fim até o início o caminho completo usando os nós pais

        # Para mover o nó testado de open_set (não testado) para closed (caminhos testados)
        open_set.remove(current)
        closed.add(current)

        # Identificar todas as cidades vizinhas da cidade/nó atual
        for neighbor in distancias[current]:
            if distancias[current][neighbor] is None:
                continue  # Ignora valores None

            tentative_g = g[current] + distancias[current][neighbor] # Calcular a distância acumulada do nó/cidade atual para o nó/cidade vizinho selecionado

            # SE a distância acumulada até o nó/cidade selecionado for menor (mas não igual) à distância acumulada atual, por favor, atualize "g[vizinho]"
            # e "f[vizinho]".
            if tentative_g < g[neighbor]:
                parents[neighbor] = current # Define o nó/cidade atual como pai do vizinho atual
                g[neighbor] = tentative_g # atualiza a distância acumulada
                f[neighbor] = g[neighbor] # estima a distância total restante para chegar à cidade/nó final

                # Teste se o vizinho atual não foi testado antes. Mova o vizinho atual testado de não testado
                if neighbor not in open_set:
                    open_set.add(neighbor)
                # FIM DE Teste se o vizinho atual não foi testado antes. Mova o vizinho atual testado de não testado

    return None # SE não houver caminho de INÍCIO para FIM, retorne None
    ### FIM DO LOOP PARA CALCULAR A MENOR DISTÂNCIA


# DEFINIÇÃO PELO USUÁRIO de INÍCIO (start) e FIM (end) como no Google Maps
start = 'PR' # digite o nome da cidade onde a viagem começará
end = 'MA' # digite o nome da cidade de destino

# Chame a função dijkstra para calcular a menor distância
path = dijkstra(start, end, distancias)

