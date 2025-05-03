import numpy as np
import interface
import pyautogui

def colocar_peca(tabuleiro, linha, coluna, peca):
    tabuleiro[linha, coluna] = peca

def verifica_vitoria(tabuleiro, peca):
    linhas = np.any(np.all(tabuleiro == peca, axis=1))
    colunas = np.any(np.all(tabuleiro == peca, axis=0))
    diagonais = np.all(np.diag(tabuleiro) == peca) or np.all(np.diag(np.fliplr(tabuleiro)) == peca)
    return linhas or colunas or diagonais

def jogo():
    tabuleiro = np.zeros((3, 3), dtype=int)
    peca_atual = 1
    vencedor = False
    empate = False

    while not vencedor and not empate:
        interface.mostrar_tabuleiro(tabuleiro)
        linha, coluna = interface.solicitar_jogada(peca_atual)

        if linha not in [0, 1, 2] or coluna not in [0, 1, 2] or tabuleiro[linha, coluna] != 0:
            pyautogui.alert("Jogada inválida, tente novamente!", "Erro")
            continue

        colocar_peca(tabuleiro, linha, coluna, peca_atual)
        vencedor = verifica_vitoria(tabuleiro, peca_atual)
        if np.all(tabuleiro != 0) and not vencedor:
            empate = True

        if not vencedor and not empate:
            peca_atual = 2 if peca_atual == 1 else 1

    interface.mostrar_tabuleiro(tabuleiro)
    pyautogui.alert(f"Jogador {peca_atual} venceu!" if vencedor else "Empate!", "Fim do Jogo")

if __name__ == "__main__":
    jogo()
