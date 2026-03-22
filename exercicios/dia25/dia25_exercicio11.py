print("Calculadora de energia cinética")

massa = int(input("Qual a massa do objeto?(Em s)\n"))
velocidade = int(input("Qual a velocidade do objeto?(Em m/s)\n"))
energia = massa * (velocidade ** 2) / 2

print(f"A energia cinética é {energia} N")
