from atendimento import SistemaAtendimento

def menu():
    sistema = SistemaAtendimento()

    while True:
        print("""
--- Sistema de Atendimento ---
1 - Adicionar cliente
2 - Atender próximo cliente
3 - Desfazer último atendimento
4 - Mostrar sistema
0 - Sair
""")

        op = input("Escolha uma opção: ")

        if op == "1":
            nome = input("Nome: ")
            tipo = input("Tipo (normal/prioritario): ")

            if tipo == "prioritario":
                prioridade = int(input("Prioridade (1 = mais urgente): "))
                sistema.adicionar_cliente(nome, tipo, prioridade)
            else:
                sistema.adicionar_cliente(nome, tipo)

        elif op == "2":
            cliente = sistema.atender()
            if cliente:
                print(f"Atendendo {cliente}")
            else:
                print("Nenhum cliente para atender.")

        elif op == "3":
            cliente = sistema.desfazer()
            if cliente:
                print(f"Atendimento desfeito. Cliente devolvido: {cliente}")
            else:
                print("Nada para desfazer.")

        elif op == "4":
            sistema.mostrar()

        elif op == "0":
            print("Encerrado.")
            break

        else:
            print("Opção inválida.")

menu()
