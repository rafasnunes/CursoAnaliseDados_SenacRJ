# Exercicio 4 - Soma de valores

# Crie um programa que leia 5 números digitados pelo usuário e mostre a soma total e calcule a média.


soma = 0.0
controle = 0

for i in range(int(input('Digite a quantidade de números para somar: '))):
    num = float(input(f'Digite o {i+1}º número: '))
    soma += num
    controle += 1

media = soma / controle

print(f'A soma dos números digitados é {soma} e a média é {media}')
