valor_init = float(input("Preço do produto: R$ "))

esc = int(input("""Escolha a forma de pagamento:

1 - à vista em dinheiro: 10% de desconto.
2 - à vista no cartão: 5% de desconto.
3 - até 2x no cartão: preço normal.
4 - 3x ou mais no cartão: 20% de juros.
"""))
if esc == 1:
    print(f"Opção {esc}, à vista em dinheiro com 10% de desconto: R$ {valor_init - valor_init*0.10}")
elif esc == 2:
    print(f"Opção {esc}, à vista no cartão com 5% de desconto: R$ {valor_init - valor_init*0.05}")
elif esc == 3:
    print(f"Opção {esc}, até 2x no cartão: preço normal: R$ {valor_init}")
elif esc == 4:
    parcela = int(input("Quantas parcelas? "))
    print(f"Opção {esc}, {parcela}x de R$ {(valor_init*1.20)/parcela}")
else:
    print("Opção inválida.")