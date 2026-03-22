#1
produtos = {}
for i in range(3):
    produto = input("Qual o produto a ser cadastrado?\n")
    preco = input("Qual o preço?(em reais)\n")
    produtos[produto] = preco
print(produtos)

#2
alunos = {}
media = 0
for i in range(3):
    aluno = input("Qual o aluno a ser cadastrado?\n")
    nota = int(input("Qual a nota?\n"))
    alunos[aluno] = nota
print(alunos)
    
for nota in alunos.values():
    media += nota
        
print(f"média: {media}")
