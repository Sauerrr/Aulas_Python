import forca
import adivinhacao

def escolha_jogo():
    print("******************************************")
    print("**************Escolha o Jogo**************")
    print("******************************************")
    print("(1)-Forca  (2)-Adivinhação")

    jogo = int(input("Qual jogo você quer jogar?"))

    if(jogo == 1):
        print("Jogando forca")
        forca.jogar()
    elif(jogo == 2):
        print("Jogando adivinhação")
        adivinhacao.jogar_adivinhacao()


if (__name__ == "__main__"):
    escolha_jogo()