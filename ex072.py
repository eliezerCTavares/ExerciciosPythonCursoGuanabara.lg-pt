numeros = (
    "zero", "um", "dois", "três", "quatro", "cinco",
    "seis", "sete", "oito", "nove", "dez", "onze",
    "doze", "treze", "quatorze", "quinze", "desesseis",
    "desessete", "dezoito", "dezenove", "vinte"
)
while True:
    while True:
        num = int(input("Digite um número entre 0 e 20: \n"))
        if num >= 0 and num <= 20:
            print(f"{num} por extenso: {numeros[num].capitalize()}\n")
            break
        else:
            print(f"{num} não é permitido. Tente novamente.", end=" ")
    if input("Você quer continuar digitando? [S/N] ").strip().upper()[0] == "N":
        break
print("Bye!")