cont = "S"
n2 = 0
qnt = 0
maior = 0
menor = float('inf')
while cont =="S":
    n_ = int(input("Digite um número:\n "))
    if n_ > maior:
        maior = n_
    if n_ < menor:
        menor = n_
    n2 += n_
    qnt += 1
    cont = str(input("Você quer continuar inserindo novos valores? (S/N)\n")).upper()

print(f"""
Soma total: {n2}
Valores inseridos: {qnt}
Média: {n2/qnt:.2f}
Maior valor: {maior} 
Menor valor: {menor}
""")