
# Função para escolher o serviço
def escolha_servico():
    while True:
        print('Serviços disponíveis:')
        print('DIG - Digitalização')
        print('ICO - Impressão Colorida')
        print('IPB - Impressão Preto e Branco')
        print('FOT - Fotocópia')

        servico = input('Digite o serviço desejado (DIG/ICO/IPB/FOT): ').upper()

        if servico in ['DIG', 'ICO', 'IPB', 'FOT']:
            return servico
        else:
            print('Serviço inválido. Por favor, escolha uma opção válida.')
            # usuário errou opção


# Função para obter desconto
def num_pagina():
    while True:
        try:
            paginas = int(input('Digite o número de páginas: '))

            if paginas >= 20000:
                print('Não aceitamos pedidos com mais de 20000 páginas.')
                continue
            elif paginas < 0:
                print('Por favor, digite um número positivo.')
                continue


            if paginas < 20:
                return paginas
            elif 20 <= paginas < 200:
                return paginas * 0.85  # 15% de desconto
            elif 200 <= paginas < 2000:
                return paginas * 0.80  # 20% de desconto
            elif 2000 <= paginas < 20000:
                return paginas * 0.75  # 25% de desconto

        except ValueError:
            print('Por favor, digite um número válido.')
            # (try/except)


# Função para serviços extras
def servico_extra():
    while True:
        print('\nServiços extras:')
        print('1 - Encadernação simples - R$ 15.00')
        print('2 - Encadernação capa dura - R$ 40.00')
        print('0 - Não desejo mais nada')

        extra = input('Digite o serviço extra desejado (1/2/0): ')

        if extra == '1':
            return 15.00
        elif extra == '2':
            return 40.00
        elif extra == '0':
            return 0.00
        else:
            print('Opção inválida. Por favor, escolha uma opção válida.')


# Programa principal
print('Bem-vindo a copiadora da Mari Valentim! \n')

# Dicionário de preços
precos = {
    'DIG': 1.10,
    'ICO': 1.00,
    'IPB': 0.40,
    'FOT': 0.20
}


servico = escolha_servico()
paginas = num_pagina()
extra = servico_extra()


valor_servico = precos[servico] * paginas
total = valor_servico + extra

#resultados
print(f'Total a pagar: R$ {total:.2f} (serviço: {servico} | extra: {extra:.2f} | total de páginas: {paginas:.0f}|)')

