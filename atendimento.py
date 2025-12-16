#importações das 'ferramentas'
from utils.cliente import Cliente
from estruturas.fila import Fila
from estruturas.heap_prioridade import HeapPrioridade
from estruturas.historico_pilha import PilhaHistorico

#construtor
class SistemaAtendimento:
    def __init__(self):
        #fila fifo ---> quem chega antes, sai antes
        self.fila_normal = Fila()
        #heap ---> quem tem o menor número, sai antes
        self.fila_prioritaria = HeapPrioridade()
        #pilha ---> o último atendido fica no topo
        self.historico = PilhaHistorico()

    #aqui é feita a criação do cliente com os dados passados pelo empacotamento
    def adicionar_cliente(self, nome, tipo, prioridade=None):
        cliente = Cliente(nome, tipo, prioridade)
        #aqui é feita a verificação condicional de acordo com o que foi inserido 
        if tipo == "prioritario":
            self.fila_prioritaria.adicionar(cliente)
        else:
            self.fila_normal.adicionar(cliente)
            
    #criação da função de atendimento
    def atender(self):
        cliente = None

        #primeiro é feita a verificação da prioridade
        if self.fila_prioritaria.heap:
            cliente = self.fila_prioritaria.remover()
            
        #se prioridade for vazia, ele olha a normal
        elif self.fila_normal.fila:
            cliente = self.fila_normal.remover()
            
        #se achou alguém de qualquer fila
        if cliente:
            self.historico.adicionar(cliente)
            return cliente
        #se não houver ninguém em lugar nenhum
        return None
        
    #estrutura que realiza o cancelamento  
    def desfazer(self):
        cliente = self.historico.desfazer() #pega o último da pilha

        if not cliente: #verifica se a pilha está vazia
            return None

        #devolve para a fila correta
        if cliente.tipo == "prioritario":
            self.fila_prioritaria.adicionar(cliente) #aqui o heap se organiza sozinho
        else:
            #aqui o appendleft 'força' um atendimento desfeito a voltar pro local original
            self.fila_normal.fila.appendleft(cliente)

        return cliente
    #aqui é feita a 'impressão' do estado atual das filas
    def mostrar(self):
        print("\nFila prioritária:", self.fila_prioritaria)
        print("Fila normal:", self.fila_normal)
        print("Histórico:", self.historico, "\n")
