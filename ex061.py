print("Calcule uma Progressão Aritmética")
primter = int(input("Primeiro termo: "))
razao = int(input("Razão: "))
x = 10
while x > 0:
    print(primter, end=" - ")
    primter+=razao
    x-=1
print("FIM")