print("Calculador de média")

print("insira como: nota,peso")
p1 = input("Qual foi a sua nota da primeira prova e o seu peso?\n").split(',')
p2 = input("Qual foi a sua nota da segunda prova e o seu peso??\n").split(',')
p3 = input("Qual foi a sua nota da terceira prova e o seu peso??\n").split(',')

media = (int(p1[0]) * int(p1[1]) + int(p2[0]) * int(p2[1]) + int(p3[0]) * int(p3[1])) / (int(p1[1]) + int(p2[1]) + int(p3[1]))
print(f"A sua média foi {media}")
