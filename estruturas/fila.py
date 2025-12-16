#importações
from collections import deque

#criação da classe e funções que ela possui
class Fila:
    #construtor
    def __init__(self):
        #inicia a fila usando o deque
        self.fila = deque()
    #Método pra adicionar um ítem na fila
    def adicionar(self, cliente):
        self.fila.append(cliente)
    #método pra remover um ítem da fila
    def remover(self):
        #verifica se a fila está vazia
        if self.fila:
            #retorna o item que tá no começo para remoção
            return self.fila.popleft()
            #se a fila estiver vazia, retorna 'none'
        return None

    #defile como a fila vai ser exibida se for inmpressa
    def __repr__(self):
        #converte o deque pra lista comum
        return str(list(self.fila))
