number = input("Digite um número:\n")
while (number.isalpha == True):
    print("Não é um número válido\n")
else:
    for i in range(1,11):
        print(f"{number} * {i} = ", int(number) * i)
