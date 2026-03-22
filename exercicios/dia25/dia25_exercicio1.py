print("Bem vindo ao caixa")
valor = int(input("Quanto custa o produto?(em reais)\n"))
desconto = int(input("Qual o percentual de desconto?\n"))
valor_final = valor * (100 - desconto) / 100
print(valor_final)
