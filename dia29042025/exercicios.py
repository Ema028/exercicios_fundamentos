#1
import os

class Aluno():
    def __init__(self, nota, nome, idade):
        self.nota = nota
        self.idade = idade
        self.nome = nome

alunos = []
mvp = 0
media = 0
count = 0

while True:
    nota = input("Qual a nota final?\n")
    if (nota.isdigit()):
        nome = input("Qual o nome do aluno?\n")
        idade = int(input("Qual a idade?\n"))
        new_aluno = Aluno(int(nota), nome, idade)
        alunos.append(new_aluno)
        if (os.name == 'nt'):
            os.system('cls') #limpar tela windows
        else:
            os.system('clear') #Linux/mac
    else:
        break
    
for aluno in alunos:
    if (aluno.nota > mvp):
        mvp = aluno.nota
    if (aluno.idade < 18):
        count += 1
        media += aluno.nota
        
if (count == 0):
    print("não há menores aqui")
else:
    print(f"A média entre menores é {media/count}")
    
print(f"maior nota foi {mvp}")
       
#4
numeros = []

for i in range(5): 
    numero = int(input("Diga um número inteiro\n"))
    numeros.append(numero)

menor = 0
menor2 = 0

for numero in numeros:
    if(menor == 0 and menor2 == 0):
        menor = numero
        menor2 = numero
    elif(numero < menor):
        menor = numero
    
for numero in numeros:
    if(numero < menor2 and numero > menor):
        menor2 = numero

print(f"menor: {menor}, segundo menor: {menor2}")

#4
numeros = []

for i in range(5): 
    numero = int(input("Diga um número inteiro\n"))
    numeros.append(numero)

menor = 0
menor2 = 0

for i in range(1, len(numeros)):
    for i in range(1, len(numeros)):
        if(numeros[i - 1] < numeros[i]):
            menor = numeros[i - 1]
            numeros[i - 1] = numeros[i]
            numeros[i] = menor

menor2 = numeros[len(numeros) - 2]
menor = numeros[len(numeros) -1]
print(f"menor: {menor}, segundo menor: {menor2}")

#5
numero = int(input("Diga um número inteiro\n"))
if(numero % 7 == 0 and numero % 3 != 0):
    print("número mágico")
else:
    print("não é número mágico")

#3
string = input("fale uma palavra\n")
count = 0

for i in range(len(string)):
    if(string[i] == 'a'):
        count += 1
        
print(count)

#2
def main():
    n1 = int(input("digite um número inteiro\n"))
    n2 = int(input("digite um número inteiro\n"))
    temp = 0
    squares = []
    
    if(n2 < n1):
        print("o primeiro número deve ser menor que o segundo")
        return
    
    for i in range(n1 + 1, n2):
        numero = i**2
        squares.append(numero)
        
    print(squares)
    
main()