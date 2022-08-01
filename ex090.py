aluno = {}
alunoss = []
while True:
    aluno ["Aluno"] = str(input("Nome do Aluno: ")).title()
    aluno ["Média"] = float(input(f"Média de {aluno['Aluno']}: "))
    if aluno ['Média'] >= 7:
        aluno['Situação'] = 'Aprovado'
    elif aluno ['Média'] >= 5:
        aluno['Situação'] = 'Recuperação'
    else:
        aluno['Situação'] = 'Reprovado'
    alunoss.append(aluno.copy())

    if input("Quer cadastrar outro aluno? (S/N)").strip().upper()[0] == "N":
        break

print("="*50)

for student in alunoss:

    for k,v in student.items():
        print(f"{k}: {v}",end=" | ")
    print()

print("="*50)