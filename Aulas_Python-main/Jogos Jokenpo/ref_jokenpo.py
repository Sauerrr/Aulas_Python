import random

def ganhador(escolha_jogador , escolha_computador):
            if escolha_jogador == escolha_computador:
                  return "Empatou!"
            elif(
                  (escolha_jogador == "papel" and escolha_computador == "pedra") or
                  (escolha_jogador == "pedra" and escolha_computador == "tesoura") or
                  (escolha_jogador == "tesoura" and escolha_computador == "papel")
                 ):
                  return "Voce ganhou meu querido"
            else:
                  return "Voce perdeu meu querido :("
            

def jogar_jokenpo():
    opcoes = ["pedra", "papel", "tesoura"]
    vitorias = 0
    print("Ola meu querido jogador, seja bem-vindo ao jogo Jokenpô")
    print("Escolha: pedra, papel ou tesoura")

    #pontuacao = 0

    while True:
        escolha_jogador = input("Sua escolha:").lower()
        if escolha_jogador not in opcoes:
            print("Escolha inválida. Tente novamente")
            continue

        escolha_computador = random.choice(opcoes)
        print(f"Computador escolheu: {escolha_computador}")

        resultado = ganhador(escolha_jogador , escolha_computador)
        print(resultado)

        if resultado == "Voce ganhou meu querido":
            vitorias += 1
        elif resultado == "Voce perdeu meu querido :(":
            vitorias -= 1
        else:
            vitorias += 0

        
        print(f"O seu total de vitórias foi: {vitorias}")


        jogar_novamente = input("Voce quer jogar novamente?").lower()
        if jogar_novamente != "sim":
            break
if __name__ == "__main__":
    jogar_jokenpo()