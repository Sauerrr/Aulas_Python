def calcArea(base, altura):
    area = (base * altura) /2
    return area

base = float(input("Digite a base do triangulo: "))
altura = float(input("Digite a altura do triangulo: "))
area = calcArea(base, altura)

print(f"A área do triangulo é {area}")

