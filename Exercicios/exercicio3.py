my_list = []

while True:
    options = input(
        '''
            Ecolha uma opção:
            N: Novo número
            S: Soma
            Q: Sair
        '''
    )

    if options == 'n':
        numero = int(input('Digite o número'))
        my_list.append(numero)

    elif options == 's':
        print(sum(my_list))
    
    elif options == 'q':
        break

    def sum(list):
        result = 0
        for i in list:
            result = result + i
        return result