print("Separador de notas")
valor = int(input("Qual o valor?"))
nota_100 = valor // 100
nota_50 = (valor - (nota_100 * 100)) // 50
nota_20 = (valor - (nota_100 * 100) - (nota_50 * 50) // 20
nota_10 = (valor - (nota_100 * 100) - (nota_50 * 50) - (nota_20 * 20) // 10
print(f"Você vai precisar de {nota_100} notas de 100, {nota_50} de 50, {nota_20} de 20, {nota_10}")
