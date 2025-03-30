from math import sqrt

print("Calculadora de  hipotenusas")
cateto1 = int(input("Qual o valor do primeiro cateto?\n"))
cateto2 = int(input("Qual o valor do segundo cateto?\n"))

hipotenusa = sqrt(cateto1 ** 2 + cateto2 ** 2)
print(f"A hipotenusa é {hipotenusa}")
