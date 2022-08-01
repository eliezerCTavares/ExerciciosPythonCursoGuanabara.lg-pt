busca = 0
qnts = 0
soma = 0
while not busca == 999:
    busca = int(input("Digite um número: \n"))
    if busca != 999:
        qnts += 1
        soma += busca
print(f"Numeros digitados: {qnts}, soma dos números: {soma}")