import heapq

class HeapPrioridade:
    def __init__(self):
        self.heap = []

    def adicionar(self, cliente):
        heapq.heappush(self.heap, (cliente.prioridade, cliente))

    def remover(self):
        if self.heap:
            return heapq.heappop(self.heap)[1]
        return None

    def __repr__(self):
        return str(self.heap)
