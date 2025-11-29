class Cliente:
    def __init__(self, nome, tipo="normal", prioridade=None):
        self.nome = nome
        self.tipo = tipo
        self.prioridade = prioridade  # quanto MENOR, mais prioritário

    def __repr__(self):
        if self.tipo == "prioritario":
            return f"{self.nome} (prioridade {self.prioridade})"
        return f"{self.nome} (normal)"

