from funcoes import *

def main():
    sistema = start()

    while True:
        print("--- Bem vindo ao gerenciador de clientes ---")
        print("1-Adicionar cliente")
        print("2-Sair")
        opcao = int(input("\nSelecione:"))

        if opcao == 1:
            adicionar_cliente(sistema)
        
        elif opcao == 2:
            print("\nEncerrando...\n")
            break
        else:
            print("\nErro! Opção Inválida!\n")

if __name__ =="__main__":
    main()