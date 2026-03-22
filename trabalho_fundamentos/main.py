from tabuleiro import Tabuleiro
from jogador import Jogador
from bot import Bot

satelites = 4
tamanho = 6
tabuleiro1 = Tabuleiro(tamanho)
tabuleiro1.gerar_satelites(satelites)
tabuleiro2 = Tabuleiro(tamanho)
tabuleiro2.gerar_satelites(satelites)
jogador1 = Jogador()

def main():
    oponente = choose_warrior()
    if (oponente == 1):
        bot = Bot()
        bot_derrubou = 0
        while (len(tabuleiro1.satelites) > 0 and len(tabuleiro2.satelites) > 0):
            jogada_jogador(jogador1, tabuleiro1)
            print("Tabuleiro do jogador:")
            print_matriz(tabuleiro1)
            print("Turno do computador:")
            jogada_bot(bot, bot_derrubou)
            print("Tabuleiro do computador:")
            print_matriz(tabuleiro2)
            bot_derrubou = tabuleiro2.derrubados
    else:
        jogador2 = Jogador()
        while (len(tabuleiro1.satelites) > 0 and len(tabuleiro2.satelites) > 0):
            print("Turno do jogador 1:")
            jogada_jogador(jogador1, tabuleiro1)
            print("Tabuleiro do jogador 1:")
            print_matriz(tabuleiro1)
            print("Turno do jogador 2:")
            jogada_jogador(jogador2, tabuleiro2)
            print("Tabuleiro do jogador 2:")
            print_matriz(tabuleiro2)
    if(len(tabuleiro1.satelites) == 0):
        print("VOCÊ VENCEU!!!")
    else:
        print("você perdeu...dundundun")

def jogada_jogador(jogador, tabuleiro):
        tentativa = jogador.human_try(tabuleiro)
        tabuleiro.check_try(tentativa[0], tentativa[1])

def print_matriz(tabuleiro):
    matriz_discreta = tabuleiro.gerar_matriz_oculta()
    for linha in matriz_discreta:
        print(linha)
    print("\n")

def jogada_bot(bot, jogadas_sucesso):
    if (jogadas_sucesso % 2 == 0):
        tentativa = bot.robot_try(tabuleiro2)
    else:
        tentativa = bot.robot_next_try(tabuleiro2)

    tabuleiro2.check_try(tentativa[0], tentativa[1])

def choose_warrior():
    print("escolha seu oponente:")
    oponente = 0
    try:
        oponente = int(input("Computador(digite 1) ou um Amigo(digite 2):\n"))
        if (oponente != 1 and oponente != 2):
            raise
    except:
        print("opção inválida")
        choose_warrior()
    return oponente

main()
