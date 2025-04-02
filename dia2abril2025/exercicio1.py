number = input("Digite um número\n")
while True:
    if(number.isdigit() == False):
        number = input("Digite um número\n")
    elif(int(number) < 0):
        number = input("Digite um número\n")
    else:
        print("O número é válido")
        break