def leia_int(frase):
    while True:
        try:
            leia = int(input(f"{frase}"))
            return leia
        except Exception as erro:
            print(f"Não é um número inteiro: {erro.__cause__}")


def leia_float(frase):
    while True:
        try:
            leia = float(input(f"{frase}"))
            return leia
        except Exception as erro:
            print(f"Não é um número real: {erro.__cause__}")


num_int = leia_int("Digite um número INTEIRO: ")
num_float = leia_float("Digite um número REAL: ")

print(f"Inteiro: {num_int} | n° Real: {num_float}")