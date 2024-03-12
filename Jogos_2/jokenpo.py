import random

def jogar_jokenpo():
    opcoes = ["pedra", "papel", "tesoura"]
    print("Ola meu querido jogador, seja bem-vindo ao jogo Jokenpô")
    print("Escolha: pedra, papel ou tesoura")

    while True:
        escolha_jogador = input("Sua escolha:").lower()
        if escolha_jogador not in opcoes:
            print("Escolha inválida. Tente novamente")
            continue

        escolha_computador = random.choice(opcoes)
        print(f"Computador escolheu: {escolha_computador}")

        pontuacao = 0

        if escolha_jogador == escolha_computador:
            pontuacao += 0

            print(f"Como voces dois escolheram {escolha_computador} o jogo empatou")
        elif(
            (escolha_jogador == "papel" and escolha_computador == "pedra") or
            (escolha_jogador == "pedra" and escolha_computador == "tesoura") or
            (escolha_jogador == "tesoura" and escolha_computador == "pedra")
        ):
            pontuacao += 1
            print("Voce ganhou!")
        else:
            pontuacao -= 1
            print("Voce perdeu.")

        print(f"Sua pontuação foi {pontuacao}")

        
            
        jogar_novamente = input("Voce quer jogar novamente, querido?").lower()
        if jogar_novamente != "sim":
            break

if __name__ == "__main__":
    jogar_jokenpo()