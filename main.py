class JogoXadrez:
    def __init__(self):
        # Matriz 8x8 representando o tabuleiro
        self.tabuleiro = [['.' for _ in range(8)] for _ in range(8)]
        self.turno = "Brancas"
        self.preparar_tabuleiro()

    def preparar_tabuleiro(self):
        # Colocando peças iniciais apenas para demonstração da lógica
        self.tabuleiro[0] = ['T', 'C', 'B', 'Q', 'K', 'B', 'C', 'T'] # Pretas
        self.tabuleiro[7] = ['t', 'c', 'b', 'q', 'k', 'b', 'c', 't'] # Brancas

    def mostrar_tabuleiro(self):
        print(f"\n--- Vez das {self.turno} ---")
        for linha in self.tabuleiro:
            print(" ".join(linha))

    def realizar_jogada(self):
        # Lógica de alternância de turno
        if self.turno == "Brancas":
            self.turno = "Pretas"
        else:
            self.turno = "Brancas"

if __name__ == "__main__":
    partida = JogoXadrez()
    partida.mostrar_tabuleiro()
    partida.realizar_jogada() # Simula o fim de um movimento
    partida.mostrar_tabuleiro()
