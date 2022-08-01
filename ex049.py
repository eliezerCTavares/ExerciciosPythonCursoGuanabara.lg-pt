
escolha = input("""Para calcular toda a tabuada, digite 1: 
Para calcular a tabuda de um número específico, digite 2: """)

def tabuada(numero):
    for num in range(1,11):
        print(f"{numero} x {num} = {numero*num}", end= "   ")


if escolha == "1":
    for numer in range (1, 11):
        tabuada(numero= numer)
        print("\n")

elif escolha == "2":
    numer = int(input("Qual número você quer calcular a tabuada? "))
    tabuada(numero=numer)