# Exercicio 03 - Coleta de Dados

# Peça o nome de 3 pessoas e mostre uma lista com os nomes digitados.

for i in range (3):
    nome = input(f'Digite o nome da pessoa {i+1}: ')
    print(f'O nome da pessoa {i+1} é {nome}.')
