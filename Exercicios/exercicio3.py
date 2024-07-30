def somaLista(lista):
    soma = 0
    i = 0
    while True:
        if i >= len(lista):
            break
        soma += lista[i]
        i += 1
    return soma


lista = [1, 2, 3, 4, 5]
resultado = somaLista(lista)
print("Soma da lista é:", resultado)
