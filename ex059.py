from time import sleep
endgame = False

while endgame == False:
    nm1 = int(input("Digite um número: \n"))
    nm2 = int(input("Digite outro número: \n"))
    escolha = ""
    while escolha != 4:
        escolha = int(input(f"""Escolha o procedimento a seguir:

    1 - Somar {nm1} + {nm2}.
    2 - Multiplicar {nm1} x {nm2}.
    3 - Maior de {nm1} e {nm2}.
    4 - Digitar novamente os valores.
    5 - Sair do programa.
    """))

        if escolha == 1:
            print(f"{nm1} + {nm2} = {nm1+nm2}\n")

        elif escolha == 2:
            print(f"{nm1} x {nm2} = {nm1*nm2}\n")

        elif escolha == 3:
            if nm1 > nm2:
                print(f"{nm2}")
            else:
                print(f"{nm2}")
            print("\n")
        elif escolha == 4:
            print("Digite novamente os valores.\n")

        elif escolha == 5:
            break
        else:
            print(f"Escolha indisponível = {escolha}\n")
        sleep(2)
    if escolha == 5:
        endgame = True

print("Até a próxima.")
