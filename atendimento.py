from utils.cliente import Cliente
from estruturas.fila import Fila
from estruturas.heap_prioridade import HeapPrioridade
from estruturas.historico_pilha import PilhaHistorico

class SistemaAtendimento:
    def __init__(self):
        self.fila_normal = Fila()
        self.fila_prioritaria = HeapPrioridade()
        self.historico = PilhaHistorico()

    def adicionar_cliente(self, nome, tipo, prioridade=None):
        cliente = Cliente(nome, tipo, prioridade)

        if tipo == "prioritario":
            self.fila_prioritaria.adicionar(cliente)
        else:
            self.fila_normal.adicionar(cliente)

    def atender(self):
        cliente = None

        if self.fila_prioritaria.heap:
            cliente = self.fila_prioritaria.remover()
        elif self.fila_normal.fila:
            cliente = self.fila_normal.remover()

        if cliente:
            self.historico.adicionar(cliente)
            return cliente

        return None

    def desfazer(self):
        cliente = self.historico.desfazer()

        if not cliente:
            return None

        if cliente.tipo == "prioritario":
            self.fila_prioritaria.adicionar(cliente)
        else:
            self.fila_normal.fila.appendleft(cliente)

        return cliente

    def mostrar(self):
        print("\nFila prioritária:", self.fila_prioritaria)
        print("Fila normal:", self.fila_normal)
        print("Histórico:", self.historico, "\n")
