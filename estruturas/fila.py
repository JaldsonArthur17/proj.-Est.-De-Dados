from collections import deque

class Fila:
    def __init__(self):
        self.fila = deque()

    def adicionar(self, cliente):
        self.fila.append(cliente)

    def remover(self):
        if self.fila:
            return self.fila.popleft()
        return None

    def __repr__(self):
        return str(list(self.fila))
