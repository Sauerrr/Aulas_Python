n = int(input("Digite o número de notas: "))

soma = 0

for i in range(n):
    nota = float(input(f"Digite a nota {i+1}: "))
    soma += nota

media = soma / n


print(f"A média das {n} notas é: {media:.2f}")
