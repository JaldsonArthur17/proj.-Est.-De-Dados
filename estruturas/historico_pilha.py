class PilhaHistorico:
    def __init__(self):
        self.pilha = []

    def adicionar(self, cliente):
        self.pilha.append(cliente)

    def desfazer(self):
        if self.pilha:
            return self.pilha.pop()
        return None

    def __repr__(self):
        return str(self.pilha)
