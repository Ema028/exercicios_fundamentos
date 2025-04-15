#exercicio1
while True:
    n = input("Digite um número inteiro(p para sair)\n").upper()
    if (n == 'P'):
        break
    elif (n.isalpha() == True):
        n = input("Digite um número inteiro(p para sair)\n").upper()
    elif (int(n) == 0):
        print("o número é 0\n")
    elif (int(n) < 0):
        print("o número é negativo\n")
    else:
        print("o número é positivo\n")

#exercicio2
n = int(input("Quantas idades?\n"))
idades = []

for i in range(n):
    idade = int(input("Digite uma idade:\n"))
    idades.append(idade)
    
media = 0

for idade in idades:
    media += idade
    
media /= len(idades)
print(media)

#exercicio3
from random import randint

number = randint(1,100)
tentativas = 0
while True:
    guess = int(input("Digite um número inteiro\n"))
    if (guess == number):
        print(f"Winner! {tentativas} tentativas")
        break
    elif (guess < number):
        print("O número é maior")
        tentativas += 1
    else:
        print("O número é menor")
        tentativas += 1

#exercicio4
n = int(input("Digite um número inteiro positivo\n"))
print("contagem regressiva...")
for i in range(n,-1,-1):
    print(f"{i} ", end = '')

#exercicio5
def main():
    n = int(input("Digite um número inteiro positivo\n"))
    fatorial = fact(n)
    print(f"o fatorial de {n} é {fatorial}")

def fact(n):
    if(n == 1):
        return 1
    else:
        return n * fact(n - 1)
        
main()

#exercicio6
n = 1
while (n < 1000):
    print(n)
    n *= 2
print(n)

#exercicio7
n = int(input("Digite um número inteiro positivo\n"))
divisores = []
for i in range(1, n + 1):
    if(n % i == 0):
        divisores.append(i)
        
print(f"Os divisores de {n} são {divisores}")

#exercicio8
n = int(input("Digite um número inteiro\n"))
pares = []
impares = []
while (n != 0):
    if (n % 2 == 0):
        pares.append(n)
    else:
        impares.append(n)
    n = int(input("Digite um número inteiro\n"))
print(f"Você digitou {len(pares)} pares, {pares}\ne {len(impares)} ímpares, {impares}")
