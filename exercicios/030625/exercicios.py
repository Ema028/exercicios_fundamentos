#1 e 2
dicionario = {}

palavra = input("diga uma palavra:\n")
for letter in palavra:
    if letter not in dicionario.keys():
        dicionario[letter] = 1
    else:
        dicionario[letter] += 1
        
print(dicionario)

new_dict = {}

for key in dicionario.keys():
    new_dict[dicionario[key]] = key
    
print(new_dict)

#3
dict1 = {}
dict2 = {}

while True:
    key = input("diga uma chave:\n")
    if (key == "0"):
        break
    
    num = input("diga um valor:\n")
    dict1[key] = int(num)
    
    num = input("diga um valor:\n")
    dict2[key] = int(num)
    
for key in dict1.keys():
    dict2[key] += dict1[key]
    
print(dict2)
#4
dict1 = {}
dict2 = {}

while True:
    key = input("diga uma chave:\n")
    if (key == "0"):
        break
    
    num = input("diga um valor:\n")
    dict1[key] = int(num)
    
for key in dict1.keys():
    if (dict1[key] > 10):
        dict2[key] = dict1[key]
    
print(dict2)
#5
nomes = []
alfabeto = {}
nome = 'a'

while (nome != ''):
    nome = input("digite um nome: ")
    nomes.append(nome)
    
nomes.pop()
    
for nome in sorted(nomes):
    if nome[0] not in alfabeto:
        alfabeto[nome[0]] = [nome]
    else:
        alfabeto[nome[0]].append(nome)
        
print(alfabeto)
#6
estoque = {}
vendas = {}

while True:
    produto = input("diga um produto:\n")
    if (produto == ""):
        break
    
    num = input("qts dele no estoque:\n")
    estoque[produto] = int(num)
    
    num = input("qts vendidos:\n")
    vendas[produto] = int(num)
    
print(f"vendas: {vendas}")

for produto in vendas.keys():
    estoque[produto] -= vendas[produto]
    
print(f"estoque atualizado: {estoque}")
#7
from  unicodedata import normalize
def main():
    count_words = {}
    
    texto = input("diga seu dizer:\n").lower()
    #decompor caracteres para seus componentes, transforma em bytes ignorando oq não pode ser representado em ASCII e dps interpreta esses bytes de volta em uma string
    texto = normalize('NFKD', texto).encode('ASCII', 'ignore').decode('ASCII').split()
    
    for palavra in texto:
        palavra = clean_word(palavra)
        if (len(palavra) >= 4):
            if palavra not in count_words:
                count_words[palavra] = 1
            else:
                count_words[palavra] += 1
                
    print(count_words)
    
def clean_word(word):
    pontuacao = [' ', ',', '.', ';', ':', '?', '!']
    new_word = ""
    for char in word:
        if char not in pontuacao:
            new_word += char
    return new_word
    
main()
#8
alunos = {}

while True:
    aluno = input("qual o nome do aluno?\n")
    notas = []
    if (aluno == ''):
        break
    while True:
        nota = input("nota dele?\n")
        if (nota == ''):
            break
        notas.append(int(nota))
        
    alunos[aluno] = notas
    
print(alunos)

for aluno in alunos.keys():
    media = 0
    for nota in alunos[aluno]:
        media += nota
    media /= len(alunos[aluno])
    alunos[aluno] = round(media)
    
print(alunos)
