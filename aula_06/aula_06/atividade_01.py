'''Olá, estou organizando as atividades ao ar livre da escola para todas as semanas do ano e preciso da sua ajuda para saber quais dias serão ensolarados e quais terão condições climáticas desfavoráveis, como nublado ou chuvoso, ou seja, qualquer coisa diferente de sol.

Eu ainda não possuo todos as informações relacionadas as previsões até o final do ano, mas tenho as previsões da próxima semana, para que você já possa iniciar esse trabalho:

* Segunda: Nublado
* Terça: Chuvoso
* Quarta: Tempestade
* Quinta: Ensolarado
* Sexta: Ensolarado

Eu gostaria que você me ajudasse a classificar esses dias em duas categorias:

1. Dias Ensolarados: Para eu saber quando podemos agendar as atividades ao ar livre.

2. Dias Sem Sol: Para planejar atividades internas.
Com esses dados: já é possível que faça essa classificação para mim?

Queria também que ao final me mostrasse o resultado, indicando quais dias serão ensolarados e quais não serão?

Agradeço muito pela sua ajuda!

Atenciosamente,

Requisitos:

* Informar quais dias serão ensolarados e quais não serão, da seguinte forma:
* o Percorrer os dados relacionados às previsões de tempo:
* Se a previsão for igual a Ensolarado, informar qual dia da semana (percorrer a Lista com os dias da semana)
* Senão (diferente de ensolarado), informar qual dia da semana (percorrer a Lista com os dias da semana)'''

previsoes_tempo = ['Ensolarado', 'Nublado', 'Chuvoso', 'Tempestade', 'Ensolarado']
dias_semana = ['Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta']

dias_ensolarados = []
dias_sem_sol = []

for i, d in enumerate(previsoes_tempo):
    print(i, d)
    if previsoes_tempo[i] == 'Ensolarado':
        dias_ensolarados.append(dias_semana[i])
    else:
        dias_sem_sol.append(dias_semana[i])

print(f'Dias Ensolarados: {dias_ensolarados}')
print(f'Dias Sem Sol: {dias_sem_sol}')