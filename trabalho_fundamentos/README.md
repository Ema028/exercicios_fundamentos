# trabalho_fundamentos

Jogo estilo batalha naval no terminal, cria 4 satélites de 2 espaços em uma matriz 6x6 como tabuleiro, têm opções de oponente jogar contra outras pessoas ou contra um algoritmo "inteligente".
### bot.py:
define a classe do oponente "robô", ele salva as tentativas que ele fez e depois de uma tentativa bem sucedida ele tenta acertar os vizinhos até achar a outra ponta do satélite.
### tabuleiro.py:
define a classe tabuleiro que cuida de gerar os satélites e salvar todas as alterações no tabuleiro, além de criar as matrizes ocultas e dar feedback se os satélites forem derrubados.
