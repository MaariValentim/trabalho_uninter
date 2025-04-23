print('Bem-vinda(o) a loja de gelados da Mariana Valentim!')
s1 = '-'*20 + 'Cardápio' + '-'*20
print(s1)

print('-'*5 + '|' + ' ' + 'Tamanho' + ' ' + '|' + ' ' + 'Cupuaçu (CP)' + ' ' + '|' + ' ' + 'Açai (AC)' + '|' + '-'*5)
print('-'*5 + '|' + ' '*4 + 'P' + ' '*4 + '|' + ' '*4 + 'R$ 9.00' + ' '*3 + '|' + ' ' + 'R$ 11.00' + ' ' + '|' + '-'*3)
print('-'*5 + '|' + ' '*4 + 'M' + ' '*4 + '|' + ' '*4 + 'R$ 14.00' + ' '*2 + '|' + ' ' + 'R$ 16.00' + ' ' + '|' + '-'*3)
print('-'*5 + '|' + ' '*4 + 'G' + ' '*4 + '|' + ' '*4 + 'R$ 18.00' + ' '*2 + '|' + ' ' + 'R$ 20.00' + ' ' + '|' + '-'*3)

total = 0  # Variável contadora para somar o valor de todos os pedidos

while True:
    # Sabor
    sabor = input('\nEntre com o sabor desejado (CP/AC): ')
    if (sabor != 'ac' and sabor != 'cp'):
        print('Sabor inválido, tente novamente!')
        continue

    # Tamanho
    tam = input('Escolha o tamanho desejado (P/M/G): ')
    if (tam != 'p' and tam != 'm' and tam != 'g'):
        print('Tamanho inválido, tente novamente!')
        continue

    # tamanhos e valores:
        #Cupuaçu
    if sabor == 'cp':
        if tam == 'p':
            valor = 9.00
        elif tam == 'm':
            valor = 14.00
        elif tam == 'g':
            valor = 18.00
            #Açaí
    elif sabor == 'ac':
        if tam == 'p':
            valor = 11.00
        elif tam == 'm':
            valor = 16.00
        elif tam == 'g':
            valor = 20.00

    qtd = int(input('Quantidade: ')) #achei mais fácil trabalhar com o quantidade junto pra fazer a conta pelos exemplos que temos em aula.
    subtotal = qtd * valor
    total += subtotal
    print(f'Você pediu {sabor} no tamanho {tam}: R${subtotal}')

    while True:
        continuar = input('Deseja pedir mais alguma coisa? (s/n): ')
        if continuar == 's' or continuar == 'n':
            break
        else:
            print('Opção inválida! Digite "s" para sim ou "n" para não.')

    # Finaliza o pedido se o usuário não quiser mais nada
    if continuar == 'n':
        print(f'\nTotal a ser pago: R${total:.2f}')
        break  #Finaliza o programa