import random

def jogar_adivinhacao():
    
    nivel = int(input("Escolha o nivel de dificuldade (1-Facil, 2-Médio, 3-Dificil)"))
    max_numero = 10 if nivel == 1 else 50 if nivel == 2 else 100
    numero_secreto = random.randint(1,max_numero)
    tentativas = 10 if nivel == 1 else 5 if nivel == 2 else 3
    pontos =  1000
    
    print(f"Jogo de adivinhação - Nivel {nivel}.")
    print(f"Tente adivinhar o numero que estou pensando entre, 1 e {max_numero}. ")
    
    for tentativa in range (1, tentativas + 1):
        print(f"Tentativa {tentativa} de {tentativas}")
        palpite = int(input("Digite seu palpite:"))
        
        if palpite < 1 or palpite > max_numero:
            print(f"Digite um numero entre 1 e {max_numero}.")
            continue
        acertou = palpite == numero_secreto
        maior = palpite > numero_secreto
        menor = palpite < numero_secreto
        
        if acertou:
            print(f"Voce acertou e fez {pontos} pontos!")
            break
        else:
            pontos_perdidos = abs(numero_secreto - palpite)
            pontos -= pontos_perdidos
            if maior:
                print("Seu palpite foi maior do que o numero secreto.")
            elif menor:
                print("Seu palpite foi menor do que o numero secreto.")
                
    if not acertou:
        print(f"Suas tentativas acabaram. O numero secreto era {numero_secreto}.")
    print("Fim de jogo!")
    
if __name__ == "__main__":
    jogar_adivinhacao()

    #teste