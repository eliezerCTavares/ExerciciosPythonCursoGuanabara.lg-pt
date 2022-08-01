# Leia nome e peso de várias pessoas / Guarde tudo em uma lista /
# Mostre:
# 1) Quantas pessoas foram cadastradas
# 2) listar a(s) pessoa(s) mais pesada(s)
# 3) Listagem das pessoas mais leves
pessoas = []
individual = []
maxx = []
minn = []
print("\nCadastre Nome e Peso.\n", "*"*40)
while True:
    individual.append(input("Nome: ").title())
    individual.append(float(input("Peso: ")))
    pessoas.append(individual[:])
    # Definir o/s peso/s máximo/s e mínimos

    if maxx == [] or individual[-1] == maxx[0][-1]:
        maxx.append(individual[:])
    elif individual[-1] > maxx[0][-1]:
        maxx.clear()
        maxx.append(individual[:])
    if minn == [] or individual[-1] == minn[0][-1]:
        minn.append(individual[:])
    elif individual[-1] < minn[0][-1]:
        minn.clear()
        minn.append(individual[:])
    individual.clear()

    if input("Quer continuar cadastrando? ").strip().upper()[0] == "N":
        break


print(f"Foram cadastradas {len(pessoas)} pessoas.")


def maimen(imprim):
    for p_s in imprim:
        print(f"{p_s[0]} com {p_s[1]} Kg.", end=" ")


print("\nMaior peso: ", end=" ")
maimen(imprim=maxx)
print("\nMenor peso: ", end=" ")
maimen(imprim=minn)

