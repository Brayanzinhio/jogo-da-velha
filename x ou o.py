# Função para imprimir o tabuleiro
def imprimir_tabuleiro(tabuleiro):
    print("\n")
    for i in range(3):
        for j in range(3):
            print(" " + tabuleiro[i][j] + " ", end="")
            if j != 2:
                print("|", end="")
        print()
        if i != 2:
            print("---+---+---")
    print("\n")

# Função para verificar se alguém venceu
def verificar_vencedor(tabuleiro, jogador):
    # Verificação de linhas
    for i in range(3):
        if tabuleiro[i][0] == jogador and tabuleiro[i][1] == jogador and tabuleiro[i][2] == jogador:
            return True
    # Verificação de colunas
    for j in range(3):
        if tabuleiro[0][j] == jogador and tabuleiro[1][j] == jogador and tabuleiro[2][j] == jogador:
            return True
    # Verificação de diagonais
    if tabuleiro[0][0] == jogador and tabuleiro[1][1] == jogador and tabuleiro[2][2] == jogador:
        return True
    if tabuleiro[0][2] == jogador and tabuleiro[1][1] == jogador and tabuleiro[2][0] == jogador:
        return True
    return False

# Função principal
def main():
    tabuleiro = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
    jogador = 'X'

    print("Jogo da Velha\n")

    # Loop principal do jogo
    for _ in range(9):
        imprimir_tabuleiro(tabuleiro)

        linha = int(input("Jogador " + jogador + ", informe a linha (1-3): "))
        coluna = int(input("Jogador " + jogador + ", informe a coluna (1-3): "))

        # Verificar se a posição está vazia
        if tabuleiro[linha - 1][coluna - 1] != ' ':
            print("Posição inválida! Tente novamente.")
            continue

        # Preencher a posição com o símbolo do jogador
        tabuleiro[linha - 1][coluna - 1] = jogador

        # Verificar se o jogador venceu
        if verificar_vencedor(tabuleiro, jogador):
            imprimir_tabuleiro(tabuleiro)
            print("Jogador", jogador, "venceu!")
            return

        # Alternar entre os jogadores
        jogador = 'O' if jogador == 'X' else 'X'

    imprimir_tabuleiro(tabuleiro)
    print("Empate!")

if __name__ == '__main__':
    main()
