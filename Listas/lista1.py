servicos = ['restauração', 'carpintaria', 'marcenaria']

while True:
    print('0: Sair')
    print('1: Adicionar tarefa')
    print('2: Remover tarefa')
    print('3: Vizualisar tarefas atuais ')

    opcoes = input('Selecione: 0, 1, 2 ou 3 ')

    if opcoes == '1':
        servico = input('Digite o serviço')
        servicos.append(servico)
    if opcoes == '2':
        print(servicos.pop(0))
    if opcoes == '3':
        print(f'{len(servicos)} - {servicos}')
    if opcoes == '0':
        break


#Lista de pedidos:


pedidos = ['Coca','Carne ','Batata']

while True:
    print('0:sair')
    print('1: Adicionar pedido')
    print('2: Remover ultimo pedido')
    print('3: vizualizar pedidos atuais')

    opcoes = input('Selecione 0, 1, 2 ou 3')

    if opcoes == '1':
        pedido = input('Digite o pedido:  ')
        pedidos.append(pedido)
    if opcoes == '2':
        print(pedidos.pop(0))
    if opcoes == '3':
        print(f'{len(pedidos)} - {pedidos}')
    if opcoes == '0':
        break

#Lista de atendimento:

atendimentos = ['idosos', 'deficientes', 'geral']

while True:
    print('0: Sair')
    print('1: Adicionar atendimento')
    print('2: Remover atendimento')
    print('3: Visualizar atendimentos atuais')

    opcoes = input('Selecione: 0, 1, 2 ou 3')

    if opcoes == '1':
        atendimento = input('Digite o serviço')
        atendimentos.append(atendimento)
    if opcoes =='2':
        print(atendimentos.pop(0))
    if opcoes == '3':
        print(f'{len(atendimentos)} - {atendimentos}')
    if opcoes == '0':
        break   

#Lista de pagamento

pagamentos = ['Pagamento 1', 'Pagamento 2', 'Pagamento 3']

while True:
    print('\nMenu:')
    print('0: Sair')
    print('1: Adicionar pagamento')
    print('2: Processar pagamento')
    print('3: Visualizar pagamentos atuais')

    opcao = input('Selecione: 0, 1, 2 ou 3: ')

    if opcao == '1':
        pagamento = input('Digite o pagamento: ')
        pagamentos.append(pagamento)
        print(f'Pagamento "{pagamento}" adicionado com sucesso.')

    elif opcao == '2':
        if pagamentos:
            pagamento_processado = pagamentos.pop(0)
            print(f'Pagamento "{pagamento_processado}" processado com sucesso.')
        else:
            print('Nenhum pagamento para processar.')

    elif opcao == '3':
        print(f'Pagamentos atuais ({len(pagamentos)}): {pagamentos}')

    elif opcao == '0':
        print('Saindo...')
        break

    else:
        print('Opção inválida. Tente novamente.')