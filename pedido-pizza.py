valores = {'pequena': 20, 'média': 25, 'grande': 30,}
ingredientes = []

while True: 
    resposta = input('Gostaria de fazer seu pedido? [S/N] ')

    if resposta.upper() == 'S':
        while True:
            opcao = input('Você pode escolher entre "MONTE SUA PIZZA" ou "PIZZA SIMPLES" que vem molho de tomate e queijo. qual você escolhe? ')

            if opcao.lower() == 'monte sua pizza':
                ingredientes = [input('Qual ingrediente você gostaria de adicionar na sua pizza? ')]

                for ingrediente in ingredientes:
                    while True:
                        print(f'Adicionando {ingrediente}.')
                        resposta = input('\nQuer adicionar mais um ingrediente[N/S]? ')

                        if resposta.upper() == 'S':
                            ingrediente = input('Digite mais um ingrediente: ')
                            ingredientes.append(ingrediente)
                            break

                        elif resposta.upper() == 'N':
                            print('Ok. Uma pizza com os seguintes ingredientes: ')
                            break
                            
                        else:
                            print('Erro. Tente novamente.')

                for ingrediente in ingredientes:
                    print(f'\t- {ingrediente}')

                break
            elif opcao.lower() == 'pizza simples':
                print('Ok. Uma pizza simples.')
                break

            else:
                print('Erro. Tente novamente.')




















        break

    elif resposta.upper() == 'N':
        print(f'Tudo bem. Volte sempre.')
        break

    else:
        print('Erro. Tente novamente.')