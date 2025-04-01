number = input("Digite um número\n")
while number.isdigit() == False:
    number = input("Digite um número\n")
while int(number) < 100:
    number *= 3
print(number)
