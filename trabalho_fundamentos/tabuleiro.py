from random import randint, shuffle

class Tabuleiro:
    def __init__(self, tamanho):
        self.tamanho = tamanho
        self.matriz = [[0] * self.tamanho for _ in range(self.tamanho)]
        self.satelites = []
        self.tentativas = []
        self.derrubados = 0

    def gerar_satelites(self, number):
        #index para vizinhos dos satélites escolhidos para satélites de 2 espaços
        vizinhos_index = [(-1, 0), (0, -1), (0, 1), (1, 0)]
        while (len(self.satelites) < 2 * number):
            sat_linha = randint(0, self.tamanho - 1)
            sat_coluna = randint(0, self.tamanho - 1)

            if ((sat_linha, sat_coluna) not in self.satelites):
                self.matriz[sat_linha][sat_coluna] = 1
                self.satelites.append((sat_linha, sat_coluna))
            else:
                continue
            while True:
                vizinho = 0
                shuffle(vizinhos_index)
                while (vizinho < len(vizinhos_index) - 1):
                    if (self.in_bounds(sat_linha + vizinhos_index[vizinho][0]) and self.in_bounds(sat_coluna + vizinhos_index[vizinho][1])):
                        break
                    vizinho += 1
                #tá onde já tem satélite
                linha = sat_linha + vizinhos_index[vizinho][0]
                coluna = sat_coluna + vizinhos_index[vizinho][1]
                if ((linha, coluna) not in self.satelites):
                    self.matriz[linha][coluna] = 1
                    self.satelites.append((linha, coluna))
                    break

    def check_try(self, x, y):
        if ((x, y) in self.satelites):
            print("satélite derrubado")
            self.matriz[x][y] = -1
            self.derrubados += 1
            self.satelites.remove((x, y))
        else:
            print("não foi dessa vez")
            self.tentativas.append((x, y))

    def gerar_matriz_oculta(self):
        matriz_oculta = [['?'] * self.tamanho for i in range(self.tamanho)]
        for i in range(self.tamanho):
            for j in range(self.tamanho):
                if (self.matriz[i][j] == -1):
                    matriz_oculta[i][j] = 'X'
                if (i, j) in self.tentativas:
                    matriz_oculta[i][j] = '.'
        return matriz_oculta

    def in_bounds(self, number):
        if (0 <= number <= self.tamanho - 1):
            return True
        return False
