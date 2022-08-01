import datetime
ano = int(input("Ano de nascimento: "))

idade = (datetime.datetime.now().year) - ano
if idade <= 9:
    print(f"{idade} anos. MIRIM.")
elif idade <= 14:
    print(f"{idade} anos. INFANTIL")
elif idade <= 19:
    print(f"{idade} anos. JÚNIOR")
elif idade <= 25:
    print(f"{idade} anos. SÊNIOR")
else:
    print(f"{idade} anos. MASTER")