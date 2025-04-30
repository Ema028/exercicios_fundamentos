#1
class Participante():
    def __init__(self, id, vel, dist):
        self.id = id
        self.vel = vel
        self.dist = dist
        
participantes = []
for i in range (5):
    id = int(input("Qual o id do participante?\n"))
    vel = int(input("Qual a velocidade média do participante?\n"))
    dist = int(input("Qual a distância total percorrida pelo participante?\n"))
    new_participante = Participante(id, vel, dist)
    participantes.append(new_participante)
    
mvp_vel = Participante(0, 0, 0)
mvp_dist = Participante(0, 0, 0)

for participante in participantes:
    if (participante.dist > mvp_dist.dist):
        mvp_dist = participante
    if (participante.vel > mvp_vel.vel):
        mvp_vel = participante
        
print(f"a velocidade do que percorreu a maior distância é {mvp_dist.vel} e o id é {mvp_dist.id}")
print(f"a velocidade do mais rápido é {mvp_vel.vel} e o id é {mvp_vel.id}")

#2
frase = input("Diga:\n").lower()
vogais = ['a', 'e', 'i', 'o', 'u']
count = 0

for letter in frase:
    if(letter in vogais):
        count += 1

print(f"você disse {count} vogais")

#3
frase = input("Diga:\n").split()
new_frase = ""

for palavra in frase:
    for letra in range(len(palavra) - 1, -1, -1):
        new_frase = new_frase + palavra[letra]
    new_frase = new_frase + " "
        
print(new_frase)

#3
frase = input("Diga:\n").split()

for palavra in frase:
    print(palavra[::-1], end = ' ')