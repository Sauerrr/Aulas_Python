def mostrarLista(lista):
    print("Sua lista atual é essa: ", lista)

def adicionarItem(lista):
    item = input("Digite algo que deseja adcionar na sua linda lista: ")
    lista.append(item)
    mostrarLista(lista)

def excluirItem(lista):
    item = input("Digite o item que voce deseja excluir da sua lista: ")
    if item in lista:
        lista.remove(item)
        mostrarLista(lista)
    else:
        print("Erro. Este item não consta em sua lista")

def main():
    lista = []
    continuar = True

    while continuar:
        print("Escolha uma das opções abaixo:")
        print("1 - Adicionar item")
        print("2 - Excluir item")
        print("3 - Exibir lista")
        print("4 - Sair")


        opcao = input("Digite o número da opção que voce deseja: ")

        if opcao == "1":
            adicionarItem(lista)
        elif opcao == "2":
            excluirItem(lista)
        elif opcao == "3":
            mostrarLista(lista)
        elif opcao == "4":
            continuar = False
        else:
            print("Opção inválida. Digite novamente.")

        print()

    print("Fim da lista.")

if __name__ == "__main__":
    main()