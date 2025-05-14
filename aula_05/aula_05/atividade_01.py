# Atividade 01

# Crie um sistema "simples" para verificar se a temperatura de um equipamento
# está dentro de uma faixa segura de operação da máquina.

# A gestora Maria, informou que a temperatura segura é até 15ºC e, que acima
# disso, o sistema deve informar a manutenção para verificar o sistema de
# refrigeração.

# O sistema deve permitir que o operador insira a temperatura,
# no momento da verificação.

# Regras

# Se a temperatura for menor ou igual a 15ºC, informar que o sistema opera
# dentro da área segura.
# Do contrário, informar que é necessário manutenção do sistema de refrigeração

temperatura = float(input('Digite a temperatura atual da máquina: '))

MAX_TEMP = 15

if temperatura <= MAX_TEMP:
    print('Sistema operando dentro da fiaxa de segurança.')
else:
    print('Sistema com problemas! Necessita de manutenção.')
