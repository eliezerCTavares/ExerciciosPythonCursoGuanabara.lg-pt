import datetime
birth_date = int(input('Insira a sua data de nascimento: '))

date_now = datetime.datetime.now().year

age = date_now - birth_date

if age >= 17:
    print(f"Você tem {age} anos, atingiu a maioridade e precisa se apresentar ao serviço militar.")
elif age < 17:
    print(f"Você tem {age} anos, ainda não atingiu a maioridade e ainda não precisa se apresentar ao serviço militar.")
elif age >= 19:
    print(f"Você tem {age} anos, e ainda pode se apresentar ao serviço militar.")
elif age > 35:
    print(f" Você tem {age} anos e já passou da idade permitida para o alistamento.")


 