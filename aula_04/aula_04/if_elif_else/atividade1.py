# Exemplo 01
# Crie um algoritmo que aplique automaticamente 16% de desconto em uma venda,
# caso o valor da compra seja maior que R$ 250. Imprima o valor do desconto e
# o valor total da compra na tela.

valor_compra = float(input('Entre com o valor da compra: R$ '))

if (valor_compra > 250.0):
    valor_desconto = (valor_compra * 0.16)
    print('Desconto aplicado: R$', "%.2f" % valor_desconto)
    print('Total da Compra: R$', valor_compra - valor_desconto)
else:
    (print('Total a pagar: R$', "%.2f" % valor_compra))
