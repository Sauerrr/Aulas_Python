import random 

numero_aleatorio = random.randint(0,10)
tentativas = 0
max_tentativa = 5


while tentativas < max_tentativa:
    palpite = int(input("Digite um número entre 1 a 10"))
    tentativas += 1
    
    if palpite == numero_aleatorio:
        print("Voce acertou")
        break
    elif palpite < numero_aleatorio:
        print("Tente um numero maior")
    else:
        print("Tente um numero menor")
    
    if tentativas < max_tentativa:
        print(f"Voce ainda tem {max_tentativa - tentativas} tentativas")
    else:
        print(f"Infelizmente voce nao conseguiu, o numero era {numero_aleatorio}")
        
print("Fim de jogo, obrigado por jogar!")
    