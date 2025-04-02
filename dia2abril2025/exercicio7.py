number = input("Digite um número\n")
while True:
    if(number.isalpha() == True):
        number = input("Digite um número\n")
    elif(int(number) > 0):
        print("O número é válido")
        break
    else:
        number = input("Número inválido\n")