def calcArea(raio):
    area = pi * (raio * raio)
    return area

raio = float(input("Digite o raio do circulo: "))
pi = 3.14
area = calcArea(raio)
print(f"A área do circulo com raio é {area}")

