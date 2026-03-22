number = input("Digite um número\n")
count = 0
while True:
    if(number.isalpha() == True):
        number = input("Digite um número\n")
    elif(int(number) != -1):
        number = input("Não é o número\n")
        if(int(number) % 2 == 0):
            count += 1
    else:
        print(f"Você acertou o número após {count} pares")
        break