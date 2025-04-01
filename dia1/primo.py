number = input("Digite um número\n")
while number.isdigit() == False:
    number = input("Digite um número\n")
for i in range(2, int(number)):
    if int(number) % i == 0:
        print(f"o número {number} não é primo")
        break;
print(f"o número {number} é primo")
