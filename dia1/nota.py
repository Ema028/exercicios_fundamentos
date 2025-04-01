nota = input("Qual foi a sua nota de 0 a 10?\n")
while True:
    if(nota.isdigit() == False):
        nota = input("Digite um número\n")
    elif(int(nota) < 0 or int(nota) > 10):
            nota = input("Digite un número de 0 a 10\n")
    else:
        break;