print("Calculadora de divisões")

dividendo = int(input("Qual o dividendo?\n"))
divisor = int(input("Qual o divisor?\n"))
if divisor == 0:
    print("Não podemos dividir por 0")
else:
    resultado = dividendo / divisor
    print(resultado)
