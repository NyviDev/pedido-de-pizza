toppings = []
if toppings == []:
    answer = input('Você quer uma pizza simples[N ou S]? ')
    if answer == 'N':
        toppings = [input('Adicione um ingrediente: ')]
        for topping in toppings:
            print(f'Adicionando {topping}.')
            answer_2 = input('Quer adicionar mais um ingrediente[N ou S]? ')
            if answer_2 == 'S':
                topping = input('Adicione um ingrediente: ')
                toppings.append(topping)
            elif answer_2 == 'N':
                print('OK.')
        print(f'Ingredientes: {toppings}')
    elif answer == 'S':
        print('Ok.')
print('Pizza finalizada.')
