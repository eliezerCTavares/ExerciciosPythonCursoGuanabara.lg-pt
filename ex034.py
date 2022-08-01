salary = float(input("Salário original: R$"))

if salary > 1250:
    percent = 10 * 0.01
    sal_raise = salary + (salary * percent)
    print(f"O salário original de R$ {salary} com 10 % de aumento será: R${sal_raise:.2f}\n")
elif salary <= 1250:
    percent = 15 * 0.01
    sal_raise = salary + (salary * percent)
    print(f"O salário original de R$ {salary} com 15 % de aumento será: R${sal_raise:.2f}\n")