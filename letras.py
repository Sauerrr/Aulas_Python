palavra_secreta = "antagorda";
letras_acertadas = ["_","_", "_" ,"_" , "_", "_", "_" ,"_", "_"];
tentativas = 8;

while tentativas > 0 and "_" in letras_acertadas:
    palpite = input("Digite uma letra, meu querido:").lower();
    if palpite in palavra_secreta:
        index = 0;
        for letra in palavra_secreta:
            if palpite == letra:
                letras_acertadas [index] = letra;
            index += 1
    else:
        tentativas -= 1;
        print(f"Voce tem {tentativas} restantes.")
    print(" ".join(letras_acertadas))
        
        
        
if "_"  not in letras_acertadas:
    print("MEUS PARABENSSSSS, VOCE GANHOUUUU")
else:
    print(f"KKKKKKKKKKKKK voce perdeu, a palavra era {palavra_secreta}");
    
                