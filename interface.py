import pyautogui

def mostrar_tabuleiro(tabuleiro):
    """Exibe o tabuleiro formatado em uma mensagem"""
    tabuleiro_str = "\n".join([" | ".join(str(x) if x != 0 else " " for x in linha) for linha in tabuleiro])
    pyautogui.alert(tabuleiro_str, "Tabuleiro Atual")

def solicitar_jogada(jogador):
    """Solicita ao usuário uma linha e coluna"""
    linha = pyautogui.prompt(f"Jogador {jogador}, escolha a linha (0, 1 ou 2):", "Entrada")
    coluna = pyautogui.prompt(f"Jogador {jogador}, escolha a coluna (0, 1 ou 2):", "Entrada")

    try:
        return int(linha), int(coluna)
    except ValueError:
        pyautogui.alert("Entrada inválida! Digite números inteiros de 0 a 2.", "Erro")
        return solicitar_jogada(jogador)
