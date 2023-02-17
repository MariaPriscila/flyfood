import itertools
import math
import time

# Leitura da matriz do arquivo de entrada
with open('matriz4.txt', 'r') as file:
    matriz = [list(line.strip().split()) for line in file]
matriz = matriz[1:]
start_time = time.time()

# Identificação dos pontos de entrega e de origem/retorno
pontos_entrega = []
ponto_origem = None
for i in range(len(matriz)):
    for j in range(len(matriz[0])):
        if matriz[i][j] != '0':
            if matriz[i][j] == 'R':
                ponto_origem = (i, j)
            else:
                pontos_entrega.append((i, j))

# Cálculo da distância euclidiana entre dois pontos
def distancia(p1, p2):
    return math.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)

# Geração de todas as possíveis sequências de rotas
rotas = list(itertools.permutations(pontos_entrega))

# Cálculo do custo total de cada rota e identificação da rota com o menor custo
menor_custo = float('inf')
melhor_rota = None
for rota in rotas:
    custo = 0
    ponto_atual = ponto_origem
    for ponto in rota:
        custo += distancia(ponto_atual, ponto)
        ponto_atual = ponto
    custo += distancia(ponto_atual, ponto_origem)
    if custo < menor_custo:
        menor_custo = custo
        melhor_rota = rota

# Criação da sequência de pontos da melhor rota
sequencia_pontos = [matriz[ponto[0]][ponto[1]] for ponto in melhor_rota]

# Impressão da sequência de pontos da melhor rota
print(' '.join(sequencia_pontos))
print("--- %s seconds ---" % (time.time() - start_time))

