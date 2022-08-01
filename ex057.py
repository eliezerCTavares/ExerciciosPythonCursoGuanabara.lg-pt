genero = str(input("Qual seu gênero (F/M):\n")).strip().upper()[0]
while genero not in "MmFf":
    print (f"{genero} não é aceito como gênero: escolha 'M' para masculino / 'F' para feminino.\n")

if genero == "M":
    print("O gênero é masculino.\n")
    endgame = "FIM"
elif genero == "F":
    print("O gênero é feminino.\n")
    endgame = "FIM"