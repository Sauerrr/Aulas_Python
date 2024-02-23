try:
    n1 = float(input("Digite um numero, meu querido"));
    n2 = float(input("Digite mais um numero, meu querido"));
    soma = n1 + n2;
    
    print (f"O número {n1} mais o número {n2} é igual a {soma}.")

except ValueError:
    print("Dado invalido. Insira um número.");