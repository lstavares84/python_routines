#REGRAS

# 1) SOMENTE UMA ELEMENTO DE TODOS PODE SER MOVIDO POR VEZ
# 2) SOMENTE O ELEMENTO DA CAMADA SUPERIOR DA TORRE PODE SER MOVIDO DE ACORDO COM AS REGRAS ANTERIORES
# 3) O ELEMENTO DA BASE (DISCO MAIOR) NÃO PODE SER POSTO EM CIMA DE UM MENOR

# A, B E C SERÃO OS PINOS CENTRALIZADORES DOS DISCOS
# disco_maior, disco_medio e disco_menor SÃO AUTO EXPLICATIVOS

import time #Esta biblioteca não é necessária para executar o código, apenas para usar na função sleep() para o usuário tem uma melhor visualização da execução do código

discos = ['disco_menor', 'disco_medio', 'disco_maior']
pinos_centralizadores = ['A', 'B', 'C']

def torre_de_hanoi(n, pino_de_origem, pino_de_destino, pino_auxiliar):
    if n == 1: #REGRA 1
        print(f"Mova o {discos[n-1]} de {pino_de_origem} para {pino_de_destino}")  # REGRA 1: Imprime o movimento
        time.sleep(2)
        return
    torre_de_hanoi(n-1, pino_de_origem, pino_auxiliar, pino_de_destino)  # Chamada recursiva da função
    print(f"Mova o {discos[n-1]} de {pino_de_origem} para {pino_de_destino}")  # Imprime o movimento
    time.sleep(2)  # Adiciona um atraso de 2 segundos
    torre_de_hanoi(n-1, pino_auxiliar, pino_de_destino, pino_de_origem)  # Chamada recursiva da função


torre_de_hanoi(len(discos), pinos_centralizadores[0], pinos_centralizadores[2], pinos_centralizadores[1])

