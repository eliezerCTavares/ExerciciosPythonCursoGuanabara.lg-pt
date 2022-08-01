def leiaInt(frase):
    while True:
        leia = input(f"{frase}").strip()
        if leia.isnumeric() == False:
            print("ERRO! Digite um número inteiro válido.")
        else:
            n=int(leia)
            break
    return n

x = leiaInt("Digite um valor inteiro: ")
print(f"Você digitou o número {x}.")