lista = [ [] , [] , [] ]
for p, x in enumerate(lista):
    for p2, y in enumerate(lista):
        lista[p].append(int(input(f"Inserir [{p}, {p2}]: ")))
for x in lista:
    for y in x:
        print(f"[{y:^5}]",end=" ")
    print(" ")
