#exercicio1
string = input("Digite uma palavra:\n")
new = string[:1] + "x" + string[2:]
print(new)

#exercicio2
string = input("Digite uma frase:\n")
string2 = string.lower()
count = 0
for i in range(len(string)):
    if(string[i] != string2[i]):
        count += 1
print(count)

#exercicio3
string = input("Digite uma frase:\n").replace(" ", "")
print(string)

#exercicio4
string = input("Digite uma frase:\n")[::-1]
print(string)

#exercicio5
string = input("Digite uma frase com letras e números:\n")
count = 0
for i in range(len(string)):
    if(string[i].isdigit() == True):
        count += int(string[i])
print(count)

#exercicio6
string = input("Digite uma palavra:\n")
new = ""
for char in string:
    if char not in new:
        new += char
print(new)

#exercicio7
string = input("Digite uma frase:\n")
letra = input("Digite uma letra:\n")
count = 0
for i in range(len(string)):
    if(letra == string[i]):
        count += 1
print(count)