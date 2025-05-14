# Exemplo 02

# Crie um algoritmo para uma empresa de expedição que solicite ao usuário a
# quantidade em estoque do produto, a quantidade do pedido e o peso total
# do pedido.

# Os pedidos serão liberados se duas condições forem atendidas. Se tiver a
# quantidade do pedido em estoque e o peso total do pedido for até 50Kg.

# Caso as duas condições sejam atendidas, exibir uma mensagem autorizando o 
# pedido.

# Caso alguma das condições não sejam atendidas, exibir uma mensagem
# informando problema com o pedido.

qtd_estoque = int(input('Informe a quantidade em estoque: '))
qtd_pedido = int(input('Informe a quantidade solicitada: '))
peso_pedido = float(input('Informe o peso total do pedido: '))

if (qtd_estoque > qtd_pedido) and (peso_pedido <= 50):
    print('Pedido OK. Prosseguir para envio.')
else:
    print('Problema com o pedido. Encaminhe para cancelamento.')
