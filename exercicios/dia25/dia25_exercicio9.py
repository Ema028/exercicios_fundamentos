print("Calculadora de IMC")

peso = int(input("Qual o seu peso?(Em kg)\n"))
altura = float(input("Qual a sua altura?(Em m)\n"))
imc = peso / altura ** 2
print(f"Seu IMC é: {imc}")
