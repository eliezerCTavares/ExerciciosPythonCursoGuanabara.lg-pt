total = 0
mil = 0

# Valor e nome do produto mais barato.
barato_valor = float("inf")
barato_nome = ""

# Loop de cadastro.
while True:
    produto = input("Produto: ").title()
    preco = int(input("Preço: R$ "))

    # Soma de todos os preços.
    total += preco
    # Quantos produtos acima de R$ 1000,00.
    if preco > 1000:
        mil += 1
    # Qual o nome do produto mais barato.
    if preco < barato_valor:
        barato_valor = preco
        barato_nome = produto

    print("="*20)

    # Escolha se o usuário quer continuar cadastrando ou quer ir para as estatísticas.
    continua = " "
    while continua not in "SNsn":
        # Loop para checar que  somente S ou N / Sim ou não seja digitado pelo usuário.
        continua = input("Continuar cadastrando? [S/N] ").strip().upper()[0]
    if continua == "N":
        break

    print("="*20)

print(f"""
Total da compra: {total}
Quantos produtos custam mais de R$ 1000,00: {mil}
O produto mais barato, {barato_nome}, custa R$ {barato_valor}
""")