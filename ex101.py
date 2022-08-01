import datetime

def voto (idade):
    data_hoje = datetime.datetime.now().year
    idade = data_hoje - idade
    if idade < 16:
        print(f"{idade} anos. Não vota.")
    elif idade <18 and idade >= 16 or idade >= 65:
        print(f"{idade} anos. Voto facultativo")
    else:
        print(f"{idade} anos. Voto obrigatório.")

data_nasc = int(input("Ano de Nascimento: "))

voto(data_nasc)