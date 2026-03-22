class Jogador:
    def __init__(self):
        self.tentativa_x = 0
        self.tentativa_y = 0

    def human_try(self, tabuleiro):
        #usuário (1,6), index(0,5), in_bounds para checar index válido
        tentativa_x = self.get_int("Qual linha(1 a 6)?\n") - 1
        while not tabuleiro.in_bounds(tentativa_x):
            print("linha fora do tabuleiro")
            tentativa_x = self.get_int("Qual linha(1 a 6)?\n") - 1

        tentativa_y = self.get_int("Qual coluna(1 a 6)?\n") - 1
        while not tabuleiro.in_bounds(tentativa_y):
            print("coluna fora do tabuleiro")
            tentativa_y = self.get_int("Qual coluna(1 a 6)?\n") - 1
        return (tentativa_x, tentativa_y)

    def get_int(self, string):
        number = 0
        try:
            number = int(input(string))
        except:
            print("número inválido")
            self.get_int(string)
        return number
