from random import randint, shuffle

vizinhos_index = [(-1, 0), (0, -1), (0, 1), (1, 0)]

class Bot:
    def __init__(self):
        self.tries = []

    def robot_try(self, tabuleiro):
        x = randint(0, tabuleiro.tamanho - 1)
        y = randint(0, tabuleiro.tamanho - 1)
        #não faz tentativas repetidas
        while (x, y) in self.tries:
            x = randint(0, tabuleiro.tamanho - 1)
            y = randint(0, tabuleiro.tamanho - 1)
        self.tries.append((x, y))
        return (x, y)

    #tentar acertar vizinhos de satélite derrubado
    def robot_next_try(self, tabuleiro):
        x = self.tries[len(self.tries) - 1][0]
        y = self.tries[len(self.tries) - 1][1]
        while True:
            vizinho = 0
            shuffle(vizinhos_index)
            while (vizinho < len(vizinhos_index) - 1):
                if (tabuleiro.in_bounds(x + vizinhos_index[vizinho][0]) and tabuleiro.in_bounds(y + vizinhos_index[vizinho][1])):
                    break
                vizinho += 1
            linha = x + vizinhos_index[vizinho][0]
            coluna = y + vizinhos_index[vizinho][1]
            if ((linha, coluna) not in self.tries):
                self.tries.append((linha, coluna))
                return (linha, coluna)
