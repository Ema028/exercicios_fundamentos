#versão corrigida
#matriz = [[0, 0], [0, 0]]
#matriz = [[1, 1, 0, 0],[1, 0, 0, 1],[0, 0, 1, 1],[0, 0, 0, 0]]

def count_ilhas(matriz):
    ilhas = 0
    vizinhos_index = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    posicoes = []
    checados = []
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if (matriz[i][j] == 1):
                posicoes.append((i, j))
                
    for posicao in posicoes:
        for vizinho in vizinhos_index:
            if (posicao in checados):
                break
            i = posicao[0] + vizinho[0]
            j = posicao[1] + vizinho[1]
            if ((i, j) in checados):
                continue
            if in_bound((i, j), matriz):
                if (matriz[i][j] == 1):
                    ilhas += 1
                    checados.append((posicao[0],posicao[1]))
                    checados.append((i, j))
    return ilhas
    
def in_bound(tupla, matriz):
    if ((tupla[0] >= 0 and tupla[0] <= (len(matriz) - 1)) and (tupla[1] >= 0 and tupla[1] <= (len(matriz[0]) - 1))):
        return True
    return False
