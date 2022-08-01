notas = []
endgame = ""

frst = 1
while endgame != "N":
    nota0 = False
    while nota0 is False:
        nota1 = float(input(f"\nDigite a {frst}ª nota do aluno: "))

        if nota1 > 10:
            print(f"Nota '{nota1}' não é permitido. Apenas notas até 10.")
            nota1 = False
        elif nota1 <= 10:
            nota0 = True
            frst+=1
            notas.append(nota1)

    terminate = False
    while terminate is False:
        terminate = input("\nVocê gostaria de adicionar mais uma nota? 'S' ou 'N':\n").upper()
        if terminate != "N" and terminate != "S":
            print(f"Comando '{terminate}' não reconhecido. Responda com 'S' ou 'N'.")
            terminate = False
        elif terminate == "N":
            terminate = True
            endgame = "N"
    if terminate == "N":
        endgame = "N"

soma = sum(notas)
media = soma / len(notas)
n1 = 1
for x in notas:
    print (f"\n{n1}ª nota: {x}")
    n1 += 1
print (f"\nA soma total das notas é: {soma:.2f}\n\nA média final é: {media:.2f}\n")

if media < 5:
    print("REPROVADO.")
elif media < 7:
    print ("RECUPERAÇÃO.")
elif media >= 7:
    print("APROVADO!") 
