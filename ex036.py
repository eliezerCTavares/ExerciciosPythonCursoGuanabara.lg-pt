#emprestimo
valor_casa = float(input("Qual é o valor da casa?"))
salario = float(input("Qual é o seu salário?"))
anos = float(input("Em quantos anos irá pagar a casa?"))
prestacao = valor_casa / (anos*12)
trinta_pc = salario * 0.30

print(f"\nTrinta porcento do salário: R${trinta_pc:.2f}  - Salário total: R$ {salario:.2f}")
print(f"\nO valor da casa: R$ {valor_casa} será dividido em {anos*12:.0f} prestações")
print(f"\nCada prestação custará: R$ {prestacao:.2f}")
if prestacao > trinta_pc:
    print(f"\nO empréstimo não pode ser realizado, o valor da prestação excede os 30% do seu salário.")
else:
    print("Seu impréstimo foi aprovado")
