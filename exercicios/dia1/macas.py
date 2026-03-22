from random import randint

class Apple:
    def __init__(self):
        self.id = 0
        self.peso = randint(1,10)
        
macas = []
macas_peso = []
        
for i in range(5):
    new_maca = Apple()
    new_maca.id = input("ID da maçã:\n")
    macas_peso.append(new_maca.peso)
    macas.append(new_maca)

maior_peso = max(macas_peso)
for maca in macas:
    if (maca.peso == maior_peso):
        print(f"O ID da maçã mais pesada é {maca.id}")
