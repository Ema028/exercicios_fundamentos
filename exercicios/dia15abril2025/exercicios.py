#exercicio 1
string = input("Digite uma frase:\n").split(' ')
espacos = len(string) - 1
print(espacos)

#exercicio 2
string = input("digite uma frase:\n")
print(string[0], string[len(string) - 1])

#exercicio 4
string = input("digite uma palavra:\n")
palindromo = True
for i in range(len(string)):
    if(string[i] != string[len(string) - 1 - i]):
        print("Não é palíndromo")
        palindromo = False
        break
if palindromo:
    print("é palíndromo")
    
#a = input()
#if a==a[::-1]:
#    print("sim")
#else:
#   print("nao")