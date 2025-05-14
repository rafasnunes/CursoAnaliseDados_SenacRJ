# Exemplo do uso do While com True & False

# contador = 1

# while True:
#     print(contador)
#     contador += 1
#     if contador > 5:
#         break

# Soma de Números até que o usuário escolha parar
    
soma = 0
resposta =''

while True:
        num = float(input('Insira um número para a soma: '))
        soma += num

        resposta = input('Quer continuar a soma? (S/N): ').upper()[0]
        if resposta == 'N':
            break
    
print(f'A soma dos números é: {soma}')
