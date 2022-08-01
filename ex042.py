
r1 = int(input("Insira, reta 1 em centrímetros: "))
r2 = int(input("Insira, reta 2 em centrímetros: "))
r3 = int(input("Insira, reta 3 em centrímetros: "))

if ((r1 + r2) > r3) and ((r3 + r2) > r1) and ((r1 + r3) > r2):
    print(f"Lado 1: {r1} Lado 2: {r2} Lado 3: {r3} Podem formar um triângulo.")
    if (r1 == r2) and (r2 == r3):
        print("Equilátero.")
    elif ((r1 == r2) and (r2 != r3)) or ((r1 == r3) and (r3 != r2)) or ((r3 == r2) and (r2 != r1)):
        print("Isósceles.")
    else:
        print("Escaleno.")
else:
    print("Não podem formar um triângulo.")
