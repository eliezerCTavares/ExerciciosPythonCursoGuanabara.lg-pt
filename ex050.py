lista = []
for x in range (0,6):
    numero = int(input("Digite um número: "))
    if numero % 2 == 0:
        lista.append(numero)
print(sum(lista))
