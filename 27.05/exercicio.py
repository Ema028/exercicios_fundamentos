matriz = []
soma = 0
linhas = 0
colunas = 0
n = 1
while True:
    lista = []
    n = 1
    while True:
        n = int(input("um num\n"))
        if (n < 0):
            break
        lista.append(n)
        colunas += 1
        soma += n
    matriz.append(lista)
    linhas += 1
    continua = input("continua?\n").lower()
    if (continua == 's'):
        continue
    break
    
buscar = int(input("um num\n"))
count = 0
count_pares = 0
diagonal = []
transposta = [[] for i in range(len(matriz[0]))]
maior = 0
for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        if (matriz[i][j] == buscar):
            count += 1
        if (matriz[i][j] % 2 == 0):
            count_pares += 1
        if (i == j):
            diagonal.append(matriz[i][j])
        transposta[i].append(matriz[j][i])
        if (matriz[i][j] > maior):
            maior = matriz[i][j]

print(f"matriz: {matriz}")
print(f"a soma é: {soma}")
print(f"{buscar} parece {count} vezes")
print(f"{count_pares} pares")
print(f"diagonal principal: {diagonal}")
print(f"transposta: {transposta}")
print(f"o maior termo: {maior}")
