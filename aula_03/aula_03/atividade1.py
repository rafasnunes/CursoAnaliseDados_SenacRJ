# Atividade 01
# Sabendo que hoje é o dia do desconto de 13% em qualquer camiseta que você 
# comprar # desenvolva um programa para que você possa saber o valordo 
# desconto e o valor final # de uma camiseta que na semana passada, você
# viu que estava um valor de R$ 83

# Requisitos
# 1. Informar o valor do desconto, sabendo que o valor da camisa é de R$ 83
# e o desconto é de 13%

# 2. Informar o valor final, que é o valor da camisa de R$ 83,00 subtraído do
# valor do desconto.

preco = float(input('Digite o preço da peça: '))
desconto = (preco * 13) / 100
preco_final = preco - desconto

print('Valor da Camisa: ', preco)
print('Total do Desconto: ', desconto)
print('Preço final: ', "%.2f" % preco_final)


# Teste