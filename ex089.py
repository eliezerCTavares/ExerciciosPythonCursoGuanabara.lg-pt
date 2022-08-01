alunos = []
while True:
    bimestres = int(input("Quantas notas serão inseridas por aluno? "))
    if bimestres > 0 and bimestres < 11:
        break
    else:
        print(f"{bimestres} não é válido. Insira um número de 1 á 10.")
while True:
    bloco = []
    aluno = input("Aluno: ").strip().title()
    bloco.append(aluno)
    notas = []
    for x in range(bimestres):
        while True:
            nota = float(input(f"Nota {x+1}: "))
            if nota >= 0 and nota <=10:
                notas.append(nota)
                break
            else:
                print(f"{nota} não é válido. Insira um número de 1 á 10.")
                
    bloco.append(notas[:])
    notas.clear()
    alunos.append(bloco[:])
    bloco.clear()
    if input("Quer continuar: ").strip().upper()[0] == "N":
        break
print("=-"*20)
print(alunos)
print("=-"*20)
print(f"{'Nº':<5} {'NOME':<20} {'MÉDIA':>5}")
print("-"*40)

for pos, bloc in enumerate(alunos):
    soma = 0
    for med in bloc[1]:
        soma += med
    media = soma / bimestres

    print(f"{pos :<5} {bloc[0] :<20} {media :>5.2f}")

while True:
    mostrar = int(input("Digite o código do aluno para mostrar as notas: ('999' interrompe)."))
    print(f"{alunos[mostrar][0]}: {alunos[mostrar][1]}")
    if mostrar == 999:
        break