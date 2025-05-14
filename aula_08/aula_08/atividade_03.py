# Crie um dicionário de nome produto representado com as seguintes informações:
# Nome = Notebook
# Preço = 3500.00
# Estoque = 15

# Em seguida, digite o comando para remover a chave estoque

# Altere o preço para R$ 4000.00

# Imprima o nome e o preço formatado com R$

produto = {
    'nome': 'Notebook',
    'preco': 3500.00,
    'estoque': 15,
}

produto.pop('estoque')

produto['preco'] = 4000.00

print(f"Produto: {produto['nome']}  Preço: R$ {produto['preco']:.2f}")

