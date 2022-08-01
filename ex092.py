from datetime import datetime
cadastro = {}

cadastro["Nome"] = input("Nome da pessoa: ").title()
cadastro["Idade"] = (datetime.now().year) - int(input("Data de nascimento: "))
cadastro["Nº_carteita"] = int(input("Nº da carteira de trabalho (0 não tem): "))
if cadastro["Nº_carteita"] != 0:
    cadastro["Ano_contratação"] = int(input("Ano de contratação: "))
    cadastro['Salário'] = float(input("Salário de contratação: R$ "))
    cadastro['Idade_aposento'] = ((cadastro["Ano_contratação"])-(datetime.now().year-cadastro["Idade"])+35)

print("\n")
print("="*51)
for k , v in cadastro.items():
    if k == "Salário":
        print(f"{k :.<20} {'R$':>20}{v:>10.2f}")
    elif v == 0:
        print(f"{k :.<20} {'Não possui':>30}")
    else:
        print(f"{k :.<20} {v:>30}")
print ("="*51)