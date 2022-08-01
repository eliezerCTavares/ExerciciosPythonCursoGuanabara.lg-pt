from datetime import date

ano = int(input("Que ano quer analizar / digite 0 para analizar o ano atual: "))

if ano == 0:
    today = str(date.today().year)
    print(today)
    ano = int(today)

if (ano % 4) == 0 and (ano % 100) != 0 or (ano % 400) == 0:
    print(f"Ano {ano} é bissexto.")
else:
    print(f"Ano {ano} NÃO é bissexto.")