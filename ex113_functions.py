def leia_int(frase):
    while True:
        try:
            leia = int(input(f"{frase}"))
            return leia
        except ValueError as erro:
            print(f'Erro: {erro.__cause__}')


def leia_float(frase):
    while True:
        try:
            leia = float(input(f"{frase}"))
            return leia
        except Exception as erro:
            print(f"Não é um número real: {erro.__cause__}")
