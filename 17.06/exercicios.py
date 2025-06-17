#1
def main():
    string = input()
    print(conta_por_inicial(string))

def conta_por_inicial(string):
    string = string.split()
    dect = {}
    for palavra in string:
        if palavra[0] in dect.keys():
            dect[palavra[0]] += 1
        else:
            dect[palavra[0]] = 1
    return dect
    
main()
#2
from unicodedata import normalize

def main():
    string = input()
    print(frequencia_caracteres(string))

def frequencia_caracteres(string):
    pont = [',', '.', ';', ':', '?', '!']
    #passa pra byte ignorando o q n pd ser representado em ascii e dps pra ascii
    string = normalize('NFKD', string).encode('ASCII', 'ignore').decode('ASCII')
    string = string.lower().split()
    dect = {}
    for palavra in string:
        for letra in palavra:
            if letra in dect.keys():
                dect[letra] += 1
            elif letra not in pont:
                dect[letra] = 1
            else:
                pass
    return dect
    
main()
#3
from random import randint
def main():
    matriz = [[randint(0,20) for i in range(5)] for j in range(6)]
    for elemento in matriz:
        print(elemento)
    print("\n\n")
    print(soma_colunas(matriz))

#m*n matriz[m][n] m linhas e n colunas
def soma_colunas(matriz):
    linhas = len(matriz)
    colunas = len(matriz[0])
    lista = [0] * colunas
    for i in range(linhas):
        for j in range(colunas):
            lista[j] += matriz[i][j]
    return lista
main()
#4
def main():
    frase = input().lower().split()
    print(palindromos(frase))

def palindromos(lista_string):
    lista = []
    for string in lista_string:
        if palindromo(string):
            if string not in lista:
                lista.append(string)
    return lista
    
def palindromo(string):
    if (string == string[::-1]):
        return True
    return False
    
main()
#5
from random import randint

def main():
    lista = [randint(0,10) for i in range(7)]
    print(lista)
    n = int(input("diga um número\n"))
    print(rotacionar(lista, n))

def rotacionar(lista, num):
    tam = len(lista)
    #index+num%tam
    new_lista = [0] * tam
    for i in range(tam):
        new_lista[(i + num) % tam] = lista[i]
    return new_lista
main()
#6
from random import randint

def main():
    matriz = [[randint(0,20) for i in range(5)] for j in range(6)]
    for elemento in matriz:
        print(elemento)
    print("\n\n")
    transposta = transpor_matriz(matriz)
    for elemento in transposta:
        print(elemento)
    
def transpor_matriz(matriz):
    #matriz[i][j] == tranp[j][i]
    transposta = [([0] * len(matriz)) for i in range(len(matriz[0]))]
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            transposta[j][i] = matriz[i][j]
    return transposta
    
main()
