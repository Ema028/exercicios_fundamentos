number = int(input("Digite um número: "))
somatorio = 0
for i in range(1, number + 1):
    somatorio += i
print(f"Somatório: {somatorio}\n")

number = input("Digite um número inteiro positivo:\n")
multiplos = []
while (number.isdigit() == False):
    number = input("Digite um número inteiro positivo:\n")
for i in range(1, int(number) + 1):
    if i % 3 == 0:
        multiplos.append(i)
print(multiplos)

number1 = int(input("Digite um número inteiro:\n"))
number2 = int(input("Digite um número inteiro:\n"))
pares = []

for i in range(number1, number2 + 1):
    if i % 2 == 0:
        pares.append(i)
        
print(pares)

def main():
    number = int(input("Digite um número inteiro:\n"))
    primos = []
    contador = 0
    while (len(primos) != number):
        contador += 1
        if (is_primo(contador)):
            primos.append(contador)
            
    print(primos)
        
def is_primo(n):
    for i in range(1, n):
        if (i != 1 and n % i == 0):
            return False
    return True
            
main()