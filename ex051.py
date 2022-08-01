print("Calcule uma Progressão Aritmética")
primter = int(input("Primeiro termo: "))
razao = int(input("Razão: "))
for x in range (0,10):
    print(primter, end=" - ")
    primter+=razao

print("Calcule uma Progressão Aritmética")
primter = int(input("Primeiro termo: "))
razao = int(input("Razão: "))
decimo = primter + 10 * razao
for n in range(primter, decimo, razao):
    print(n, end=" - ")