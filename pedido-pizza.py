valores = {'pequena': 20, 'média': 25, 'grande': 30,}
ingredientes = []

while True: 
    resposta = input('Gostaria de fazer seu pedido? [S/N] ')

    if resposta.upper() == 'S':
        while True:
            mensagem = ('Você pode escolher entre "PIZZA SIMPLES", que vem molho de tomate e queijo ou "MONTE SUA PIZZA", que você pode adicionar qualquer ingrediente além do molho e queijo. qual você escolhe?')
            mensagem += ('\n*Cada ingrediente adicionado será cobrado um adicional de R$0,50. ')
            opcao = input(mensagem)

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

        print("\n--- Escolha o tamanho ---")
        print("PEQUENA ------------ R$20,00")
        print("MÉDIA -------------- R$25,00")
        print("GRANDE ------------- R$30,00")
        tamanho = input('')
        preco = valores[tamanho.lower()]
        
        if len(ingredientes) > 0:
            preco = preco + (len(ingredientes) * 0.5)

        print("Pedido Finalizado.")
        print(f"O valor total do seu pedido é R${preco}.")
        print("Obrigada pela preferência.")
        break

    elif resposta.upper() == 'N':
        print(f'Tudo bem.')
        break

    else:
        print('Erro. Tente novamente.')

print("Volte Sempre.")
close = input()