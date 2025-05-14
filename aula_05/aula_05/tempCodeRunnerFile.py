soma = 0.0

for num in range(5):
    numero = float(input('Informe o número: '))
    soma = soma + numero
    # soma += numero | Quando você soma a própria variável a um número seguinte

media = soma / 5

print(f'A média dos números é: {media}.')