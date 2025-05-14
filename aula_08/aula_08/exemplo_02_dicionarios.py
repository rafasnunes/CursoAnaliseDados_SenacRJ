# Exemplo de utilização de dicionários no Python

aluno = {
    'Nome' : 'Maria',
    'Idade': 29,
    'Curso': 'Análise de Dados',
}

print(aluno) # Imprime todos os itens do dicionario

print(aluno['Idade']) # Imprime a chave específica do dicionário

aluno['Nome'] = 'Pedro' # Altera o valor na chave 'Nome'

print[aluno] # Imprime todos os itens do dicionario novamente, mostrando a alteração de Maria para Pedro

aluno('E-mail') = 'pedro@gmail.com' # Cria uma nova chave no dicionário e atribui o valor pedro@gmail.com

if 'tel' in aluno: # Verifica se existe a chave 'tel" no dicionário aluno
    aluno.pop('E-mail') # Se existir, apaga a chave e-mail com o comando .pop

print(aluno)

# aluno.clear() # Limpa as chaves do dicionário
# print(aluno)

# del aluno # Apaga todo o dicionário, incluindo a variavel aluno

for chave, valor in aluno.items()
    print(chave, valor)