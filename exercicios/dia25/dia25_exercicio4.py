from math import sqrt

print("Calculadora de distâncias")
point1 = input("Insira as coordenadas x e y do ponto 1(x,y)\n").lstrip('(').rstrip(')').split(',')
point2 = input("Insira as coordenadas x e y do ponto 2(x,y)\n").lstrip('(').rstrip(')').split(',')

# d = raiz((x1 - x2) ** 2 + (y1 - y2) ** 2)
distance = sqrt((int(point1[0]) - int(point2[0])) ** 2 + (int(point1[1]) - int(point2[1])) ** 2)

print(f"A distância entre os pontos é {distance:.2f}")
