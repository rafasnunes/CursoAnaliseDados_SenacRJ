# Atividade A
# Elabore um algoritmo que leia um número e escreva na tela, além do próprio
# número, mostre também o anterior e o sucessor.

num = int(input('Digite um número: '))
num_ant = num - 1
num_suc = num + 1

print('Número digitado: ', num)
print('Número antecessor: ', num_ant)
print('Número sucessor: ', num_suc)

# Atividade B
# Crie um programa, que leia um número e mostre o seu dobro,
# o triplo e o seu quadrado

num_dobro = num * 2
num_triplo = num * 3
num_quadrado = num * num  # Outra forma de fazer ( num_quadrado = num ** 2 )

print('Número dobrado: ', num_dobro)
print('Número triplicado: ', num_triplo)
print('Número ao quadrado: ', num_quadrado)

# Atividade C
# Crie um programa que leia um número em metros e converta-o para centímetros
# e milimetros

num_metro = float(input('Insira o número em metros: '))
num_centimetro = num_metro * 100
num_milimetro = num_metro * 1000

print('Conversão para centímetros: ', num_centimetro)
print('Conversão para milímetros ', num_milimetro)
