number = input("Digite um número\n")
while True:
    if(number.isdigit() == False):
        number = input("Digite um número\n")
    elif(int(number) < 10 or int(number) > 20):
        number = input("Digite um número\n")
    else:
        print("O número é válido")
        break