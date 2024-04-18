num1 = int(input("Digite um número meu gatão:"))
num2 = int(input("Digite mais um número meu gatão:"))

operacao = input("Digite qual operação o senhor deseja: +,-,*,/")

def soma(num1, num2):
    return num1 + num2

def sub(num1, num2):
    return num1 - num2

def mult(num1, num2):
    return num1 * num2

def div(num1, num2):
    if  num2 == 0:
        return "O número não pode ser dividido por zero"
    else:
        return num1 / num2

if (operacao == "+"):
    print(soma(num1, num2))
elif (operacao == "-"):
    print(sub(num1, num2))
elif (operacao == "*"):
    print(mult(num1, num2))
elif (operacao == "/"):
    print(div(num1, num2))
else:
    print("Sua operação foi inválida, tente usar +,-,*,/.")