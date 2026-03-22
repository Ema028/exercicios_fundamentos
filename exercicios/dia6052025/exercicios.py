#2
A = []
V = []
for i in range(5):
    a = int(input("biribiri\n"))
    A.append(a)
for a in A:
    if (a % 2 == 1):
        V.append(3 * a)
    else:
        V.append(2 * a)
        
print(V)

#3
from random import *
mega = []
for i in range(6):
    num = randint(1,60)
    while(num in mega):
        num = randint(1,60)
    mega.append(num)
print(mega)

#4
num = input("qual o número para procurar?\n")
lista = input("insira valores para a lista\n").split()
count = 0

for numero in lista:
    if (numero == num):
        count += 1
        
print(count)

#5
lista1 = []
lista2 = [0] * 5
for i in range(5):
    num = input("biribiri\n")
    lista1.append(num)
    lista2[4 - i] = num
    
print(lista1, lista2)

#6
lista = input("birabira\n").split()
print(set(lista))

#6
lista = []
lista2 = []
while True:
    num = input("biri?\n")
    lista.append(num)
    if num not in lista2:
        lista2.append(num)
    contunua = input("birbiribiri?\n")
    if (contunua != 's'):
        break
print(lista, lista2)