import os


def mostrarLista(lista):
    print("Sua lista atual é essa: ", lista)

def gravarLista(lista):
    nome_arq = input("Digite o nome do arquivo:")
    nome_arq += ".txt"
    with open (nome_arq, "w") as arquivo:
        for item in lista:
            arquivo.write(item + "/n")
    print("Gravado com sucesso!", nome_arq)

def carregar_arquivo(lista):
    nome_arquivo = input("Digite o nome do arquivo para carregar a lista:")
    nome_arquivo += ".txt"
    try:
        with open (nome_arquivo, "r") as arquivo:
            lista.clear()
            for linha in arquivo:
                lista.append(linha.strip())
        print("Lista carregada com sucesso do arquivo" , nome_arquivo)
    except FileNotFoundError:
        print("O arquivo não foi encontrado.")
    except Exception as e:
        print("Ocorreu um erro." , e)


def ordenar_lista(lista):
    lista.sort(reversed = True)
    print("Lista ordenada com sucesso")

def listar_arquivos(extensao = ".txt"):

    diretorios = os.getcwd()
    arquivos = os.listdir(diretorios)
    print(f"Os arquivos .{extensao} desse diretorio são:")
    for lista_arquivo in arquivos:
        if lista_arquivo.endswith(extensao):
            print(lista_arquivo)


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
        print("4 - Gravar lista")
        print("5 - Listar arquivos")
        print("6 - Carregar o arquivo")
        print("7 - Ordenar lista")
        print("8 - Sair")


        opcao = input("Digite o número da opção que voce deseja: ")

        if opcao == "1":
            adicionarItem(lista)
        elif opcao == "2":
            excluirItem(lista)
        elif opcao == "3":
            mostrarLista(lista)
        elif opcao == "4":
            gravarLista(lista)
        elif opcao == "5":
            listar_arquivos()
        elif opcao == "6":
            carregar_arquivo(lista)
        elif opcao == "7":
            ordenar_lista(lista)
        elif opcao == "8":
            continuar = False
        else:
            print("Opção inválida. Digite novamente.")


    print("Fim da lista.")

if __name__ == "__main__":
    main()