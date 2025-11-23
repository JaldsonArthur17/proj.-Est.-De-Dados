import heapq
from collections import deque 

class Cliente: 
    def __init__(self, nome, grau_prioride):
        self.nome = nome;
        self.grau_prioridade = grau_prioride;
        
    def __lt__(self,other):
        return self.grau_prioridade < other.grau_prioridade;
    
    def __repr__(self):
        tipo = "prioridade" if self.grau_prioridade < 5 else "prioridade normal"
        return f"[{tipo} - Grau {self.grau_prioridade}] {self.nome}"

