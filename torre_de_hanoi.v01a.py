#REGRAS

# 1) SOMENTE UMA ELEMENTO DE TODOS PODE SER MOVIDO POR VEZ
# 2) SOMENTE O ELEMENTO DA CAMADA SUPERIOR DA TORRE PODE SER MOVIDO DE ACORDO COM AS REGRAS ANTERIORES
# 3) O ELEMENTO DA BASE (DISCO MAIOR) NÃO PODE SER POSTO EM CIMA DE UM MENOR

# A, B, C, D, E... SERÃO OS PINOS CENTRALIZADORES DOS DISCOS
# disco_1, disco_2, disco_3, etc. são os nomes dos discos, sendo que os discos com maior numeração são os maiores.

import time #Esta biblioteca não é necessária para executar o código, apenas para usar na função sleep() para o usuário tem uma melhor visualização da execução do código

def torre_de_hanoi(n, pino_de_origem, pino_de_destino, pino_auxiliar):
    if n > 0:
        torre_de_hanoi(n - 1, pino_de_origem, pino_auxiliar, pino_de_destino)
        print(f"Mover {discos[n-1]} do pino {pino_de_origem} para o {pino_de_destino}")
        time.sleep(1)
        torre_de_hanoi(n - 1, pino_auxiliar, pino_de_destino, pino_de_origem)


qnt_discos = int(input("Por favor, digite a quantidade de discos: ")) #Usuário define a quantidade de discos do problema
qnt_pinos_centralizadores = qnt_discos #A mesma quantidade de discos será a de pinos centralizadores

discos = [f"disco_{i+1}" for i in range(qnt_discos)] #Criação da lista com a quantidade de discos definido pelo usuário
pinos_centralizadores = [chr(65 + i) for i in range(qnt_pinos_centralizadores)] #Criação da lista alfabética com a quantidade de letras igual a quantidade de pinos inserida pelo usuário
print(pinos_centralizadores)
print(discos)

#Chamada da função da torre de hanoi
torre_de_hanoi(len(discos), pinos_centralizadores[0], pinos_centralizadores[-1], pinos_centralizadores[1])
    
'''
    Nesta versão a quantidade de pinos centralizadores é igual a quantidade de discos
porém como visto na execução do algoritmo v01 somente os dois primeiros e o último pino
são utilizados para resolução do problema, sendo desnecessário ter mais que 3 pinos
centralizadores ocupando espaço da memória.
'''