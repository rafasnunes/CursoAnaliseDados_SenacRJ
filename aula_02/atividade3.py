# Atividade A
# Implemente um algoritmo que leia as notas de teste e da prova de um aluno,
# retire a média e mostre o resultado na tela

nota_teste = float(input('Insira a nota do Teste: '))
nota_prova = float(input('insira a nota da Prova: '))

nota_media = (nota_teste + nota_prova) / 2

print('A média do aluno é: ', nota_media)
