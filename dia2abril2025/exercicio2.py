number = input("Digite um número\n")
count = 0
while True:
    if(number.isdigit() == False):
        number = input("Digite um número\n")
    elif(int(number) != 100):
        number = input("Não é o número\n")
        count += 1
    else:
        print(f"Você acertou o número em {count} tentativas")
        break