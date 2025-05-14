# Exemplo 01 - While

# contador = 1

# while contador <= 5:
#     print(contador)
#     contador += 1


# Exemplo 02 - Usuário digita o número de repetições

# cont = 1
# rep = int(input('Digite o número de repetições:'))

# while cont <= rep:
#     print(f'Aprendendo Python {cont}')
#     cont += 1

# Exemplo 03 - Soma de 06 números

cont = 6
soma = 0

while cont > 0:
    num = float(input('Informe o número: '))
    soma = soma + num
    cont -= 1 

print (f'A soma dos números é {soma:.2f}.')