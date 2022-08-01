lista = [[], [], []]
col3 = 0
for p, x in enumerate(lista):
    for p2, y in enumerate(lista):
        lista[p].append(int(input(f"Inserir [{p}, {p2}]: ")))
        print (p2)
        if p2 == 2:
            col3 += lista[p][p2]         
par = 0
maxx = 0
for p, x in enumerate(lista):
    for p2, y in enumerate(x):
        print(f"[{y:^5}]", end=" ")
        if p2 % 2 == 0:
            par += y
        if p2 == 2:
            maxx+=y
    print(" ")

print(f"Pares: {par}")
print(f"Soma da 3ª Coluna: {col3}")
print(f"O maior valor da segunda linha é {maxx}.")