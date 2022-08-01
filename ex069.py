maior = 0
masc = 0
fem_men = 0
while True:

    while True:
        idade = int(input("IDADE: "))
        if idade > 0:
            break
        else:
            print(f"{idade} não é aceito. Digite uma idade válida.")

    while True:
        sexo = str(input("SEXO [M/F]: ")).strip().upper()[0]
        if sexo in "MmFf":
            break
        else:
            print(f"{sexo} não é aceito. Digite um sexo válido.")

    if idade >= 18:
        maior += 1
    if sexo == "M":
        masc += 1
    if sexo == "F":
        if idade < 20:
            fem_men += 1

    continua = ""
    while True:
        continua = input(
            "Você quer continuar cadastrando? [S/N]: ").strip().upper()[0]
        if continua not in "SsNn":
            print("Comando não permitido. Somente [S/N]")
        elif continua == "N":
            break
        if continua in "Ss":
            break
    if continua in "Nn":
        break

print(f'''
{maior} pessoas tem mais de 18 anos.
Foram cadastrados {masc} homens.
{fem_men} mulheres tem menos de 20 anos.
''')
