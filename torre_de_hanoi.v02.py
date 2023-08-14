#REGRAS

# 1) SOMENTE UMA ELEMENTO DE TODOS PODE SER MOVIDO POR VEZ
# 2) SOMENTE O ELEMENTO DA CAMADA SUPERIOR DA TORRE PODE SER MOVIDO DE ACORDO COM AS REGRAS ANTERIORES
# 3) O ELEMENTO DA BASE (DISCO MAIOR) NÃO PODE SER POSTO EM CIMA DE UM MENOR

# A, B, C SERÃO OS PINOS CENTRALIZADORES DOS DISCOS*
# disco_1, disco_2, disco_3, etc. são os nomes dos discos, sendo que os discos com maior numeração são os maiores.


import time #Esta biblioteca não é necessária para executar o código, apenas para usar na função sleep() para o usuário tem uma melhor visualização da execução do código




############### INÍCIO DA FUNÇÃO DE RECURSÃO DA TORRE DE HANOI ###############
def torre_de_hanoi(n, pino_de_origem, pino_de_destino, pino_auxiliar):
    if n > 0:
        torre_de_hanoi(n - 1, pino_de_origem, pino_auxiliar, pino_de_destino)
        print(f"Mover {discos[n-1]} do pino {pino_de_origem} para o {pino_de_destino}")
        mover_discos_graficamente(pino_de_origem, pino_de_destino)
        imprimir(len(discos))
        torre_de_hanoi(n - 1, pino_auxiliar, pino_de_destino, pino_de_origem)
############### FINAL DA FUNÇÃO DE RECURSÃO DA TORRE DE HANOI ###############




############### INÍCIO DAS FUNÇÕES GRÁFICA ###############
temp = []



def tamanho_discos(n):
    global alocacao_grafica_discos
    for i in range(1, n + 1):
        s = '█' + '█' * i * 2
        temp.append(s)
    alocacao_grafica_discos[pinos_centralizadores[0]] += temp[::-1]


def imprimir(n):
    t = alocacao_grafica_discos[pinos_centralizadores[0]][::-1]
    u = alocacao_grafica_discos[pinos_centralizadores[1]][::-1]
    v = alocacao_grafica_discos[pinos_centralizadores[2]][::-1]
    p = len(t)
    q = len(u)
    r = len(v)
    ds = n - p
    dd = n - q
    da = n - r

    for j in range(n):
        a = j - ds
        if a >= 0:
            print(t[a].center(21), end="  ")
        else:
            print('║'.center(21), end="  ")
        b = j - dd
        if b >= 0:
            print(u[b].center(21), end="  ")
        else:
            print('║'.center(21), end="  ")
        c = j - da
        if c >= 0:
            print(v[c].center(21))
        else:
            print('║'.center(21))

    print('═════════════════════', end="  ")
    print('═════════════════════', end="  ")
    print('═════════════════════')
    print(pinos_centralizadores[0].center(21), end="  ")
    print(pinos_centralizadores[1].center(21), end="  ")
    print(pinos_centralizadores[2].center(21))
    print('\n')
    time.sleep(1.5)


def mover_discos_graficamente(pino_de_origem, pino_de_destino):
    global tamanho_discos
    alocacao_grafica_discos[pino_de_destino].append(alocacao_grafica_discos[pino_de_origem][-1])
    alocacao_grafica_discos[pino_de_origem].pop(-1)
############### FINAL DAS FUNÇÕES GRÁFICA ###############





############### INÍCIO DA FUNÇÃO MAIN() ###############
qnt_discos = int(input("Por favor, digite a quantidade de discos: ")) #Usuário define a quantidade de discos do problema
qnt_pinos_centralizadores = 3 #A quantidade de pinos é fixada em 3 conforme visto na versão 01a e 01b do código.

discos = [f"disco_{i+1}" for i in range(qnt_discos)] #Criação da lista com a quantidade de discos definido pelo usuário
pinos_centralizadores = [chr(65 + i) for i in range(qnt_pinos_centralizadores)] #Criação da lista alfabética com a quantidade de letras igual a quantidade de pinos inserida pelo usuário
print('\n')
print(f'Os pinos centralizadors serão: {pinos_centralizadores}')
print(f'Os discos serão: {discos}')
print('\n')
print('POSIÇÃO INICIAL DE TODOS OS DISCOS:')

alocacao_grafica_discos = {
    pinos_centralizadores[0]: [],
    pinos_centralizadores[1]: [],
    pinos_centralizadores[2]: [],
}

#Funções de impressão em gráfica em tela
tamanho_discos(len(discos))
imprimir(len(discos))

#Chamada da função da torre de hanoi
torre_de_hanoi(len(discos), pinos_centralizadores[0], pinos_centralizadores[-1], pinos_centralizadores[1])
############### FINAL DA FUNÇÃO MAIN() ###############
    