print("Insira nota1,nota2")

provas = input("Qual foi a sua nota nas duas provas?\n").split(',')
media = int(provas[0]) + int(prvas[1]) / 2

if media >= 7:
    print("Aprovado")
elif media < 4:
    print("Reprovado")
else:
    print("Você vai pra prova final")
