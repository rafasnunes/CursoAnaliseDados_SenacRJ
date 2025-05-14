# Exemplo FOR

# Crie um algoritmo que mostre os números de 0 a 10 utilizando FOR

for num in range(11):
    print(num)

for i in range (5,20): # Range 5 = posicao inicial | 20 = posicao final
    print(i)

for i in range (5, 50, 5) # Range (inicio, fim, salto)
    print(i)

inicio = int(input('Informe o início da contagem: '))
fim = int(input('Informe o final da contagem: '))

for i in range(inicio, fim):
    print(i)

for n in range(3): # Exemplo de commo pegar o nome de 3 pessoas com um único for
    print(f'\nPessoa {n+1}:')
    nome = input('Informe o nome: ')
    print(f'O nome da pessoa é: {nome}')

