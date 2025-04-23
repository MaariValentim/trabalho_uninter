print ('Bem vindo(a) a loja da Mariana Valentim!!')

valor_uni = int(input('Entre com o valor do produto:'))
qtd = int(input('Entre com a quantidade do produto:'))
valor_total = valor_uni *qtd

if ( valor_uni < 2500) :
    desconto = 0
    porcentagem = (desconto / 100) * valor_total
    valor_final = valor_total - porcentagem
    print(f'Valor total sem desconto:{valor_total}')
    print(f'Valor total com desconto: {valor_final}')

elif ( valor_uni >= 2500  and valor_uni < 6000): # eu coloquei o and porque se não ele não lia o desconto de 7%, travava aqui
    desconto = 4
    porcentagem = (desconto / 100) * valor_total
    valor_final = valor_total - porcentagem
    print(f'Valor total sem desconto:{valor_total}')
    print(f'Valor total com desconto: {valor_final}')

elif ( valor_uni >= 6000  and valor_uni < 10000):
    desconto = 7
    porcentagem = (desconto / 100) * valor_total
    valor_final = valor_total - porcentagem
    print(f'Valor total sem desconto:{valor_total}')
    print(f'Valor total com desconto: {valor_final}')

else:
    desconto = 11
    porcentagem = (desconto / 100) * valor_total
    valor_final = valor_total - porcentagem
    print(f'Valor total sem desconto:{valor_total}')
    print(f'Valor total com desconto: {valor_final}')



