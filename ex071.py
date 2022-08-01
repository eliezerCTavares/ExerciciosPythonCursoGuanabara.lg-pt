print(f'''
{"CAIXA ELETRÔNICO":^30}
''')

saque = int(input("Valor do saque: R$ "))

notas = 50, 20, 10, 1

for x in notas:
    x2 = saque//x
    mod = saque % x
    print(f"{x2} notas de {x}.  Sobra: {mod}")
    saque = mod