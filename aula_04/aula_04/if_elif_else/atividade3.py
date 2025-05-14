# Exemplo 03

# Verificação de Acesso a Benefício em uma Cooperativa de Crédito

# Crie um algoritmo para a Cooperativa para analisar a situação dos cooperados de acordo com as condições informadas pela empresa
# Podem receber o benefício os cooperados em que pelo menos ua das seguintes condições sejam verdadeiras:

# Tenham mais de 3 anos de filiação
# Tenham movimentado mais de R$ 5.000,00 nos últimos 6 meses

# Pedir ao usuário que informe:

# Tempo de filiação em anos
# Valor movimentado nos últimos 6 meses

# Verificar se o tempo de filiação é maior que 3 anos ou o valor movimentado é superior a R$ 5.000,00.
# Caso positivo, informar na tela que o cooperado tem direito ao benefício.
# Caso negativo, informar que o cooperado ainda não atende aos critérios para receber o benefício.

tempo_filiacao = int(input('Informe o tempo de filiação do cooperado (em anos): '))
valor_movimentado = float(input('Informe o valor movimentado nos últimos 6 meses (em R$): '))

if tempo_filiacao >= 3 or valor_movimentado >= 5000:
    print('Cooperado elegível ao benefício especial.')
else:
    print('Cooperado ainda não atende aos requisitos para o benefício.')
