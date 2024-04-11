nome = input("Escreva seu nome, meu querido!");
try: 
    idade = int(input("Escreva sua idade, meu querido!"));
except ValueError:
    print("Voce é buro e digitou errado")
print(f"Ola{nome},você tem {idade} anos");
 
