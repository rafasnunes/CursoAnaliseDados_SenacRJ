def cadastra_vendas(num):
 
    for i in range(num):

        nome = input('Informe o nome do vendedor: ')
        valor = input('Informe o valor da venda: ')

        venda = {
            'Nome': nome,
            'Valor': valor,
        }

        lst_vendas.append(venda)

# Principal


lst_vendas = []

qtd = int(input('Quantas vendas deseja cadastrar? '))
cadastra_vendas(qtd)

print(lst_vendas)
