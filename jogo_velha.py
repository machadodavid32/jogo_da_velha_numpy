import numpy as np

def colocar_peca(tabuleiro, linha, coluna, peca):
    """Coloca a peça do jogador na posição escolhida"""
    tabuleiro[linha, coluna] = peca

def verifica_vitoria(tabuleiro, peca):
    """Verifica se o jogador ganhou o jogo"""
    linhas = np.any(np.all(tabuleiro == peca, axis=1))  # verifica se o jogador conseguiu alinhar as peças
    colunas = np.any(np.all(tabuleiro == peca, axis=0))  # axis=0 verifica se o jogador alinhou as peças na coluna
    diagonais = np.all(np.diag(tabuleiro) == peca) or np.all(np.diag(np.fliplr(tabuleiro)) == peca)
    # verifica se o jogador alinhou as diagonais pra esquerda e para a direita
    return linhas or colunas or diagonais  # basta que apenas uma condição seja True para vencer o jogo

def imprimir_tabuleiro(tabuleiro):
    """Imprime o tabuleiro no terminal de forma visível ao jogador"""
    for linha in tabuleiro:
        print(" | ".join(str(x) if x != 0 else " " for x in linha))
        print("-" * 8)

def jogo():
    """Função principal para rodar o jogo da velha"""
    tabuleiro = np.zeros((3, 3), dtype=int)

    peca_atual = 1  # jogador 1
    vencedor = False
    empate = False

    while not vencedor and not empate:
        imprimir_tabuleiro(tabuleiro)

        while True:
            try:
                linha = int(input(f"Jogador {peca_atual}, escolha a linha (0, 1 ou 2):"))
                coluna = int(input(f"Jogador {peca_atual}, escolha a coluna (0, 1 ou 2):"))

                # Verifica se a linha e a coluna são inválidas
                if linha not in [0, 1, 2] or coluna not in [0, 1, 2]:
                    print("\nEscolha linhas e colunas válidas (de 0 a 2.)\n")
                    continue

                # verifica se a posição já está ocupada
                if tabuleiro[linha][coluna] != 0:  # posição está ocupada
                    print("\nPosição ocupada. Tente novamente.\n")
                    continue

                colocar_peca(tabuleiro, linha, coluna, peca_atual)
                vencedor = verifica_vitoria(tabuleiro, peca_atual)

                # Se houve empate
                if np.all(tabuleiro != 0) and not vencedor:
                    empate = True
                break

            except ValueError:
                print("\nEntrada Inválida! Por favor, insira números inteiros de 0 a 2\n")

        # Troca jogador
        if not vencedor and not empate:
            peca_atual = 2 if peca_atual == 1 else 1

    imprimir_tabuleiro(tabuleiro)

    if vencedor:
        print(f"\nParabéns, jogador {peca_atual} venceu!")
    else:
        print("\n\nEmpate")

jogo()
