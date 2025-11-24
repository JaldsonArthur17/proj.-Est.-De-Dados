import heapq
from collections import deque

class Cliente:
    def __init__(self, nome, eh_prioridade):
        self.nome = nome
        self.eh_prioridade = eh_prioridade

def adicionar_cliente(sistema):
    nome = input("\ninsira o nome do ciente:")
    prioridade = input("\nqual o nível de prioridade? (Normal/Alta):").strip().upper()

    eh_prioridade = (prioridade == "ALTA")
    novo_cliente = Cliente(nome, eh_prioridade)

    if prioridade == "ALTA":
        heapq.heappush(sistema['prioridade'], novo_cliente)
        print(f"o cliente ---> {nome} foi adicionado a fila de alta prioridade\n")

    elif prioridade == "NORMAL":
        sistema['normal'].append(novo_cliente)
        print(f"o cliente ---> {nome} foi adicionado a fila de prioridade normal\n")
    else: 
        print("Erro! Tente Novamente.")

def start():
    return {
        "prioridade": [],
        "normal": deque(),
        "historico": []
    }