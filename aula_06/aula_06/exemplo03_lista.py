# Narcisa Tamborindeguy (Ai que loucura!) me ligou e pediu para eu auxiliá-la
# na verificação da previsão do tempo dos próximos 5 dias e informá-la se o
# dia será ensolarado ou não. # O objetivo é auxilia-la na preparação adequada
# para o clima de cada dia.

# Requisitos:

# - Obter os dados, da seguinte forma:
# - Previsões = Ensolarado, Nublado, Chuvoso, Tempestade, Ensolarado
# - Informar a previsão do tempo, a partir dos dados acima.
#   percorrendo cada item do conjunto de dados e:
# - Se a previsão for Ensolarado, informar para aproveitar e
#   passear
# - Senão (diferente de ensolarado), informar para não esquecer o guarda-chuva

previsoes_tempo = ['Ensolarado','Nublado','Chuvoso', 'Tempestade', 'Ensolarado']
i = 1
for previsao_dia in previsoes_tempo:
    if previsao_dia == 'Ensolarado':
        print(f'Dia {i}: Aproveite para passear, previsão: {previsao_dia}')
        i = i + 1
    else:
        print(f'Dia {i}: Leve o guarda-chuva, previsão: {previsao_dia}')
        i = i + 1

print(previsoes_tempo) # Imprime toda a lista

print(previsoes_tempo[0]) # Imprime o item na posição 0 da lista

print(previsoes_tempo[1:3]) # Imprime os itens no intervalo (Posição 1 e 2), a 3 é o ponto de parada e não é exibido.

print(previsoes_tempo[2][4]) # Imprime os itens nas posições especificadas.

print(previsoes_tempo[-1]) # Imprime o último item da lista.
