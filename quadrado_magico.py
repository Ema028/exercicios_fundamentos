#matriz = [[2, 7, 6], [9, 5, 1], [4, 3, 8]]
n = int(input("insira o número de linhas/colunas da matriz:\n"))
matriz = [[int(input("diga um número\n")) for j in range(n)] for i in range(n)]

def main():
    if quadrado_magico(matriz):
        print("quadrado mágico")
    else:
        print("não é")
        
def quadrado_magico(matriz):
    soma = 0
    #achar a soma da 1 linha para comparar
    for i in range(len(matriz[0])):
        soma += matriz[0][i]
        
    somaaux_diagonal = 0
    somaaux_diagonal_inversa = 0
    for i in range(len(matriz)):
        somaux_linha = 0
        somaux_coluna = 0
        for j in range(len(matriz[i])):
            somaux_linha += matriz[i][j]
            somaux_coluna += matriz[j][i]
            if (i == j):
                somaaux_diagonal += matriz[i][j]
            if ((i + j) == (len(matriz) - 1)):
                somaaux_diagonal_inversa += matriz[j][i]
        if (somaux_linha != soma or somaux_coluna != soma):
            return False
    if (somaaux_diagonal != soma or somaaux_diagonal_inversa != soma):
        return False
    return True
    
main()
