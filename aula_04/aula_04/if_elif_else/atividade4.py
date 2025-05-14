# Exemplo 04

# Crie um algoritmo que receba duas notas e exiba as mensagens de acordo com
# os critérios 

# Média igual ou maior que 7, imprimir "Aluno aprovado!"
# Média igual ou maior que 5 e menor que 7 "Aluno de recuperação!"
# Média menor que 5 "Aluno Reprovado"

nota1 = float(input('Digite a nota do teste: '))
nota2 = float(input('Digite a nota da prova: '))
media = (nota1 + nota2) /2

if media >= 7:
    print("Aluno aprovado!")
eif media >= 5:
    print("Aluno em recuperação!")
else:
    print("Aluno reprovado!")
