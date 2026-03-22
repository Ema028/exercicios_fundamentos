#1
biri = []
bim = 0
for i in range(5):
    num = int(input("biribiri\n"))
    biri.append(num)
    bim += num
print(bim)

#2
list = []
count = 0
while True:
    num = int(input("birim\n"))
    list.append(num)
    if (num > 10):
        count += 1
    continua = input("biri?").lower()
    if (continua != 's'):
        break
print(count)

#3
list = []
while True:
    num = int(input("birim\n"))
    if (num < 0):
        list.append(0)
    else:
        list.append(num)
    continua = input("biri?").lower()
    if (continua != 's'):
        break
print(list)

#4
lista1 = []
lista2 = []
while True:
    num = int(input("birim\n"))
    if (num % 2 == 0):
        lista1.append(num)
    else:
        lista2.append(num)
    continua = input("biri?").lower()
    if (continua != 's'):
        break
print(lista1, lista2)

#5
lista1 = input("qual os números para a lista 1(separados por espaço)?\n").split()
lista2 = input("qual os números para a lista 2(separados por espaço, mesma qdd da 1)?\n").split()
lista3 = []
for i in range (len(lista1)):
    lista3.append(lista1[i])
    lista3.append(lista2[i])
    
print(lista1, lista2, lista3)