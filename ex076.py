materiais = (
    "Lápis", 1.50,
    "Caneta", 3.00,
    "Caderno", 15.99,
    "mochila", 79,
    "borracha", 1.29,
    "carrinho", 490.99
    )

print("_"*40)
print(f'{"LISTA DE PRODUTOS/PREÇOS":^40}')
print("_"*40)
for x in range(0, len(materiais),2):
    print(f"{materiais[x].title() :.<30}R${materiais[x+1]:>7.2f}")