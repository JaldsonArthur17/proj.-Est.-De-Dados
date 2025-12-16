#importação do 'cerebro' que contem a lógica do sistema
from atendimento import SistemaAtendimento

#criação da função do menu que chama o SistemaAtendimento e executa
def menu():
    sistema = SistemaAtendimento()
    
#criação do Loop que vai ser executado ---> 'Menu'
    while True:
        print("""
--- Sistema de Atendimento ---
1 - Adicionar cliente
2 - Atender próximo cliente
3 - Desfazer último atendimento
4 - Mostrar sistema
0 - Sair
""")
        #aqui é feita a captura da escolha do usupário
        op = input("Escolha uma opção: ")

        #a partir daqui ele verifica qual opção foi selecionada 
        if op == "1":
            #armazenamento de dados
            nome = input("Nome: ")
            tipo = input("Tipo (normal/prioritario): ")

            #verifica se o atendimento pede nível de prioridade
            if tipo == "prioritario":
                #conversão de string pra int
                prioridade = int(input("Prioridade (1 = mais urgente): "))
                #aqui chama o método que adiciona os clientes com base nos campos informados
                sistema.adicionar_cliente(nome, tipo, prioridade)
            else:
                #se for normal, chama o mesmo método mas sem passar o campo de prioridade
                sistema.adicionar_cliente(nome, tipo)
                
        #verificação da opção 2
        elif op == "2":
            #aqui é feita a solicitação pra atender alguém ---> prioritário primeiro
            cliente = sistema.atender()
            #se o cliente foi retornado, informa quem foi atendido
            if cliente:
                print(f"Atendendo {cliente}")
            else:
                #se o sistema encontrar 'none' ---> filas vazias
                print("Nenhum cliente para atender.")

        #verificação da opçã 3
        elif op == "3":
            #aqui pede ao sistema para pegar o último histórico e devolver a fila
            cliente = sistema.desfazer()
            if cliente:
                #se um cliente foi retornado, informa que ele voltou pra fila
                print(f"Atendimento desfeito. Cliente devolvido: {cliente}")
            else:
                #se retornou 'none' ---> o histórico tá vazio
                print("Nada para desfazer.")

        #verificação da opção 4
        elif op == "4":
            #chama a função que mostra as filas
            sistema.mostrar()
        #verificação da opção 0 que encerra o sistema
        elif op == "0":
            print("Encerrado.")
            #encerramento do loop
            break
        #se o usuário inserir uma opção inválida, volta pro começo do loop
        else:
            print("Opção inválida.")
#aqui chama a função menu pra iniciar o sistema quando o script é ativado
menu()
